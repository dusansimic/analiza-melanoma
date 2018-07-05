#!/usr/bin/env python3
from multiprocessing import Pool
from resize import resize
from os import listdir
from os.path import isfile, join

imagesPath = '/home/dusan/Documents/melanoma-images/'

filesList = [join(imagesPath, f) for f in listdir(imagesPath) if (isfile(join(imagesPath, f)) and f.endswith('.jpg'))]

with Pool(8) as p:
	p.map(resize, filesList)
