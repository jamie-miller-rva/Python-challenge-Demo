# TODO psuedo code before I begin
# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""


# load our modules (Dependencies)
import os
import csv

# create file_path to our csv file
path_to_csv = os.path.join("Resources", "budget_data.csv")
print(path_to_csv)

# create file_path to output text file
path_to_output = os.path.join("Analysis", "budget_analysis.txt")

# create some variables and containers
total_months = 0



# read the csv file
with open(path_to_csv) as csv_file:

    # # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',') 

    # print(csv_reader)

    # Read the header in the csv_reader object
    header = next(csv_reader)

    # Extract header (first row) to avoid conflict with other data
    first_row = header
    total_months += 1


    # iterate through rows
    for row in csv_reader:

        #Track the total_months
        total_months += 1

        # track other items

    

# Generate output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $\n"
    f"Average  Change: $\n"
    f"Greatest Increase in Profits: ($)\n"
    f"Greatest Decrease in Profits: ($)\n"    
)

# print output
print()
print(output)


# Export to the results to text file
with open(path_to_output, "w") as text_file:
    text_file.write(output) 



