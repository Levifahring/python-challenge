import os
import csv
from io import StringIO

py_poll_csv = os.path.join('resources', 'election_data.csv') #this establishes a variable with the path to my csv
print("Path to the file:", py_poll_csv)
#This function is to get the total months in the csv
def tot_vot(csvreader, buffer): #defing the function (buffer apears as I need it to help read the contents to a text file)
    total_votes = 0  #declaring an empty variable to use
    for row in csvreader: #this loops though every row of the csv
        total_votes = total_votes + 1 #this adds one for every row it goes through 
    print("Total Votes:", total_votes) #output, the count is equal to the number of rows/months
    print("Total Votes:", total_votes, file=buffer) #this statement is so that I can copy the output to the text file
#This function fins the name of the candidates, their vote percentage, and the total votes. finanly it outputs a winner
def candidates(file_path, buffer): #defing the function (buffer apears as I need it to help read the contents to a text file)
    can_list_full = []
    total_votes = 0
    #open the file to read
    with open(file_path, 'r') as csvfile:
         #reads the csv file with delimeter
        csvreader = csv.reader(csvfile, delimiter=',')
        #gets the first row as a header
        header = next(csvreader)  
        for row in csvreader: #this loops through each row
            can_list_full.append(row[2]) #appends the canditates to a list
            total_votes = total_votes + 1 #reestablishes total votes within the function
    
    can_list_clean = list(set(can_list_full))  #this gets us unique candidates only by making it a set, and then returns them to a list

    vote_dict = {can: can_list_full.count(can) for can in can_list_clean} #this dictionary counts how many time a candidate got a vote by counting the number of times they appear
   
    for can in can_list_clean: #this loop goes through each candidate
        elect_one = vote_dict[can] #this is the number of votes
        vote_per = (elect_one / total_votes) * 100 #this calculates the perctange of votes that each person recieved 
        print(f"{can}: {vote_per:.3f}% ({elect_one})") #prints the output of the loop, candidate name, vote percentage, votes
        print() #allows spaces
        print(f"{can}: {vote_per:.3f}% ({elect_one})", file=buffer) #output, copy for the text file
        print(file=buffer)

    elected = max(vote_dict, key=vote_dict.get) #calculates which candidate recieved the most votes

    print(f"Winner: {elected}") #outputs winner
    print(f"Winner: {elected}", file=buffer) #output, copy for text file


buffer = StringIO() #creates in memory buffer 4 strings
     


with open(py_poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(file=buffer) #output, copy for text file
    print() #prints empty line
    print("Election Results", file=buffer)
    print("Election Results")
    print(file=buffer)
    print()
    print("------------------------", file=buffer)
    print("------------------------")
    print(file=buffer)
    print()
    tot_vot(csvreader, buffer) #outputs the fuction tot_vot()
    print(file=buffer)
    print()
    print("------------------------", file=buffer)
    print("------------------------")
    print(file=buffer)
    print()
    candidates(py_poll_csv, buffer) #outputs the fuction candidates()
    print(file=buffer)
    print()
    print("------------------------", file=buffer)
    print("------------------------")
    
output = os.path.join('analysis', 'election_results.txt') #establishes path to where the text file is going to be
with open(output, 'w') as file: #allows us to write to the file
    file.write(buffer.getvalue()) #ouput to the text file
