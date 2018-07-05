#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math
from plotting import *
from sys import argv

asymmetryDataList = []
borderDataList = []
hsvStdDevDataList = []
hsvMeansDataList = []

with open(argv[1], 'r') as csvfile:
	for line in csvfile.readlines():
		splitLine = line.split(',')
		asymmetryDataList.append(float(splitLine[1]))
		borderDataList.append(float(splitLine[2]))
		hsvStdDevDataList.append([float(splitLine[3]), float(splitLine[5]), float(splitLine[7])])
		hsvMeansDataList.append([float(splitLine[4]), float(splitLine[6]), float(splitLine[8])])

plotDataBar(asymmetryDataList, 'Asymmetry')
plotDataBar(borderDataList, 'Border')
# plotDataError(hsvStdDevDataList, hsvMeansDataList, 'Color')
hStdDevDataList = [e[0] for e in hsvStdDevDataList]
plotColorsData(hsvStdDevDataList, 'Color')
