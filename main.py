from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.donor import router as donor_router
from app.routes.registrations import router as registration_router


app = FastAPI(
    title="eBloodLine API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(

    donor_router,

    prefix="/api",

    tags=["Donor"]

)

app.include_router(
    registration_router
)

@app.get("/")
def root():
    return {
        "message": "eBloodLine API is Running"
    }
