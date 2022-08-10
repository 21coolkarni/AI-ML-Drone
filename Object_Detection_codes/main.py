from Detector import *
detector = Detector(use_cuda=True)

detector.processVideo("http://192.168.127.183:9000/stream.mjpg")