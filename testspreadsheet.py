import unittest
import spreadsheet

class TestSpreadsheetFunctions(unittest.TestCase):

    def setUp(self):
        matr = [[str(x) for x in xrange(9)] for x in xrange(26)]
        self.testspreadsheet = spreadsheet.Spreadsheet(matr)

    def test_get_value_default(self):
        for i in xrange(26):
            for j in xrange(1,10):
                self.assertEqual(self.testspreadsheet.get_value(i,j),j-1)
        self.__show_helper__()        
                
    def test_set_value_formula(self):
        self.testspreadsheet.set_value(0,1,"B2+C3") # 20
        self.testspreadsheet.set_value(1,2,"D4+E5") # 3 + 4 = 7
        self.testspreadsheet.set_value(2,3,"Z9+5")  # 8 + 5 = 13

        self.assertEqual(self.testspreadsheet.get_value(0,1),20)
        self.assertEqual(self.testspreadsheet.get_value(1,2),7)
        self.assertEqual(self.testspreadsheet.get_value(2,3),13)
        self.__show_helper__()

    def __show_helper__(self):
        print "\n\n-------------------------------------------------\n"    
        for i in xrange(26):
            for j in xrange(1,10):
                print self.testspreadsheet.get_value(i,j),
            print '\n'    
