from fastapi import APIRouter
from app.schemas.auth import RegisterRequest

router = APIRouter(
	prefix="/auth",
	tags=["Auth"]
)

@router.post("/register")
def register(request: RegisterRequest):
	return {
		"email": request.email,
		"message": "success"
	}

@router.post("/login")
def login():
	return {
		"message": "login"
	}