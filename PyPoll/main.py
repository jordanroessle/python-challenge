import os 
import csv

#output variables 
total_count = 0 
name_list = []
count_list = []


#basic csv read file set up
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as election_data:
	csviterator = csv.reader(election_data, delimiter = ',')

	#skip header before loop
	next(csviterator)

	#loop through the dataset 
	for row in csviterator:
		total_count += 1
		if(name_list.count(row[2]) == 0):
			name_list.append(row[2])
			count_list.append(1)
		else:
			index = name_list.index(row[2])
			count_list[index] += 1

print(total_count)
print(name_list)
print(count_list)