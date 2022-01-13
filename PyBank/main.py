import os
import csv

financial_data = os.path.join("..", "PyBank/Resources", "budget_data.csv")

#Lists to store data
date = []
profit_loss = []


#Open and read csv file
with open(financial_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csvheader = next(csvreader)

    # Read through each row of data after the header
    for row in csvreader:

        #Add date to python list
        date.append(row[0])

        #Add profit_loss to python list
        profit_loss.append(int(row[1]))

    #New variable to hold value for total number of rows (months) in the date list.
    total_months = len(date)

    #New varialble to hold the sum of "profit_loss" list.  Formats to dollars.
    total_profit_loss = "${}".format(sum(profit_loss))
    
    #New placeholder to store list of differences in profit loss for the next loop.
    difference_list = []
    
    #Loop to compare adjacent values in "profit_loss" list
    for row in range(total_months - 1):
        first_number = profit_loss[row]
        second_number = profit_loss[row+1]

        #New variable to calculate difference between adjacent values
        difference = second_number - first_number
        
        #Appends placeholder list with the results of the calculation.
        difference_list.append(difference)

    #New variable generated from calculation which determines average of difference of adjacent values.
    #Formatted for dollars and cents
    average = "${:,.2f}".format((sum(difference_list)) / len(difference_list))
    
    #New variable to hold max value in "difference_list."
    greatest_increase = max(difference_list)
    #New variable to hold index of greatest increase in "difference_list."
    greatest_increase_index = difference_list.index(greatest_increase)
    #New variable to hold date using index from previous step.
    greatest_date = date[greatest_increase_index + 1]
    #Formats for dollars
    greatest_increase = "${}".format(greatest_increase)

    #Same operations as above, except for decreases.
    greatest_decrease = min(difference_list)
    greatest_decrease_index = difference_list.index(greatest_decrease)
    greatest_decrease_date = date[greatest_decrease_index + 1]
    greatest_decrease = "${}".format(greatest_decrease)

    #F strings to print results as requested.
    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit_loss}')
    print(f'Average Change: {average}')
    print(f'Greatest Increase in Profits: {greatest_date} ({(greatest_increase)})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({(greatest_decrease)})')




    

 


   

    
    
  
        


        
        
  

       










