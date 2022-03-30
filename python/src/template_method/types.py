from pydantic import ConstrainedStr


class Char(ConstrainedStr):
    min_length = 1
    max_length = 1
