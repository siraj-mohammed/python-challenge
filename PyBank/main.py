import os
import csv

datafile = os.path.join(".","budget_data.csv")

# Verify file exists, if not ask user for full path
while not os.path.exists(datafile):
    print(f"Error reading {datafile}: File Not Found")
    datafile = input("Enter the absolute data file path: ")

line_count = 0 # To count number of records 
total_profit = 0 #  Sum of profits and losses for all months
last_profit = 0 # Profit/Loss from previous month, to calculate change per month
changes = {} # Dictionary containing each month in data and the profit/loss change for that month
total_changes = 0 # Sum of all per-month changes, to calculate average change
the_greatest = {
    "_increase":{"month":"", "value":0}, 
    "_decrease":{"month":"", "value":0}
}

with open(datafile, "r") as csvinput:
    csvreader = csv.reader(csvinput, delimiter=',')
    # Skip the headers
    headers = next(csvreader)
    for row in csvreader:
        line_count += 1
        # Calculate change starting from the second row
        if last_profit != 0:
            changes[row[0]] = int(row[1]) - last_profit
        last_profit = int(row[1])
        total_profit += last_profit

for month, change in changes.items():
    total_changes += change
    # capture the month with greatest increase and the profit/loss value
    if change > the_greatest["_increase"]["value"]:
        the_greatest["_increase"]["value"] = change
        the_greatest["_increase"]["month"] = month
    # capture the month with greatest decrease and the profit/loss value
    if change < the_greatest["_decrease"]["value"]:
        the_greatest["_decrease"]["value"] = change
        the_greatest["_decrease"]["month"] = month

average_change = total_changes / (line_count - 1) # 1 less than total rows since 'change' starts from second month

## Print the analysis to file
with open("output.txt", "w") as output:
    output.write("PyBank Financial Analysis:\n")
    output.write("--------------------------\n")
    output.write(f"Total Months: {line_count}\n")
    output.write(f"Total: ${total_profit}\n")
    output.write(f"Average Change: ${round(average_change, 2)}\n")
    output.write(f"Greatest Increase in Profits: {the_greatest['_increase']['month']} (${the_greatest['_increase']['value']})\n")
    output.write(f"Greatest Decrease in Profits: {the_greatest['_decrease']['month']} (${the_greatest['_decrease']['value']})\n")

## Print the analysis to console
try:
    os.system("cls")
except:
    os.system("clear")
with open("output.txt", "r") as output:
    display = output.read()
    print(display)