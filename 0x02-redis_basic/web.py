import redis
import requests
from functools import wraps


r = redis.Redis(decode_responses=True)


def cache_page(func):
    """Decorator to cache the HTML content of
    URLs with an expiration time and track access count."""
    @wraps(func)
    def wrapper(url):
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"
        r.incr(count_key)
        cached_content = r.get(cache_key)
        if cached_content is not None:
            return cached_content
        result = func(url)
        r.set(cache_key, result, ex=10)
        return result
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL."""
    response = requests.get(url)
    return response.text
