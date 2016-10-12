#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------

import urllib.request
from datetime import datetime
from datetime import timedelta
import sys

DayOfWeek = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday') 
#Monday = 0,Tuesday = 1, ... Sunday = 6
base_url = "http://dl.loveq.cn/program/"

if __name__ == '__main__':

    args = sys.argv
    if len(args) < 3:
        print("Usage:loveq.py save_directory from_date(%Y-%m-%d) [to_date]")
        exit()

    save_dir = args[1]
    from_date_str = args[2]
    if len(args) == 4:
        to_date_str = args[3]
    else:
        to_date_str = from_date_str    

    from_date = datetime.strptime(from_date_str,'%Y-%m-%d')
    #print(from_date)

    if to_date_str != from_date_str:
        to_date = datetime.strptime(to_date_str,'%Y-%m-%d')
        #print(to_date)

        while to_date != from_date : 
            week = from_date.weekday()
            if DayOfWeek[week] != 'Saturday' and DayOfWeek[week] != 'Sunday' :
                #print('unavailable')
                from_date = from_date + timedelta(days=1) 
                continue
            else :
                #print(from_date)

                date = from_date.strftime('%Y-%m-%d')
                #print(date)
                filename = save_dir + '/' + date + "-LoveQ.mp3"
                #print(filename)
                target_url = base_url + "LoveQ.cn_" + date + "-1.mp3"
                print ("Downloading",target_url)
                urllib.request.urlretrieve(target_url, filename)

                from_date = from_date + timedelta(days=1) 
        
        print("Tasks Finish!")            


    else:   #if to_date_str == from_date_str
        week = from_date.weekday()
        if DayOfWeek[week] != 'Saturday' and DayOfWeek[week] != 'Sunday' :
            print("It is not an available date for download!")
            exit() 

        date = from_date.strftime('%Y-%m-%d')
        #print(date)
        filename = save_dir + '/' + date + "-LoveQ.mp3"
        #print(filename)
        target_url = base_url + "LoveQ.cn_" + date + "-1.mp3"
        print ("Downloading",target_url)
        urllib.request.urlretrieve(target_url, filename)
        print("Finish!")

