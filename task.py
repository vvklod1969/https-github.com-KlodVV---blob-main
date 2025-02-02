from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks():
    return {"message":"All tasks"}

@router.get("/{task_id}")
async def task_by_id(task_id:int):
    return {"message": f"Task with ID: {task_id}"}

@router.post("/create")
async def create_task():
    return {"message": "Task created"}

@router.put("/update")
async def update_task():
    return {"message": "Task updated"}

@router.delete("/delete")
async def delete_task():
   return {"message": "Task deleted"}
