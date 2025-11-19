# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Nick Fuda, Neo Ling, Patrick Spalton, Anirudh Kandula"

# Update with your student number (e.g., 100100100)
__student_number__ = "101276459, 101283484, 101260915, 101257041"

# Update "" with your team (e.g. T102)
__team__ = "T-125"

#==========================================#
# Place your sort_students_age_bubble function after this line

def sort_students_age_bubble(lst: list, order: str) -> None:
    """Returns a list of student dictionaries sorted by age in either ascending or descending order.
    If there is no age, returns a printed message and returns the original list.
    
    Preconditions: List must contain dictionaries, order must be "A" or "D", all entries must contain Age or the list will not sort.
    
    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
     [{"Age":19,"School":"MS"},{"Age":10,"School":"GP"}], "D")
   
    >>>sort_students_age_bubble([{"School":"GP"},{"School":"MS"}], "D")
    "Age" key is not present
    ["School":"GP"},{"School":"MS"}]
    
    >>>sort_students_age_bubble([{"Age":15,"School":"MS"},{"Age":16,"School":"GP"}], "D")
    [{"Age":16,"School":"GP"},{"Age":15,"School":"MS"}]
    """
    list_length = len(lst)

    for i in range(list_length):
        if "Age" not in lst[i]:
            print('"Age" is not in list')
            return lst

    for i in range(list_length):
        if order == "D":
            swap = True
            while swap:
                swap = False #will cancel the loop if the if condition isn't met in the next loop (if in proper order)
                for i in range(len(lst) - 1):
                    first = lst[i].get("Age", '"Age" key is not present')
                    if first < lst[i + 1].get("Age"): #if the number at i is greater than the next number
                        aux = lst[i] #saves the number at i
                        lst[i] = lst[i + 1] #replaces i with the smaller number
                        lst[i + 1] = aux #replaces the smaller number with i
                        swap = True #continues the original loop

        elif order == "A":
            swap = True
            while swap:
                swap = False #will cancel the loop if the if condition isnt met in the next loop
                for i in range(len(lst) - 1):
                    first = lst[i].get("Age", '"Age" key is not present')
                    if first > lst[i + 1].get("Age"): #if the number at i is greater than the next number
                        aux = lst[i] #saves the number at i
                        lst[i] = lst[i + 1] #replaces i with the smaller number
                        lst[i + 1] = aux #replaces the smaller number with i
                        swap = True #continues the original loop

    return lst

#==========================================#
# Place your sort_students_time_selection function after this line

def sort_students_time_selection(input_list: list, order: str) -> None:
    """Returns a list of dictionaries sorted by study time in either ascending 
    or descending order. Prints a message and returns the original list if 
    there is no study time.
    
    Preconditions: List must contain dictionaries, string must be either "A" or
    "D".
    
    >>> sort_students_time_selection([{"StudyTime": 10.2, "School": "GP"},
    {"StudyTime": 19.1, "School": "MS"}], "D")
    
    [{"StudyTime": 19.1, "School":"MS"}, {"StudyTime":10.2, "School":"GP"}]
    
    >>> sort_students_time_selection([{"School": "GP"}, {"School": "MS"}], "D")
    
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    """
    len_list = len(input_list)

    for i in range(len_list):
        if "StudyTime" not in input_list[i]:
            print('"StudyTime" key is not present.')
        
        else:
            for j in range(i+1, len_list):
                if input_list[i]["StudyTime"] > input_list[j]["StudyTime"] and order == "A":
                    input_list[i], input_list[j] = input_list[j], input_list[i]
                    
                elif input_list[i]["StudyTime"] < input_list[j]["StudyTime"] and order == "D":
                    input_list[i], input_list[j] = input_list[j], input_list[i]

    return input_list

#==========================================#
# Place your sort_students_g_avg_insertion function after this line

def sort_students_g_avg_insertion(list_dict_list: list, order: str) -> list:
    """Return a list of students' dictionaries in descending or ascending order, order, from an inputted list of student dictionaries, dict_list.
    
    Preconditions: order = 'A' or order = 'D', dict_list must contain dictionaries.
    
    
    >>>sort_students_g_avg_insertion([{'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 9.1, 'School': 'MS'}], 'D')
    [{'G_Avg': 9.1,'School': 'MS'}, {'G_Avg': 7.2,'School': 'GP'}]
    
    >>>sort_students_g_avg_insertion([{'School': 'GP'}, {'School': 'MS'}], 'D')
    'G_Avg' key is not present
    [{'School': 'GP'}, {'School': 'MS'}]
    """
    
    #Checking if the 'G_Avg' key is or isn't present
    persistant_present_check = 0
    for dict_list in range(len(list_dict_list)):
        present_check = list_dict_list[dict_list].get('G_Avg', False)
        
        if present_check == False:
            persistant_present_check += 1
            if dict_list == 0:
                print("The 'G_Avg' key is not present in the " + str(dict_list + 1) + "st student's list")
            elif dict_list == 1:
                print("The 'G_Avg' key is not present in the " + str(dict_list + 1) + "nd student's list")
            elif dict_list == 2:
                print("The 'G_Avg' key is not present in the " + str(dict_list + 1) + "rd student's list")
            else:
                print("The 'G_Avg' key is not present in the " + str(dict_list + 1) + "th student's list")
        
        present_check = True
    
    if persistant_present_check != 0:
        return list_dict_list
    

    #Main code
    #For descending order
    if order == 'D':
        for j in range(1, len(list_dict_list)):
            compare = list_dict_list[j]
            i = j

            while i > 0 and compare.get('G_Avg') > list_dict_list[i - 1].get('G_Avg'):
                list_dict_list[i] = list_dict_list[i - 1]
                i -= 1

            list_dict_list[i] = compare
            
    #For ascending order
    elif order == 'A':
        for j in range(1, len(list_dict_list)):
            compare = list_dict_list[j]
            i = j

            while i > 0 and compare.get('G_Avg') < list_dict_list[i - 1].get('G_Avg'):
                list_dict_list[i] = list_dict_list[i - 1]
                i -= 1

            list_dict_list[i] = compare

    return list_dict_list

#==========================================#
# Place your sort_students_failures_bubble function after this line

def sort_students_failures_bubble(dict_list: list, order: str) -> None:
    """Returns an ordered list of dictionaries from either an ascending or descending order. Returns a statement stating the key is not in the dictionary.
    
    Preconditions: The String must be the letters A or D, in caps.
    
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
    
    >>>sort_students_failures_bubble([{"School":"GP"},{"School":"MS"}], "D")
    "Failures" key is not present.
    [{'School': 'GP'}, {'School': 'MS'}]
    
    >>>sort_students_failures_bubble([{"Failures":10,"School":"GP"},{"Failures":21,"School":"MS"},{"Failures":19,"School":"MS"}], "D")
    [{'Failures': 21, 'School': 'MS'}, {'Failures': 19, 'School': 'MS'}, {'Failures': 10, 'School': 'GP'}]
    
    """
    list_length = len(dict_list)
    
    for i in range(list_length):
        
        if "Failures" not in dict_list[i]:
            
            print('"Failures" key is not present.')
            
            return dict_list
        
        else:
            for x in range(list_length - 1):
                
                if dict_list[x]["Failures"] > dict_list[x + 1]["Failures"] and order == "A":
                    
                    dict_list[x], dict_list[x + 1] = dict_list[x + 1], dict_list[x]
                    
                if dict_list[x]["Failures"] < dict_list[x + 1]["Failures"] and order =="D":
                    
                    dict_list[x], dict_list[x + 1] = dict_list[x + 1], dict_list[x]
                    
    return dict_list

#==========================================#
# Place your sort function after this line

def sort(dict_list: list, order: str, sort_attribute: str) -> str:
    """Return a list of students' dictionaries in descending or ascending order, order, based on an inputted sorting attribute, sort_attribute, from an inputted list of student dictionaries, dict_list.
    
    Preconditions: dict_list must contain dictionaries, order = 'A' or order = 'D', sort_attribute = 'Age' or sort_attribute = 'StudyTime' or sort_attribute = 'Failures' or sort_attribute = 'G_Avg'.
    
    
    >>>sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>>sort([{"StudyTime": 10.2, "School": "GP"}, {"StudyTime": 19.1, "School": "MS"}], "D", "StudyTime")
    [{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 10.2, 'School': 'GP'}]
    
    >>>sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by School as it is not a valid input
    [{"School":"GP"}, {"School":"MS"}]
    """
    if sort_attribute == "Age":
        sort_students_age_bubble(dict_list, order)
    
    elif sort_attribute == "StudyTime":
        sort_students_time_selection(dict_list, order)
    
    elif sort_attribute == "G_Avg":
        sort_students_g_avg_insertion(dict_list, order)
    
    elif sort_attribute == "Failures":
        sort_students_failures_bubble(dict_list, order)
    
    else:
        print("Cannot be sorted by", sort_attribute, "as it is not a valid input")
    
    return dict_list
    

# Do NOT include a main script in your submission
