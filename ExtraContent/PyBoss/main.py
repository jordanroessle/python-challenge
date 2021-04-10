import os 
import csv

#using main function for clarity, called at the very bottom
def main():
	#basic csv read file set up
	csvpath = os.path.join("employee_data.csv")

	#output list, intialize with new header
	output_list = [["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]]


	with open(csvpath) as employee_data:
		csviterator = csv.reader(employee_data, delimiter = ",")
		
		#skip header
		next(csviterator)

		#row[0] -> Emp ID, row[1] -> Name, row[2] -> Date, row[3] -> SSN, row[4] -> State
		for row in csviterator:
			#list to be added to output list, intialized with emp ID
			changed_list = [row[0]]

			#add first and last names to new list, split gives first at 0 and last at 1
			changed_list.append(row[1].split(' ')[0])
			changed_list.append(row[1].split(' ')[1])

			#modify date by splitting, reorganizing, and adding '/'
			split_date = row[2].split("-")
			changed_list.append(split_date[1] + "/" + split_date[2] + "/" + split_date[0])

			#string to output later for new SSN  
			newSSN = ""

			#only want to modify first 6 characters, so use counter to track that  
			counter = 0
			for character in row[3]:
				if((counter < 6) & (character != '-')):
					newSSN += '*'
				else:
					newSSN += character
				counter += 1

			#append updated SSN 
			changed_list.append(newSSN)

			#append 2 letter state
			changed_list.append(stateToTwo(row[4]))

			#changed_list has been fully updated, add it to output_list
			output_list.append(changed_list)

	#output updated employee data 
	output_file = "employee_data_updated.csv"
	with open(output_file, "w", newline='') as datafile:
		csvwriter = csv.writer(datafile, delimiter= ',')
		csvwriter.writerows(output_list)		
		

def stateToTwo(state_name):
	#given dictionary
	us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
	}
	#returns result of provided dictionary
	return us_state_abbrev[state_name]

#main call
main()