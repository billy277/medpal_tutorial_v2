# Medpal - Command Line Medicine Planner

## Part 1 - Project Setup and Python Application Introduction

### Goal

- To build a proof of concept medicine planner application that takes user input using the command line, and stores all data in a local file and shows the current week's status for a given user

### What the final application will look like

- Use Python to build application
- Project must be version controlled using Git
- User input to start the program should look like this

```
$ medpal planner ashish
 > Welcome Ashish, here is a look at this week
 > Dates    | AM               | PM                |
    ========|==================|===================|
    Mon 1   | ~~MedA~~  | ~~2~~| --------  | ----- |
    Tue 2   | ~~MedB~~  | ~~2~~| ~~MedA~~  | ~~1~~ |
    Wed 3   | --------  | ---- | --------  | ----- |
    Thu 4   | ~~MedB~~  | ~~2~~| ~~MedA~~  | ~~1~~ |
  * Fri 5   | ~~MedA~~  | ~~2~~| --------  | ----- |
    Sat 6   |   MedB    | 2    | MedA      |   1   |
    Sun 7   | MedA      | 2    | MedA      |   1   |

```

In the input note that:

- `*` indicates that the current day in the example is Friday the 5th (we dont have a month specified for now)
- `~~ ~~` indicates that the medicine for that day and time has been taken
- `-----` indicates no medicines for that day and time slot

This data comes from a comma separated file for each user which lists each medicine, its dosage and its frequency - and for the example above the file will be called `ashish.txt` will look like this:

```
Medicine,Day,Time,Qty,Taken
MedA,Mon,AM,2,True
MedA,Tue,PM,1,True
MedA,Thu,PM,1,True
MedA,Fri,AM,2,True
MedB,Tue,AM,2,True
MedB,Thu,AM,2,True
MedB,Sat,AM,2,False
MedA,Sat,PM,1,False
MedA,Sun,AM,2,False
MedA,Sun,PM,1,False
```

### Assignments List for Part 1

1.1 Project Setup

- Git Setup
- Python and python virutal environment setup
  1.2 Hello World Python CLI application
- Application to print hello world to console
  1.3 Python CLI with input
- Take user input, make it uppercase and print to console
  1.4 Read from user defined file
- Take user input filename, open and read the file, output contents of file to console
