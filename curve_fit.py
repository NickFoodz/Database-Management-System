# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Anirudh Kandula"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101257041"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-125"

#==========================================#
# Place your curve_fit function after this line

def curve_fit(dict_list: list, compare_attribute: str, poly_degree:int) -> str:
    """Return a string representation of the equation of the best fit for the average of the 'G_Avg' key, from a list of dictionaries, dict_list, from an attribute which is used to compare the dictionaries, compare_attribute, and from the degree of the polynomial that will be fitted, poly_degree.
    
    Preconditions: dict_list contains dictionaries which contain the 'G_Avg' key, compare_attribute must be a key in each of the dictionaries in dict_list, compare_attribute's key must have a numerical value assigned to it, poly_degree >= 1 and poly_degree <= 5.
    
    
    """
    # Importing and initializing
    import numpy as np
    
    key_values = []
    
    num_values = []
    
    #obtaining the values corresponding to the x and y coordinates
    for i in range(len(dict_list)):
        
        key_values.append(dict_list[i]['G_Avg'])
        
        num_values.append(dict_list[i][compare_attribute])
    
    #getting an array of coefficients    
    coeffs = np.polyfit(num_values, key_values, poly_degree)
    
    #setting up the equation and making sure the signs are also correct
    
    n = len(coeffs)-1
    
    function = ''
    
    first = 0
    
    for coef in coeffs:
        
        sign = " + "
        
        if coef <= 0:
            
            sign = "-"
            
        if n == 1:
            
            if first == 0:
                
                if sign == "-":       
                    
                    function += (sign + "{0:0.2}x".format(coef))
                else:
                    
                    function += ("{0:0.2}x".format(coef))
            else:
                
                function += (sign + "{0:0.2}x".format(coef))
                
        elif n == 0:
            
            if first == 0:
                
                if sign == "-":
                    
                    function += (sign + "{0:0.2}".format(coef))  
                    
                else:
                    
                    function += ("{0:0.2}".format(coef)) 
            else: 
                
                function += (sign + "{0:0.2}".format(coef)) 
        
        else:
            
            if first == 0:
                
                if sign == "-":
                    
                    function += (sign + "{0:0.2}x^".format(coef) + str(n))
                else:
                    
                    function += ("{0:0.2}x^".format(coef) + str(n))
            else:
                
                function += (sign + "{0:0.2}x^".format(coef) + str(n))
        n -= 1
        
        first = 1
        
    return ("y = " + function)


    

# Do NOT include a main script in your submission

#Delete this before submitting, here so it is faster to test the function
#[{'School': 'MB', 'Age': 16, 'StudyTime': 2.0,'Failures': 0, 'Health': 3, 'Absences': 12,'G1': 5, 'G2': 5, 'G3': 5,'G_Avg': 5},{'School': 'CF', 'Age': 17, 'StudyTime': 1.0,'Failures': 2, 'Health': 5, 'Absences': 0,'G1': 7, 'G2': 6, 'G3': 0,'G_Avg': 4.33}, {'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7, 'G_Avg': 7.0}, {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12, 'G_Avg': 11.33}]