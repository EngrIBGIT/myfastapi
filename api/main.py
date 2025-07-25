from fastapi import FastAPI

from mangum import Mangum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



handler = Mangum(app=app)  # This is the handler for AWS Lambda