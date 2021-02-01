import requests

url = 'http://127.0.0.1:5000/'
final_url = url+'result/5'
print(final_url)
response = requests.get('http://127.0.0.1:5000/mul/5/6')
print(response.json())