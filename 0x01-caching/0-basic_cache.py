#!/usr/bin/env python3
"""
Module: 0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns a new key value pair to the cached_data"""
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
