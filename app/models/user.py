from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True)

    name = Column(String)

    email = Column(String)

    password_hash = Column(String)

    role = Column(String)

    created_at = Column(DateTime, default=func.now())