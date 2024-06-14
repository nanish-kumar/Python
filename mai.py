from fastapi import FastAPI, Form, Body, Query, Path
from pydantic import BaseModel, Field
from uuid import uuid4


class student(BaseModel):
    name:str
    age:100
    id:str = uuid4().hex

    def update_student

app = FastAPI()


@app.get("/")
def root():
    return ("Hello World")
   
   
   
   
'''#192.168.29.232.8123

#uvicorn main:app --host 0.0.0.0 --port 8123 --reload>>Automatically Reloading API
#uvicorn main:app --reload --host 0.0.0.0
/mark/(student_id)
/report'''