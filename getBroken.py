#!/usr/bin/env python3
from pprint import pprint
from sys import argv
import numpy as np

brokenList = []
nLines = 0
nanBrokenList = []

with open(argv[1], 'r') as csvfile:
	for line in csvfile.readlines():
		nLines += 1
		splitLine = line.split(',')
		if float(splitLine[1]) > 200.0:
			brokenList.append(splitLine[0])
		for i in range(1, 10):
			if np.isnan(float(splitLine[i])):
				nanBrokenList.append(splitLine[0])
				break

print(len(brokenList))
print(len(brokenList)*100/nLines, '%')

f = open('brokenlist.txt', 'a')
[f.write(brokenFile + '\n') for brokenFile in brokenList]
f.close()

f = open('nanbrokenlist.txt', 'a')
[f.write(brokenFile + '\n') for brokenFile in nanBrokenList]
f.close()
