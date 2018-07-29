import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvfile,None)

    total_months = 0
    total_profit = 0

    greatest_increase = 0
    greatest_decrease = 0

    for row in csvfile:
        total_months = total_months + 1
        total_profit = float(row[1]) + total_profit

        if float(row[1]) > greatest_increase:
            greatest_increase = float(row[1])
            increase_date = row[0]
        elif float(row[1]) < greatest_decrease:
            greatest_decrease = float(row[1])
            decrease_date = row[0]

average = round(total_profit / total_months,2)

print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(total_profit))
print("Average: " + str(average))
print("Greatest Increase in Profits: " + increase_date + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + decrease_date + " $(" + str(greatest_decrease) + ")")
