
import os
import csv

csvpath = os.path.join('PyPoll', 'Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:
    file = open('MG_poll_results.txt','w') 
#loop to count all rows/votes
    csvreader = csv.reader(csvfile, delimiter=',')
    votecount = 0
    allVotes = []
    candidateList = [] 
    
    for row in csvreader:
        votecount += 1 
        allVotes.append(row[2])
                      
        if row[2] not in candidateList: 
            candidateList.append(row[2])    
    print("Election Results")
    file.write("Election Results")
    
    print("----------------------")
    file.write(("----------------------"))
    
    print(f'Total Votes: {votecount}')
    
    file.write((f'Total Votes: {votecount}'))
    
#if name = candidate, add to their list
    winningVotes = 0
    
    for x in candidateList: 
        
        tally = allVotes.count(x)
        
        if (x == "Candidate"):
            print("----------------------")
            file.write("----------------------")
        else:
            percent = round((tally/votecount)*100, 3)
            print(f'{x}: {percent}% ({tally})')
            file.write((f'{x}: {percent}% ({tally})'))
        
        if tally > winningVotes:
            winningVotes = tally
            winner = x
    
print("----------------------")
file.write("----------------------")
                       
print(f'Winner: {winner}')
file.write((f'Winner: {winner}'))