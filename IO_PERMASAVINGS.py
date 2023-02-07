from FolderCreation import get_p,current_date,main_folder
from gpiozero import LED,Button
from time import sleep
import shutil
ledyellow=LED(5)
fifteen=Button(25)
thirty=Button(24)
hour=Button(23)
destination="/home/cheka/Project/Rec/PERMANENT"



def Perma_Save():	
	if fifteen.is_pressed:
		p=get_p()
		source=main_folder+current_date+"/"+current_date+"_"+str(p.strip("\n"))
		shutil.copytree(source,destination,dirs_exist_ok=True)
		ledyellow.blink(n=1)
		print("Files Stored")
		sleep(5)
	
	if thirty.is_pressed:
		p=get_p()
		p2=str(int(p.strip("\n"))-1)
		source=main_folder+current_date+"/"+current_date+"_"+str(p.strip("\n"))
		source2=main_folder+current_date+"/"+current_date+"_"+str(p2)
		shutil.copytree(source,destination,dirs_exist_ok=True)
		shutil.copytree(source2,destination,dirs_exist_ok=True)
		ledyellow.blink(n=2)
		print("Files Stored")
		sleep(5)
	if hour.is_pressed:
		p=get_p()
		p2=str(int(p.strip("\n"))-1)
		p3=str(int(p2)-1)
		p4=str(int(p3)-1)
		source=main_folder+current_date+"/"+current_date+"_"+str(p.strip("\n"))
		source2=main_folder+current_date+"/"+current_date+"_"+str(p2)
		source3=main_folder+current_date+"/"+current_date+"_"+str(p3)
		source4=main_folder+current_date+"/"+current_date+"_"+str(p4)
		shutil.copytree(source,destination,dirs_exist_ok=True)
		shutil.copytree(source2,destination,dirs_exist_ok=True)
		shutil.copytree(source3,destination,dirs_exist_ok=True)
		shutil.copytree(source4,destination,dirs_exist_ok=True)
		ledyellow.blink(n=3)
		print("Files Stored")
		sleep(5)
		
while True:
	try:
		Perma_Save()
	except:
		print("")
