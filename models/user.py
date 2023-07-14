#!/usr/bin/python3
"""user inherits from base"""
from models import BaseModel


class User(BaseModel):
    """initializes class user """
    def __init__(self, *args, **kwargs):
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        super().__init__()
