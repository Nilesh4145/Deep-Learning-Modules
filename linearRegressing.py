'''
Implementation of Linear Regressing
'''

import openpyxl as reader
import numpy
import theano

training_data_list = []
input_data_list = []
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

for i in training_data:
	training_data_list.append(i[0])
for i in testing_data:
	input_data_list.append(i[0])

training_matrix = numpy.array(training_data_list)
testing_matrix = numpy.array(input_data_list)

print(testing_matrix.shape)
print(training_matrix.shape)