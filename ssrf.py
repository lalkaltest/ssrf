import requests

x = requests.get('http://lalka.eu.ngrok.io.ngrok.io/ssrf.ph')
print(x.status_code)
