import os
import csv

# Path to collect data from the Resources folder
electiondata = os.path.join('Resources', 'election_data.csv')

totalvotes = 0
candidates = []
votecount = []

# Open the CSV
with open(electiondata, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    #skip header
    row = next(csvreader, None)

    #loop through each row of election data
    for row in csvfile:
    	totalvotes = totalvotes + 1
    	candidate = row[2]

    if candidate in candidates:
    	candidate_index = candidates.index(candidate)
    	votecount[candidate_index] = votecount[candidate_index] + 1
    else:
   		candidates.append(candidate)
   		votecount.append(1)


candidate_percentage = []
highvotes = votecount[0]
max_index = 0

#for each candidate, calculate out the percentage of votes
for count in range(len(candidates)):
	percent_votes = votecount[count]/totalvotes*100
	candidate_percentage.append(percent_votes)

	if votecount[count] > highvotes:
		highvotes = votecount[count]
		#print(highvotes)
		max_index = count

#assign winner from highest vote count in list
winner = candidates[max_index]

results = (
	f"Election Results: \n"
	f"-------------------------\n"
	f"Total Votes: {totalvotes}\n"
	f"-------------------------\n"
	f"{candidates[0]}: got {votecount[0]} votes {round((votecount[0]/totalvotes)*100,2)}%\n"
	f"{candidates[1]}: got {votecount[1]} votes {round((votecount[1]/totalvotes)*100,2)}%\n"
	f"{candidates[2]}: got {votecount[2]} votes {round((votecount[2]/totalvotes)*100,2)}%\n"
	f"{candidates[3]}: got {votecount[3]} votes {round((votecount[3]/totalvotes)*100,2)}%\n"
	f"-------------------------\n"
	f"And the winner is {winner}! \n"
	f"\n"
	)

print(results)

'''txtOutputPath = os.path.join('PyPoll.txt')
with open (txtOutputPath, "w") as pypolltxt:
		pypolltxt.write(results)'''



