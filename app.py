import os
from typing import Union
from fastapi import FastAPI, UploadFile
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from pydantic import BaseModel

class Contestant(BaseModel):
    id: str
    name: str
    school: str
    score: int
    grade: str
    group: str
    contest: str

class Register(BaseModel):
    name: str
    school: str
    grade: str
    group: str
    contest: str

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadCSV")
async def uploadCSV(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        if file.content_type != "text/csv":
            print(file.content_type)
            return {"message": "File is not CSV"}
        else:
            data = pd.read_csv(file.file)
            if os.path.exists("contestants.json"):
                df = pd.read_json("contestants.json")
                data = df.append(data, ignore_index=True)
            with open("contestants.json", "w") as f:
                f.write(data.to_json(orient="records"))
            return {"message": "File uploaded successfully"}

@app.post("/uploadVideo/{id}")
async def uploadFile(id: str = None, file: UploadFile = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        filename = id + '.' + file.filename.split(".")[-1]
        with open(filename, "wb") as buffer:
            buffer.write(file.file.read())
        return {"message": "File uploaded successfully"}

@app.get("/contestants")
async def rankBoard():
    data = open("contestants.json", "r")
    return data.read()

@app.post("/contestants")
async def contestants(register: Register = None):  # type: ignore
    data = pd.read_json("contestants.json")
    last_id = data["id"].iloc[-1]
    new_id = last_id[:-1] + str(int(last_id[-1]) + 1)
    print(new_id)
    contestant = Contestant(id=new_id, name=register.name, school=register.school, score=0, grade=register.grade, group=register.group, contest=register.contest)
    data = data.append(contestant.dict(), ignore_index=True)
    with open("contestants.json", "w") as f:
        f.write(data.to_json(orient="records"))
    return {"message": "Contestant added successfully"}

@app.get("/contestants/{contestant_id}")
async def getContestant(contestant_id: str = None):
    data = pd.read_json("./contestants.json")
    contestant = data[data["id"] == contestant_id]
    return contestant.to_json(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
