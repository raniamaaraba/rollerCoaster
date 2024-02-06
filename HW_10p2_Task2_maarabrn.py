# Activity Python 1: Task 3
# File: ACT_Python_HeaderTemplate_Team355_maarabrn.py 
# Date:    29 10 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# Convert a LabVIEW VI into python that calculates
# the speed of a roller coaster at a given point

import math

F1 = float(input('Enter the friction coefficient, f ='))
D1 = float(input('Enter the traveled distance, D ='))
V1 = float(input('Enter the car speed at position 1, v1 ='))
Y_1 = float(input('Enter the initial elevation, Y1 ='))
Y_2 = float(input('Enter the dinal elevation, Y2 ='))

P1 = V1**2

P2 = F1*D1
P4 = P2*9.81

P3 = Y_1 - Y_2
P5 = P3*9.81

P6 = P1 - P4
P7 = P5*2
P8 = P6 + P7
P9 = math.sqrt(P8)

print("The value of V2 is {0:.2f} m/s".format(P9))



