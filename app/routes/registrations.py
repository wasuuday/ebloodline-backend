from datetime import datetime

from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
    Form,
    UploadFile,
    File
)

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.donor import Donor
from app.utils.upload import upload_photo

router = APIRouter(prefix="/api/registrations", tags=["Registrations"])

@router.get("")
def get_all_registrations(
    db: Session = Depends(get_db)
):

    donors = (

        db.query(Donor)

        .order_by(Donor.created_at.desc())

        .all()

    )

    return donors




@router.get("/{donor_id}")
def get_registration(

    donor_id: str,

    db: Session = Depends(get_db)

):

    donor = (

        db.query(Donor)

        .filter(Donor.id == donor_id)

        .first()

    )

    if donor is None:

        raise HTTPException(
            status_code=404,
            detail="Donor not found"
        )

    return donor

@router.delete("/{donor_id}")
def delete_registration(

    donor_id: str,

    db: Session = Depends(get_db)

):

    donor = (

        db.query(Donor)

        .filter(Donor.id == donor_id)

        .first()

    )

    if donor is None:

        raise HTTPException(
            status_code=404,
            detail="Donor not found"
        )

    db.delete(donor)

    db.commit()

    return {

        "message":"Donor deleted"

    }



@router.put("/{donor_id}")
async def update_registration(

    donor_id: str,

    first_name: str = Form(...),
    last_name: str = Form(None),
    dob: str = Form(...),

    email: str = Form(None),
    phone: str = Form(...),

    occupation: str = Form(None),

    blood_group: str = Form(...),

    address_line1: str = Form(None),
    address_line2: str = Form(None),

    zipcode: str = Form(None),

    city: str = Form(None),
    taluka: str = Form(None),
    district: str = Form(None),
    state: str = Form(None),
    
    photo: UploadFile = File(None),
    
    db: Session = Depends(get_db)

):

    donor = (

        db.query(Donor)

        .filter(Donor.id == donor_id)

        .first()

    )

    if donor is None:

        raise HTTPException(
            status_code=404,
            detail="Donor not found"
        )

    donor.first_name = first_name
    donor.last_name = last_name
    donor.dob = datetime.strptime(
        dob,
        "%Y-%m-%d"
    ).date()

    donor.email = email
    donor.phone = phone

    donor.occupation = occupation
    donor.blood_group = blood_group

    donor.address_line1 = address_line1
    donor.address_line2 = address_line2

    donor.zipcode = zipcode
    donor.city = city
    donor.taluka = taluka
    donor.district = district
    donor.state = state
    if photo:
    
        donor.photo_url = await upload_photo(photo)

    db.commit()

    db.refresh(donor)

    return donor
