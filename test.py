import unittest
from speciallecture.speciallecture import CSVPrinter

class TestCSVPrinter (unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("test/Sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))
        
    def test_read2(self):
        printer = CSVPrinter("test/Sample.csv")
        line = printer.read()
        self.assertEqual(" bbb2",line[1][1])
        
    def test_read3(self):
        try:
            printer = CSVPrinter("test/Sample.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except ValueError as e:
            print("Error: ",e)