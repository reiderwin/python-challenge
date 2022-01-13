import os
import csv

election_data = os.path.join("..", "PyPoll/Resources", "election_data.csv")

#Lists to store data
voter_id = []
candidate = []

#Open and read csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csvheader = next(csvreader)

    # Read through each row of data after the header
    for row in csvreader:

        #Add column index 0, "vote id" from csv file to python list
        voter_id.append(row[0])

        #Adds column index 2, "candidate" from csv file to python list
        candidate.append(row[2])

    #New variable.
    #Determines total number of votes via length of voter_id list & converts to integer
    total_votes = int(len(voter_id))

    #New varialbe.
    #Function creates a list of 2 new lists. The first list is a unique set of the names.  
    #The second list counts the amount of times the name in the first list appears.
    #Note, I did reference this from the interwebs, but felt it was pretty boilerplate, so fair game.
    candidate_count = [[j,candidate.count(j)] for j in set(candidate)]

    #New variables.
    #Since "candidate_count" is a list of 2 lists, the following separates the lists into standalone list.
    #Both lists contain 4 entries with this particular dataset since there are 4 unique names.
    #This enables soft coding for a similar dataset of election data.
    name_list = [i[0] for i in candidate_count]
    count_list = [i[1] for i in candidate_count]

    #New variable to hold max value from variable "count_list"
    max_value = max(count_list)

    #New variable to determine index where the max value occurs in "count_list"
    winner_index = count_list.index(max_value)
    
    #New variable to store name of winning cadidate using the index from the previous step.
    winner_name = name_list[winner_index]

    #New placeholder list to hold percentages of votes for each candidate that will be calculated next.
    percentages = []

    #Loop to calculate percent of votes for each candidate and format as a percentage with a decimal place.
    #The percentages list is appended with the resulting values.
    for k in range(0, len(count_list)):
        percent = round((count_list[k] / total_votes) * 100, 2)
        percentages.append(percent)

    #Prints results. Need loop to print names of each candidate with required information.
    #The loop allows me to soft code. Yay.
    print("Election Results")
    print("---------------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------------")
    for n in range(0, len(name_list)):
        print(f'{name_list[n]}: {percentages[n]}% ({count_list[n]})')
    print("---------------------------")
    print(f'Winner: {winner_name}')
    print("---------------------------")




  