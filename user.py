from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users():
   return {"message":"All users"}

@router.get("/{user_id}")
async def user_by_id(user_id:int):
    return {"message": f"User with ID: {user_id}"}

@router.post("/create")
async def create_user():
    return {"message": "User created"}

@router.put("/update")
async def update_user():
   return {"message": "User updated"}

@router.delete("/delete")
async def delete_user():
    return {"message":"User deleted"}
