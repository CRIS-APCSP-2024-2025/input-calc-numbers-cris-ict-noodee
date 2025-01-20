'''
Noodee, Grade 12 APCSP
Assignment: Celcius to Fahrenheit

This program will prompt the user to input Celcius temperature 
and output the equivalent Fahrenheit temperature.
'''
#
C = input('Enter a Celsius temperature: ')

#
F = (float(C) * (9 / 5)) + 32

# Convert Celsius to Farenheit using the formula F= (C*9 /5) + 32
print(str(C) + ' degrees Celsius is ' + str(F) + ' degrees Farenheit.')