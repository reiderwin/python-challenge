import os
import csv

election_data = os.path.join("..", "PyPoll/Resources", "election_data.csv")

#Lists to store data
voter_id = []
candidate = []

#Open and read csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    for row in csvreader:

        #Add column index 0, "vote id" from csv file to python list
        voter_id.append(row[0])

        #Adds column index 2, "candidate" from csv file to python list
        candidate.append(row[2])

    total_votes = int(len(voter_id))

    
    candidate_count = [[j,candidate.count(j)] for j in set(candidate)]


    name_list = [i[0] for i in candidate_count]
    count_list = [i[1] for i in candidate_count]

    max_value = max(count_list)

    winner_index = count_list.index(max_value)
    
    winner_name = name_list[winner_index]

    percentages = []

    for k in range(0, len(count_list)):
        percent = round((count_list[k] / total_votes) * 100, 2)
        percentages.append(percent)

    print("Election Results")
    print("---------------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------------")
    for n in range(0, len(name_list)):
        print(f'{name_list[n]}: {percentages[n]}% ({count_list[n]})')
    print("---------------------------")
    print(f'Winner: {winner_name}')
    print("---------------------------")




  