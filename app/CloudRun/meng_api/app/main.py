#!/usr/bin/python
# -*- coding: utf8 -*-

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import sample

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


# internal tools routers
app.include_router(sample.router, prefix="/sample")