from fastapi import APIRouter
from app.routers.api import auth , books

api_router = APIRouter()

api_router.include_router(user.router)
api_router.include_router(upload.router)
api_router.include_router(case.router)
api_router.include_router(prescription.router)
api_router.include_router(drug.router)
api_router.include_router(investigation.router)
api_router.include_router(blog.router)
api_router.include_router(abdm.router)
api_router.include_router(contact_us.router)
api_router.include_router(symptom_bot.router)

