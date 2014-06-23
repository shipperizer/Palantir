You have a spreadsheet with 26 rows and 9 columns. The rows are labeled A-Z and the columns are 
numbered 1-9. Each cell is identified by its row label followed by its column number.
Each cell in the spreadsheet either has a value (a decimal number), or a formula which can be used to 
compute its value. The formula is an expression with the four standard binary operators (+, -, *, /), and 
operands as either decimal numbers, or other cell identifiers.
Your goal is to implement a class that allows you to get the value of a specified cell in the spreadsheet. 
ClassName: Spreadsheet
Constructor:
− Spreadsheet(String[][] spreadsheetCells) : Creates a Spreadsheet where spreadsheetCells[i]
[j] is the initial expression/value specifying the contents of the cell in the ith row and jth 
column.
Methods:
− double getValue(int row, int column): Returns the decimal value of the corresponding cell.
Questions to think about before you begin:
− What is a good way to specify an input expression for the problem?
− Efficiency: How efficiently can your code process getValue method calls?
− Bonus: Also implement a setValue method. void setValue(int row, int column, String value) 
sets the value of the corresponding cell. “value” can either represent a decimal value, or an 
expression. Avoid recomputing values of cells not affected by this operation. 
Evaluation:
− We will be evaluating your solution on class structure/design, correctness, efficiency (both 
in space and time), readability, and test coverage. Please keep all of those aspects in mind 
as you work on this problem.
Submitting your answer:
− When you’re ready (or when 4 hours has elapsed), please email us your solution. We 
recommend including a paragraph or two describing how you would continue to improve 
your solution if you had more time.