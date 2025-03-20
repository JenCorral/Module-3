# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Define absolute file paths for reliability
file_to_load = r"C:\Users\12096\Desktop\UCI Homework\Starter_Code\PyPoll\Resources\election_data.csv"
file_to_output = r"C:\Users\12096\Desktop\UCI Homework\Starter_Code\PyPoll\analysis\election_analysis.txt"

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track candidate names and vote counts

# Winning Candidate and Winning Count Tracker
winning_count = 0
winning_candidate = ""

try:
    # Open the CSV file and process it
    with open(file_to_load, mode="r") as election_data:
        reader = csv.reader(election_data, delimiter=",")

        # Skip the header row
        header = next(reader)

        # Loop through each row of the dataset and process it
        for row in reader:
            candidate_name = row[2]

            # Increment the total vote count for each row
            total_votes += 1

            # Track the vote count for each candidate
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            else:
                candidate_votes[candidate_name] = 1

except FileNotFoundError:
    print(f"Error: The file at {file_to_load} was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

try:
    # Open a text file to save the output
    with open(file_to_output, mode="w") as txt_file:

        # Print the header and total votes (to terminal and text file)
        header = (
            "Election Results\n"
            "-------------------------\n"
            f"Total Votes: {total_votes}\n"
            "-------------------------\n"
        )
        print(header)
        txt_file.write(header)

        # Loop through the candidates to determine vote percentages and identify the winner
        for candidate_name, votes in candidate_votes.items():
            vote_percentage = (votes / total_votes) * 100

            # Update the winning candidate if this one has more votes
            if votes > winning_count:
                winning_count = votes
                winning_candidate = candidate_name

            # Print and save each candidate's vote count and percentage
            candidate_results = f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n"
            print(candidate_results)
            txt_file.write(candidate_results)

        # Generate and print the winning candidate summary
        winning_summary = (
            "-------------------------\n"
            f"Winner: {winning_candidate}\n"
            "-------------------------\n"
        )
        print(winning_summary)
        txt_file.write(winning_summary)

except FileNotFoundError:
    print(f"Error: Could not write to the file at {file_to_output}. Check the directory path.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
