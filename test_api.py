import requests

# url = 'http://127.0.0.1:5000/'
# final_url = url+'result/5'
# print(final_url)
# response = requests.get('http://127.0.0.1:5000/mul/5/6')
# print(response.json())

# name = input('Enter the name: ')
# response_1 = requests.get('http://127.0.0.1:5000/info/{}'.format(name))
# print(response_1.json())

response_video = requests.put('http://127.0.0.1:5000/info/10', {'likes':100})
print(response_video.json())