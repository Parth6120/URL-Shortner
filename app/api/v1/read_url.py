from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from services.url_shortener import URLShortenerService, get_url_shortener_service

router = APIRouter()

@router.get("/{short_code}", tags=["Read"])
async def redirect_to_url(
    short_code: str,
    service: URLShortenerService = Depends(get_url_shortener_service)
):
    original_url = service.get_original_url(short_code)

    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url)

