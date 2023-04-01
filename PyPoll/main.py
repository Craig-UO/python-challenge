# Imports for file input/output
import os
import csv

# Sets a name for the file path to the data .csv file to be analyzed
election_data=os.path.join('Resources', 'election_data.csv')

#DEFINE VARIABLES HERE
# Variable to hold the name of the candidate for the row currently under consideration
current_candidate=""

# Variables to hold counts of votes for each candidate and compute percentage
vote_percentage_each=0
vote_percentages=[]
vote_total_each=0
vote_totals=[]

# List to hold the names of all unique candidates and count them
candidates=[]
unique_candidates=0

# Variable to count the total number of ballot IDs (votes) included in the data set
ballot_count=0

# Read in the file and analyze data
with open(election_data) as csvfile:
    
    vote_set = csv.reader(csvfile, delimiter=",")

    next(vote_set)

    # Populate cadidates list with all unique names                
    for row in vote_set:
        # Count the number of rows of data (votes), ignoring the header
        ballot_count+=1

        current_candidate=row[2]  # Store name of current line

        if current_candidate not in candidates:  # Checks list of candidates for current name
            candidates.append(current_candidate)  # Adds new unique names to the list
            unique_candidates+=1

    # Go through votes for each unique candidate and accumulate results
    for name in candidates:
        #print(name)

        for row in vote_set:
            if row[2]==name:
                print(row[2])
                vote_total_each+=1  # Counts votes for this candidate

        # Compute and add results for the current name to their lists
        vote_percentage_each=vote_total_each/ballot_count
        vote_percentages.append(vote_percentage_each)
        vote_totals.append(vote_total_each)
        #print(vote_total_each)

        vote_total_each=0 # Reset this for the next name on the list



# Display results on screen
print(ballot_count)
print(candidates)
print(unique_candidates)
print(vote_percentages)
print(vote_totals)

