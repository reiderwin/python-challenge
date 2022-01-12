import os
import csv

financial_data = os.path.join("..", "PyBank/Resources", "budget_data.csv")

#Lists to store data
date = []
profit_loss = []


#Open and read csv file
with open(financial_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    for row in csvreader:

        #Add date to python list
        date.append(row[0])

        #Add profit_loss to python list
        profit_loss.append(int(row[1]))

    total_months = len(date)
    total_profit_loss = "${}".format(sum(profit_loss))
    
    difference_list = []
    
    for row in range(total_months - 1):
        first_number = profit_loss[row]
        second_number = profit_loss[row+1]

        difference = second_number - first_number
        difference_list.append(difference)

    average = "${:,.2f}".format((sum(difference_list)) / len(difference_list))
    
    greatest_increase = max(difference_list)
    greatest_increase_index = difference_list.index(greatest_increase)
    greatest_date = date[greatest_increase_index + 1]
    greatest_increase = "${}".format(greatest_increase)

    greatest_decrease = min(difference_list)
    greatest_decrease_index = difference_list.index(greatest_decrease)
    greatest_decrease_date = date[greatest_decrease_index + 1]
    greatest_decrease = "${}".format(greatest_decrease)


    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit_loss}')
    print(f'Average Change: {average}')
    print(f'Greatest Increase in Profits: {greatest_date} ({(greatest_increase)})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({(greatest_decrease)})')




    

 


   

    
    
  
        


        
        
  

       










