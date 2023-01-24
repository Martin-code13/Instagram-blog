import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Username(Base):
    __tablename__ = 'username'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('username.id'))
    user_to_id = Column(Integer, ForeignKey('username.id'))
    



class Comment(Base):
    __tablename__ = 'comment.id'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    comments = relationship("Comments", backref="comments")



class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    username_id = Column(Integer, ForeignKey('username.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    





    

    

# class Address(Base):
#     __tablename__ = 'address'
    
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
