#!/usr/bin python3.7

import cv2
import numpy as np
from time import sleep
from loguru import logger as log

log.info("Author: Anjul Sharma.")
log.info("""\n\nHey!! Would you like to try Harry Potter invisibility cloak??\nIts awesome\U0001F60A""")

cap = cv2.VideoCapture(0)
sleep(3)
background=0
for i in range(30):
	ret,background = cap.read()

background = np.flip(background,axis=1)
use_red_color_range = True
plog = True

while(cap.isOpened()):
	ret, img = cap.read()
	
	# Flipping the image (Can be uncommented if needed)
	img = np.flip(img,axis=1)
	
	# Converting image to HSV color space.
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	value = (35, 35)
	
	blurred = cv2.GaussianBlur(hsv, value,0)
	
	if use_red_color_range:
		# Defining lower range for red color detection.
		lower_red = np.array([0,120,70])
		upper_red = np.array([100,255,255])
		mask1 = cv2.inRange(hsv,lower_red,upper_red)
		
		# Defining upper range for red color detection
		lower_red = np.array([170,120,70])
		upper_red = np.array([180,255,255])
		mask2 = cv2.inRange(hsv,lower_red,upper_red)
		
		# Addition of the two masks to generate the final mask.
		mask = mask1+mask2
		mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	else:
		# Defining upper range for red color detection
		lower_red = np.array([138, 28, 62])
		upper_red = np.array([207, 180, 255])
		mask = cv2.inRange(hsv,lower_red,upper_red)
		
		# Addition of the two masks to generate the final mask.
		mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	# Replacing pixels corresponding to cloak with the background pixels.
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.imshow('Display',img)
	k = cv2.waitKey(10)
	if plog:
		log.info("Press ESC to close.")
		plog = False
	if k == 27:
		log.success("""\n\nIf you like it, Please Appreciate\U0001f44d \nAnjul khush hoga\U0001F92A, shabashi dega\U0001F910\n""")
		break
		

