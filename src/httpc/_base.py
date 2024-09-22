from __future__ import annotations

import logging
import re

logger = logging.getLogger("httpc")
logger.setLevel(logging.INFO)


def extract_headers(curl_command: str) -> dict[str, str]:
    raw_headers = re.findall(r"(?<=\n  -H ')([^:]+): (.*)(?=' \\\n|'\Z)", curl_command.strip())
    headers = dict(raw_headers)
    return headers


class FullDunder:
    def __getattr(self, __name, *args, **kwargs):
        return getattr(self, __name)(args, kwargs)

    async def __agetattr(self, __name, *args, **kwargs):
        return await getattr(self, __name)(args, kwargs)

    def __setattr__(self, *args, **kwargs):
        return self.__getattr("__setattr__", *args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        return self.__getattr("__setitem__", *args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        return self.__getattr("__getitem__", *args, **kwargs)

    def __delitem__(self, *args, **kwargs):
        return self.__getattr("__delitem__", *args, **kwargs)

    def __eq__(self, *args, **kwargs):
        return self.__getattr("__eq__", *args, **kwargs)

    def __ge__(self, *args, **kwargs):
        return self.__getattr("__ge__", *args, **kwargs)

    def __gt__(self, *args, **kwargs):
        return self.__getattr("__gt__", *args, **kwargs)

    def __le__(self, *args, **kwargs):
        return self.__getattr("__le__", *args, **kwargs)

    def __ne__(self, *args, **kwargs):
        return self.__getattr("__ne__", *args, **kwargs)

    def __lt__(self, *args, **kwargs):
        return self.__getattr("__lt__", *args, **kwargs)

    def __hash__(self, *args, **kwargs):
        return self.__getattr("__hash__", *args, **kwargs)

    def __add__(self, *args, **kwargs):
        return self.__getattr("__add__", *args, **kwargs)

    def __and__(self, *args, **kwargs):
        return self.__getattr("__and__", *args, **kwargs)

    def __divmod__(self, *args, **kwargs):
        return self.__getattr("__divmod__", *args, **kwargs)

    def __floordiv__(self, *args, **kwargs):
        return self.__getattr("__floordiv__", *args, **kwargs)

    def __lshift__(self, *args, **kwargs):
        return self.__getattr("__lshift__", *args, **kwargs)

    def __matmul__(self, *args, **kwargs):
        return self.__getattr("__matmul__", *args, **kwargs)

    def __mod__(self, *args, **kwargs):
        return self.__getattr("__mod__", *args, **kwargs)

    def __mul__(self, *args, **kwargs):
        return self.__getattr("__mul__", *args, **kwargs)

    def __or__(self, *args, **kwargs):
        return self.__getattr("__or__", *args, **kwargs)

    def __pow__(self, *args, **kwargs):
        return self.__getattr("__pow__", *args, **kwargs)

    def __rshift__(self, *args, **kwargs):
        return self.__getattr("__rshift__", *args, **kwargs)

    def __sub__(self, *args, **kwargs):
        return self.__getattr("__sub__", *args, **kwargs)

    def __truediv__(self, *args, **kwargs):
        return self.__getattr("__truediv__", *args, **kwargs)

    def __xor__(self, *args, **kwargs):
        return self.__getattr("__xor__", *args, **kwargs)

    def __radd__(self, *args, **kwargs):
        return self.__getattr("__radd__", *args, **kwargs)

    def __rand__(self, *args, **kwargs):
        return self.__getattr("__rand__", *args, **kwargs)

    def __rdiv__(self, *args, **kwargs):
        return self.__getattr("__rdiv__", *args, **kwargs)

    def __rdivmod__(self, *args, **kwargs):
        return self.__getattr("__rdivmod__", *args, **kwargs)

    def __rfloordiv__(self, *args, **kwargs):
        return self.__getattr("__rfloordiv__", *args, **kwargs)

    def __rlshift__(self, *args, **kwargs):
        return self.__getattr("__rlshift__", *args, **kwargs)

    def __rmatmul__(self, *args, **kwargs):
        return self.__getattr("__rmatmul__", *args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        return self.__getattr("__rmod__", *args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        return self.__getattr("__rmul__", *args, **kwargs)

    def __ror__(self, *args, **kwargs):
        return self.__getattr("__ror__", *args, **kwargs)

    def __rpow__(self, *args, **kwargs):
        return self.__getattr("__rpow__", *args, **kwargs)

    def __rrshift__(self, *args, **kwargs):
        return self.__getattr("__rrshift__", *args, **kwargs)

    def __rsub__(self, *args, **kwargs):
        return self.__getattr("__rsub__", *args, **kwargs)

    def __rtruediv__(self, *args, **kwargs):
        return self.__getattr("__rtruediv__", *args, **kwargs)

    def __rxor__(self, *args, **kwargs):
        return self.__getattr("__rxor__", *args, **kwargs)

    def __abs__(self, *args, **kwargs):
        return self.__getattr("__abs__", *args, **kwargs)

    def __neg__(self, *args, **kwargs):
        return self.__getattr("__neg__", *args, **kwargs)

    def __pos__(self, *args, **kwargs):
        return self.__getattr("__pos__", *args, **kwargs)

    def __invert__(self, *args, **kwargs):
        return self.__getattr("__invert__", *args, **kwargs)

    def __index__(self, *args, **kwargs):
        return self.__getattr("__index__", *args, **kwargs)

    def __trunc__(self, *args, **kwargs):
        return self.__getattr("__trunc__", *args, **kwargs)

    def __floor__(self, *args, **kwargs):
        return self.__getattr("__floor__", *args, **kwargs)

    def __ceil__(self, *args, **kwargs):
        return self.__getattr("__ceil__", *args, **kwargs)

    def __round__(self, *args, **kwargs):
        return self.__getattr("__round__", *args, **kwargs)

    def __iter__(self, *args, **kwargs):
        return self.__getattr("__iter__", *args, **kwargs)

    def __len__(self, *args, **kwargs):
        return self.__getattr("__len__", *args, **kwargs)

    def __reversed__(self, *args, **kwargs):
        return self.__getattr("__reversed__", *args, **kwargs)

    def __contains__(self, *args, **kwargs):
        return self.__getattr("__contains__", *args, **kwargs)

    def __next__(self, *args, **kwargs):
        return self.__getattr("__next__", *args, **kwargs)

    def __int__(self, *args, **kwargs):
        return self.__getattr("__int__", *args, **kwargs)

    def __bool__(self, *args, **kwargs):
        return self.__getattr("__bool__", *args, **kwargs)

    def __complex__(self, *args, **kwargs):
        return self.__getattr("__complex__", *args, **kwargs)

    def __float__(self, *args, **kwargs):
        return self.__getattr("__float__", *args, **kwargs)

    def __format__(self, *args, **kwargs):
        return self.__getattr("__format__", *args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.__getattr("__call__", *args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.__getattr("__str__", *args, **kwargs)

    def __repr__(self, *args, **kwargs):
        return self.__getattr("__repr__", *args, **kwargs)

    def __bytes__(self, *args, **kwargs):
        return self.__getattr("__bytes__", *args, **kwargs)

    def __fspath__(self, *args, **kwargs):
        return self.__getattr("__fspath__", *args, **kwargs)

    def __sizeof__(self, *args, **kwargs):
        return self.__getattr("__sizeof__", *args, **kwargs)

    async def __aiter__(self, *args, **kwargs):
        return await self.__agetattr("__aiter__", *args, **kwargs)

    async def __anext__(self, *args, **kwargs):
        return await self.__agetattr("__anext__", *args, **kwargs)

    async def __await__(self, *args, **kwargs):
        return await self.__agetattr("__await__", *args, **kwargs)
