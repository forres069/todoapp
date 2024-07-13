from schemas import STask, STaskAdd, STaskId
from typing import Annotated
from fastapi import Depends, APIRouter
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

tasks = []

@router.post("")
async def add_tasks(
    task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    
    return {
       "status": 200,
       "task_id": task_id
    }


@router.get("")
async def get_tasks() -> STask:
    tasks  = await TaskRepository.find_all()
    return {
        "tasks": tasks
    }