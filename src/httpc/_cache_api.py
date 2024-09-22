from __future__ import annotations

from typing import Any
from collections import deque

from . import _api as api

__all__ = ["crequest", "cget", "coptions", "chead", "cpost", "cput", "cpatch", "cdelete"]
_caches: deque[tuple[Any, Any, Any, Any]] = deque([], maxlen=127)


def crequest(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if crequest is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.request(*args, **kwargs)
    _caches.append((crequest, args, kwargs, result))
    return result


def cget(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if cget is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.get(*args, **kwargs)
    _caches.append((cget, args, kwargs, result))
    return result


def coptions(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if coptions is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.options(*args, **kwargs)
    _caches.append((coptions, args, kwargs, result))
    return result


def chead(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if chead is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.head(*args, **kwargs)
    _caches.append((chead, args, kwargs, result))
    return result


def cpost(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if cpost is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.post(*args, **kwargs)
    _caches.append((cpost, args, kwargs, result))
    return result


def cput(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if cput is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.put(*args, **kwargs)
    _caches.append((cput, args, kwargs, result))
    return result


def cpatch(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if cpatch is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.patch(*args, **kwargs)
    _caches.append((cpatch, args, kwargs, result))
    return result


def cdelete(*args, **kwargs):
    for func, args_cache, kwargs_cache, value in _caches:
        if cdelete is func and args == args_cache and kwargs == kwargs_cache:
            return value
    result = api.delete(*args, **kwargs)
    _caches.append((cdelete, args, kwargs, result))
    return result
