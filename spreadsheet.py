import re

class Spreadsheet:
    
    def __init__(self,spreadsheetCells):
        self.spreadsheet=self.__dict_spreadsheet__(spreadsheetCells)            

    def get_value(self,row,column):
        return self.__get__value(row,column)

    def __get__value(self,row,column):
        try:
            return float(self.spreadsheet[chr(row+65)][column-1])
        except:
            return float(self.__parser__(row,column))

    # working only if there are no multiple occurrences of the same cell in a formula        
    def __parser__(self,row,column):
        cell= self.spreadsheet[chr(row+65)][column-1]
        values={}
        match = re.findall(r'([A-Z]\d)',self.spreadsheet[chr(row+65)][column-1])
        for el in match:
            if el not in values:
                values[el]=self.__get__value(ord(el[0])-65,int(el[1])-1) # recursive point 
        for el in match:
            cell=cell.replace(str(el),str(values[el]))           
        return eval(cell)    

    def __dict_spreadsheet__(self,spreadsheetCells):
        tmp={}
        for i in range(0,26):
            tmp[chr(i+65)]=[]
            for j in range(0,9):
                tmp[chr(i+65)].append(spreadsheetCells[i][j])
        return tmp        


matr=[]
for i in range(0,26):
    tmp=[]
    matr.append(tmp)
    for j in range(0,9):
        matr[i].append(i+j*i)

matr[0][1]="A1+B2+C3+8+A1"

spr=Spreadsheet(matr)        

for i in range(0,26):
    for j in range(0,9):
        print spr.get_value(i,j),
    print "\n"    