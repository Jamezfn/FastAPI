from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": {"name": "James"}}

@app.get('/about')
def about():
    return {"data": "about page"}

@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': {'1', '2'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'Unpublished'}
