import os 
import csv
from io import StringIO

py_bank_csv = os.path.join('resources', 'budget_data.csv') #this establishes a variable with the path to my csv
print("Path to the file:", py_bank_csv)

#This function is to get the total months in the csv
def tot_mon(csvreader, buffer):   #defing the function (buffer apears as I need it to help read the contents to a text file)
    total_months = 0         #declaring an empty variable to use
    for row in csvreader:    #this loops though every row of the csv
        total_months = total_months + 1       #this adds one for every row it goes through
    print("Total Months:", total_months)      #the count is equal to the number of rows/months
    print("Total Months:", total_months, file=buffer) #this statement is so that I can copy the output to the text file
#This function totals the profit
def tot_sum(file_path, buffer): #defing the function (buffer apears as I need it to help read the contents to a text file)
    total = 0 #declaring an empty variable to use
    #open the file to read
    with open(file_path, 'r') as csvfile:
        #reads the csv file with delimeter
        csvreader = csv.reader(csvfile, delimiter=',')
        #gets the first row as a header
        header = next(csvreader)
        #loops through every row  
        for row in csvreader:
            total = total + int(row[1]) #adds every value in index 1, or column two
        print("Total:", total)
        print("Total:", total, file=buffer)
#calculate the average change from month to month
def av_change(file_path, buffer): #defing the function (buffer apears as I need it to help read the contents to a text file)
    prof_list = [] #declaring an empty variable to use
    fin_list = []  #declaring an empty variable to use
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)  
        for row in csvreader:
            prof_list.append(int(row[1])) #this loops through the rows can puts the value of everythin in index 1 into a list
        for i in range(1, len(prof_list)): #this loops though the new list that was created and iterate over starting from second element
            diff = prof_list[i] - prof_list[i - 1] #this subtracts each value from the next
            fin_list.append(diff) #this adds the new value of each to a list
    
        if len(fin_list) > 0: #this just makes sure that the list is not empty
            average_change = round(sum(fin_list) / len(fin_list), 2) #caluclation for the average change from month to month
        print("Average Change:", average_change) #output
        print("Average Change:", average_change, file=buffer) #text file output
#finds the greatest increase between months
def greatest_increase(file_path, buffer): #defing the function (buffer apears as I need it to help read the contents to a text file)
    date_col = []
    pl_col = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)  
        for row in csvreader:
            date_col.append(row[0]) #puts the dates into a list
            pl_col.append(int(row[1])) #puts profit/losses into a list

        max_val = float('-inf') #sets the value to the smallest float value
        max_date = None #no value assigned


        for i in range(1, len(pl_col)): #iterates over pl_col from the second element on
            diff_two = pl_col[i] - pl_col[i - 1] #finds the difference between each element
            if diff_two > max_val: 
                max_val = diff_two #this makes it to where the biggest value is always put into max_value
                max_date = date_col[i] #this finds the corresponding date

        print(f"Greatest Increase in Profits: {max_date} (${max_val})")
        print(f"Greatest Increase in Profits: {max_date} (${max_val})", file=buffer)
#finds the greatest decrease between months, essentionlly the same code as above, will highlight differences
def greatest_decrease(file_path, buffer): #defing the function (buffer apears as I need it to help read the contents to a text file)
    date_col = []
    pl_col = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)  
        for row in csvreader:
            date_col.append(row[0])
            pl_col.append(int(row[1]))

        min_val = float('inf') #sets to positave infinity
        min_date = None


        for i in range(1, len(pl_col)):
            diff_two = pl_col[i] - pl_col[i - 1]
            if diff_two < min_val: #this swap of the greater than/ lesser than symbol helps to find the smaller of the two
                min_val = diff_two
                min_date = date_col[i]

        print(f"Greatest Increase in Profits: {min_date} (${min_val})")
        print(f"Greatest Increase in Profits: {min_date} (${min_val})", file=buffer)

buffer = StringIO() #creates in memory buffer 4 strings

with open(py_bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #prints the contents along with a copy that is for the text file output
    print(file=buffer) #for spacing on text file
    print() #for spacing
    print("Financial Analysis")
    print("Financial Analysis", file=buffer)
    print(file=buffer)
    print()
    print("------------------------------", file=buffer)
    print("------------------------------")
    print(file=buffer)
    print()
    tot_mon(csvreader, buffer) #outputs tot_mon() contents
    print(file=buffer)
    print()
    tot_sum(py_bank_csv, buffer) #outputs tot_sum() contents
    print(file=buffer)
    print()
    av_change(py_bank_csv, buffer) #outputs av_change() contents
    print(file=buffer)
    print()
    greatest_increase(py_bank_csv, buffer) #outputs greatest_increase() contents
    print(file=buffer)
    print()
    greatest_decrease(py_bank_csv, buffer) #outputs greatest_decrease() contents
    
output = os.path.join('analysis', 'bank.txt') #establishes path to where the text file is
with open(output, 'w') as file: #allows us to write to the file
    file.write(buffer.getvalue()) #ouput to the text file
        