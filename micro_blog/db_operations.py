# these would be written in routes but makes debugging and testing cumbersome

import datetime

from sqlalchemy.orm import Session
from . import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_author_by_email(db: Session, email: str):
    return db.query(models.Author).filter(models.Author.email == email).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    joined_at = datetime.datetime.now()
    db_author = models.Author(email=author.email, first_name=author.first_name, last_name=author.last_name,
                              joined_at=joined_at)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_author_posts(db: Session, author_id):
    return db.query(models.Post).filter(models.Post.author_id == author_id).all()


def create_author_post(db: Session, post: schemas.PostCreate, author_id: int):
    created_at = datetime.datetime.now()
    edited_at = datetime.datetime.now()
    db_post = models.Post(**post.model_dump(), author_id=author_id, created_at=created_at,
                          edited_at=edited_at)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_post_comments(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()


def create_post_comment(db: Session, comment: schemas.CommentCreate, post_id: int):
    created_at = datetime.datetime.now()
    db_comment = models.Comment(**comment.model_dump(), post_id=post_id, created_at=created_at)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
