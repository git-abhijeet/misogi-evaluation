from typing import Union
from pymongo import MongoClient
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()
    

MONGO_DETAILS = "mongodb+srv://akc972527:akc972527@clusterswati.73qfujt.mongodb.net/misogi-test"

class User(BaseModel):
    username: str
    email: str
    password: str
    age: int
    weight: int
    height: int
    goals: str
    
class Workouts(BaseModel):
    user_id: int
    plan_name: str
    date: str
    exercises: str
    duration: str
    
class Nutrition(BaseModel):
    user_id: int
    date: str 
    meals: str
    calories: str
    macros: str
    
class Progress(BaseModel):
    user_id: int
    workout_id: str
    sets: str
    reps: str
    weights: int
    notes: str
    

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = MongoClient(MONGO_DETAILS)
    app.mongodb = app.mongodb_client.get_database("misogi-test") # Replace "mydatabase"
    print("Connected to the MongoDB database!")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/auth/register")
def register(name: str, email: str, password: str):
    print(name, email, password)
    return {"name": name, "email": email, "password": password }

@app.post("/auth/login")
def register(email: str, password: str):
    print(email, password)
    return {"email": email, "password": password }

@app.post("/auth/login/{user_id}")
def register(email: str, password: str):
    print(email, password)
    return {"email": email, "password": password }

@app.post("/workouts")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.get("/workouts")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.delete("/workouts")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.post("/exercises ")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.get("/exercises ")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.delete("/exercises ")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.post("/nutrition")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.get("/nutrition")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.delete("/nutrition")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.post("/progress")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.get("/progress")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)
    
@app.delete("/progress")
def workout(name: str, exercise: str, duration: int):
    print(name, exercise, duration)