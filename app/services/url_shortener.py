
from services.utils import encode_base62

class URLShortenerService:
    def __init__(self):
        self._current_id = 100000
        self._url_database = {}

    def shorter_url(self, raw_url: str)-> str:
        unique_id = self._current_id

        short_code = encode_base62(unique_id)
        print(f"Original_url: {raw_url} -> Short url: {short_code}" )
        
        self._url_database[short_code] = raw_url

        # Update the instance variable, not the local variable
        self._current_id += 1

        return short_code
    
    def get_original_url(self, short_code):
        return self._url_database.get(short_code)

# Create a single instance to be reused across all requests
url_shortener_service = URLShortenerService()
def get_url_shortener_service():
    return url_shortener_service
