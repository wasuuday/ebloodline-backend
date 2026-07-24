from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi import Form
from fastapi import File
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.donor_service import create_donor

router = APIRouter()


@router.post("/registrations")
async def register_donor(

    first_name: str = Form(...),

    last_name: str = Form(""),

    dob: str = Form(...),

    email: str = Form(""),

    phone: str = Form(...),

    occupation: str = Form(...),

    blood_group: str = Form(...),

    address_line1: str = Form(...),

    address_line2: str = Form(""),

    zipcode: str = Form(...),

    city: str = Form(""),

    taluka: str = Form(""),

    district: str = Form(""),

    state: str = Form(""),

    photo: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    try:
    
        donor = await create_donor(
        
            db,
    
            {
            
                "first_name": first_name,
    
                "last_name": last_name,
    
                "dob": dob,
    
                "email": email,
    
                "phone": phone,
    
                "occupation": occupation,
    
                "blood_group": blood_group,
    
                "address_line1": address_line1,
    
                "address_line2": address_line2,
    
                "zipcode": zipcode,
    
                "city": city,
    
                "taluka": taluka,
    
                "district": district,
    
                "state": state
    
            },
    
            photo
    
        )
    
    except HTTPException:
        raise
    
    except Exception as e:
    
        raise HTTPException(
        
            status_code=500,
    
            detail=str(e)
    
        )

    return {

        "success": True,

        "message": "Donor Registered Successfully",

        "donor_id": str(donor.id),

        "photo_url": donor.photo_url

    }