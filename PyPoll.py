import os
import csv
import collections

file_path=os.path.join('.','Resources','PyPoll_election_data.csv')

total_votes=[]
unique_names=[]
list_of_votes=[]
candidate_votes={}
vote_count=[]
percents=[]


csvfile=open("./Resources/PyPoll_election_data.csv")
csvreader=csv.reader(csvfile, delimiter=',') 

csv_header=next(csvreader)

for each_row in (csvreader):
    c_name=each_row[2]
    list_of_votes.append(c_name)
    if c_name not in unique_names:
        unique_names.append(c_name)



total_votes=len(list_of_votes)
number_of_candidates=len(unique_names)


for x in range(number_of_candidates):
    candidate_votes[unique_names[x]]=list_of_votes.count(unique_names[x])
       
    percents=(candidate_votes[unique_names[x]])/total_votes*100
    



# the following is literally line for line as the TA showed it and its giving the candidate with the lowest number of votes
poll_winner = 0

for x, y in candidate_votes.items():
    if y > poll_winner:
        poll_winner_votes = y
        poll_winner_name = x



Election_Results=(
"Election Results\n"
f"----------------------------\n"
f"Total Votes: {len(list_of_votes)}\n"
f"----------------------------\n"
f"{candidate_votes}\n"
f"----------------------------\n"
f"{poll_winner_name}\n"
)

with open("Analysis/Election_Results.txt",mode="w") as output_text_file:
    output_text_file.write(Election_Results)