

output = []
# Function to generate welcome message
def welcome():
    username = input("What is your name? ")
    output.append("Welcome " + str(username) + ", here is a look at this week")

# Function to print Output

def printOutput(x):
    for item in x:
        print(item)

# write a function to generate the header row of the table and add it to output list

def headerRow():
    output.append("Dates    | AM               | PM                |")
    output.append(" ========|==================|===================|")

# Write a function that takes the following inputs (Day, date, am_medicine, am_dose, pm_medicine, pm_dose) outputs one row into the output table

def outputRow(day, date, am_medicine, am_dose, pm_medicine, pm_dose):
    output.append(f'{day}\t| {date}\t| {am_medicine}\t| {am_dose}\t| {pm_medicine}\t| {pm_dose}\t|')
    

# Order Of Operations

welcome()
headerRow()
outputRow("Sun", "1", "MedA", "2", "", "")
outputRow("Mon", "2", "MedA", "2", "", "")
outputRow("Tue", "3", "MedA", "2", "", "")
outputRow("Wed", "4", "MedA", "2", "", "")
outputRow("Thu", "5", "MedA", "2", "", "")
outputRow("Fri", "6", "MedA", "2", "", "")
outputRow("Sat", "7", "MedA", "2", "", "")

printOutput(output)

