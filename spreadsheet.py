import re

class Spreadsheet:
    
    def __init__(self,spreadsheetCells):
        self.spreadsheet=self.__spreadsheet__(spreadsheetCells)            

    def get_value(self,row,column):
        if column < 1 :
            print "Column value {0} not valid".format(column)
            return 0
        return self.__get__value(row,column)

    def set_value(self,row,column,value):
        if column < 1 :
            print "Column value {0} not valid".format(column)
            return 0
        self.__set_value__(row,column,value)
        
    def __get__value(self,row,column):
        
        try:
            return float(self.spreadsheet[row][column-1])
        except:
            return float(self.__parser__(row,column))

    def __set_value__(self,row,column,value):
        self.spreadsheet[row][column-1]=str(value).upper()

    def __parser__(self,row,column):
        cell= self.spreadsheet[row][column-1]
        values={}
        match = re.findall( r'([A-Z]\d)', str(self.spreadsheet[row][column-1]))
        for el in match:
            if el not in values:
                values[el]=self.__get__value(ord(el[0])-65,int(el[1])) # recursive point ASCII 'A'=65
        for el in match:
            cell=cell.replace(str(el),str(values[el]))           
        return eval(cell)    

    def __spreadsheet__(self,spreadsheetCells):
        tmp=[[0 for x in xrange(9)] for x in xrange(26)]
        for i in xrange(26):
            for j in xrange(9):
                tmp[i][j]=spreadsheetCells[i][j]
        return tmp        
