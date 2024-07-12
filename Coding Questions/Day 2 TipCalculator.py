"""

Write a Python program that acts as a tip calculator. The program should prompt the user for the total bill amount,
the percentage of tip they would like to give, and the number of people to split the bill among. The program
should then calculate and display how much each person should pay. Ensure that the amount each person should pay
is rounded to two decimal places

"""


print("Welcome to the tip calculator?")
bill=input("what was the total bill?\n")
tip=input("how much tip would you like to give\n")
people=input("how many people to split the bill\n")
perperson=round(((float(bill)*((float(tip)+100)/100)))/7,2)
print(f"each person should pay {perperson}")


