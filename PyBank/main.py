import os 
import csv

#basic csv read file set up
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as budget_data:
	csviterator = csv.reader(budget_data, delimiter = ",")
	
	#skip header before loop
	next(csviterator)

	#initialize variables using first row 
	first_month = next(csviterator)
	month_counter = 1
	net_profit = int(first_month[1])
	first_month_profit = first_month[1]
	greatest_month_profit = ["", 0]
	least_month_profit = ["", 0]

	#loop through the dataset
	for row in csviterator:
		print(row)		
		month_counter += 1
		net_profit += int(row[1])
		if(int(row[1]) > int(greatest_month_profit[1])):
			greatest_month_profit = row
		elif(int(row[1]) < int(least_month_profit[1])):
			least_month_profit = row


	# casting to float to avoid integer division
	# month_counter - 1, because that is the total count of changes
	average_change = (float(row[1]) - float(first_month_profit)) / (month_counter - 1)
	average_change = round(average_change, 2)

	print(f"Month counter: {month_counter}\nNet profit: {net_profit}\n\
Average change: {average_change}\nGreatest: {greatest_month_profit}\n\
Least: {least_month_profit}")
