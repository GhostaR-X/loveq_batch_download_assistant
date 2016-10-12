#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------

import urllib.request
from datetime import datetime 

base_url = "http://dl.loveq.cn/program/"

date = datetime(2016,10,1).strftime('%Y-%m-%d')
print(date)

filename = date + "_LoveQ.mp3"
print(filename)

target_url = base_url + "LoveQ.cn_" + date + "-1.mp3"
#print(target_url)

print ("Downloading",target_url)
urllib.request.urlretrieve(target_url, filename)
print("Finish!")




#url = "http://dl.loveq.cn/program/LoveQ.cn_2016-10-08-1.mp3" 

#print ("Downloading with urllib!")
#urllib.request.urlretrieve(url, "demo.mp3")
#print("Finish!")
