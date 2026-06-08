from fastapi import APIRouter

router = APIRouter(
	prefix="/auth",
	tags=["Auth"]
)

@router.post("/register")
def register():
	return {
		"message": "register"
	}

@router.post("/login")
def login():
	return {
		"message": "login"
	}