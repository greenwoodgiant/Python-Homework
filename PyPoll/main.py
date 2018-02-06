import csv

with open("election_data_2.csv", newline="") as csv_file:

    polldata = csv.reader(csv_file, delimiter=",")

    # HEADERS : [0] Voter ID
    #           [1] County
    #           [2] Candidate

    # Skip the header row
    next(polldata)
    
    # Empty variables to populate with the reader
    total_votes_cast = 0
    candidate_pool = []
    votes_per_candidate = {}

    for row in polldata:

        # Set the candidate to a variable
        candidate = row[2]

        # Tick the total votes cast up one
        total_votes_cast += 1

        # If the candidate has already been voted for,
        if candidate in candidate_pool:
            # Tick the candidate's vote count up one
            votes_per_candidate[candidate] += 1
        
        else:
            # Add the candidate to the pool
            candidate_pool.append(candidate)
            # Add them to the dict with count of 1
            votes_per_candidate[candidate] = 1

    # Create a text file for the summary
    poll_summary = open("poll_summary.txt", "w+")

    # Create a function to both print to the terminal and write to the .txt
    def print_write(text):
        print(text)
        poll_summary.write(text)

    # Skip a space for posterity
    print ()

    # Print the results
    print_write("Election Results\n")
    print_write("-------------------------\n")
    print_write("Total Votes: " + str(total_votes_cast) + "\n")
    print_write("-------------------------\n")
    
    for item in candidate_pool:
        # Find the percent of the total vote    
        percent = round(float((votes_per_candidate[item] / total_votes_cast) * 100), 1)
        print_write("{0}: {1}% ({2})\n".format(item,percent,votes_per_candidate[item]))

    print_write("-------------------------\n")

    # Find the winner
    winner = max(votes_per_candidate, key=votes_per_candidate.get)

    print_write("Winner: " + winner + "\n")
    print_write("-------------------------\n")