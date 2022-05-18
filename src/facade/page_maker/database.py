from typing import Dict


class Database:
    def __init__(self) -> None:
        raise Exception("Database class cannot be instantiation.")

    @staticmethod
    def get_properties(dbname: str) -> Dict[str, str]:
        filename = f"{dbname}.txt"
        properties: Dict[str, str] = {}

        with open(filename, mode="r", encoding="utf-8") as f:
            for line in f:
                key, value = line.strip().split("=")
                properties[key] = value

        return properties
