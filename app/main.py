from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from . import models, schemas, crud, database, utils

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# FastAPI app configuration
app = FastAPI(
    title="Address Book API",
    description="API to manage addresses and retrieve nearby addresses based on coordinates",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Addresses",
            "description": "Operations for creating, updating, deleting, and retrieving addresses",
        },
        {
            "name": "Search",
            "description": "Operations for searching addresses based on location coordinates",
        },
    ],
)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Dependency for database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Address
@app.post(
    "/addresses",
    tags=["Addresses"],
    summary="Create a new address",
    description="Create a new address with coordinates and store it in the SQLite database",
    response_model=schemas.Address,
)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):

    logger.info("Creating new address")

    return crud.create_address(db, address)


# Get All Addresses
@app.get(
    "/addresses",
    tags=["Addresses"],
    summary="Retrieve all addresses",
    description="Retrieve all stored addresses from the database",
    response_model=list[schemas.Address],
)
def get_addresses(db: Session = Depends(get_db)):

    logger.info("Fetching all addresses")

    return crud.get_addresses(db)


# Update Address
@app.put(
    "/addresses/{address_id}",
    tags=["Addresses"],
    summary="Update an address",
    description="Update an existing address using its ID",
    response_model=schemas.Address,
)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):

    logger.info(f"Updating address with ID {address_id}")

    updated = crud.update_address(db, address_id, address)

    if not updated:
        raise HTTPException(status_code=404, detail="Address not found")

    return updated


# Delete Address
@app.delete(
    "/addresses/{address_id}",
    tags=["Addresses"],
    summary="Delete an address",
    description="Delete an address from the database using its ID",
)
def delete_address(address_id: int, db: Session = Depends(get_db)):

    logger.info(f"Deleting address with ID {address_id}")

    deleted = crud.delete_address(db, address_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Address deleted successfully"}


# Find Nearby Addresses
@app.get(
    "/addresses/nearby",
    tags=["Search"],
    summary="Find nearby addresses",
    description="Retrieve addresses within a given distance from the provided latitude and longitude",
)
def nearby_addresses(lat: float, lon: float, distance: float, db: Session = Depends(get_db)):

    logger.info("Searching for nearby addresses")

    if distance <= 0:
        raise HTTPException(status_code=400, detail="Distance must be greater than 0")

    addresses = crud.get_addresses(db)

    result = []

    for addr in addresses:

        d = utils.calculate_distance(lat, lon, addr.latitude, addr.longitude)

        if d <= distance:
            result.append(addr)

    return result