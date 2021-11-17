import urllib.request, urllib.parse, urllib.error
import json

#Note that Google is increasingly requiring keys
#for this API
serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input('Enter Location: ')
    if len(adress) < 1 : break

    url = serviceurl + urllib.parse.urlencode(
        {'address' : address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('=== Failure to Retrieve ===')
    print(data)
    continue

print(json.dumps(js, indent=4))

lat = 
