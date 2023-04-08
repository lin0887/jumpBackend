import requests

url = 'http://120.125.89.209:8000/uploadVideo/A1111'

with open('./009.mp4', 'rb') as f:
    r = requests.post(url, files={'video': f})
    
print(r.status_code)
