import threading
from time import sleep
from typing import Callable

import pytest
from pydantic import BaseModel, StrictStr

from src.common.decorator import synchronized


class User(BaseModel):
    name: StrictStr


class Room(BaseModel):
    _lock = threading.Lock()

    def _use_room(self, user: User) -> None:
        print(f"IN: {user.name} entered.")
        sleep(0.1)
        print(f"OUT: {user.name} exited.")

    def use_room_async(self, user: User) -> None:
        self._use_room(user)

    @synchronized(_lock)
    def use_room_sync(self, user: User) -> None:
        self._use_room(user)


class TestSynchronized:
    @pytest.mark.parametrize(("mode"), [("async"), ("sync")])
    def test_normal(self, mode: str) -> None:
        ned = User(name="Ned")
        robb = User(name="Robb")
        sansa = User(name="Sansa")
        room = Room()

        target: Callable[[User], None]
        if mode == "async":
            target = room.use_room_async
        elif mode == "sync":
            target = room.use_room_sync
        else:
            raise Exception("!?!?!?")

        thread_ned = threading.Thread(target=target, args=(ned,))
        thread_robb = threading.Thread(target=target, args=(robb,))
        thread_sansa = threading.Thread(target=target, args=(sansa,))

        print("")
        print(f"=== MODE: {mode} ===")
        thread_ned.start()
        thread_robb.start()
        thread_sansa.start()
        thread_ned.join()
        thread_robb.join()
        thread_sansa.join()
