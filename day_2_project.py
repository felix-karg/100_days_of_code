# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_per_person = bill / people
tip_factor = float("1." + str(tip))
total_bill = bill_per_person * tip_factor

print(f"Each person should pay: ${total_bill: .2f}")
