import inquirer

questions = [
    inquirer.Text('name', message='What is your name?'),
    inquirer.List('interests', message="Choose your interests", choices=[
        'Coding', 'Gaming', 'Music']),
    inquirer.Text('choice', message="details1",
                  when=lambda answers: answers['interests'] == 'Coding')
]

answers = questions.prompt(questions)

print(answers)
