# Raspberry Pi 3 Dashcam
This is a Junior University Project showing the code and algorithm to create a Dashcam utilizing a Raspberry Pi 3 Model B.

The purpose of this Project is to create an autonomous system that allows recordings to be made until hitting a storage threshold, after which the program will automatically delete the oldest files in order to leave room for the newest. The system also contains a feature to store recordings manually using switches preset to store either 15, 30, or 60 minutes of footage, this feature is optional.

Files are stored into subfolders indicating the moment of the recording. Each video file is 60 seconds long. Since files are stored sequentially, you can take several files and combine them into a single video.


![image](https://user-images.githubusercontent.com/124648406/217351196-965a1836-e1f6-45dc-b31b-01f3984d9cd0.png)


Detailed description and documentation for this work can be found in the following PDF: [Jose_Doliner_RaspberryPi3Dashcam.pdf](https://github.com/Jcdoliner/Raspberry-Pi-3-Dashcam/files/10678316/Jose_Doliner_RaspberryPi3Dashcam.pdf)

I have also prepared a youtube video explaining different aspects of the code and algorithm: https://www.youtube.com/watch?v=kKfFATqXj1o

# Requirements
In order to Successfully integrate this program into your Pi 3 the following requirements must be met:
- Raspbian Version 11 (Bullseye)
- Picamera2 Library: https://github.com/raspberrypi/picamera2 
- OV5627 Raspberry Pi Camera (either official or third party)
- Have the Legacy Support for the PiCamera **Disabled**
- 220 &#937; Resistors (x3)
- LED Lights (x2)

To allow permanent recordings to be taken without physically accessing the Pi's memory the following components are needed:
- Three-SPDT switches
- An extra 220 &#937; resistor and LED

# To Record
You need to install all files into a single directory.
Some of the Python files within the project contain a variable called main_folder, the string assigned to this variable needs to reflect the address of the directory you want the recordings to be stored.

Example:
```
main_folder="/home/cheka/Project/Rec/RECORDINGS/"

```
The string "/home/cheka/Project/Rec/RECORDINGS/" in this case will be replaced with the address of the folder storing your recordings. After this is done, running **"Recording_Management.py"** will initiate recordings. 


To automatically run this program each time the Pi is powered up you can open the terminal and add the following command:
```
sudo nano /etc/rc.local.
```
After opening this folder the following command needs to be inserted. Keep in mind that you have to modify the address to match the location of the **"Recording_Management.py"** file and keep the **"&"** symbol after the address.
```
sudo python3 /home/pi/Desktop/Recording_Management.py &
```
# To Store Recordings Using Switches (Optional)
Similarly for to run this part of the program two functions need to be modified depending on your addresses.
On Recording_Management.Py and FolderCreation.py there is a line containing the following code:

```
f=open("/home/cheka/Project/Rec/CODE/iopointer.txt","w")
  
```
Modify the part containing "/home/cheka/Project/Rec/CODE/" to indicate the directory address where you have stored the downloaded python files (the location of Recording_Management.py, FolderCreation.py etc...)


After this is done the IOPERMARECORDINGS.py file can be run in order to store files depending on input selections. You can make this file run at startup by following the same method performed at the end of the **"To Record"** section.

# Wiring and Outputs
The Following wiring diagram shows the input and output connections for LEDs and switches:
            ![image](https://user-images.githubusercontent.com/124648406/217343718-5c740d65-1b5c-4df4-a37d-7de94d8278d8.png)

Note that if you don't want the optional feature of permanent recordings you can connect the LEDs and Resistors without the switches.
Consult your manual in order to include the correct pin assignments, otherwise you will need to modify the code to match your GPIO Pins.

The colors of the LEDS are highlighted by the wire colors on the diagram above. Following this color scheme, the following table shows the messages represented by each LED response:


![image](https://user-images.githubusercontent.com/124648406/217345915-fcfc0df5-c91b-4bd5-ad6c-4ec0b570d690.png)

# Notes
- Default resolution for the recordings is 480p in order to optimize the maximum time recorded. You can modify this to your liking by editing the rec.py file using the PiCamera2 Documentation. To simplify the code for recordings, it is set right now to automatically select a preview configuration, which leads to the video being 480p.

PiCamera 2 Documentation:
https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
 
- If you do not change the address values described above you are going to run into errors, if you are not sure of a certain address you can always right click the directory to obtain its exact address.
- Pin connections for the LEDS can not be changed, doing so will cause incorrect outputs to be displayed
- This is my first major project in python so any feedback is appreciated.
