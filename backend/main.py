from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    age: int
    is_allowed: bool
    secret: str = "Do not write"

class ItemResponse(BaseModel):
    name: str
    age: int
    is_allowed: bool

@app.get("/")
def health():
    return {"Health":"OK"}

@app.post("/items",response_model = ItemResponse)
def post_items(item: Item):
    return item

