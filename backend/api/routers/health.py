from fastapi import APIRouter


router = APIRouter()


@router.get("", status_code=200, operation_id="healthCheck")
def health():
    """
    General health check endpoint
    """
    return {"status": "ok"}
