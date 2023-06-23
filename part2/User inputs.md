# Getting user inputs 

We will use the `inquirer` package to get user inputs  - we want to ask the user about the `dose`, `name`, and `timing` of each of their medicines.
**LOOK AT THE `questions.py` for this whole assignment**

To do this we need to learn the following things:

- What is the inquirer package and how to use it in python
- How to ask questions and provide different options (multiple choice, list of options etc...)
- How to combine the different questions and save the answers into an object


## Section 1. Inquirer Package Setup
This is a package that supercharges the `input()` method. It allows you to ask more detailed questions and have multiple choice options.

For new packages we need to **import** the package at the top of your file (_Already Done_)

```
import inquirer
```

Inquirer works in **THREE STEPS**. Step 1. you need to set up the question in an array, Step 2. you need to `prompt` the question, and Step 3. read the answers from the object returned by `prompt()`
- Step 1. Setting up the question into an array

```
# questions is an array with only one element inside (a `inquirer.Text()` element)
questions = [inquirer.Text('answerVar', message="What is your name?")]
```
- Step 2. `prompt` the question
```
# calling `prompt()` will run through your questions on the command line for the user and store all of the answers in the returned object

answers = inquirer.prompt(questions)
```
- Step 3. read the answers
```
# the `answers` object is a dictionary which has the key specified in step 1 for each question, and values are the user's answers.
```


### Getting Text inputs
Imagine asking questions like `What is your name?` or `What is the name of your medicine`. We expect to get `string` or `text` objects as responses to these questions so we use a `Text` type question in inquirer. In the example above you see how to get text inputs


## Section 2. Getting Checkbox inputs
Imagine asking a user to select items from a list, ex. `Choose all the time slots that work for you` there we want to give the user a set of options and have them able to scroll between the options and check or uncheck an option. We can do this using the `Checkbox` question type in `inquirer` package.

To get checkbox inputs we only need to change **STEP 1** of how `inquirer` works. We need to define `.Checkbox()` instead of `.Text()` in the question type.

```
inquirer.Checkbox('daysOfTheWeek',
                          message="Which days of the week do you run?",
                          choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
```

Adding this question into the list of questions passed to `prompt` will result in multiple choice options being presented to the user.

All answers are stored in the variable returned by `prompt`. In the examples able look at how it is being stored -- and note that the key in the final dictionary is the same as the first input of the `inquirer.Checkbox(...)` or `inquirer.Text(...)` methods.


## Assignment

   
1. Look at new file in `part2` named `questions.py`
2. Uncomment section 1 and follow along with the section 1 above 
3. Uncomment section 2 and follow along with the section 2 above
4. In section 3 of the `questions.py` file, use inquirer to __get the following data__ from a user and __save into a single object__:
   1. Medicine name
   2. Days of the week for each medicine
   (HINT): Keep asking user if they have more medicines until they say no (While loop)
