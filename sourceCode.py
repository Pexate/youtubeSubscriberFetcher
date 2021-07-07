
import urllib.request
import json
ime = input("Input the name of a youtuber with over 5k subscribers: ")

key = '' # input your own key cause i am not going to leak mine


try:    
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&key="+key+"&forUsername="+ime).read()
    sub = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    if int(sub) > 5000:
        print(ime+" has "+"{:,d}".format(int(sub)) + " subscribers")
    else:
        print("The specified youtuber does not exceed 5,000 subscribers!")
except:
    print("Channel was not found (try to input original channel name)")

 