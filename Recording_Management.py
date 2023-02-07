from datetime import datetime
from FolderCreation import *
from Folder_Management import Storage_Management
from rec import *
import os
import time
from gpiozero import LED
main_folder1="/home/cheka/Project/Rec/RECORDINGS/"
count = 0
ledred=LED(13)
ledgreen=LED(6)

while True:
	try:
		Folder_Day()
	except OSError as error:
		print("")
	current_time1=datetime.now()
	current_date1=str(current_time.month)+"."+str(current_time.day)+"."+str(current_time.year)
	rectime=str(current_time1.hour)+"-"+str(current_time1.minute)+"-"+str(current_time1.second)
	
	if os.path.exists(main_folder1+current_date1+"/"+current_date1+".txt")==True:
		n=int(Retrieve_p())
		print("current day folder is: "+str(n))
	else:
		Folder_15min(1)
		Day_Pointer(1)
		n=1
	
	if os.path.exists(main_folder+current_date+"/"+current_date+"_"+str(n)+"/"+current_date+".txt")==True:
		count=int(Retrieve_videop(n))
		print("There are: "+str(count)+" files on the folder")
	else:
		print("Video Pointer file created")
		Video_Pointer(1,n)
		count=1
        
	f=open("/home/cheka/Project/Rec/CODE/iopointer.txt","w")
	f.write(str(n)+"\n")
	f.close()
	count+=1
	Video_Pointer(count,n)
	ledgreen.blink(on_time=0.5,off_time=2,n=30)
	Storage_Management()
	try:
		Rec_Start(str(n),rectime)
	except:
		ledred.on()
	
	ledred.blink(n=3)
	
	if count>=15:
		n+=1
		Folder_15min(n)
		Day_Pointer(n)
		count=0
		
#rec_location1=main_folder1+current_date1+"/"+current_date1+"_"+str(n)
	#https://pynative.com/python-count-number-of-files-in-a-directory/#:~:text=Getting%20a%20count%20of%20files,of%20files%20of%20a%20directory.
#	for path in os.listdir(rec_location1):
    # counts the files in the folder
##			count += 1
