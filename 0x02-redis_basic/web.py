#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable, Optional


redis_store = redis.Redis(decode_responses=True)


def data_cacher(method: Callable[[str], str]) -> Callable[[str], str]:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''The wrapper function for caching the output.
        '''
        redis_store.incr(f'count:{url}', amount=1)
        result: Optional[str] = redis_store.get(f'result:{url}')
        if result is not None:
            return result
        # Fetch new result if not cached
        result = method(url)
        # Reset the count and cache the new result with expiration time
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    return requests.get(url).text
