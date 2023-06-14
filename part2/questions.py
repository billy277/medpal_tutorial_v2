import inquirer


# Section 1 -- starts HERE <--
# questions is an array with only one element inside (a `inquirer.Text()` element)
questions = [inquirer.Text('nameQuestion', message="What is your name?")]

# we can add new questions into the questions_text array to also ask it together
newQuestion = inquirer.Text('ageQuestion', message="How old are you?")
questions.append(newQuestion)
# calling `prompt()` will run through your questions on the command line for the user and store all of the answers in the returned object
answers_text = inquirer.prompt(questions)
# the `answers` object is a dictionary which has the key specified in step 1 for each question, and values are the user's answers.
print("answers_text: ", answers_text)

# Q1: What happens when we change the key for our question? (i.e. answerVar)

# Section 1 -- ends HERE <--
#######################################################
# Section 2  -- starts HERE <--
# questions_checkbox = [inquirer.Checkbox('daysOfTheWeek',
#                                         message="Which days of the week do you run?",
#                                         choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])]
# answers_checkbox = inquirer.prompt(questions_checkbox)

# print(answers_checkbox)
# Section 2 -- ends HERE <--
#######################################################################
# ADD SECTION 3 CODE BELOW and COMMENT ALL CODE ABOVE
