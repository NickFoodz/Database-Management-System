# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Nick Fuda, Anirudh Kandula, Patrick Spalton, Neo Ling"

# Update "" with your team (e.g. T102)
__team__ = "T125"

#==========================================#
# Place your student_school_list function after this line
def student_school_list(filename: str, school: str) -> dict:
    """Return a list of students with the same age as the input age.

    Preconditions: school = ('GP' or 'MB' or 'CF' or 'BD' or 'MS'), filename = 'student-mat.csv'.


    >>> student_school_list('student-mat.csv', 'GP')
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 
    'G1': 5, 'G2': 6, 'G3': 6}, {element 2}, etc...]

    >>> student_school_list('student-mat.csv', 'MB')
    [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 
    'G1': 5, 'G2': 5, 'G3': 5}, {element 2}, etc...]

    >>> student_school_list('student-mat.csv', 'BD')
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 2, 'Absences': 0,
    'G1': 7, 'G2': 7, 'G3': 0}, {element 2}, etc...]
    """
    import string
    file = open(filename, 'r')
    school_list = []
    i = 0

    for line in file:
        value = line.replace('\n', '').replace(' ', '').split(',')

        if i == 0:
            header = value
        elif value[0] == str(school):
            directory = {}
            directory[header[1]] = int(value[1])
            directory[header[2]] = float(value[2])
            directory[header[3]] = int(value[3])
            directory[header[4]] = int(value[4])
            directory[header[5]] = int(value[5])
            directory[header[6]] = int(value[6])
            directory[header[7]] = int(value[7])
            directory[header[8]] = int(value[8])
            school_list.append(directory)

        i += 1

    return school_list

#==========================================#
# Place your student_health_list function after this line
def student_health_list(filename: str, health: int) -> list:
    """Return a list of students whose health value, Health, equals the value inputted.
    
    Precondition: Health <= 5, Health >= 1, filename = 'student-mat.csv'.
    
    
    >>>student_health_list('student-mat.csv', 2)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 10, 'G2': 8, 'G3': 9}, 
    {'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14},
    {another element}, ... ]
    
    >>>student_health_list('student-mat.csv', 5)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 15, 'G2': 14, 'G3': 15}, 
    {'School': 'GP', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'G1': 6, 'G2': 10, 'G3': 10}, 
    {another element}, ... ]
    
    >>>student_health_list('student-mat.csv', 1)
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, 
    {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18, 'G3': 19}, 
    {another element}, ... ]
    """
    import string
    infile = open(filename, 'r')
    directory_list = []
    counter = 0
    
    for line in infile:
        value_list = line.replace('\n', '').replace(' ','').split(',')

        if counter == 0:
            header = value_list
        elif value_list[4] == str(health):
            directory = {}
            directory[header[0]] = value_list[0]
            directory[header[1]] = int(value_list[1])
            directory[header[2]] = float(value_list[2])
            directory[header[3]] = int(value_list[3])
            directory[header[5]] = int(value_list[5])
            directory[header[6]] = int(value_list[6])
            directory[header[7]] = int(value_list[7])
            directory[header[8]] = int(value_list[8])
            directory_list.append(directory)

        counter += 1

    infile.close()
    return directory_list

#==========================================#
# Place your student_age_list function after this line
def student_age_list(filename: str, age: int) -> dict:
    """Return a list of students with the same age as the input age.

    Preconditions: filename = 'student-mat.csv'.
    
    
    >>> student_age_list('student-mat.csv', 18)
    [{'School': 'GP', 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6,'G1': 5, 'G2': 6, 'G3': 6}, {another element}, ... ]

    >>> student_age_list('student-mat.csv', 19)
    [{'School': 'BD', 'StudyTime': 2, 'Failures': 3, 'Health': 5, 'Absences': 2,'G1': 7, 'G2': 8, 'G3': 9}, {another element}, ... ]

    >>> student_age_list('student-mat.csv', 20)
    [{'School': 'BD', 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 0,'G1': 17, 'G2': 18, 'G3': 18}, {another element}, ... ]
    """
    import string
    infile = open(filename, 'r')
    directory_list = []
    i = 0

    for row in infile:
        value = row.replace('\n', '').replace(' ', '').split(',')

        if i == 0:
            header = value
        elif value[1] == str(age):
            directory = {}
            directory[header[0]] = value[0]
            directory[header[2]] = float(value[2])
            directory[header[3]] = int(value[3])
            directory[header[4]] = int(value[4])
            directory[header[5]] = int(value[5])
            directory[header[6]] = int(value[6])
            directory[header[7]] = int(value[7])
            directory[header[8]] = int(value[8])
            directory_list.append(directory)

        i += 1

    return directory_list

#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str, failure_number: int) -> list:
    """
    Return a dictionary of the number of failures from the data set.
    
    Preconditions: failure_number >= 0, failure_number <= 4, filename = 'student-mat.csv'.
    
    
    >>>student_failures_list("student-mat.csv", 3)
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3,'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {another element}, ... ]

    >>>student_failures_list("student-mat.csv", 2)
    [{'School': 'GP', 'Age': 16, 'StudyTime': 1.0, 'Health': 5, 'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}, {another element}, ... ]
    
    >>>student_failures_list("student-mat.csv", 5)
    []
    """

    infile = open(filename, 'r')
    
    header = infile.readline().strip().strip('\n').split(',')
    
    dictionary = []

    
    for row in infile:
        
        nth_line = row.strip().replace('\n','').split(',')
        
        nth_line_diction = dict(zip(header, nth_line))
        
        if int(nth_line_diction['Failures']) == failure_number:
            
            del nth_line_diction['Failures'] 
            
            nth_line_diction['School'] = nth_line_diction['School']
            nth_line_diction['Age'] = int(nth_line_diction['Age'])
            nth_line_diction['StudyTime'] = float(nth_line_diction['StudyTime'])
            nth_line_diction['Health'] = int(nth_line_diction['Health'])
            nth_line_diction['G1'] = int(nth_line_diction['G1'])
            nth_line_diction['G2'] = int(nth_line_diction['G2'])
            nth_line_diction['G3'] = int(nth_line_diction['G3'])
            
            dictionary += [(nth_line_diction)]
    
    return dictionary

#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, tup: tuple) -> dict:
    """Return the data from the specified file as a dictionary, which uses a tuple for the second argument where the first element as a data type filter, and the second element as a student/school filter.
    
    Preconditions: Second tuple element must have some input, filename = 'student-mat.csv'.
    
    
    >>>load_data('student-mat.csv', ('School','GP'))
    [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, ... ]
    
    >>>load_data('student-mat.csv', ('All',0))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3,'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, ... ]
    
    >>>load_data('student-mat.csv', ('Blue', 18 ))
    Invalid input
    []
    """
    data_filter, filter2 = tup
    file = open(file_name, 'r')
    data = []
    i = 0
    
    
    if data_filter == 'All':
        for line in file:
            value = line.replace('\n', '').replace(' ', '').split(',') 
            
            if i == 0:
                header = value
            if i > 0:
                directory = {}
                directory[header[0]] = value[0]
                directory[header[1]] = int(value[1])
                directory[header[2]] = float(value[2])
                directory[header[3]] = int(value[3])
                directory[header[4]] = int(value[4])
                directory[header[5]] = int(value[5])
                directory[header[6]] = int(value[6])
                directory[header[7]] = int(value[7])
                directory[header[8]] = int(value[8]) 
                data.append(directory)
                
            i += 1
            
        
    elif data_filter == 'School':
        add = student_school_list(file_name, filter2)
        data = add                
    
    elif data_filter == 'Age':
        add = student_age_list(file_name, filter2)
        data = add
    
    elif data_filter == 'Health':
        add = student_health_list(file_name, filter2)
        data = add
    
    elif data_filter == 'Failures':
        add = student_failures_list(file_name, filter2)
        data = add
    
    else:
        print("Invalid input")
    
    return data

#==========================================#
# Place your add_average function after this line
def add_average(student: list) -> list:
    """Return an updated list containing dictionaries for students with their calculated average grade added to their individual dictionary.
    
    Precondition: The list, student, must contain at least one dictionary, len(dictionary) >= 3, each dictionary must have the keys: 'G1', 'G2', 'G3'.
    
    
    >>>add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,'Failures': 1, 'Health': 3, 'Absences': 7,'G1': 5, 'G2': 6, 'G3': 6},{another element}, ... ])
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,'Failures': 1, 'Health': 3, 'Absences': 7,'G1': 5, 'G2': 6, 'G3': 6,'G_Avg': 5.67},{another element}, ... ]
    
    >>>add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2,'Failures': 0, 'Health': 3, 'Absences': 12,'G1': 5, 'G2': 5, 'G3': 5},{another element}, ... ])
    [{'School': 'MB', 'Age': 16, 'StudyTime': 2.0,'Failures': 0, 'Health': 3, 'Absences': 12,'G1': 5, 'G2': 5, 'G3': 5,'G_Avg': 5},{another element}, ... ]
    
    >>>add_average([{'School': 'CF', 'Age': 17, 'StudyTime': 1,'Failures': 2, 'Health': 5, 'Absences': 0,'G1': 7, 'G2': 6, 'G3': 0},{another element}, ... ])
    [{'School': 'CF', 'Age': 17, 'StudyTime': 1.0,'Failures': 2, 'Health': 5, 'Absences': 0,'G1': 7, 'G2': 6, 'G3': 0,'G_Avg': 4.33},{another element}, ... ]
    """
    for dictionary in student:
        G1 = dictionary['G1']
        G2 = dictionary['G2']
        G3 = dictionary['G3']
        
        G_Avg = round((G1 + G2 + G3) / 3, 2)
        dictionary['G_Avg'] = G_Avg
        
    return student

# Do NOT include a main script in your submission
