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

	#rubric says to save header, I don't use it anywhere else though
	throwaway_variable = next(csviterator)

	#loop through the dataset
	#loop creates list for name of each candidate and another list for how many votes they got 
	for row in csviterator:
		total_count += 1
		#if name hasn't been seen before add to name list
		if(name_list.count(row[2]) == 0):
			name_list.append(row[2])
			count_list.append(1)
		#otherwise add count to number of votes for that name
		else:
			index = name_list.index(row[2])
			count_list[index] += 1

#set up list for output
output_list = []
output_list.append("Election Results")
output_list.append("-------------------------")
output_list.append(f"Total Votes: {total_count}")
output_list.append("-------------------------")

index = 0
winner_count = 0
#for loop to add results per candidate by name 
for name in name_list:
	#if number of votes is greater than highest seen so far, update it
	if(count_list[index] > winner_count):
		winner_count = count_list[index]
	#add candidate and their number of votes to output list
	output_list.append(f"{name}: {round(100 * (float(count_list[index]) / (total_count)), 3)}\
% ({count_list[index]})")
	index +=1

#find name of winner
winner = name_list[count_list.index(winner_count)]

output_list.append("-------------------------")
output_list.append(f"Winner: {winner}")
output_list.append("-------------------------")

#prepare for output to text file and print output
output_path = os.path.join("analysis", "election_results.txt")

with open(output_path, 'w', newline='') as output_file:
	for text in output_list:
		output_file.write(text + "\n")
		print(text)