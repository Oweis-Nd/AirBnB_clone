#!/usr/bin/python3
"""defines city of user"""
from models.base_model import BaseModel


class City(BaseModel):
    """ the city of the user"""
    state_id = ""
    name = ""
