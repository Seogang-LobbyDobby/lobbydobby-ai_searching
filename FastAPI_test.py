import requests, json, uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from button_searching import Button
from lecture_searching import LectureRs


app = FastAPI()
lsearching = LectureRs()
bsearching = Button()

class Item(BaseModel):
    name: str

# @app.post("/test/")
# def test():
#     data = {'name':'기능'}
#     headers = {'Content-Type': 'application/json; charset=utf-8'}
#     req = requests.post("http://127.0.0.1:8000/model/",
#                         data=json.dumps(data),
#                         headers=headers)
#     return req.text

@app.post("/model/")
def model_send(data: Item):
    req = requests.post("http://127.0.0.1:8000/send/",
                        data=data.dict())
    return req

@app.post("/send/")
def send_result(item: Item):
    now = bsearching.button(item.name)
    return now