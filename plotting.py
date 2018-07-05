import matplotlib.pyplot as plt
import numpy as np
from lister import *

def plotDataBar(dataList, title):
	resultsLabels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	y_pos, resultsList = getResultsList(dataList)

	plt.bar(y_pos, resultsList, align='center')
	plt.xticks(y_pos, resultsList)
	plt.ylabel('Amount')
	plt.title(title)

	plt.show()

def plotDataThreeBars(dataList, title):
	resultsLabels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	y_pos, resultsList1 = getResultsList(dataList[0])
	_, resultsList2 = getResultsList(dataList[1])
	_, resultsList3 = getResultsList(dataList[2])

	plt.bar(y_pos-0.2, resultsList1, width=0.2, color='b', align='center')
	plt.bar(y_pos, resultsList2, width=0.2, color='g', align='center')
	plt.bar(y_pos+0.2, resultsList3, width=0.2, color='r', align='center')
	plt.xticks(y_pos, resultsLabels)
	plt.ylabel('Amount')
	plt.title(title)

	plt.show()

def plotDataError(stdDataList, meanDataList, title):
	resultsLabels = ['H', 'S', 'V']

	y = np.power(meanDataList, 2)

	plt.errorbar(meanDataList[0], y[0], stdDataList[0], linestyle='None', marker='^')

	plt.show()

def plotColorsData(hsvStdDevData, title):
	hsvStdDevStacked = [arr[0] for arr in hsvStdDevData]
	print(len(hsvStdDevStacked))
	y_pos, resultsList = getResultsList(hsvStdDevStacked)

	plt.bar(y_pos, resultsList, align='center')
	plt.xticks(y_pos, resultsList)
	plt.ylabel('Amount')
	plt.title(title)

	plt.show()
