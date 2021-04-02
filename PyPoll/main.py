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

output_list = []
output_list.append("Election Results")
output_list.append("-------------------------")
output_list.append(f"Total Votes: {total_count}")
output_list.append("-------------------------")

index = 0
winner_count = 0
#for loop to add results per candidate 
for name in name_list:
	if(count_list[index] > winner_count):
		winner_count = count_list[index]
	output_list.append(f"{name}: {round(100 * (float(count_list[index]) / (total_count)), 3)}\
% ({count_list[index]})")
	index +=1

#find name of winner
winner = name_list[count_list.index(winner_count)]

output_list.append("-------------------------")
output_list.append(f"Winner: {winner}")
output_list.append("-------------------------")

for row in output_list:
	print(row)