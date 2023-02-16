import uvicorn
from fastapi import FastAPI, Form
from button_searching import Button
from lecture_searching import LectureRs


app = FastAPI()
lsearching = LectureRs()
bsearching = Button()

@app.post("/lecture_model/")
def lectureRs_send(username: str = Form()):
    now_lecture = lsearching.lectureSc(username)
    return now_lecture

@app.post("/button_model/")
def buttonSc_send(username: str = Form()):
    now_button = bsearching.button(username)
    return now_button

@app.post("/LRS/")
def buttonSc_send(name: str = Form(), aff: str = Form()):
    lrs = lsearching.LRS(name, aff)
    return lrs

if __name__ == "__main__":
    uvicorn.run()