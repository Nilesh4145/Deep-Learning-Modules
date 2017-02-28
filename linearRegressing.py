'''
Implementation of Linear Regressing
'''

import openpyxl as reader
import numpy
import theano

training_data = {}
input_data = {}
i = 0
workbook = reader.load_workbook('data_carsmall.xlsx')

first_sheet = workbook.get_sheet_by_name('Sheet1')

training_data = []
testing_data = []

for row in list(first_sheet.iter_rows())[2:]:

	features = numpy.matrix([row[i].value for i in range(5)])
	value = row[5].value

	if value == 'NaN':
		testing_data.append(features)
	else:
		training_data.append((features, value))

	# acceleration = row[0].value
	# cylinders = row[1].value
	# displacement = row[2].value
	# horsepower = row[3].value
	# weight = row[4].value
	
	# if row[5].value == "NaN":
	# 	input_data[row[5].value] = {"Acceleration" : acceleration, "Cylinders" : cylinders, "Displacement" : displacement, "Horsepower" : horsepower, "Weight" : weight}
	# else:
	# 	training_data[row[5].value] = {"Acceleration" : acceleration, "Cylinders" : cylinders, "Displacement" : displacement, "Horsepower" : horsepower, "Weight" : weight} 
	
for i in testing_data:
	print(i[0])