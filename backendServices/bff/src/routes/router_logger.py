from fastapi import APIRouter

from backendServices.domain.src.services.db_connector import get_collection
from backendServices.shared.utils.config import LOG_COLLECTION, LOG_DB

router = APIRouter()

log_collection = get_collection(LOG_COLLECTION, LOG_DB)


@router.get("/logs")
async def get_logs():
    """Fetch and return logs from MongoDB"""
    coll = await log_collection
    logs = coll.find().sort("timestamp", -1).limit(100)
    return {"logs": list(logs)}
