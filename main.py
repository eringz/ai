from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Thank you for calling"}