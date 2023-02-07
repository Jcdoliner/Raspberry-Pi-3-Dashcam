from datetime import datetime
import os
current_time=datetime.now()
current_date=str(current_time.month)+"."+str(current_time.day)+"."+str(current_time.year)
main_folder="/home/cheka/Project/Rec/RECORDINGS/"

def Folder_Day():
	#creates a folder for the current day
	location=main_folder
	file_name=current_date
	path=os.path.join(location,file_name)
	os.mkdir(path)

def Day_Pointer(n):
	#gets value from a counter for Folder_15min and stores it on a txt file, if file does not exist it is created automatically
	f=open(main_folder+current_date+"/"+current_date+".txt",'a')
	f.write(str(n)+'\n')
	f.close()

def Video_Pointer(n,p):
	#gets value from a counter for a video and stores it on a txt file, if file does not exist it is created automatically
	f=open(main_folder+current_date+"/"+current_date+"_"+str(p)+"/"+current_date+".txt",'a')
	f.write(str(n)+'\n')
	f.close()
def get_p():
	#Retrieves the pointer last stored on the file
	with open("/home/cheka/Project/Rec/CODE/iopointer.txt", "r") as fp:
		lines = fp.readlines()
		end = lines[-1]
		return end

def Retrieve_p():
	#Retrieves the pointer last stored on the file
	with open(main_folder+current_date+"/"+current_date+".txt") as f:
		for line in f:
			pass
		last_line = line
		f.close()
		return(last_line)
def Retrieve_videop(p): #argument being the pointer of the 15 min folder
	#Retrieves the pointer last stored on the file
	with open(main_folder+current_date+"/"+current_date+"_"+str(p)+"/"+current_date+".txt") as f:
		for line in f:
			pass
		last_line = line
		f.close()
		return(last_line)


def Folder_15min(n):
	#argument being the value of a counter
	location=main_folder+current_date
	file_name=current_date+"_"+(str(n))
	path=os.path.join(location,file_name)
	os.mkdir(path)


#try:
#	Folder_Day()
#except OSError as error:
#	print(error)

