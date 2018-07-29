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

