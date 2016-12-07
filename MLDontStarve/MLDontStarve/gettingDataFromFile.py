def readDataFromFile():
	print("start getting data from file 'data_set'")	
	file = open('dataSet.txt', 'r')
	dataSet = file.read()	
	file.close()
	return dataSet