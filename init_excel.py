import openpyxl
import xlrd



def init_excel(path):
    loc = path
    wb = openpyxl.open(loc)
    sheet = wb.active
    return sheet, wb



# path="C:\\Users\\Enabling\\Desktop\\Enabling\\data\\data2.xlsx"
# temp=init_excel(path)
# sheet=temp[0]
# wb=temp[1]
# for i in range(1,sheet.nrows):
#     email = sheet.cell_value(i, 0)  # re
#     firstname = sheet.cell_value(i, 1)
#     lastname = sheet.cell_value(i, 2)
#     print(email)

