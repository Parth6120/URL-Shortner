from fastapi import APIRouter, HTTPException, Depends
from api.v1.schema import URLShortnerRequest
from services.url_shortener import URLShortenerService, get_url_shortener_service

router = APIRouter()

@router.post("/shorten", tags= ["Write"])
async def url_input(
    payload: URLShortnerRequest,
    service: URLShortenerService = Depends(get_url_shortener_service)
):

    raw_url = str(payload.target_URL)

    short_code = service.shorter_url(raw_url)

    return {
        "original_url": raw_url,
        "short_url": f"https://short.ty/{short_code}"
    }