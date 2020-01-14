import requests
from datetime import datetime
#add proper address
resp = requests.get('http://192.168.99.101:30814/stats')
 
if resp.status_code == 200:
    print (resp.content)
elif resp.status_code == 400:
        print ("Status code:400\n Page not found")
elif resp.status_code == 500:
        print ("Status code:500\n Internal Server Error")
else:
    print("Unknown status code: ", resp._content)
 
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f = open("logi.txt", "a")
f.write("resp.content ")
f.write(resp._content)
f.write("Time ")
f.write(current_time)
f.close()