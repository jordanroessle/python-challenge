import os 
import csv

#basic csv read file set up
csvpath = os.path.join("Resources", "budget_data.csv")

#open csv file
with open(csvpath) as budget_data:
	csviterator = csv.reader(budget_data, delimiter = ",")
	
	#skip header before loop
	next(csviterator)

	#initialize variables using the first month's values 
	first_month = next(csviterator)
	month_counter = 1
	net_profit = int(first_month[1])
	great_month_profit = ["", 0]
	least_month_profit = ["", 0]

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

	print(f"Finacial Analysis")
	print(f"----------------------------")
	print(f"Total Months: {month_counter}")
	print(f"Total: ${net_profit}")
	print(f"Average  Change: ${average_change}")
	print(f"Greatest Increase in Profits: {great_month_profit[0]} (${great_month_profit[1]})")
	print(f"Greatest Decrease in Profits: {least_month_profit[0]} (${least_month_profit[1]})")
