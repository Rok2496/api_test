from fastapi import APIRouter, HTTPException, Path
from typing import List
from app.models import Item, ItemOut
from app.database import items_db, next_id

router = APIRouter()

def get_next_id():
    global next_id
    val = next_id
    next_id += 1
    return val

@router.post("/items", response_model=ItemOut, status_code=201)
def create_item(item: Item):
    item_out = ItemOut(id=get_next_id(), **item.dict())
    items_db.append(item_out)
    return item_out

@router.get("/items", response_model=List[ItemOut])
def get_items():
    return items_db

@router.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int = Path(..., gt=0)):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int = Path(..., gt=0), item: Item = ...):
    for idx, existing_item in enumerate(items_db):
        if existing_item.id == item_id:
            updated_item = ItemOut(id=item_id, **item.dict())
            items_db[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int = Path(..., gt=0)):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[idx]
            return
    raise HTTPException(status_code=404, detail="Item not found") 