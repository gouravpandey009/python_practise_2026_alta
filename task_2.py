# ============================================================
# Task 2: LOAN QUALIFIER
# ============================================================
# Aim:
# Write a Python program to determine whether a bank customer
# qualifies for a loan.
#
# Conditions for getting the loan:
# 1. Annual income must be at least ₹50,000
# 2. Customer must have worked for at least 2 years
# ============================================================


# Taking annual income from the user
annual_income = float(input("Enter your annual income: ₹"))


# Taking number of years worked from the user
years_worked = int(input("Enter the number of years you have worked: "))


# Checking whether the customer satisfies both conditions
if annual_income >= 50000 and years_worked >= 2:

    # This block executes when both conditions are True
    print("Congratulations!")
    print("You qualify for the loan.")

else:

    # This block executes when at least one condition is False
    print("Sorry!")
    print("You do not qualify for the loan.")