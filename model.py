import os
import datetime

from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=100)
    email = fields.CharField(max_length=50, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class Token(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="tokens")
    token = fields.CharField(max_length=100, unique=True)
    target_email = fields.CharField(max_length=50)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class Students_info(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
    stuno = fields.CharField(max_length=20, unique=True)
    photoname = fields.CharField(max_length=100)
    modeofstudy = fields.CharField(max_length=40)
    email = fields.CharField(max_length=50, unique=True)
    validuntil = fields.DateField()
    idcardpath = fields.CharField(max_length=200)
    createdtoken = fields.CharField(max_length=200)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

