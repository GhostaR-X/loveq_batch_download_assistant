#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Author : GhostaR
# Email  : GhostaR@163.com
# Date   : 2016-11-02
# Descripton : This application is use for batch downloading loveq programs.
#              You can type "python loveq.py -help" in command line for detail  
# ------------------------------------------------------------------------------

__author__ = "GhostaR"
__date__   = "2016-11-02"

import urllib.request
from datetime import datetime
from datetime import timedelta
import sys

class LOVEQ:
    #定义初始化
    def __init__( self ):
        #常量 Monday = 0,Tuesday = 1, ... Sunday = 6
        self.week_table = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
        self.base_url = "http://dl.loveq.cn/program/"
        self.loveq_launch_date = datetime(2003,5,11)   #节目开播日期 
        self.today_date = datetime.now()   
        #初始化变量
        self.save_dir = "."  #当前目录        
        self.start_date = datetime.now()  
        self.end_date = None
       
    def is_available_date( self, date ):
        if date < self.loveq_launch_date or date >= self.today_date:
            return False
        day_of_week = date.weekday()    
        if self.week_table[day_of_week] != 'Saturday' and self.week_table[day_of_week] != 'Sunday':
            return False
        else:
            return True

    def get_target_url( self, date ):  
        str_date = date.strftime('%Y-%m-%d')    #datetime --> str,and format it as '%Y-%m-%d'(delete %H:%M:%S)
        #print(str_date)
        target_url = self.base_url + "LoveQ.cn_" + str_date + "-1.mp3"
        return target_url

    def get_save_filename( self, date ):
        str_date = date.strftime('%Y-%m-%d')  
        filename = self.save_dir + '/' + str_date + "-LoveQ.mp3"
        #print(filename)
        return filename 

    def process_cmdline( self, *argv ):
        i = 0
        argc = len( *argv )       
        #print( argc )
        while i < argc :
            #print(argv[0][i])
            
            if argv[0][i] == "-o":
                i += 1
                self.save_dir = argv[0][i]
                #print( "save_dir=",self.save_dir ) 
            elif argv[0][i] == "-s":
                i += 1
                self.start_date = datetime.strptime(argv[0][i],'%Y-%m-%d')
                #print( "start_date=",self.start_date )
            elif argv[0][i] == "-e":
                i += 1
                self.end_date = datetime.strptime(argv[0][i],'%Y-%m-%d')
                #print( "end_date=",self.end_date )
            elif argv[0][i] == "-v" or argv[0][i] == "-version":
                print("Version: V1.0.0.1 \n"
                      "Author : GhostaR\n"   
                    )
                return 0
                #print( "end_date=",self.end_date )
            elif argv[0][i] == "-h" or argv[0][i] == "-help":
                print("Usage:python loveq.py \n"  
                      " -o <setup Output save directory,default directory is '.'>\n" \
                      " -s <setup download Start date,default date is today>\n" \
                      " -e <setup download End date,default is none>\n" \
                      " -h(-help) <print this menu>\n" \
                      " -v(-version) <print version and author information>\n" \
                    )
                return 0
            i += 1
        return 1

    def cbfunc_progress( self, blocknum, blocksize, totalsize ) :  #callbackfunc_progress
        percent = 100.0 * blocknum * blocksize / totalsize
        print( "%3d%%" %(percent),end='\r')
        if percent >= 100 :
            percent = 100
            print("")   #change line                     

    def start_tasks( self, start_date, end_date ):
        if end_date == None :
            print("LoveQ Download Task",start_date,"Start!")
            if self.is_available_date( start_date ) == False:   
                print("It is not an available date for download!")
                exit() 
            else:
                target_url = self.get_target_url( start_date )
                save_file = self.get_save_filename( start_date ) 

                print ("Downloading %s ,waiting..." %(target_url))
                try :
                    urllib.request.urlretrieve( target_url, save_file, self.cbfunc_progress )
                    print("LoveQ Download Task Finish!")
                except urllib.request.HTTPError as e :                   
                    print("LoveQ Download Task Fail!")
                    print("Error Code:", e.getcode())
                
        else:   #end_date != None
            print("LoveQ Download Tasks from",start_date,"to",end_date,"Start!")            
            if start_date > end_date : 
                sign = -1
            else :
                sign = 1    
            while True:     #simulate  do...while 
                if self.is_available_date( start_date ) == False:   
                    #print('unavailable')
                    start_date = start_date + timedelta( days = sign ) 

                    if end_date == start_date or start_date >= self.today_date or start_date < self.loveq_launch_date :
                        break
                    else :
                        continue
                else :
                    #print(start_date)
                    target_url = self.get_target_url(  start_date )
                    save_file = self.get_save_filename(  start_date )
                    print ("Downloading %s ,waiting..." %(target_url))
                    try :
                        urllib.request.urlretrieve( target_url, save_file,self.cbfunc_progress )
                    except urllib.request.HTTPError as e :
                        print("Download   ",target_url,"Fail!") 
                        print("Error Code:", e.getcode())                          

                    start_date = start_date + timedelta( days = sign )  

                if end_date == start_date :
                    break 

            print("LoveQ Download Tasks Finish!")


if __name__ == '__main__':
    print("*****************************************************")
    print("****Welcome using LoveQ Batch Download Assistant!****")
    print("*****************************************************")
    loveq = LOVEQ()

    if loveq.process_cmdline( sys.argv ) == 1 :
        loveq.start_tasks( loveq.start_date,loveq.end_date )

