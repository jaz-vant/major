import serial
import time
from picamera2 import Picamera2, Preview
# import numpy as np
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration
picam2.configure(preview_config)
try:
    tfmini_s = serial.Serial('/dev/AMA0',115200,timeout=1)
except Exception as e:
    print(f"Error occured with serial port, {e}")
    exit()
def convert_distance_data(data):
    dist_l = data[2]
    dist_h = data[3]
    dist_total = (dist_h << 8) + dist_l  
    return dist_total

i = 0
l_dist = []

def lidar(tfmini_s):
    while True:
        try:
            while tfmini_s.in_waiting < 9:
                pass
            data = tfmini_s.read(9)
            if len(data) >= 9 and data[0] == 0x59 and data[1] == 0x59:
                distance = convert_distance_data(data) #Need to store this distances in an array
                l_dist.append(distance)
                print(f"Distance: {distance} cm")
            else:
                print("Invalid data recieved")
        except Exception as e:
            print(f'Error occured, {e}')
            
while i<60: #should be 360
    if i%15==0:
        name=str(i)+'.jpg'
        picam2.start_preview(Preview.QTGL)
        picam2.start()
        time.sleep(2)
        img=picam2.switch_mode_and_capture_image(capture_config)
        img.save(name)
        picam2.stop_preview()
        picam2.close()
    lidar(tfmini_s)
    i+=1
print(l_dist)
    
    
    

        


        
    