import openpyxl

# Load the Excel workbook
workbook = openpyxl.load_workbook('Book1.xlsx')
# Select the worksheet you want to work with
worksheet = workbook['Sheet1']

# Specify the coordinates of the cell you want to retrieve
cell_coordinate = 'B2'

# Get the value of the specified cell
cell_value = worksheet[cell_coordinate].value

# Print the value
print("Value of cell ", cell_coordinate, ":", cell_value)


x = worksheet['F2'].value
print("Random ass value", x*8)

y = worksheet.cell(2, 6).value

print(y*9)