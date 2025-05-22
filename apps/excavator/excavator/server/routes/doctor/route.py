from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/doctor", tags=["doctor"])


@router.get("/")
async def doctor():
    """Check the status and condition of the API server"""
    try:
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
