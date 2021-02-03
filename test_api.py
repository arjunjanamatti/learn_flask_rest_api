import requests

# url = 'http://127.0.0.1:5000/'
# final_url = url+'result/5'
# print(final_url)
# response = requests.get('http://127.0.0.1:5000/mul/5/6')
# print(response.json())

# name = input('Enter the name: ')
# response_1 = requests.get('http://127.0.0.1:5000/info/{}'.format(name))
# print(response_1.json())

# response_video = requests.put('http://127.0.0.1:5000/info/10', {'likes':100})
# print(response_video.json())
# video_id = int(input('Enter the video_id: '))
# response_video_1 = requests.put('http://127.0.0.1:5000/info/{}'.format(video_id), {'likes':100})

data_list = [{'name':'aj', 'views':2, 'likes':10}, 
             {'name':'bj', 'views':12, 'likes':110},
             {'name':'cj', 'views':22, 'likes':210},]

for index, data in enumerate(data_list):
    # print(index, data)
    response = requests.put('http://127.0.0.1:5000/info/{}'.format(index), data)

response = requests.get('http://127.0.0.1:5000/info/1')
print(response.json())
