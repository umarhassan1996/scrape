# Hello World program in Python
    
print "Hello World!\n"

import urllib, json
url = "https://data.police.uk/api/forces"
response = urllib.urlopen(url)
data = json.loads(response.read())
#print data
for i in data:
    print i
    print i['name']
    if i['id'] == 'warwickshire':
        print 'THIS IS WARWICKSHIRE2'
    if 'wilt' in i['id']:
        print 'CONTAINS WARW'
