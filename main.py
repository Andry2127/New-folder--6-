from typing import List, Optional

from fastapi import FastAPI, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse
import uvicorn

from data_action import get_db, save_db
from models import BookModel, BookModellResponse, UserModel, EventModel, EventModellResponse



app = FastAPI()
event_db: List[EventModel] = []


@app.get("/books/", response_model=List[BookModellResponse], status_code=status.HTTP_200_OK)
async def get_books():
    return get_db()


@app.get("/books/{index}/",response_model=Optional[BookModellResponse], status_code=status.HTTP_202_ACCEPTED )
async def get_book(index: int):
    book = next((book for book in get_db() if book.get("index") == index), None)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with id {index} not found")
    return book




@app.post("/books/", status_code=status.HTTP_201_CREATED)
async def add_book(book_model: BookModel):
    db = get_db()
    db.append(book_model.model_dump())
    save_db(db)
    return JSONResponse("new book is added")




@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def add_user(user: UserModel):
    return JSONResponse("New user is added")




@app.get("/events/", response_model=List[EventModellResponse], status_code=status.HTTP_200_OK)
async def get_events():
    return event_db()


@app.post("/events/", status_code=status.HTTP_201_CREATED)
async def add_events(event_model: EventModel):
    db = event_db
    db.append(event_model.model_dump())
    save_db(db)
    return JSONResponse("new event is added")


@app.put("/events/{index}", response_model=EventModellResponse)
def update_event(index: int, updated_event: EventModel):
    for i, event in enumerate(event_db):
        if event.index == index:
            event_db[i] = updated_event
            return updated_event
    raise HTTPException(status_code=404, detail="Event not found")




@app.delete("/events/{index}", status_code=204)
def delete_event(index: int):
    for i, event in enumerate(event_db):
        if event.index == index:
            event_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Event not found")



# @app.post("/books/", status_code=status.HTTP_201_CREATED)
# async def add_book(book: BookModel):
#     books.append(book)
#     return dict(msg="ok")



# @app.get("/books/")
# async def get_book():
#     return books



# @app.get("/books/{book_id}/")
# async def get_book(book_id: int = Path(description="book number")):
#     if 0 <= book_id < len(books):
#         return books[book_id]
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book is not found")





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8005)