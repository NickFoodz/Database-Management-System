# ECOR 1042 Lab 6 - Team Submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nick Fuda"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101276459"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-125"

#==========================================#
from string import *
from sort import*
from load_data import *
from histogram import *
from curve_fit import *
import numpy
import matplotlib

run = True
while run:
   command_from_file = []
   keys = ["Command", "Argument 1", 'Argument 2', 'Argument 3']
   filename = input("Please enter the name of the file where your commands are stored: ")
   file = open(filename, "r")
   
   for line in file:
      i = 0
      directory = {}
      line_value = line.split()
      for word in line_value:
         word = word.strip(';')   
         if word != '':
               directory[keys[i]] = word
               i +=1
      command_from_file.append(directory)
   
   file.close()
   
   for entry in command_from_file:
      command = entry.get("Command")
      argument_1 = entry.get('Argument 1')
      argument_2 = entry.get('Argument 2')
      argument_3 = entry.get('Argument 3')
   
      if command == 'L':      
         data = load_data(argument_1, (argument_2, argument_3))
         add_average(data)
         print('Data loaded')
      
      elif command == 'S':
         sort(data, argument_2, argument_1)
         print('Data sorted')
         if argument_3 == 'Y':
            print(data)
         
      elif command == 'C':
         equation = curve_fit(data, argument_1, int(argument_2))
         print(equation)
      
      elif command == 'H':
         histogram(data, argument_1)



   input('Press enter to continue... ')
   run = False



