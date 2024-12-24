#! /usr/bin/python3

import re
from pydantic import BaseModel, Field, validator
from datetime import datetime

""" defining validation functions later we could add to them """

def validate_password(line:str):
    regex =\
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if re.match(pattern, line):
        return password
    else: raise ValueError("Weak password")

def validate_email(email:str):
    regex = r"^[a-z0-9]+[\._-]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}$"
    if re.match(regex, email):
        return email
    else:
        raise ValueError("Invalid input")

""" defining class models """"
        
class User(BaseModel):
    """ class for every normal user """
    id           :int
    bio          :str=""
    email        :str 
    username     :str
    is_staff     :False
    is_admin     :False
    is_active    :False
    password_hash:str
    date_joined  :datetime | None = None
    last_login   :datetime | None = None
    profile_image:str | None = Field(None, 
                                     description="URL /path to imaage file" 
                                    )
                                    
    def __init__(self, **data ):
        for field, value in data.items():
            setattr(self, field, value)

class UserAdmin(User):
    pass


class NewUserRegistration(BaseModel):
    email     :str
    username  :str
    password  :str
    
    # validate email
    @validator("email")
    def validate_email(cls, email):
        return validate_email(email)
    
    #validate password
    @validator("password")
    def validate_password(cls, password):
        return validate_password(password) 


class Post(BaseModel):
    """ Model that validates and defines every post on the site"""
    id              :int
    slug            :str #to know about this check models.txt    
    title           :str
    content         :str
    author_id       :int #(Foreign Key to user)
    created_at      :datetime
    category_id     :int #(Foreign key to PostCategory)    
    published_at    :datetime
    featured_image  :str
    

class PostCategory(BaseModel):
    """ Model to organize post made based on it's content"""
    id          :int
    name        :str=""
    decription  :str=""



class Category(BaseModel):
    id              :int
    name            :str=""
    description     :str=""
 
