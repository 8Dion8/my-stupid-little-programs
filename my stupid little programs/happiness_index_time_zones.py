import requests as r
from bs4 import BeautifulSoup
import openpyxl as o
import matplotlib.pyplot as plt
'''
url = 'https://timezonedb.com/time-zones'
timezones = {}
final = {}

page = r.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all(class_='default')[0]
rows = table.find_all('tr')[1:]

for i in rows:
    collumns = i.find_all('td')
    try:
        timezone = collumns[3].text.split()[1]
        parts = timezone.split(':')
    except:pass
    #print(timezone)
    if collumns[1].text in timezones.keys():
        timezones[collumns[1].text].append(eval("".join(parts[0].split('0')) + '.' + str(int(parts[1])//6)))
    else:
        timezones[collumns[1].text] = [eval("".join(parts[0].split('0')) + '.' + str(int(parts[1])//6))]


print(timezones)
'''
wb = o.load_workbook('WHR20_DataForFigure2.1.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')

happiness = sheet['A1':'C154']
print(happiness)

#print(final)