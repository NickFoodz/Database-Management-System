# ECOR 1042 Lab 4 - team submission

import check
import load_data

# Update "" with your the name of the active members of the team
__author__ = "Nick Fuda, Neo Ling, Patrick Spalton, Anirudh Kandula"

# Update with your student number (e.g., 100100100)
#In order of authors "101276459, 101283484, 101260915, 101257041" 

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T125"

#==========================================#

# Place test_return_list function here 
def test_return_list():
    #Complete the function with your test cases
    import check
    #test that student_school_list returns a list (3 different test cases required)
    from load_data import student_school_list
    first_school = isinstance(student_school_list("student-test.csv","GP"), list)
    second_school = isinstance(student_school_list("student-test.csv","MB"), list)
    third_school = isinstance(student_school_list("student-test.csv","CF"), list)
    
    check.equal(first_school, True)
    check.equal(second_school, True)
    check.equal(third_school, True)
    
    #test that student_age_list returns a list (3 different test cases required)
    from load_data import student_age_list
    first_age = isinstance(student_age_list("student-test.csv",18), list)
    second_age = isinstance(student_age_list("student-test.csv",16), list)
    third_age = isinstance(student_age_list("student-test.csv",17), list)
    
    check.equal(first_age, True)
    check.equal(second_age, True)
    check.equal(third_age, True)
    
    #test that student_health_list returns a list (3 different test cases required)
    from load_data import student_health_list
    
    health_check1 = isinstance(student_health_list("student-test.csv", 1), list)
    health_check2 = isinstance(student_health_list("student-test.csv", 4), list)
    health_check3 = isinstance(student_health_list("student-test.csv", 3), list)
    
    check.equal (health_check1, True)
    check.equal (health_check2, True)
    check.equal (health_check3, True)
    
    #test that student_failures_list returns a list (3 different test cases required)
    from load_data import student_failures_list
    failure_check1 = isinstance(student_failures_list("student-test.csv", 1), list)
    failure_check2 = isinstance(student_failures_list("student-test.csv", 2), list)
    failure_check3 = isinstance(student_failures_list("student-test.csv", 3), list)
    
    check.equal(failure_check1, True)
    check.equal(failure_check2, True)
    check.equal(failure_check3, True)
    
    #test that load_data returns a list (6 different test cases required)
    from load_data import load_data
    
    load_all = isinstance(load_data("student-test.csv",("All", 0)), list)
    load_school = isinstance(load_data("student-test.csv",("School", "GP")), list)
    load_age = isinstance(load_data("student-test.csv",("Age", 18)), list)
    load_failures = isinstance(load_data("student-test.csv",("Failures", 3)), list)
    load_health = isinstance(load_data("student-test.csv",("Health", 1)), list)
    load_None = isinstance(load_data("student-test.csv",("Blue", 2)), list)
    
    check.equal(load_all, True)
    check.equal(load_school, True)
    check.equal(load_age, True)
    check.equal(load_failures, True)
    check.equal(load_health, True)
    check.equal(load_None, True)
    
     #test that add_average returns a list (3 different test cases required)
    from load_data import add_average
    
    add_av1 = isinstance(add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7,'Failures': 1, 'Health': 3, 'Absences': 7,'G1': 5, 'G2': 6, 'G3': 6}]), list)
    add_av2 = isinstance(add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2,'Failures': 0, 'Health': 3, 'Absences': 12,'G1': 5, 'G2': 5, 'G3': 5}]), list)
    add_av3 = isinstance(add_average([{'School': 'CF', 'Age': 17, 'StudyTime': 1,'Failures': 2, 'Health': 5, 'Absences': 0,'G1': 7, 'G2': 6, 'G3': 0}]), list)
    
    check.equal(add_av1, True)
    check.equal(add_av2, True)
    check.equal(add_av3, True)
    
    
    #Return summary of Checks
    return check.summary()

# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list with the correct lenght (3 different test cases required)
    from load_data import student_school_list
    import check
    
    first_school_list = len(student_school_list("student-test.csv", 'GP'))
    second_school_list = len(student_school_list("student-test.csv", 'MB'))
    third_school_list = len(student_school_list("student-test.csv", 'MS'))
    
    check.equal(first_school_list, 3)
    check.equal(second_school_list, 2)
    check.equal(third_school_list, 4)
    
    #test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    from load_data import student_age_list
    
    first_age_list = len(student_age_list("student-test.csv", 18))
    second_age_list = len(student_age_list("student-test.csv", 15))
    third_age_list = len(student_age_list("student-test.csv", 16))
    
    check.equal(first_age_list, 4)
    check.equal(second_age_list, 3)
    check.equal(third_age_list, 2)
    
    #test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    from load_data import student_health_list
    
    first_health_list = len(student_health_list("student-test.csv", 3))
    second_health_list = len(student_health_list("student-test.csv", 5))
    third_health_list = len(student_health_list("student-test.csv", 1))

    check.equal(first_health_list, 8)
    check.equal(second_health_list, 3)
    check.equal(third_health_list, 1)
    
    #test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    from load_data import student_failures_list
    
    first_failures_list = len(student_failures_list("student-test.csv", 0))
    second_failures_list = len(student_failures_list("student-test.csv", 2))
    third_failures_list = len(student_failures_list("student-test.csv", 3))
    
    check.equal(first_failures_list, 11)
    check.equal(second_failures_list, 2)
    check.equal(third_failures_list, 1)
    
    
    #test that load_data returns a list  with the correct lenght (6 different test cases required)
    from load_data import load_data
    
    load_all_list = len(load_data("student-test.csv", ("All", 15)))
    load_school_list = len(load_data("student-test.csv", ("School", "MB")))
    load_age_list = len(load_data("student-test.csv", ("Age", 17)))
    load_failures_list = len(load_data("student-test.csv", ("Failures", 0)))
    load_health_list = len(load_data("student-test.csv", ("Health", 5)))
    load_second_health_list = len(load_data("student-test.csv", ("Health", 4)))
    
    check.equal(load_all_list, 15)
    check.equal(load_school_list, 2)
    check.equal(load_age_list, 6)
    check.equal(load_failures_list, 11)
    check.equal(load_health_list, 3)
    check.equal(load_second_health_list, 3)
    
    #test that add_average returns a list   with the correct lenght (3 different test cases required)
    from load_data import add_average
    
    first_add_average_list = len(add_average([]))
    second_add_average_list = len(add_average([{'School': 'CF', 'Age': 17, 'StudyTime': 1.0,'Failures': 2, 'Health': 5, 'Absences': 0,'G1': 7, 'G2': 6, 'G3': 0,'G_Avg': 4.33}]))
    third_add_average_list = len(add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2.0,'Failures': 0, 'Health': 3, 'Absences': 12,'G1': 5, 'G2': 5, 'G3': 5,'G_Avg': 5}, {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,'Failures': 1, 'Health': 3, 'Absences': 7,'G1': 5, 'G2': 6, 'G3': 6,'G_Avg': 5.67}]))
    
    check.equal(first_add_average_list, 0)
    check.equal(second_add_average_list, 1)
    check.equal(third_add_average_list, 2)
    
    
    return check.summary()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    """Test to confirm that all functions return the correct data."""
    import check
    import load_data
    #Complete the function with your test cases
    
    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    from load_data import student_school_list
    school1 = student_school_list("student-test.csv", "GP")
    school2 = student_school_list("student-test.csv", "MB")
    school3 = student_school_list("student-test.csv", "CF")
    
    check.equal(school1[0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(school2[0], {'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5})
    check.equal(school3[0], {'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})

    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    from load_data import student_age_list
    
    age1 = student_age_list("student-test.csv", 15)
    age2 = student_age_list("student-test.csv", 16)
    age3 = student_age_list("student-test.csv", 17)
    
    check.equal(age1[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    check.equal(age2[0], {'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5})
    check.equal(age3[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6})
    
    #check.equal(age1[0],)
    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    from load_data import student_health_list
    
    health1 = student_health_list("student-test.csv", 3)
    health2 = student_health_list("student-test.csv", 4)
    health3 = student_health_list("student-test.csv", 5)
    
    check.equal(health1[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(health2[0], {'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9})
    check.equal(health3[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})    
    
    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    from load_data import student_failures_list
    
    fails1 = student_failures_list("student-test.csv", 0)
    fails2 = student_failures_list("student-test.csv", 1)
    fails3 = student_failures_list("student-test.csv", 2)
    
    check.equal(fails1[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': '6', 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(fails2[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': '4', 'G1': 10, 'G2': 12, 'G3': 12})
    check.equal(fails3[0], {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': '6', 'G1': 5, 'G2': 9, 'G3': 7})
    
    #test that load_data returns a correct dictionary inside the list (6 different test cases required)
    from load_data import load_data
    
    data1 = load_data("student-test.csv", ("School", "GP"))
    data2 = load_data("student-test.csv", ("Age", 18))
    data3 = load_data("student-test.csv", ("Health", 3))
    data4 = load_data("student-test.csv", ("School", "MS"))
    data5 = load_data("student-test.csv", ("Health", 5))
    data6 = load_data("student-test.csv", ("Failures", 0))   
    
    check.equal(data1[0], {'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(data2[0], {'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(data3[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    check.equal(data4[0], {'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'G1': 11, 'G2': 10, 'G3': 10})
    check.equal(data5[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})
    check.equal(data6[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': '6', 'G1': 5, 'G2': 6, 'G3': 6})
    
     #test that add_average returns a correct dictionary inside the list  (3 different test cases required)
    from load_data import add_average
    average_test_call = load_data("student-test.csv", ('All', 0))   
    add_average(average_test_call)
    
    check.equal(average_test_call[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0,'Failures': 0, 'Health': 3, 'Absences': 6,'G1': 5, 'G2': 6, 'G3': 6,'G_Avg': 5.67})
    check.equal(average_test_call[1], {'School': 'GP', 'Age': 17, 'StudyTime': 2.0,'Failures': 0, 'Health': 3, 'Absences': 4,'G1': 5, 'G2': 5, 'G3': 6,'G_Avg': 5.33})
    check.equal(average_test_call[2], {'School': 'GP', 'Age': 15, 'StudyTime': 2.0,'Failures': 3, 'Health': 3, 'Absences': 10,'G1': 7, 'G2': 8, 'G3': 10,'G_Avg': 8.33})    
    return check.summary()


#Place test_add_average function here
def test_add_average():
    #Complete the function with your test cases
    from load_data import student_school_list
    from load_data import student_health_list
    from load_data import student_age_list
    from load_data import student_failures_list
    from load_data import add_average
    import check

    #test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    list_length_1 = len(add_average(student_school_list('student-test.csv', 'GP')))
    list_length_2 = len(add_average(student_health_list('student-test.csv', 4)))
    list_length_3 = len(add_average(student_age_list('student-test.csv', 18)))
    list_length_4 = len(add_average(student_failures_list('student-test.csv', 2)))
    list_length_5 = len(add_average(student_school_list('student-test.csv', 'GP') + student_health_list('student-test.csv', 4) + student_age_list('student-test.csv', 18) + student_failures_list('student-test.csv', 2)))

    check.equal(list_length_1, 3)
    check.equal(list_length_2, 3)
    check.equal(list_length_3, 4)
    check.equal(list_length_4, 2)
    check.equal(list_length_5, 12)

    #test that the function returns an empty list when it is called with an empty list
    list_length_6 = len(add_average(student_school_list('student-test.csv', '')))
    check.equal(list_length_6, 0)

    #test that the function incrememnts the number of keys of the dictionary inside the list by one (5 different test cases required)
    dictionary_standard_length = 8
    dictionary_1 = add_average(student_school_list('student-test.csv', 'MB'))
    dictionary_1_length = len(dictionary_1[0])
    dictionary_2 = add_average(student_health_list('student-test.csv', 5))
    dictionary_2_length = len(dictionary_2[0])
    dictionary_3 = add_average(student_age_list('student-test.csv', 16))
    dictionary_3_length = len(dictionary_3[0])
    dictionary_4 = add_average(student_failures_list('student-test.csv', 0))
    dictionary_4_length = len(dictionary_4[0])
    dictionary_5 = add_average(student_school_list('student-test.csv', 'MB') + student_health_list('student-test.csv', 5) + student_age_list('student-test.csv', 16) + student_failures_list('student-test.csv', 0))
    dictionary_5_length = len(dictionary_5[0])

    check.equal(dictionary_1_length, dictionary_standard_length + 1)
    check.equal(dictionary_2_length, dictionary_standard_length + 1)
    check.equal(dictionary_3_length, dictionary_standard_length + 1)
    check.equal(dictionary_4_length, dictionary_standard_length + 1)
    check.equal(dictionary_5_length, dictionary_standard_length + 1)

    #test that the G_Avg value is properly calculated (5 different test cases required)
    value_1 = add_average(student_school_list('student-test.csv', 'CF'))
    value_1_alt = value_1[0]
    avg_value_1 = value_1_alt['G_Avg']
    value_2 = add_average(student_health_list('student-test.csv', 1))
    value_2_alt = value_2[0]
    avg_value_2 = value_2_alt['G_Avg']
    value_3 = add_average(student_age_list('student-test.csv', 15))
    value_3_alt = value_3[0]
    avg_value_3 = value_3_alt['G_Avg']
    value_4 = add_average(student_failures_list('student-test.csv', 1))
    value_4_alt = value_4[0]
    avg_value_4 = value_4_alt['G_Avg']
    value_5 = add_average(student_school_list('student-test.csv', 'CF') + student_health_list('student-test.csv', 1) + student_age_list('student-test.csv', 15) + student_failures_list('student-test.csv', 1))
    value_5_alt = value_5[0]
    avg_value_5 = value_5_alt['G_Avg']

    alt_avg_value_1 = round((value_1_alt['G1'] + value_1_alt['G2'] + value_1_alt['G3']) / 3, 2)
    alt_avg_value_2 = round((value_2_alt['G1'] + value_2_alt['G2'] + value_2_alt['G3']) / 3, 2)
    alt_avg_value_3 = round((value_3_alt['G1'] + value_3_alt['G2'] + value_3_alt['G3']) / 3, 2)
    alt_avg_value_4 = round((value_4_alt['G1'] + value_4_alt['G2'] + value_4_alt['G3']) / 3, 2)
    alt_avg_value_5 = round((value_5_alt['G1'] + value_5_alt['G2'] + value_5_alt['G3']) / 3, 2)

    check.equal(avg_value_1, alt_avg_value_1)
    check.equal(avg_value_2, alt_avg_value_2)
    check.equal(avg_value_3, alt_avg_value_3)
    check.equal(avg_value_4, alt_avg_value_4)
    check.equal(avg_value_5, alt_avg_value_5)

    check.summary()


# Do NOT include a main script in your submission
