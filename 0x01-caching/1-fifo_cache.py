#!/usr/bin/env python3
"""
Module: 1-fifo_cache.py
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache"""
    q = []

    def __init__(self):
        '''Initialization'''
        super().__init__()

    def put(self, key, item):
        """Adds an item to a dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            FIFOCache.q.append(key)

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            key_to_be_removed = FIFOCache.q[0]
            self.cache_data.pop(key_to_be_removed)
            print("DISCARD: {}".format(FIFOCache.q.pop(0)))

    def get(self, key):
        """Returns an item based on the key"""
        if (key is None or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
