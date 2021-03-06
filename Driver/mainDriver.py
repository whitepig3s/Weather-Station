#!/usr/bin/python
#-*- coding=utf-8 -*-

'''
School Weather Service Project 2016-2017
Github https://github.com/oxygen-TW/Weather-Station
E-mail weatherstationTW@gmail.com
Service Website http://weather.nhsh.tp.edu.tw
'''
import sys
import time
import httplib
import urllib
import re
import serial
import json
from time import sleep


# Format python Bridge.py [USB PORT] [DataLog]

APIKEY = 'Y1JUZC930YOKH5JA'

def upload(temperature, humidity, UV_value, light_value, RainFall):
        params = urllib.urlencode({'field1': temperature, 'field2': humidity, 'field3': UV_value, 'field4': light_value, 'field5':RainFall, 'key': APIKEY})
        
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print response.status, response.reason
        data = response.read()
        conn.close()

def WriteFile(current_weather,_File):
    try:
        fp = open(_File,'a')
        fp.write(current_weather)    
    except IOError:
        print('File Open Error')
    finally:
        fp.close()
    
def GetJsonData():
#Open Serial Port To Arduino nano
    ser = serial.Serial(str(sys.argv[1]), 9600, timeout=1)
    ser.isOpen()
    
    try:
        while True:
        #print 'RPi is sending request to arduino'
            print ('connecting to MCU...')
            ser.write('D')
            sleep(0.5) #Wait for MCU processing
            response = ser.readline()
            
            #print (response) #debug only
            if response != '':
                break
            
    except KeyboardInterrupt:
        ser.close()
    finally:
        ser.close()
    return response

def main():
    #Check Argv
    if len(sys.argv) != 3:
        print("argv Error")
        exit()

    print ("Detector on "+sys.argv[1])
    print ("Data log in "+sys.argv[2])
    
    LogFile = sys.argv[2]
    
    #Get ang Resolve data
    JsonData = GetJsonData()
    print (JsonData)
    data = json.loads(JsonData)
    temperature = data['Temp']
    humidity = data['Humi']
    light_value = data['light']
    UV_value = data['UV']
    RainFall = data['Rain']

    #light_value=1023-light_value
        
    
    current_weather=time.strftime("%Y/%m/%d %H:%M:%S ")
    
    #if humidity is not None and temperature is not None:
    if temperature == "NAN":
        current_weather+='Temp=Err'
    else:
        current_weather+='Temp='+str(temperature)+'*'

    if humidity == "NAN":
        current_weather+=' Humidity=Err'
    else:
        current_weather+=' Humidity='+str(humidity)+'%'
        
    if light_value > 1023 or light_value < 0:
        light_value = "Err"
    
    if UV_value > 1023 or UV_value < 0:
        UV_value = "Err"
        
    if RainFall > 1023 or RainFall < 0:
        RainFall = "Err"
        
    current_weather+= ' light_value={0:0.1f} UV={1:0.1f} Rain={1:0.1f}'.format(light_value, UV_value,RainFall) 
    print(current_weather)
    #	print(UV_value)
    WriteFile(current_weather+'\n',LogFile)
    upload(temperature, humidity, UV_value, light_value,RainFall)    	

if __name__ == "__main__":
    main()