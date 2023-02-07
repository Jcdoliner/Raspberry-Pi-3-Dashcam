from FolderDeletion import*
import os
from gpiozero import LED
from time import sleep
ledyellow=LED(5)
def Storage_Management():
	n=1
	#Checks and manages storage
	if get_dir_size(main_folder)<(10000000000):
		print("Normal Storage Threshold")
		try:
			ledyellow.off()
		except:
			print("led could not be turned off")
			
	if get_dir_size(main_folder)>(9000000000) and get_dir_size(main_folder)<10000000000:
		#checkes if the storage is greater than 6 GB
		print("Warning, Reaching Storage Threshold")
		try:
			ledyellow.blink(n=10)
		except:
			print("LED on use")
	while get_dir_size(main_folder)>(10000000000):
		#if the main folder size reaches the 7GB threshold if will delete files until a save zone is reached
		print("Current Storage Ocupied "+str(get_dir_size(main_folder))+" Bytes")

		deletefile=find_old(main_folder)
		print("deleting file: "+str(deletefile)+"_"+str(n))
		try:
			ledyellow.on()
		except:
			print("LED Channel on use")
		try:
			Sub_Folder_Delete(deletefile,n)
		except:
			print("Could not delete sub folder")
		n+=1
        
		if n>=24:
			print("deleting main day folder: "+str(deletefile))
			n=1
			try:
				Folder_Delete(deletefile)
			except:
				print("could not delete main folder")
		if get_dir_size(main_folder)>(10000000000):
			ledyellow.off()
		sleep(1)

