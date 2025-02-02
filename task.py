from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
async def all_tasks():
    return {"message":"All tasks"}
