import cv2
import time
#cap=cv2.VideoCapture("udp://192.168.2.1:5000", cv2.CAP_FFMPEG)
cap=cv2.VideoCapture("udp://196.168.10.1:11111")

#cap=cv2.VideoCapture("output.avi")
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("h:{}".format(height))

#cap=cv2.VideoCapture("udpsrc host=192.168.2.4 port=5000 caps = \"application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96\" ! rtph264depay ! decodebin ! videoconvert ! appsink",cv2.CAP_GSTREAMER)
#fourcc = cv2.VideoWriter_fourcc(*'X264')
#out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
start_time=time.time()
while True:
	ret, frame=cap.read()

	if ret:
		'''
		with open("output.txt","a+") as f:
			now_time=time.time()
			f.write("{}\n".format(now_time-start_time))

			out.write(frame)
		'''
		cv2.imshow("webcam",frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()

'''

./test-launch "( v4l2src device=/dev/video0 ! "image/jpeg,width=640,height=480,frame-rate=30/1" !  rtpjpegpay name=pay0 pt=96 )" -p 8554


./test-launch "udpsrc port=5000 ! application/x-rtp,media=(string)video,clock-rate=(int)90000,encoding-name=(string)H264 ! rtph264depay ! h264parse ! decodebin ! videoconvert ! x264enc ! rtph264pay name=pay0 pt=96 " -p 8554

./test-launch "( v4l2src device=/dev/video0 ! "video/x-raw,framerate=30/1" !  videoscale ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay  )" -p 8554

./test-launch "( v4l2src device=/dev/video0 ! "video/x-raw,framerate=30/1" ! videoconvert ! rtph264pay name=pay0 pt=96 )" -p 8554

gst-launch-1.0 -v v4l2src device=/dev/video0 ! video/x-raw,framerate=30/1 ! videoscale ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink host=127.0.0.1 port=5000



'''
