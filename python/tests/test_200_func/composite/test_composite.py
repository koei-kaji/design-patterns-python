import pytest

from src.composite.directory import Directory
from src.composite.entry import FileTreatmentException
from src.composite.file import File


class TestEntry:
    def test_exc_call_add_with_file(self) -> None:
        file = File(name="dummy", size=999)

        with pytest.raises(FileTreatmentException):
            file.add(File(name="sub", size=10))

    def test_normal(self) -> None:
        # TODO: テストが面倒なのでとりあえず標準出力
        print("Making root entries...")
        dir_root = Directory(name="root")
        dir_bin = Directory(name="bin")
        dir_tmp = Directory(name="tmp")
        dir_usr = Directory(name="usr")
        dir_root.add(dir_bin)
        dir_root.add(dir_tmp)
        dir_root.add(dir_usr)
        dir_bin.add(File(name="vi", size=10000))
        dir_bin.add(File(name="latex", size=20000))
        dir_root.print_list()

        print("")
        print("Making user entries...")
        dir_ned = Directory(name="ned")
        dir_robb = Directory(name="robb")
        dir_sansa = Directory(name="sansa")
        dir_usr.add(dir_ned)
        dir_usr.add(dir_robb)
        dir_usr.add(dir_sansa)
        dir_ned.add(File(name="diary.html", size=100))
        dir_ned.add(File(name="composite.py", size=200))
        dir_robb.add(File(name="memo.tex", size=300))
        dir_sansa.add(File(name="game.doc", size=400))
        dir_sansa.add(File(name="junk.mail", size=500))
        dir_root.print_list()

    def test_normal_parent(self) -> None:
        # TODO: テストが面倒なのでとりあえず標準出力
        dir_root = Directory(name="root")
        dir_usr = Directory(name="usr")
        dir_root.add(dir_usr)

        dir_ned = Directory(name="ned")
        dir_usr.add(dir_ned)

        file = File(name="dummy.txt", size=100)
        dir_ned.add(file)

        dir_root.print_list()

        print("")
        print(f"file: {file.get_full_name()}")
        print(f"ned: {dir_ned.get_full_name()}")
