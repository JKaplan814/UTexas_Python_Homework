import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvfile,None)

    candidates = []

    total_votes = 0

    for rows in csvreader:
        total_votes = total_votes + 1

        if rows[2] in candidates:
            pass
        else:
            candidates.append(rows[2])
    
    num_candidates = len(candidates)

    votes = [0] * num_candidates

    csvfile.seek(0)
    next(csvfile,None)

    for rows in csvreader:
        i = candidates.index(rows[2])
        votes[i] = votes[i] + 1
    print(votes)

winner = votes.index(max(votes))

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

i = 0
while i <= num_candidates - 1:
    percentage = votes[i] / total_votes
    print(str(candidates[i]) + ": " + str("{:.2%}".format(percentage)) + " (" + str(votes[i]) + ")")
    i = i + 1

print("------------------------")
print("Winner: " + candidates[winner])
print("------------------------")

f = open("PyPoll_Analysis.txt", "w")
f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(total_votes) + "\n")
f.write("-------------------------\n")

i = 0
while i <= num_candidates - 1:
    percentage = votes[i] / total_votes
    f.write(str(candidates[i]) + ": " + str("{:.2%}".format(percentage)) + " (" + str(votes[i]) + ")\n")
    i = i + 1

f.write("------------------------\n")
f.write("Winner: " + candidates[winner] +"\n")
f.write("------------------------\n")