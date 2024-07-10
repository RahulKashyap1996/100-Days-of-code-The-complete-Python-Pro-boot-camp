print("Welcome to the tip calculator?")
bill=input("what was the total bill?\n")
tip=input("how much tip would you like to give\n")
people=input("how many people to split the bill\n")
perperson=round(((float(bill)*((float(tip)+100)/100)))/7,2)
print(f"each person should pay {perperson}")


