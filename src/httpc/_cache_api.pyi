from typing import Callable
from collections import deque

from httpc._css import CSSResponse

from . import _api as api

__all__ = ["crequest", "cget", "coptions", "chead", "cpost", "cput", "cpatch", "cdelete"]
_caches: deque[tuple[Callable, tuple, dict, CSSResponse]] = deque([], maxlen=127)

crequest = api.request
cget = api.get
coptions = api.options
chead = api.head
cpost = api.post
cput = api.put
cpatch = api.patch
cdelete = api.delete
