import urllib.request
import re

link = 'http://www.diabetespilot.com/mac/docs/abbrev'
file = urllib.request.urlopen(link)
f = file.read().decode('utf-8')
data = {}
result = re.findall("(?<=<td>)(.*)(?:<\/td>\n<td>)(.*)(?:<\/td>)", f)

for item in result:
    data[item[1]] = item[0]

with open ('abbrv.py', 'w+') as file:
    file.write('ABBREVIATIONS =' + repr(data))
    file.close()
