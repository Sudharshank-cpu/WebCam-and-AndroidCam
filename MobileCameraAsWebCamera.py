#You need to install "IP Webcam" or "DroidCam" application in your Android or Any Devices
#It requires Internet. If not, Connect them through Wifi.
import cv2
 
print('''If your URL only contain IP Address and Port, add "[ProtocolType]://[IP Address]:[Port]/video" in it.
For Example: 
	https://123.43.203.19:5680/video
	http://123.43.203.19:2350/video
	rtsp://123.32.256.8:8080/video
 You can choose any of ProtocolTypes from examples''')
url=input("Enter Webcam URL: ")

cp=cv2.VideoCapture(url)
if not cp.isOpened():
	print("Input Error: I could not able to Open provided URL.")

while True:
	camera,frame=cp.read()
	if frame is not None:
		cv2.imshow("Frame",frame)

	q=cv2.waitKey(30)             #Waiting to access the key
	if q==27 or q==ord('q'):      #Process will end when "Escape key"[ASCII value=27] or "q"[ASCII value=113] pressed
		break

cv2.destroyAllWindows()           #Closes running process in cv module and Exits Program
