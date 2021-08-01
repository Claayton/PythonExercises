# Ex105.2
"""Make a program that has a notes() function that can receive multiples grades from students and it will return a dictionary with the following information:
- Number of notes;
- Te highest grade;
- The lowest grade;
- The average of the class;
- The situation (optional);
- Also add the docstrings."""

def notes(*grades, situation=False):
    """
    -> Receives the grades os several students and returns a dictionary with varous information regarding the grades of the class
    :param grades: Receives student grades (undefined amount).
    :param situation: Indicates wheter or not show the class situation.
    :return: A dictionary with some of the following information about the class:
            number of notes, highest grade, lowest grade, class grade average, class situation(optional).
    """
    notes = grades
    dict = {}
    number_of_notes = len(grades)
    cont = 0
    highest = 0
    lowest = 0
    total = 0
    for c in notes:
        if cont == 0:
            highest = c
            lowest = c
        if c > highest:
            highest = c
        if c < lowest:
            lowest = c
        total += c
        cont += 1
    average = total / number_of_notes
    if average < 6:
        situation_class = 'BAD'
    elif 6 <= average <= 7.5:
        situation_class = 'REGULAR'
    else:
        situation_class = 'EXELLENT'
    dict['Total'] = number_of_notes
    dict['Highest'] = highest
    dict['Lowest'] = lowest
    dict['Average'] = average
    if situation:
        dict['Situation'] = situation_class
    return dict


response = notes(5.5, 9.5, 10, 6.5, situation=True)
print(response)
# help(notes)