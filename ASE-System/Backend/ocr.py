import requests
from pprint import pprint
regions = ['gb', 'tz'] # Change to your country
with open('media/', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 97b701930466ea9f17b39d28a213ea9b8ff8fffe'})
#pprint(response.json())
data = response.json()
s=(data['results'][0]['plate'][0]['fp'])
b=str(s).upper()
print(b)