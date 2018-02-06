import csv

with open("budget_data_2.csv", newline="") as csvfile:

    budget = csv.reader(csvfile, delimiter=",")

    # HEADERS : [0] Date (12-Oct)    [1] Revenue (1154293)

    # Skip the header row
    next(budget)

    total_months = 0
    total_rev = 0
    
    max_rev_month = ""
    max_rev = 0

    min_rev_month = ""
    min_rev = 0

    for row in budget:
        # Make the Revenue an integer
        row[1] = int(row[1])

        # Add one to the month counter
        total_months = total_months + 1
        
        # Add the revenue to the total
        total_rev = total_rev + row[1]

        # If revenue is greater than current leader,
        if row[1] > max_rev:
            # Set month / revenue to variable
            max_rev_month = row[0]
            max_rev = row[1]
        
        # If revenue is lower than current leader,
        if row[1] < min_rev:
            # Set month / revenue to variable
            min_rev_month = row[0]
            min_rev = row[1]
        
    # Create a text file for the summary
    fin_analysis = open("fin_analysis.txt", "w+")
    
    # Create a function to both print to the terminal and write to the .txt
    def print_write(text):
        print(text)
        fin_analysis.write(text)

    # Calculate the Average revenue per month
    average_rev = round(total_rev / total_months)

    # Skip a space for posterity
    print ()

    print_write("Financial Analysis\n")
    print_write("----------------------------\n")
    print_write("Total Months: {0}\n".format(str(total_months)))
    print_write("Total Revenue: ${0}\n".format(str(total_rev)))
    print_write("Average Revenue Change: ${0}\n".format(str(average_rev)))
    print_write("Greatest Increase in Revenue: {0} (${1})\n".format(max_rev_month, max_rev))
    print_write("Greatest Decrease in Revenue: {0} (${1})\n".format(min_rev_month, min_rev))