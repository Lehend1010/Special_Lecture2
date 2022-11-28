import unittest
from speciallecture import CSVPrinter

class TestCSVPrinter (unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("Sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))
        
    def test_read2(self):
        printer = CSVPrinter("Sample.csv")
        line = printer.read()
        self.assertEqual(" bbb2",line[1][1])
        
    def test_read3(self):
        with self.assertRaises(FileNotFoundError) as e:
            printer = CSVPrinter("yample.csv")
            line = printer.read()
            print(line)
