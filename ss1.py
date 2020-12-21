import smartsheet
import time
import json

# Initialize client
access_token = 'qkxytqvgpu7qu0ujitlpwc32j1'
ss_client = smartsheet.Smartsheet(access_token)

# Make sure we don't miss any errors
ss_client.errors_as_exceptions(True)

print("WELCOME")

search_string = "ABHA DAILY REPOT"

def print_sheet_name(ss_client, ss_name):
  search_results = ss_client.Search.search(ss_name).results
  sheet_id = next(result.object_id for result in search_results if result.object_type == 'sheet')
  the_sheet = ss_client.Sheets.get_sheet(sheet_id)
  print("Sheet Name : ", the_sheet.name)
  print("Sheet ID : ", the_sheet.id)
  return the_sheet

the_sheet = print_sheet_name(ss_client,search_string)
sheet_id = the_sheet.id

the_rows = the_sheet.rows
print("ROWS TYPE : ", type(the_rows))

the_row_count = the_sheet.total_row_count
print("ROWS COUNT : ", the_row_count)

cols = the_sheet.get_columns(sheet_id)

cols_count = cols.total_count
print("No of Cols :", cols_count)

for n in range(cols_count)
  print(cols.title)
  if(n==3):
    break

col_title ="WORK DONE"

col = the_sheet.get_column_by_title(col_title)

print("COL NAME : ", col.title)
print("COL ID : ", col.id)

for n in range(the_row_count):
  print("ROW ID : ", the_rows[n].id)
  the_row = the_rows[n]
  the_col = the_row.get_column(col.id)
  print(the_col.value)
  print(the_rows[n])
  if(n==2):
    break
  time.sleep(2)




        
print("THE END")
