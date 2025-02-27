#!/usr/bin/python
# -*- coding: utf8 -*-

from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def hello():
    print("Hello World!")
    return {'status_code': 200, 'content':"OK, Hello World!"}