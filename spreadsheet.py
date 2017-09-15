import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Reconhecimento').sheet1

reconhecimento = sheet.get_all_records()

seerow = sheet.row_values(1)
seecol = sheet.col_values(1)
seecell = sheet.cell(2,1).value

sheet.update_cell(3,1,'usando o update')

'''
row = ["Usando","o", "insert"]
index = 4
sheet.insert_row(row, index)
'''
#sheet.delete_row(3)


#print(reconhecimento)

print(sheet.row_count)

#print(seerow)

#print(seecol)

#print(seecell)
