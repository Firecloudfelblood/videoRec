from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import cv2
from datetime import datetime, time
import time as time2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="~/temp ")
ap.add_argument("-a", "--min-area", type=int, default=500, help="1024" )