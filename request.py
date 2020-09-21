import requests

r = requests.get('https://bpnet.gbp.ma/Public/FinaServices/ExchangeRate')

print(r.headers)