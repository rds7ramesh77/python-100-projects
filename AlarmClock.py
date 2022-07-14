#Python Program to create Alarm Clock

""" For this we have to import DateTime Module"""

from datetime import datetime
from playsound import playsound

alarm_time=input("Enter time of alarm to be set: HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()

print("Setting up alarm...")

while True:
    now =datetime.now()
    current_hrs=now.strftime("%I")
    current_min=now.strftime("%M")
    current_sec=now.strftime("%S")
    current_period=now.strftime("%p")
    
    
    if(alarm_period==current_period):
        if(alarm_hour==current_hrs):
            if(alarm_minute==current_min):
                if(alarm_seconds==current_sec):
                    print("Wake Up!!!!")
                    break