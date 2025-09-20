import xlsxwriter
from main1 import array1, array2

 
def writer():
    book = xlsxwriter.Workbook(r'C:\Users\Sonic\OneDrive\Рабочий стол\After Christ\pythonPROJECTS\power_unit\git_les\Table_gpu_Pblock.xlsx')
    page1 = book.add_worksheet('Видеокарта')
    page2 = book.add_worksheet('Блок питания')
    
    data_array1 = list(array1())
    row = 0
    for item in data_array1:
        page1.write(row, 0, item[0])
        page1.write(row, 1, item[1])
        row += 1
    
    
    data_array2 = list(array2())
    row = 0
    for item in data_array2:
        page2.write(row, 0, item[0])
        page2.write(row, 1, item[1])
        page2.write(row, 2, item[2])
        row += 1
    
    book.close()


writer()