import RPi.GPIO as GPIO
import time
import pygame
import random
import datetime
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN)
GPIO.setup(35,GPIO.IN, pull_up_down=GPIO.PUD_UP)
pygame.mixer.init()
def CheckAlarm():
    
    x=True
    while x==True:
        file=open('/var/www/html/Data.txt')
        lines = file.readlines()
        if len(lines) != 3:
            print(len(lines))
            print(datetime.datetime.now())
            file.close()
        else:
            x=False
            


    Alarm = lines[2].split(":")
    if Alarm[0]=="Off":
        Alarm=["26","99"]

    
    hourtm = datetime.datetime.now()

    if hourtm.hour==int(Alarm[0]):
        if hourtm.minute==int(Alarm[1]):
            print("blinds")
            publish.single("Blinds", "0",hostname="localhost")
            client = mqtt.Client()
            client.connect("localhost",1883,60)
            client.publish("topic/test", "cycle");
            client.disconnect()
            time.sleep(60)

y=1
while y==1:
    try:
        hourtm = datetime.datetime.now()
        while hourtm.hour >= 22 or hourtm.hour < 10:
            print("Sleep Time Son")
            time.sleep(5)
            CheckAlarm()
            hourtm = datetime.datetime.now()
        CheckAlarm()
        with open('/var/www/html/Data.txt') as f:
            first_line = f.readline().rstrip()
            
        while first_line=="Music is On.":
            #print("music is playing")
            #print(pygame.mixer.music.get_busy())
            #time.sleep(5)
            
            if pygame.mixer.music.get_busy()==0:
            
                music = (random.randint(1,25))                         
                
                pygame.mixer.music.load("/home/pi/Downloads/" + str(music) + ".mp3")
                pygame.mixer.music.play()

            with open('/var/www/html/Data.txt') as f:
                first_line = f.readline().rstrip()
                #print ("file is" + first_line)

        pygame.mixer.music.stop()
        #print ("looking")
        if GPIO.input(37)==1:
            print ("motion")
            music = (random.randint(1,15))
                             
            pygame.mixer.init()
            pygame.mixer.music.load("/home/pi/Downloads/" + str(music) + ".mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.get_busy()
            #time.sleep(14)
            c=1
            for i in range(279):
                x= GPIO.input(35)
                if x == False:
                    print('Pressed')
                    pygame.mixer.music.stop()
                    c=0
                    time.sleep(5)
                    break
                time.sleep(.05)
            print("Done sleeping for 14")
            
            t0 = time.time()
            #print (t0)
            while c==1:
                if GPIO.input(37)==1 or GPIO.input(35)==0:
                    
                    pygame.mixer.music.stop()
                    print (time.time()-t0)
                    print ("stop motion")
                    #print (time.time()-t0)
                    time.sleep(14)
                    c=0
                    print (time.time()-t0)
                    print("looking for motion")
                elif (time.time()-t0)> 300:
                    print (time.time()-t0)
                    pygame.mixer.music.stop()              
##        print ("no motion")
    except KeyboardInterrupt:
        var=0
        print ("user exit")
        GPIO.cleanup()
