"""
********************************************************************************
* Project Name:  Leap Year Calculator
* Description:   This project calculates if the year is a leap year
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

print("Welcome to the Leap Year Calculator")
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} | Leap year.")
        else:
            print(f"{year} | Not leap year.")
else:
    print(f"{year} | Not leap year")