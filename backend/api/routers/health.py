from fastapi import APIRouter

router = APIRouter()


@router.get("", status_code=200, operation_id="healthCheck")
def health() -> dict[str, str]:
    """General health check endpoint"""
    return {"status": "ok"}
