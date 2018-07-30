import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    header=next(csvfile,None)

    monthly_change = []
    total_months = 0
    total_profit = 0

    greatest_increase = 0
    greatest_decrease = 0


    previous = 0
    for row in csvreader:
        current = float(row[1])

        if previous == 0:
            pass
        else:
            monthly_change.append(current - previous)

        total_months = total_months + 1
        total_profit = float(row[1]) + total_profit

        if (current - previous) > greatest_increase:
            greatest_increase = current - previous
            increase_date = row[0]
        elif current - previous < greatest_decrease:
            greatest_decrease = current - previous
            decrease_date = row[0]
        
        previous = float(row[1])

average = round(sum(monthly_change) / len(monthly_change),2)

print("Financial Analysis")
print("------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(total_profit))
print("Average: $" + str(average))
print("Greatest Increase in Profits: " + increase_date + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + decrease_date + " $(" + str(greatest_decrease) + ")")

f = open('PyBank_Analysis.txt','w')
f.write("Financial Analysis\n")
f.write("------------------------------\n")
f.write("Total Months: " + str(total_months)+ "\n")
f.write("Total: " + str(total_profit) + "\n")
f.write("Average: " + str(average) + "\n")
f.write("Greatest Increase in Profits: " + increase_date + " $" + str(greatest_increase) + "\n")
f.write("Greatest Decrease in Profits: " + decrease_date + " $(" + str(greatest_decrease) + ")\n")
f.close()