from __future__ import annotations

from typing import Generic, TypeVar
from collections.abc import Callable

from ._base import FullDunder

__all__ = ["BroadcastList"]

T_co = TypeVar("T_co", covariant=True)


class BroadcastList(list, Generic[T_co]):
    @property
    def bc(self) -> Broadcaster[T_co]:
        return Broadcaster(self)


class Broadcaster(FullDunder, Generic[T_co]):
    __slots__ = ("__value",)

    def __init__(self, sequence: BroadcastList[T_co], /) -> None:
        self.__value = sequence

    def __getattr__(self, name: str, /) -> Callable[..., BroadcastList] | BroadcastList:
        if not self.__value:
            # Skip operations
            return BroadcastList()

        if callable(getattr(self.__value[0], name)):
            # broadcast callables
            def broadcaster(*args, **kwargs):
                return BroadcastList(getattr(i, name)(*args, **kwargs) for i in self.__value)
            return broadcaster

        else:
            # broadcast attributes
            return BroadcastList(getattr(i, name) for i in self.__value)

    def __setattr__(self, name: str, value) -> None:
        if name.removeprefix("_Broadcaster") in self.__slots__:
            object.__setattr__(self, name, value)
        else:
            super().__setattr__(value)

    def __str__(self) -> str:
        return repr(self)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.__value!r})"

    def str(self) -> BroadcastList[str]:
        return BroadcastList(str(i) for i in self.__value)

    def repr(self) -> BroadcastList[str]:
        return BroadcastList(repr(i) for i in self.__value)
