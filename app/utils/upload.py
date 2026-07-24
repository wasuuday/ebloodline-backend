import os
import uuid

from fastapi import HTTPException, UploadFile
from app.config.supabase import supabase

BUCKET = os.getenv("SUPABASE_BUCKET")


async def upload_photo(photo: UploadFile) -> str:

    if photo is None:
        raise HTTPException(
            status_code=400,
            detail="Photo is required."
        )

    try:

        extension = photo.filename.split(".")[-1].lower()

        filename = f"{uuid.uuid4()}.{extension}"

        contents = await photo.read()

        result = supabase.storage.from_(BUCKET).upload(
            filename,
            contents,
            {
                "content-type": photo.content_type
            }
        )

        # SDK may return an error object
        if hasattr(result, "error") and result.error:
            raise Exception(result.error)

        public_url = supabase.storage.from_(BUCKET).get_public_url(
            filename
        )

        return public_url

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Photo upload failed: {str(e)}"
        )