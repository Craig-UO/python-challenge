# Imports for file input/output
import os
import csv

# Sets a name for the file path to the data .csv file to be analyzed
budget_data=os.path.join('Resources', 'budget_data.csv')

# Variable to count the total number of months included in the data set
period_count=0

# Variable to sum the net profits/losses over the whole period
net_profit=0

# Variables for the period-to-period change in profits/losses and to accumulate the average
profit_now=0
profit_last=0
sum_of_profit_changes=0

# Variables to hold the value for increase in profits and greatest decrease in profits during the entire period
greatest_profit_increase=0
greatest_profit_decrease=0

# Read in the file and analyze data
with open(budget_data) as csvfile:
    
    data_set = csv.reader(csvfile, delimiter=",")

    next(data_set)
                    
    for row in data_set:
        # Count the number of rows of data, ignoring the header
        period_count+=1

        # Keep running tally of net profits/losses
        net_profit=net_profit+int(row[1])
        #print(f"{net_profit}")

        # Calculate change in profit compared to prior period starting with the second period
        if period_count>1:  # This will ignore the first row, which has no prior row to compare to
            profit_now=int(row[1])
            profit_change=profit_now-profit_last
            sum_of_profit_changes=sum_of_profit_changes+profit_change
            change_running_average=sum_of_profit_changes/(period_count-1)

            if profit_change>greatest_profit_increase:
                greatest_profit_increase=profit_change
                high_change_month=row[0]
            
            if profit_change<greatest_profit_decrease:
                greatest_profit_decrease=profit_change
                low_change_month=row[0]

        else:
            profit_now=int(row[1])

        # Set profit_last to be the current value so it's the prior value for the next iteration
        profit_last=profit_now

# Report results to screen
print("Financial Anlysis")
print("---------------------------------------------")
print(f"Total Months:", period_count)
print("Total: $"+str(net_profit))
print("Average Change: $"+str(round(change_running_average,2)))
print("Greatest Increase in Profits: " + str(high_change_month) + " ($"+str(greatest_profit_increase)+")")
print("Greatest Decrease in Profits: " + str(low_change_month) + " ($"+str(greatest_profit_decrease)+")")
