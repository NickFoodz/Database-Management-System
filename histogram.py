# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Patrick Spalton"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101260915"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-125"

#==========================================#
# Place your histogram function after this line


def histogram(dict_list: list, dict_attribute: str) -> None:
    """Return and plot a histogram, which will be based on the number of dictionaries from a list, dict_list, whose specified key's assigned value matches the assigned values of that same key, dict_attribute, in other dictionaries from the list.
    
    Preconditions: dict_attribute must be a key in each of the dictionaries in dict_list.
    
    """

    #Importing library and initializing some variables
    import matplotlib.pyplot as plt
    attribute_values = []
    num_attribute_values = {}

    #Obtaining the assigned value of the specified key from each dictionary
    for dictionary in dict_list:
        attribute_values.append(dictionary[dict_attribute])

    #Ordering values in ascending or alphabetical order
    for j in range(1, len(attribute_values)):
        compare = attribute_values[j]
        i = j
        while i > 0 and compare < attribute_values[i - 1]:
            attribute_values[i] = attribute_values[i - 1]
            i -= 1
        attribute_values[i] = compare

    #Finding the amounts of each particular value
    for value in attribute_values:
        num_attribute_values[value] = num_attribute_values.get(value, 0) + 1

    #Plotting histogram
    fig1 = plt.figure()
    plt.title('Student ' + dict_attribute)
    plt.xlabel(dict_attribute)
    plt.ylabel('Number of Students')
    plt.bar(list(num_attribute_values), list(num_attribute_values.values()), color='purple')
    plt.show()

    return None

# Do NOT include a main script in your submission
