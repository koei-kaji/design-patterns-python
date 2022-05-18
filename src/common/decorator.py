from threading import Lock
from typing import Any, Callable, TypeVar

R = TypeVar("R")


def synchronized(lock: Lock) -> Callable[..., Callable[..., R]]:
    def wrapper(func: Callable[..., R]) -> Callable[..., R]:
        def inner(*args: Any, **kwargs: Any) -> Any:
            with lock:
                return func(*args, **kwargs)

        return inner

    return wrapper
