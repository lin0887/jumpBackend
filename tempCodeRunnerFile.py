import requests
import time
num = int(input('input id:'))
headers = {
    'accept': 'application/json',
}

files = {
    'file': ('A1111.MOV',open('.//A1111.MOV', 'rb')),
}
begin = 1
end = 2
for i in range (begin,end):
    files = {
        'file': ('A1111.MOV',open('.//A1111.MOV', 'rb')),
    }
    response = requests.post('http://120.125.89.209:8000/uploadVideo/A'+str(i), headers=headers, files=files)
    print(i)
    time.sleep(30)