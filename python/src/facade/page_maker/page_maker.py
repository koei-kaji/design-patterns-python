from io import FileIO
from pathlib import Path
from typing import Dict, Final

from .database import Database
from .html_writer import HtmlWriter

DIR_BASE: Final[Path] = Path(__file__).parent


class PageMaker:
    def __init__(self) -> None:
        raise Exception("Database class cannot be instantiation.")

    @staticmethod
    def _get_mail_properties() -> Dict[str, str]:
        return Database.get_properties(str(DIR_BASE.parent / "maildata"))

    @staticmethod
    def make_welcome_page(mail_address: str, file_name: str) -> None:
        mail_properties = PageMaker._get_mail_properties()
        user_name = mail_properties[mail_address]
        writer = HtmlWriter(writer=FileIO(file=file_name, mode="w"))
        writer.title(f"Welcome to {user_name}'s page!")
        writer.paragraph(f"{user_name}のページへようこそ")
        writer.paragraph("メール待っていますね")
        writer.mailto(mail_address, user_name)
        writer.close()

        print(f"{file_name} is created for {mail_address} ({user_name})")

    @staticmethod
    def make_link_page(file_name: str) -> None:
        mail_properties = PageMaker._get_mail_properties()
        writer = HtmlWriter(writer=FileIO(file=file_name, mode="w"))
        writer.title("Link page")
        for key, value in mail_properties.items():
            writer.mailto(key, value)
        writer.close()
