
import xlrd
from zipfile import ZipFile
datafile = "/home/khalef/Workspace/Data wrangling with Mongodb/Data Extraction Fundamentals/2013_ERCOT_Hourly_Load_Data.xls"


#def open_zip(datafile):
#    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#        myzip.extractall()


workbook = xlrd.open_workbook(datafile)
xl_sheet = workbook.sheet_by_index(0)

#sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

max = 0
min = 100000
avg = 0
max_indice = 0
min_indice = 0
somme = 0 
num_cols = xl_sheet.ncols   # Number of columns
for row_idx in range(1,xl_sheet.nrows):    # Iterate through rows
       cell_obj = xl_sheet.cell_value(row_idx, 1)  # Get cell object by row, col
       somme += float(cell_obj)
       if(float(cell_obj) > max):
           max = float(cell_obj)
           max_indice = row_idx
           
       if(float(cell_obj) < min):
           min = float(cell_obj)
           min_indice = row_idx
max_time = xl_sheet.cell_value(max_indice,0)
min_time = xl_sheet.cell_value(min_indice,0)         
           
           
           
avg = somme / xl_sheet.nrows
print("avg" ,avg)
print("max :",max , "min :",min)
print("max_indice:",max_indice,"min_indice:",min_indice)

print(xlrd.xldate_as_tuple(max_time, 0),xlrd.xldate_as_tuple(min_time, 0))