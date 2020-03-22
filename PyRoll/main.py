import os
import csv

datafile = os.path.join(".","election_data.csv")

# Verify file exists, if not ask user for full path
while not os.path.exists(datafile):
    print(f"Error reading {datafile}: File Not Found")
    datafile = input("Enter the absolute data file path: ")

total_votes = 0 # Count of all entries in the dataset
candidate_votes = {} # Dictionary of all candidates and the total count of votes they won
winner = {'name':'','votes':0} # To stote the winning candidate name and vote count

with open(datafile, "r") as csvinput:
    csvreader = csv.reader(csvinput, delimiter=',')
    # Skip the header
    next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1

## Print the analysis to file
with open("output.txt", "w") as output:
    output.write("PyRoll Election Results:\n")
    output.write("--------------------------\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("--------------------------\n")
    for candidate,votes in candidate_votes.items():
        if votes > winner['votes']:
            winner['name'] = candidate
            winner['votes'] = votes
        output.write(f"{candidate}: {round((votes/total_votes)*100,3)}% ({votes})\n")
    output.write("--------------------------\n")
    output.write(f"Winner: {winner['name']}\n")
    output.write("--------------------------\n")

## Print the analysis to console
try:
    os.system("cls")
except:
    os.system("clear")
with open("output.txt", "r") as output:
    display = output.read()
    print(display)
