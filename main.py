from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get('/')
def index():
    return {"data": {"name": "James"}}

@app.get('/about')
def about():
    return {"data": "about page"}

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f'{limit} published blogs from the db'}
    return {"data": f'{limit} blogs from the db'}

@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'Unpublished'}
