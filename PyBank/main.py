import os 
import csv

#basic csv read file set up
csvpath = os.path.join("Resources", "budget_data.csv")

#output variables
month_counter = 1
great_month_profit = ["", 0]
least_month_profit = ["", 0]
net_profit = 0 
average_change = 0

#open csv file
with open(csvpath) as budget_data:
	csviterator = csv.reader(budget_data, delimiter = ",")
	
	#skip header before loop
	next(csviterator)

	#initialize variables using the first month's values 
	first_month = next(csviterator)
	net_profit = int(first_month[1])

	#holds previous months information to accurately calculate change between months
	change_holder = first_month

	#loop through the dataset
	for row in csviterator:
		#cumulative variables		
		month_counter += 1
		net_profit += int(row[1])

		#check change vs greatest and least, update greatest and least if condition is met
		if( (int(row[1]) - int(change_holder[1])) > int(great_month_profit[1])):
			great_month_profit[0] = row[0]
			great_month_profit[1] = (int(row[1]) - int(change_holder[1]))
		elif((int(row[1]) - int(change_holder[1])) < int(least_month_profit[1])):
			least_month_profit[0] = row[0]
			least_month_profit[1] = (int(row[1]) - int(change_holder[1]))

		#update change_holder before iterating
		change_holder = row


	# casting to float to avoid integer division
	# month_counter - 1, because that is the total count of changes
	average_change = (float(row[1]) - float(first_month[1])) / (month_counter - 1)
	average_change = round(average_change, 2)

#store finacial analysis in a list to print and output into a file late
finacial_analysis = [] 
finacial_analysis.append(f"Finacial Analysis")
finacial_analysis.append(f"----------------------------")
finacial_analysis.append(f"Total Months: {month_counter}")
finacial_analysis.append(f"Total: ${net_profit}")
finacial_analysis.append(f"Average Change: ${average_change}")
finacial_analysis.append(f"Greatest Increase in Profits: {great_month_profit[0]}\
 (${great_month_profit[1]})")
finacial_analysis.append(f"Greatest Decrease in Profits: {least_month_profit[0]}\
 (${least_month_profit[1]})")

#prepare for output to text file
output_path = os.path.join("analysis", "results.txt")

with open(output_path, 'w', newline='') as output_file:
	for text in finacial_analysis:
		output_file.write(text + "\n")
		print(text)


