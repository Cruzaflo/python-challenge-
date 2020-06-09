#!/usr/bin/env python
# coding: utf-8

# In[205]:


import os
import csv

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

months = []

profit_losses = []

monthly_changes = []

month_count = 0

net_total = 0 

average_change = 0.0

index = 0

count = 0

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline = "", encoding='utf-8') as csvfile:
    
    datafile = csv.reader(csvfile, delimiter=",")
    
    next(datafile, None)
    
    for row in datafile:        
        months.append(row[0])       
        profit_losses.append(int(row[1]))       
        month_count += 1
        net_total = net_total + int((row[1]))
    
    for number in profit_losses:
        i = profit_losses.index(number)
        if i + 1 < month_count:
            change = profit_losses[i + 1] - profit_losses[i]
            monthly_changes.append(change)                  
            
    #Average Monthly change 
    average_change = (round(average(monthly_changes),2))
    
    #Greatest/Lowest
    greatest_increase = max(monthly_changes)
    greatest_i = monthly_changes.index(greatest_increase)
    min_increase = min(monthly_changes)
    min_i = monthly_changes.index(min_increase)
    
    #print to terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(months[greatest_i + 1]) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(months[min_i + 1]) + " ($" + str(min_increase) + ")")
    
#write to text
results = 'Financial Analysis\n----------------------------\nTotal Months: ' + str(month_count) + '\nTotal: $' + str(net_total) + '\nAverage Change: $' + str(average_change) + '\nGreatest Increase in Profits: ' + str(months[greatest_i + 1]) + ' ($' + str(greatest_increase) + ')' + '\nGreatest Decrease in Profits: ' + str(months[min_i + 1]) + ' ($' + str(min_increase) + ')'
with open('resource_results.txt','w', newline='', encoding='utf-8') as output:
    output.write(results)
    output.close

        
    
        


        


# In[ ]:





# In[ ]:




