# This file holds pydantic models for data validations and structure

from datetime import datetime

from pydantic import BaseModel


class CommentBase(BaseModel):
    """ In the base model we add common fields across all """
    body: str


class CommentCreate(CommentBase):
    """ I am still learning how to effectively use this """
    pass


class Comment(CommentBase):
    """ Here mostly i define the way the API response is going to look like, the fields that will be shown"""
    id: int
    post_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime
    edited_at: datetime
    comments: list[Comment] = []

    class Config:
        from_attributes = True


class AuthorBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class AuthorCreate(AuthorBase):
    joined_at: datetime | None = None


class Author(AuthorBase):
    id: int
    joined_at: datetime
    posts: list[Post] = []

    class Config:
        from_attributes = True
