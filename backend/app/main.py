from fastapi import FastAPI
import os
import psycopg2

app = FastAPI(title='DevSecOps Backend')

@app.get('/')
async def root():
    return {"message": "Backend is running securely!"}
