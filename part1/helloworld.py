print("hello world!")
userInput = input("Enter some input: ")
upperInput = userInput.upper()
print(upperInput)
file = open("part_c_answers.txt", "r")
print(file.read())
userInput2 = input("Enter some input: ")
file2 = open("file2.txt", "a")
file2.write(userInput2)
file2.close
file2 = open("file2.txt", "r")
print(file2.read())