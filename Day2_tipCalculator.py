print("Welcome to the tip calculator!")

bill = int(input("what was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 "))
total_people = int(input("How many people to split the bills? "))

cost = bill + (bill/100*tip)
cost_pp = cost/total_people

print(f"Each person should pay: £{round(cost_pp, 2)}")
