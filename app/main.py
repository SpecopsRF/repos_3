from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="DevSecOps Demo API",
    description="Учебный проект для изучения DevSecOps",
    version="1.0.0"
)

class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1

# Хранилище данных (в памяти)
items_db = {}

@app.get("/")
def read_root():
    return {
        "message": "Добро пожаловать в DevSecOps Demo API!",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "devsecops-demo"}

@app.get("/items")
def get_items():
    return {"items": items_db, "total": len(items_db)}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items_db[item_id] = item.dict()
    return {"message": f"Item {item_id} created", "item": items_db[item_id]}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item not found"}
    return {"item_id": item_id, "item": items_db[item_id]}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"message": f"Item {item_id} deleted"}
    return {"error": "Item not found"}

# Test VS Code
