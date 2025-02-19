import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(30), nullable=False)
    email = Column(String(75), nullable=False)
    follower = relationship('Follower', backref='user')
    post = relationship('Post', backref='user')
    comment = relationship('Comment', backref='user')

class MediaType(enum.Enum):
    VIDEO = 'video'
    PHOTO = 'photo'
    AUDIO = 'audio'


class Media(Base):
    __tablename__ = 'Media'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType))
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    media = relationship('Media', backref='post')
    comment = relationship('Comment', backref='post')

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id')) 



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
