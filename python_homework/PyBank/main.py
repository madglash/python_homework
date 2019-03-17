import os
import csv

csvpath = os.path.join('PyBank', 'Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    monthcount = 0
    total = 0
    for row in csvreader:
        monthcount = monthcount + 1
        total += int(row[1])
    
    #Number of months.
    print(monthcount)
    #Sum of profits/losses.
    print(total)

    previous = 0
    current = 0
    
    differencesList = []
    monthsList=[]
    
    for row in csvreader: 
        if(row[1] == "Profit/Losses"):
            previous = 0
        else:
            current = int(row[1])
            myDiff = (current - previous)
            differencesList.append(myDiff)
            monthsList.append(row[0])
            previous = current
      
    averageChange = sum(differencesList)/ monthcount
    print(differencesList)
    print(monthsList)

  DLmax = differencesList.index(max(differencesList))
          
  DLmin = differencesList.index(min(differencesList))
    
  print(f'${sum(differencesList)}')
  print(sum(differencesList))
  print(len(differencesList))
  print(sum(differencesList) / (len(differencesList)-1))
    
  print(monthsList)

print("Financial Analysis")
print("-----------------------------")

print("Total Months: " + str(monthcount))
print("Total: $" + str(total))
print("Average Change: $" + str(round(averageChange, 2)))

print("Greatest Increase in Profits: " + monthsList[DLmax] + " $" + str(max(differencesList)))
print("Greatest Decrease in Profits: " + monthsList[DLmin] + " $" + str(min(differencesList)))
