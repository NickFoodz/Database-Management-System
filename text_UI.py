# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nicholas Fuda"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101276459"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-125"

#==========================================#
# Place your script for your text_UI after this line
from load_data import *
from sort import *
from histogram import *
from curve_fit import *

data = 0
run = True
while run:

    list_of_acceptable_commands = ['L', 'S', 'C', 'H', 'E']
    print("The available commands are: \n", "L)oad Data \n", 'S)ort Data \n', 'C)urve Fit \n', 'H)istogram \n', 'E)xit \n')
    command = input('Please type your command: ')
    command = command.upper()

    if command not in list_of_acceptable_commands: #sends back to start with error notice
        print("Invalid entry. Please enter the first letter of the command you wish to use")

    elif command == 'L': #Load data option
        filename = input('Please enter the name of the file: ')
        load_acceptable_attributes = ['School', 'Age', 'Failures', 'Health', 'All']
        filter_attribute = input('Please enter the attribute to use as a filter: ')

        while filter_attribute not in load_acceptable_attributes: #if entry is invalid
            filter_attribute = input('Invalid attribute, please enter the attribute to use as a filter: ')

        if filter_attribute == 'All':
            data = load_data(filename, ('All', 0))
            add_average(data) #Creates a G_Avg key in the file
        else: #if filter_attribute uses a value to filter
            attribute_value = input('Please enter the value of the attribute: ')
            data = load_data(filename, (filter_attribute, attribute_value)) #binds list to data variable
            add_average(data) #Creates a G_Avg key in the file

        print(data, '\n') #displays data

    elif command == 'S': #sort data option
        sort_acceptable_attributes = ['Age', 'StudyTime', 'Failures', 'G_Avg'] #attributes to sort by
        sort_acceptable_order = ['A', 'D'] #ascending or descending order

        if data == 0: #if data is not loaded
            print("Error: No data loaded. Please load a file first\n")

        else: #if data is loaded
            sort_attribute = input('Please enter the attribute you want to use for sorting: \n \'Age\' \'StudyTime\' \'Failures\' \'G_Avg\' \n')

            while sort_attribute not in sort_acceptable_attributes or (sort_attribute == filter_attribute):
                sort_attribute = input("Invalid entry. Please enter the attribute you want to use for sorting: \n \'Age\' \'StudyTime\' \'Failures\' \'G_Avg\' \n")

            sort_order = input("Ascending (A) or Descending (D) order: ")

            while sort_order.upper() not in sort_acceptable_order:
                sort_order = input("Invalid Entry. Ascending (A) or Descending (D) order:")

            sort(data, sort_order.upper(), sort_attribute)

            display_sort_inputs = ['Y', 'N']
            display_sort = input('Data sorted. Do you want to display the data? (Y/N):')

            while display_sort.upper() not in display_sort_inputs:
                display_sort = input('Invalid input.\nData sorted. Do you want to display the data? (Y/N):')

            if display_sort.upper() == 'Y':
                print('\n', data, '\n')

            elif display_sort.upper() == 'N':
                continue

    elif command == "C": #User selects Curve Fit
        if data == 0:
            print('Error: No data loaded. Please load a file first\n')
        else:
            curve_attribute_inputs = ['Age', 'StudyTime', 'Failures', 'Health', 'Absences', 'G1', 'G2', 'G3', 'G_Avg']
            curve_attribute = input("Please enter the attribute you want to use for plotting: ")

            while curve_attribute not in curve_attribute_inputs or (curve_attribute == filter_attribute):
                curve_attribute = input("Invalid Entry. Please enter the attribute you want to use for plotting: ")

            test_type_int = True
            while test_type_int: #To test if order input is valid
                try: #Does not give error in terminal
                    curve_order = input("Please enter the order of the polynomial to be fitted: ")
                    curve_order = int(curve_order)
                    test_type_int = False
                except ValueError:
                    print("Invalid entry. Please try again using an integer value.")

            print(curve_fit(data, curve_attribute, curve_order), "\n")

    elif command == 'H':
        if data == 0:
            print('Error: No data loaded. Please load a file first \n')

        else:
            hist_attributes_list = ['School', 'Age', 'Health', 'Failures', 'G1', 'G2', 'G3', 'G_Avg']
            hist_attribute = input('Please enter the attribute you want to use for plotting: ')

            while hist_attribute not in hist_attributes_list or (hist_attribute == filter_attribute):
                hist_attribute = input('Invalid entry. Please enter the attribute you want to use for plotting: ')

            histogram(data, hist_attribute)

    elif command == 'E':
        run = False
