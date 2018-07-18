import pandas as pd
csvpath ="resources/budget_data.csv"

budget_df = pd.read_csv(csvpath)

totalmonths = len(budget_df)
#printing for verification
#print(totalmonths)

netprofit = budget_df[["Revenue"]].sum()
#printing for verification
#print(netprofit)

import os
import csv

budgetcsv=os.path.join("Resources","budget_data.csv")

# Open and read csv
with open(budgetcsv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	# Read the header row first
	csv_header = next(csvfile)
	print(f"Header: {csv_header}")

	#declare
	previousrevenue = int(budgetcsv[1])
	avg_list = []
	maxprof = change[0]
	maxloss = change[0]

	# Read through each row of data after the header
	for row in csvreader:
		change = int(row[1] - previousrevenue)
		previousrevenue = int(row[1])
		avg_list.append(change)
		previousrevenue = int(row[1])

		if change > maxprof:
			maxprof = change[row]

		if change < maxloss:
			maxloss = change[row]

avg = sum(avg_list)/len(avg_list)


print("Financial Analysis"
"---------------------------"
"Total Months: " + totalmonths)
print("Total Revenue: $" + netprofit)
print("Average Change in Revenue: $" + avg)
print("Greatest Increase in Profits: " + maxprof)
print("Greatest Loss in Profits: " + maxloss)

