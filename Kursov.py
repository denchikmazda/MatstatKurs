import csv
import pandas
import matplotlib.pyplot as plt
with open('/Users/Ефимов Данила/Desktop/курсач матстат/r1z1.csv') as csvfile:
    reader = csv.reader(csvfile)
    sample = []
    for row in reader:
        sample.extend(row)
name_of_random_value = sample[0]
sample.remove('X')
sample = [float(value) for value in sample]

data = pandas.read_csv('/Users/Ефимов Данила/Desktop/курсач матстат/r1z1.csv')

#print(data.shape)
#for value in sample:
#    print(value)
#print(data['X'].value_counts())
#plt.show()