from fastapi import FastAPI,HTTPException
import uvicorn
from pydantic import BaseModel
app=FastAPI()
books=[
    {
        "id":1,
        "title":"programming with python",
        "book":"python"
    },
    {
        "id":2,
        "title":"linux for babes",
        "book":"linux"
    }
]
@app.get(path="/books",tags=["Books"],summary="get all books")
def book():
    return books
@app.get(path="/books/{id}",tags=["Books"],summary="get determinant book")
def get_book(id:int):
    for book in books:
        if book["id"]==id:
            return book
    raise HTTPException(status_code=404,detail="The book not found")
class NewBook(BaseModel):
    title:str
    book:str
    
@app.post("/books",tags=["books"])
def create_book(new_book:NewBook):
    books.append({"id":len(books)+1,"title":new_book.title,"book":new_book.book})
    return {"success":True,"message":"The book successful append"}

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)  