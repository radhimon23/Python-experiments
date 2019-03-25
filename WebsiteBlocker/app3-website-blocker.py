import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="/Users/radhikamonpara/WebsiteBlocker/hosts"
redirect="172.20.10.2"
website_list=["www.facebook.com","facebook.com","https://www.facebook.com"]

#line 11 ma 13 to 16 working hours mukya che.. you can change according to your schedule,the time of your work hours for eg for me i work from 13 to 1
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
#mac ma run as admin karvu hoi to terminal ma lakh sudo python filename.py
