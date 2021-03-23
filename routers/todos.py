from fastapi import APIRouter
from db import Mongo
from models.todos_model import Item
from odmantic import AIOEngine

router = APIRouter(prefix="/todos", tags=["items"])
mongo = Mongo("todos")


@router.post("/")
def add_todo(item: Item):
    print(item)
    todo = mongo.create(item)
    print(todo)
    return todo