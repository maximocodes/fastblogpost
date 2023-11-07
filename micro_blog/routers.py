from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from micro_blog import db_operations, models, schemas
from micro_blog.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# dependency # Not well conversant yet
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# we define our endpoints

@router.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_author = db_operations.get_author_by_email(db, email=author.email)
    if db_author:
        raise HTTPException(status_code=400, detail="Email already Registered")
    return db_operations.create_author(db=db, author=author)


@router.get("/authors/", response_model=list[schemas.Author])
def read_authors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    authors = db_operations.get_authors(db, skip=skip, limit=limit)
    return authors


@router.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = db_operations.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail=f"Author with id:  {author_id} not found")
    return db_author


@router.post("/authors/{author_id}/posts/", response_model=schemas.Post)
def create_author_post(author_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = db_operations.create_author_post(db, post=post, author_id=author_id)
    return db_post


@router.get("/authors/{author_id}/posts/", response_model=list[schemas.Post])
def read_author_posts(author_id: int, db: Session = Depends(get_db)):
    db_post = db_operations.get_author_posts(db, author_id=author_id)
    return db_post


@router.get("/posts/", response_model=list[schemas.Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = db_operations.get_posts(db, skip=skip, limit=limit)
    return posts


@router.post("/posts/{post_id}/comments/", response_model=schemas.Comment)
def create_post_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    db_comment = db_operations.create_post_comment(db, comment=comment, post_id=post_id)
    return db_comment


@router.get("/posts/{post_id}/comments/", response_model=list[schemas.Comment])
def read_post_comments(post_id: int, db: Session = Depends(get_db)):
    db_comment = db_operations.get_post_comments(db, post_id=post_id)
    return db_comment
