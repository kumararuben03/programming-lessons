from fastapi import FastAPI, Body

app = FastAPI()

ITEMS = [
    {"task_id": 456, "date":"2024-05-15", "user":"John", "task": "Learn VueJS", "priority": 5 },
    {"task_id": 123, "date":"2024-05-16", "user":"Kelly", "task": "Read a novel", "priority": 3 },
    {"task_id": 100, "date":"2024-06-22", "user":"Luke", "task": "Clean living room", "priority": 3 },
    {"task_id": 211, "date":"2024-07-12", "user":"John", "task": "Write a blog", "priority": 4 },
    {"task_id": 332, "date":"2024-07-15", "user":"Kelly", "task": "Go to salon", "priority": 2 },
]

@app.get("/items")
async def get_all_items():
    return ITEMS

@app.get("/items/{user}")
async def get_user(user: str):
    for item in ITEMS:
        if item.get("user").casefold() == user.casefold():
            return item
        
    return "User not found"

@app.get("/items/")
async def get_item_by_query(date:str, user:str):
    items_to_return = []
    for item in ITEMS:
        if item.get("date") == date and item.get("user") == user:
            items_to_return.append(item)

    return items_to_return

@app.post("/items/create_item")
async def create_item(new_item=Body()):
    ITEMS.append(new_item)

    return "New Item Created Successfully!"

@app.put("/items/update_item")
async def update_item(updated_item = Body()):
    for i in range(len(ITEMS)):
        if ITEMS[i].get("task_id") == updated_item.get("task_id"):
            ITEMS[i] = updated_item

    return "Item Updated Successfully!"

@app.delete("/items/delete_item/{task_id}")
async def delete_item(task_id: int):
    for i in range(len(ITEMS)):
        if ITEMS[i].get("task_id") == task_id:
            ITEMS.pop(i)
            break
    
    return "Item Deleted Successfully!"