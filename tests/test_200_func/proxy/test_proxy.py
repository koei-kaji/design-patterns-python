from src.proxy.printable import PrintableIF
from src.proxy.printer_proxy import PrinterProxy


class TestPrinterProxy:
    def test_normal(self) -> None:
        print("")
        printable: PrintableIF = PrinterProxy(name="Alice")
        print(f"名前は現在{printable.get_printer_name()}です")
        printable.set_printer_name("Bob")
        print(f"名前は現在{printable.get_printer_name()}です")
        printable.print("Hello, world.")
