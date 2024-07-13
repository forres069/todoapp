from typing import Optional
from pydantic import BaseModel

class STaskAdd(BaseModel):
    name: Optional[str] = None
    description: str
    

class STask(STaskAdd):
    id: int
    
    
class STaskId(BaseModel):
    status: Optional[int] = 200
    task_id: int 