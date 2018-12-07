#import the os, the csv and path to csv file
import os
import csv
budgetcsv = os.path.join('..', 'PyBank', 'budget_data.csv')

#name variables 
totalmonths = []
profits_losses = []
total_profit = 0
index = 0
ProLossList = []
ListOfChanges = []
TotalofChanges = 0.0
BestMonth = ""
WorstMonth = ""

#read csv and perform the commands
with open(budgetcsv, 'r') as budgetfile:
    budget_reader = csv.reader(budgetfile, delimiter=',')
    budget_header = next(budget_reader)


    for row in budget_reader:
        #total number of months
        month = row[0]
        totalmonths.append(month)
        #sum of profit and loss
        profits_losses = int(row[1])
        ProLossList.append(profits_losses)
        total_profit = total_profit + profits_losses
        #average change between months
        index = len(totalmonths) - 2
        Start = ProLossList[index]
        Change =  profits_losses - Start
        ListOfChanges.append(Change)
        TotalofChanges += Change
    average_change = TotalofChanges/(len(ListOfChanges)-1)

    for x in range(len(ListOfChanges)):
        Inc = max(ListOfChanges)
        Dec = min(ListOfChanges)
        if ListOfChanges[x] >= Inc:
            BestMonth = totalmonths[x]
        elif ListOfChanges[x] <= Dec:
            WorstMonth = totalmonths[x]

print(f"Financial Report")
print(f"-----------------------------------------------")
print(f"Total Number of Months: {len(totalmonths)}")
print(f"Total Profit: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Profit: {BestMonth} ${Inc}")
print(f"Greatest Loss: {WorstMonth} ${Dec}")

FinancialAnalysis = os.path.join("FinancialAnalysis.csv")

with open(FinancialAnalysis, "w", newline="") as datafile:
    
    FinancialAnalysisWriter = csv.writer(datafile, delimiter = ',')

    FinancialAnalysisWriter.writerow(["Total Months", "Total Profit", "Average Change", "Best Month", "Greatest Profit", "Worst Month", "Least Profit"])

    FinancialAnalysisWriter.writerow([len(totalmonths), total_profit, average_change, BestMonth, Inc, WorstMonth, Dec])