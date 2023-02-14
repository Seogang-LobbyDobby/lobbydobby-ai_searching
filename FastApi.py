import requests, json, uvicorn
from fastapi import FastAPI, Form
from pydantic import BaseModel
from button_searching import Button
from lecture_searching import LectureRs


app = FastAPI()
lsearching = LectureRs()
bsearching = Button()

@app.post("/lecture_model/")
def lectureRs_send(username: str = Form()):
    now_lecture = lsearching.lectureRs(username)
    return now_lecture

@app.post("/button_model/")
def buttonSc_send(username: str = Form()):
    now_button = bsearching.button(username)
    now_button['username'] = now_button.pop('buttonSearching')
    return now_button

if __name__ == "__main__":
    uvicorn.run(app, host='192.168.50.55', port=8000)