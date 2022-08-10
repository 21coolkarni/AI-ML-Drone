import cv2
import  pyshine as ps
HTML="""
<html>
<head>
<title>PyShine Live Streaming</title>
</head>

<body>
<center><img src="stream.mjpg" width='1280' height='960' ></center>
</body>
</html>
"""
def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,HTML)
    address = ('192.168.127.183',9000) # Enter your IP address 
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,960)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        capture.set(cv2.CAP_PROP_FPS,15)
        capture.set(cv2.CAP_PROP_ROLL,180)
        capture.set(cv2.CAP_PROP_AUTOFOCUS,1)
        #capture.set(cv2.CAP_PROP_BRIGHTNESS,50)
        capture.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.1)
        capture.set(cv2.CAP_PROP_ZOOM,27)
        StreamProps.set_Capture(StreamProps,capture)
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        print('Server started at','http://'+address[0]+':'+str(address[1]))
        server.serve_forever()
        
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()
        
if __name__=='__main__':
    main()
