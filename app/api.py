from fastapi import FastAPI

app = FastAPI(titile="okteto api")

@app.get("/", tags=["Home"])
def get_root() -> dict:
    return {
        "message": "Welcome to the okteto's app."
    }

@app.post("/", tags=["Home"])
def post_root() -> dict:
    return {
        "message": "Welcome to the okteto's app. (post)"
    }
