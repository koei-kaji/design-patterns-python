from typing import List, MutableSequence

from pydantic import BaseModel

from src.common.custom_typing import Comparable


class Test(BaseModel):
    data: MutableSequence[Comparable]


# Test(data=[1, 2, 3])
#
