from datetime import date
from typing import Optional

from pydantic import BaseModel


class DonorCreate(BaseModel):

    first_name: str

    last_name: Optional[str] = None

    dob: date

    email: Optional[str] = None

    phone: str

    occupation: str

    blood_group: str

    address_line1: str

    address_line2: Optional[str] = None

    zipcode: str

    city: Optional[str] = None

    taluka: Optional[str] = None

    district: Optional[str] = None

    state: Optional[str] = None


class DonorResponse(BaseModel):

    id: str

    first_name: str

    last_name: Optional[str]

    blood_group: str

    phone: str

    photo_url: Optional[str]

    class Config:

        from_attributes = True