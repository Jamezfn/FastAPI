from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

class ShowBlog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[ShowBlog] = []

class ShowBlogWithUser(ShowBlog):
    creator: ShowUser

class UserLogin(BaseModel):
    email: str
    password: str