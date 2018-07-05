#!/usr/bin/env python3
import cv2 as cv

def resize(file):
	img = cv.imread(file)

	height, width, _ = img.shape
	newHeight = 0
	newWidth = 0

	if height > 1000 and width > 1000:
		if width > height:
			coef = width / 1000
			newWidth = 1000
			newHeight = int(height / coef)
		elif height > width:
			coef = height / 1000
			newHeight = 1000
			newWidth = int(width / coef)
		else:
			newHeight = 1000
			newWidth = 1000
	else:
		return

	img = cv.resize(img, (newWidth, newHeight))

	cv.imwrite(file, img)

	print(file)
