#!/usr/bin/python3
"""user inherits from base"""
from models.base_model import BaseModel


class User(BaseModel):
    """defines public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
