from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firsname:str
    lastname:str
    age:int

class Createtask(BaseModel):
    title:str
    content:str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int