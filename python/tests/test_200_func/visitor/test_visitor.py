import pytest

from src.visitor.directory import Directory
from src.visitor.element import ElementList
from src.visitor.exc import FileTreatmentException
from src.visitor.file import File
from src.visitor.file_find_visitor import FileFindVisitor
from src.visitor.list_visitor import ListVisitor


class TestEntry:
    def test_exc_call_add_with_file(self) -> None:
        file = File(name="dummy", size=999)

        with pytest.raises(FileTreatmentException):
            file.add(File(name="sub", size=10))


class TestListVisitor:
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
        dir_root.accept(ListVisitor())

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
        dir_root.accept(ListVisitor())


class TestFileFindVisitor:
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

        dir_ned = Directory(name="ned")
        dir_robb = Directory(name="robb")
        dir_sansa = Directory(name="sansa")
        dir_usr.add(dir_ned)
        dir_usr.add(dir_robb)
        dir_usr.add(dir_sansa)
        dir_ned.add(File(name="diary.html", size=100))
        dir_ned.add(File(name="composite.py", size=200))
        dir_robb.add(File(name="memo.tex", size=300))
        dir_robb.add(File(name="index.html", size=350))
        dir_sansa.add(File(name="game.doc", size=400))
        dir_sansa.add(File(name="junk.mail", size=500))

        visitor = FileFindVisitor(ext=".html")
        dir_root.accept(visitor)

        print("")
        print("HTML files are:")
        for file in visitor.get_found_files():
            print(file)


class TestSizeVisitor:
    def test_normal(self) -> None:
        # TODO: テストが面倒なのでとりあえず標準出力
        print("Making root entries...")
        dir_root = Directory(name="root", use_visitor=True)
        dir_bin = Directory(name="bin", use_visitor=True)
        dir_tmp = Directory(name="tmp", use_visitor=True)
        dir_usr = Directory(name="usr", use_visitor=True)
        dir_root.add(dir_bin)
        dir_root.add(dir_tmp)
        dir_root.add(dir_usr)
        dir_bin.add(File(name="vi", size=10000))
        dir_bin.add(File(name="latex", size=20000))
        dir_root.accept(ListVisitor())

        print("")
        print("Making user entries...")
        dir_ned = Directory(name="ned", use_visitor=True)
        dir_robb = Directory(name="robb", use_visitor=True)
        dir_sansa = Directory(name="sansa", use_visitor=True)
        dir_usr.add(dir_ned)
        dir_usr.add(dir_robb)
        dir_usr.add(dir_sansa)
        dir_ned.add(File(name="diary.html", size=100))
        dir_ned.add(File(name="composite.py", size=200))
        dir_robb.add(File(name="memo.tex", size=300))
        dir_sansa.add(File(name="game.doc", size=400))
        dir_sansa.add(File(name="junk.mail", size=500))
        dir_root.accept(ListVisitor())


class TestElementList:
    def test_normal(self) -> None:
        dir_root1 = Directory(name="root1")
        dir_root1.add(File(name="diary.html", size=10))
        dir_root1.add(File(name="index.html", size=20))

        dir_root2 = Directory(name="root2")
        dir_root2.add(File(name="diary.html", size=1000))
        dir_root2.add(File(name="index.html", size=2000))

        element_list = ElementList()
        element_list.append(dir_root1)
        element_list.append(dir_root2)
        element_list.append(File(name="etc.html", size=1234))

        print("")
        element_list.accept(ListVisitor())
