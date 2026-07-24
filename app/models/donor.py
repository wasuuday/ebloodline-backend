from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.database.database import Base


class Donor(Base):

    __tablename__ = "donors"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    first_name = Column(String, nullable=False)

    last_name = Column(String)

    dob = Column(Date, nullable=False)

    email = Column(String)

    phone = Column(String, nullable=False)

    occupation = Column(String)

    blood_group = Column(String, nullable=False)

    address_line1 = Column(String)

    address_line2 = Column(String)

    zipcode = Column(String)

    city = Column(String)

    taluka = Column(String)

    district = Column(String)

    state = Column(String)

    photo_url = Column(String)

    entered_by = Column(
    UUID(as_uuid=True),
    ForeignKey("users.id"),
    nullable=True
    )

    created_at = Column(
        DateTime,
        server_default=func.now()
    )