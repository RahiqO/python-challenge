import csv 

filepath = "Pypoll/Resources/election_data.csv"
total = 0
first_vote = 0
second_vote = 0
numberofvoters = 0 
with open (filepath, "r") as election_file:
    Data = csv.reader (election_file, delimiter= ",")

    next(Data)
    
    for row in Data:
       # print(f"voter {numberofvoters+1}")
        first_vote = row[1]
        current_vote= row[0]
        total = total+1
        if first_vote 
print (total)
