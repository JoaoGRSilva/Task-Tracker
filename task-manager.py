import json
from typing import Optional
from datetime import datetime


class Task:
    _id_counter = 0 
    
    def __init__(self,
                 description: str, 
                 status: str ="todo",
                 updatedAt: Optional[datetime] = None):
        Task._id_counter += 1
        self.id = Task._id_counter
        self.description = description
        self.status = status
        self.createdAt = datetime.now()
        self.updatedAt = updatedAt or self.createdAt
        
    def delete_task():
        pass
    
    def update_task():
        pass
    
    @classmethod
    def create_task(cls, descrption: str, status: str = "todo") -> "Task":
        return cls(descrption=descrption, status=status)