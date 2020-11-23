import requests as r
from bs4 import BeautifulSoup
import openpyxl as o
import matplotlib.pyplot as plt
import collections

plt.style.use('dark_background')

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
wb = o.load_workbook('/Users/glebsvarcer/Desktop/my-stupid-little-programs/test/data.xlsx')

sheet = wb.get_sheet_by_name('Sheet1')

happiness_countries = sheet['A1':'C154']
print(happiness_countries)

for row in happiness_countries:
    country = row[0].value
    if country in timezones.keys():
        for i in timezones[country]:
            if str(i) in final.keys():
                final[str(i)] = (final[str(i)] + row[2].value)/2
            else:
                final[str(i)] = row[2].value

print(final)

ordered = collections.OrderedDict(sorted(final.items()))

plt.bar([i for i in ordered.keys()],ordered.values(),width=0.5)

plt.show()