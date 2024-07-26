# tip calculator


print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15?")) / 100
people_number = int(input("How many people to split the bill?"))

cost = total_bill * (1+tip_percentage)
cost_per_person = "{:.2f}".format(round(cost / people_number,2))

print(f"Each payment is ${cost_per_person}.")