import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from typing import Optional

app = FastAPI()

from data import default_curriculums
from fastapi.responses import JSONResponse
from graphing import get_dot_source


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# open the dot files
f1 = open('./dots/g1.gv')
f2 = open('./dots/g2.gv')
f3 = open('./dots/g3.gv')
f4 = open('./dots/g4.gv')

# read the dot files
d1 = f1.read()
d2 = f2.read()
d3 = f3.read()
d4 = f4.read()
dots = [d1, d2, d3, d4]

# not sure if these will ever get called
f1.close()
f2.close()
f3.close()
f4.close()


# origins = ['*'] # DEBUG
# origins = ['http://localhost:*'] # dev
origins = ['https://gt-planner.com'] # prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/example_graph/{item_id}")
def read_examples(item_id: int):
    # return {"item_id": item_id, "q": q}
    return {"item_id": dots[item_id]}

class Curriculum(BaseModel):
    curr: dict

@app.post("/graph")
def graph(curr: Curriculum): # if I add optional, then I add another level. # how to get json argument in fastapi?
    # curr = req_curr.json()
    curr_ = curr.curr
    print(curr_)
    return get_dot_source(curr_)

@app.get("/curr/{major}")
def get_curr(major: str):
    return JSONResponse(default_curriculums[major])

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=443,
    )
