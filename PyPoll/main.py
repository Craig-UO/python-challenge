# Imports for file input/output
import os
import csv

# Sets a name for the file path to the data .csv file to be analyzed
election_data=os.path.join('Resources', 'election_data.csv')

# Variable to hold the name of the candidate for the row currently under consideration
current_candidate=""

# Variables to hold counts of votes for each candidate and compute percentage
vote_percentage_each=0
vote_total_each=0

# List to hold the names of all unique candidates and count them
candidates={}

# Variable to count the total number of ballot IDs (votes) included in the data set
ballot_count=0

# Read in the file to count unique candidates and total votes
with open(election_data) as csvfile:
    
    vote_set = csv.reader(csvfile, delimiter=",")

    next(vote_set)

    # Populate cadidates list with all unique names                
    for row in vote_set:
        # Count the number of rows of data (votes)
        ballot_count+=1

        current_candidate=row[2]  # Store name of current line

        if current_candidate not in candidates.keys():  # Checks list of candidates for name in current row
            # Adds new unique name to the Dictionary of names with a Dictionary for that candidate's vote total and vote percentage
            candidates[current_candidate]={"Total Votes": 1, "Vote Percentage":1/ballot_count}
        else:
            candidates[current_candidate]["Total Votes"]+=1  # Adds one vote for each line with this existing candidate's name
            
            
# Compute percentage results for each candidate and determine the winner of the election
most_votes=0 # Placeholder variable to start checking each total against the others to determine the winner
for name in candidates.keys():
    candidates[name]["Vote Percentage"]=candidates[name]["Total Votes"]/ballot_count  # Computes this candidate's vote percentage
    if candidates[name]["Total Votes"]>most_votes: # Sets this candidate as the winner if their vote total is currently the highest that's been looked at
        most_votes=candidates[name]["Total Votes"]
        election_winner=name

# Display results on screen-----------------------------------------------------------------------------------------------

print("Election Results \n")
print("-------------------------------------------\n")
print("Total Votes: " + str(ballot_count) + "\n")
print("-------------------------------------------\n")

# Print out each unique candidate's name and their results
for name in candidates.keys():
    print(name + ": " + str(round(candidates[name]["Vote Percentage"]*100, 3)) + "% " + "(" + str(candidates[name]["Total Votes"]) + ")\n")

# Declare the winner
print("-------------------------------------------\n")
print("Winner: " + election_winner + "\n")
print("-------------------------------------------\n")

# File path to save results to a text file
election_results=os.path.join('Analysis', 'election_results.txt')

with open(election_results, 'w') as text_file:

    text_file.write("Election Results \n")
    text_file.write("-------------------------------------------\n")
    text_file.write("Total Votes: " + str(ballot_count) + "\n")
    text_file.write("-------------------------------------------\n")

    # Print out each unique candidate's name and their results
    for name in candidates.keys():
        text_file.write(name + ": " + str(round(candidates[name]["Vote Percentage"]*100, 3)) + "% " + "(" + str(candidates[name]["Total Votes"]) + ")\n")

    # Declare the winner
    text_file.write("-------------------------------------------\n")
    text_file.write("Winner: " + election_winner + "\n")
    text_file.write("-------------------------------------------\n")