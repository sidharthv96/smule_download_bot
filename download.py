import urllib.request
import requests
x = requests.get('http://www.smule.com/p/1695845141_2189897499').text
print(x[x.find('<title>') + 7 : x.find('</title>')-9]+".m4a")
# print(x.split('twitter:player:stream" content="')[1].split('">')[0].replace('amp;', ''))
urllib.request.urlretrieve(x.split('twitter:player:stream" content="')[1].split('">')[0].replace('amp;', ''), x[x.find('<title>') + 7 : x.find('</title>')-9]+".m4a")