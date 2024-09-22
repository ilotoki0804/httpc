from __future__ import annotations

import typing

from selectolax.parser import HTMLParser, Node, Selector
from httpx._models import Response

from ._broadcaster import BroadcastList

__all__ = ["CSSTool", "CSSResponse"]

T = typing.TypeVar("T")


class CSSTool:
    __slots__ = "text", "_cache"

    def __init__(self, text: str | None) -> None:
        if text is not None:
            self.text: str = text

    def parse(self) -> HTMLParser:
        try:
            return self._cache
        except AttributeError:
            self._cache = HTMLParser(self.text)
            return self._cache

    def select(self, query: str) -> Selector:
        result = self.parse().select(query)
        if result is None:
            raise ValueError(f"{self} does not have root node.")
        return result

    def css(self, query: str) -> BroadcastList[Node]:
        return BroadcastList(self.parse().css(query))

    def css_only(self, query: str, remain_ok: bool = False) -> Node:
        css_result = self.parse().css(query)
        css_result_len = len(css_result)

        if css_result_len == 0:
            raise ValueError(f"Query {query!r} matched with no nodes.")
        elif remain_ok or css_result_len == 1:
            return css_result.pop()
        else:
            raise ValueError(f"Query {query!r} matched with {css_result_len} nodes.")

    @typing.overload
    def css_one(self, query: str) -> Node | None: ...

    @typing.overload
    def css_one(self, query: str, default: T) -> Node | T: ...

    def css_one(self, query, default=None):
        return self.parse().css_first(query, default=default)


class CSSResponse(Response, CSSTool):
    def __init__(self, response: Response) -> None:
        self.__dict__ = response.__dict__
