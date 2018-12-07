#import the os, the csv and path to csv file
import os
import csv

pollcsv = os.path.join('..', 'PyPoll', 'election_data.csv')


#variables
totalvotes = []
kcount = 0
licount = 0
ccount = 0
ocount = 0

#read csv and perform the commands
with open(pollcsv, 'r') as electionfile:
    election_reader = csv.reader(electionfile, delimiter=',')
    election_header = next(election_reader)

    for row in election_reader:
        #total votes
        voterid = row[0]
        totalvotes.append(voterid)
        if row[2] == "Khan":
            kcount = kcount + 1
        elif row[2] == "Li":
            licount = licount + 1
        elif row[2] == "Correy":
            ccount = ccount + 1
        elif row[2] == "O'Tooley":
            ocount = ocount + 1
    
    percent_khan = kcount/len(totalvotes) * 100
    percent_li = licount/len(totalvotes) * 100
    percent_correy = ccount/len(totalvotes) * 100
    percent_otool = ocount/len(totalvotes) * 100
 

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(totalvotes)}")
print(f"Khan:{round(percent_khan,5)}% {kcount}")
print(f"Li: {round(percent_li,5)}%  {licount}")
print(f"Correy:{round(percent_correy,5)}%  {ccount}")
print(f"O'Tooley:{round(percent_otool,5)}%  {ocount}")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")

ElectionResults = os.path.join("ElectionResults.csv")

with open(ElectionResults, "w", newline="") as datafile:
    
    ElectionResultsWriter = csv.writer(datafile, delimiter = ',')

    ElectionResultsWriter.writerow(["Total Votes", "Winner"]) 
    ElectionResultsWriter.writerow([len(totalvotes), "Khan"])
    ElectionResultsWriter.writerow(["Khan Votes", "Khan Percent"])
    ElectionResultsWriter.writerow([kcount, round(percent_khan,5)])
    ElectionResultsWriter.writerow(["Correy Votes", "Correy Percent"])
    ElectionResultsWriter.writerow([ccount, round(percent_correy,5)])
    ElectionResultsWriter.writerow(["Li Votes", "Li Percent"])
    ElectionResultsWriter.writerow([licount, round(percent_li,5)])
    ElectionResultsWriter.writerow(["O'Tooley Votes", "O'Tooley Percent"])
    ElectionResultsWriter.writerow([ocount, round(percent_otool,5)])
    
