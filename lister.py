import numpy as np
import math

def getResultsList(dataList):
	divider = max(dataList)/10
	resultsList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for dataItem in dataList:
		resultsList[math.trunc(dataItem/divider)-1] += 1

	y_pos = np.arange(len(resultsList))

	return (y_pos, resultsList)
