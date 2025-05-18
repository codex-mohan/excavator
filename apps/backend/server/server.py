from fastapi import FastAPI

app = FastAPI(title="Skyhigh API", description="""Skyhigh API for the backend""", version="0.1.0")


@app.get("/")
async def root():
    """
    The root endpoint of the API.

    This endpoint is not for use, and exists only to provide a convenient target
    for tools like curl or Postman to test the API's health.

    Returns:
        dict: A dictionary containing a single key-value pair, with the key
            "message" and the value "The root Endpoint is not for use."
    """
    return {"message": "The root Endpoint is not for use."}