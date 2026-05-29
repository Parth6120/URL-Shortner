from pydantic import BaseModel, HttpUrl

class URLShortnerRequest(BaseModel):
    target_URL : HttpUrl