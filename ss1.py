import smartsheet
import time
import threading
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



for i in range(cols_count):
  print(cols.data[i].title)
  if(i==3):
    break

wks_col_title ="WORK DONE"

dt_col_title ="DATE"

wks_col = the_sheet.get_column_by_title(wks_col_title)
dt_col = the_sheet.get_column_by_title(dt_col_title)

print("WKS COL NAME : ", wks_col.title)
print("WKS COL ID : ", wks_col.id)

print("DT COL NAME : ", wks_col.title)
print("DT COL ID : ", dt_col.id)

for n in range(the_row_count):
  print("ROW ID : ", the_rows[n].id)
  the_row = the_rows[n]
  the_wks_col = the_row.get_column(wks_col.id)
  the_dt_col = the_row.get_column(dt_col.id)
  if(the_dt_col.value == "2013-09-19"):
    print(the_wks_col.value)
    print(the_dt_col.value)
    print(the_rows[n])
  if(n==2):
    break
  time.sleep(2)

     
print("THE END")
