
from picamera2 import Picamera2, Preview
import time
from datetime import datetime

current_time=datetime.now()

picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
time.sleep(3)
main_folder="/home/cheka/Project/Rec/RECORDINGS/"

def Rec_Start(p,clock):
	
	current_date=str(current_time.month)+"."+str(current_time.day)+"."+str(current_time.year)
	rec_location=main_folder+current_date+"/"+current_date+"_"+str(p)+"/"+clock+str(".mp4")
	print("recording started"+" "+clock)
	picam2.start_and_record_video(output=rec_location, duration=60)
	

