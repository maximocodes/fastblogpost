# Here we define models / db tables to store our data

from sqlalchemy import Column, ForeignKey, DateTime, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Author(Base):
    """
    This serves as the table to hold authors of our blog posts
    """

    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    joined_at = Column(DateTime)

    posts = relationship("Post", back_populates="author")


class Post(Base):
    """
        This serves as the table to hold Posts of our blog
    """

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime)
    edited_at = Column(DateTime)

    author = relationship('Author', back_populates='posts')
    comments = relationship("Comment", back_populates="post")


class Comment(Base):
    """
        This serves as the table to hold comments on the blog post
    """

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    body = Column(String)
    created_at = Column(DateTime)

    post = relationship('Post', back_populates='comments')
