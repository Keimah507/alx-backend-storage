#!/usr/bin/env python3
"""Redis tasks"""
from functools import wraps
from typing import Optional, Callable, Union
import redis
import uuid


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function"""
    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(in_key, str(args))
        res = method(self, *args)
        self._redis.rpush(out_key, str(args))
        return res
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of the Cache class have been called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        k = method(self, args)
        self._redis.incr(key)
        return k

    return wrapper


def replay(method: Callable):
    """Displays history of calls of a particular function"""
    client = redis.Redis()
    store_name = Cache.store.__qualname__

    inputs = client.lrange("{} inputs".format(store_name), 0, -1)
    outputs = client.lrange("{} outputs".format(store_name), 0, -1)

    print("{] was called {} times:".format(store_name,
                                           client.get(store_name).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(store_name, i.decode("utf-8"),
                                          o.decode("utf-8")))


class Cache:
    def __init__(self, _redis=None):
        """Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key, stores input data in Redis using the random key and returns the key
        """
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Converts data in Redis cache to desired format"""
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)
