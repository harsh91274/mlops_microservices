"""Schema for Apartment"""

from pydantic import BaseModel

class Apartment(BaseModel):

    """Apartment Schema
    
    area - apt area
    constraction_year - apartment construction year
    bedrooms - count of apt bedrooms
    garden_area - apt garden area
    balcony_present - indicates if balcony is present (0/1)
    parking_present - indicates if parking is present (0/1)
    furnished - indicates if apt is furnished (0/1)
    garage_present - indicates if garage is present (0/1)
    storage_present - indicates if storage is present (0/1)
    """

    area: int
    constraction_year: int
    bedrooms: int
    garden_area: int
    balcony_present: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int
