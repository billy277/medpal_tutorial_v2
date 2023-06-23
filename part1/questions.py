import inquirer

medicines = []
# objects in this array will be of the form
# {
# name: string,
# am_days: [(day,dose)],
# pm_days: [(day,dose)]}


def askMedicineQuestion():

    medicineQuestions = [
        inquirer.Text(
            'medicine', message="What is the name of the medicine?"),
        inquirer.Checkbox('daysOfTheWeek',
                          message="Which days of the week do you take this medicine?",
                          choices=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],),
    ]
    medicinesAnswers = inquirer.prompt(medicineQuestions)
    print(medicinesAnswers)
    medicineName = medicinesAnswers['medicine']
    am_pm_questions = []
    for day in medicinesAnswers['daysOfTheWeek']:
        am_pm_questions.append(inquirer.Checkbox(
            day, message=f"What time do you take {medicineName} on {day}?", choices=['AM', 'PM']))
    am_pm_answers = inquirer.prompt(am_pm_questions)

    print(am_pm_answers)

    for day, times in am_pm_answers.items():

        medicine = {
            'name': medicineName,
            'am_days': [],
            'pm_days': []}
        for time in times:
            doseageQuestion = [
                inquirer.Text(
                    f'dose', message=f'What dose do you take of {medicineName} on {day} and {time}?')
            ]
            dose = inquirer.prompt(doseageQuestion)['dose']
            if time == 'AM':
                medicine['am_days'].append((day, dose))
            elif time == 'PM':
                medicine['pm_days'].append((day, dose))
        medicines.append(medicine)
    print(medicines)


moreMeds = True
while moreMeds:
    askMedicineQuestion()
    moreMeds = input("Do you have more medicines? (y/n) ") == 'y'
