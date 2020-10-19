# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:43:25 2020

@author: brook
"""

# Dependencies
import csv
import os
 
# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_profit = 0

# READ THE CVS AND CONVERT IT INTO A LIST OF DICITONARIES
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

     # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to profit_change_list
    first_row = next(reader)
    total_months += 1
    total_profit += int(first_row[1])
    prev_profit = int(first_row[1])


    for row in reader:
        
        # TRACK TOTALS FOR ENTIRE PERIOD
        total_months += 1
        total_profit += int(row[1])
        

        # TRACK THE MONTHLY CHANGE IN PROFIT
        # VERY IMPORTANT that the prior_month_profit is defined AFTER the 
        #    current month calculation is performed (flow of execution)
        # Append profit change calculation to the profit list so that we 
        #    have a complete list of all monthly profits
        # VERY IMPORTANT that we use square brackets around [monthly_profit] 
        #    to ensure it's appended to the end of the list instead of adding 
        #    the value of the monthly_gain_loss field to EACH existing value of 
        #    the monthly_gain_loss_list
        # Effectively, we're creating a series - Month-to-Month Change in Profit - 
        #    in working memory but never appending it to the original csv file.
        

        # TRACK MONTHLY PROFIT CHANGE
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_change_list += [profit_change]
        month_of_change += [row[0]]
        
        # CALCULATE THE GREATEST MONTHLY INCREASE
        if(profit_change > greatest_increase[1]):
            greatest_increase[0] = (row[0])
            greatest_increase[1] = profit_change
        
        # CALCULATE THE GREATEST MONTHLY DECREASE
        if(profit_change < greatest_decrease[1]):
            greatest_decrease[0] = (row[0])
            greatest_decrease[1] = profit_change

# CALCULATE THE AVERAGE PROFIT CHANGE
        
profit_change_avg = sum(profit_change_list) / len(profit_change_list)


# GENERATE OUTPUT SUMMARY
output = (
    f"\nFinancial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit(Loss): ${total_profit:,.0f}\n"
    f"Average Profit Change: ${profit_change_avg:,.2f}\n"
    f"Greatest Profit Increase: {greatest_increase[0]} ${greatest_increase[1]:,.0f}\n"
    f"Greatest Profit Decrease: {greatest_decrease[0]} ${greatest_decrease[1]:,.0f}\n"
    )

# PRINT THE OUTPUT
print(output)

# EXPORT FINANCIAL SUMMARY TO TEXT FILE
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)