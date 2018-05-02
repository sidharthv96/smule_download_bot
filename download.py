import urllib.request
import requests
x = requests.get('URL').text
print(x[x.find('<title>') + 7 : x.find('</title>')-9]+".m4a")
urllib.request.urlretrieve(x.split('twitter:player:stream" content="')[1].split('">')[0].replace('amp;', ''), x[x.find('<title>') + 7 : x.find('</title>')-9]+".m4a")