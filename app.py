from math import *
import matplotlib.pyplot as plt
from time import sleep

y_axis = []
x_axis = []

try:
    print('Welcome to the Frequency response graph plotter.')
    print('You can calculate and plot the value of the value of magnitude and phase')
    sleep(2)
    while True:
        choice = input('Would you like to plot for Magnitude (Press A) or Plot for Phase (Press B): ').lower()
        print(choice)
        if choice == 'a' or choice == 'b':
            break
        else:
            print('Please enter a Valid Choice: A or B')
            continue
        break
    E = float(input('Please enter the value of E: '))
    a = float(input('Please enter the (minimum value) for the range of U: '))*10
    b = float(input('Please enter the (maximum value) for the range of U: '))*10

    def calculate_m(E, U):
        x = pow((1 - U*U),2) + pow(2*E*U, 2)
        m = 1/sqrt(x)
        return m

    def calculate_phi(E, U):
        x = 2*E*U
        y = 1 - (U**2)
        if y == 0: x = 0
        phi = -tanh(x)
        return phi


    for i in range(0, 22, 2):
        u = float(i/10)
        x_axis.append(u)
        if choice == 'a':
            m = calculate_m(E, u)
            y_axis.append(m)
        else:
            phi = calculate_phi(E, u)
            y_axis.append(phi)
        
        
    print(x_axis)
    print(y_axis)                  

    plt.plot(x_axis, y_axis)
    plt.ylabel('Magnitude/Phase of resonant freuency: y-axis')
    plt.xlabel('Normalised driving signal frequency: x-axis')
    plt.show()

except ValueError:
    print('There is an error in your inputs, Please run this program again!')