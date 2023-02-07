from datetime import datetime
import os
import itertools
import shutil
main_folder="/home/cheka/Project/Rec/RECORDINGS/"
def dateolder(a,b):#compares two dates and returns true if a>b, else returns false
	a=datetime.strptime(str(a),"%m.%d.%Y")
	b=datetime.strptime(str(b),"%m.%d.%Y")
	return(a<b)

#https://note.nkmk.me/en/python-os-path-getsize/
def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
#https://realpython.com/working-with-files-in-python/#:~:text=To%20get%20a%20list%20of,scandir()%20in%20Python%203.


def find_old(path="."):
    dayfolders=[]
    
    with os.scandir(path) as entries:
        for entry in entries:
            dayfolders.append(str(entry.name))
    oldest=dayfolders[0]
    
    for a,b in itertools.combinations(dayfolders,2):
	    if dateolder(oldest,b)==True:
		    oldest=oldest
	    else:
		    oldest=b
    return oldest

def Sub_Folder_Delete(date,p):
    #takes the folder date and subfolder pointer
    folderpath=main_folder+date+"/"+date+"_"+str(p)
    shutil.rmtree(folderpath,ignore_errors=False)

def Folder_Delete(date):
    #takes the folder date and subfolder pointer
    folderpath=main_folder+date
    shutil.rmtree(folderpath,ignore_errors=False)



