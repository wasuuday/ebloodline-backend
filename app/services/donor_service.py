from datetime import datetime


from fastapi import HTTPException

from app.models.donor import Donor
from app.utils.upload import upload_photo


async def create_donor(db, data, photo):

    try:

        dob = datetime.strptime(
            data["dob"],
            "%Y-%m-%d"
        ).date()

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid DOB format."
        )



    photo_url = await upload_photo(photo)

    donor = Donor(

        first_name=data["first_name"],

        last_name=data["last_name"],

        dob=dob,

        email=data["email"],

        phone=data["phone"],

        occupation=data["occupation"],

        blood_group=data["blood_group"],

        address_line1=data["address_line1"],

        address_line2=data["address_line2"],

        zipcode=data["zipcode"],

        city=data["city"],

        taluka=data["taluka"],

        district=data["district"],

        state=data["state"],

        photo_url=photo_url,

        entered_by=None

    )

    try:

        db.add(donor)

        db.commit()

        db.refresh(donor)

    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=f"Database Error: {str(e)}"

        )

    return donor