import math

# Menu with "Investment" and "Bond" definitions and selection of 
# "investment" or "bond" removing the whitespace and correcting 
# the input in lower case.
menu = input(
    "Investment - to calculate the amount of interest you'll earn on"
    " your investment.\n" 
    "Bond - to calculate the amount you'll have to pay on your home loan.\n"
    "Enter einther \"investmemt\" or \"bond\" from the menu above to "
    "proceed: ").lower().strip()

# User selects "investtment", the program will ask user to select
# "simple" or "compound" investment. User input is white space removed, 
# lower case input.
if menu == "investment":
    options = input("Select \"simple\' or \"compound\" "
    "interest: ").lower().strip()

    # User selects "simple" interest, the program will ask for user input
    # data for forumla calculation.
    if options == "simple":
        P = float(input("Enter the amount of money you deposit: "))
        r = float(input("Enter the interest rate (in precentage): "))
        r = r / 100
        t = int(input("Enter the number of years you plan on investinmg: "))
        A = P * (1 + r * t)

        # Program prints the required result of the calculation.
        print(f"Total amount of money after {t} years with simple interest is {A}")

    # User selects "compound" interest, the program wil ask for user input
    # data required for the formula calculation.
    elif options == "compound":
        P = float(input("Enter the amount of money you deposit: "))
        r = float(input("Enter the interest rate (in precentage): "))
        r = r / 100
        t = int(input("Enter the number of years you plan on investing: "))
        A = P * math.pow((1 + r), t)

        # Programm prints the required result of the calculation.
        print(f"Total amount of money after {t} years with compound interest is",
              end=" ")
        print(f"{A:2f}")
              

# User select "bond", the program will ask user for input data 
# required for the formula calculation.  
elif menu == "bond":
    P = float(input("Enter the value of the house: "))
    i = float(input("Enter your monthly interest rate (in precentage): "))
    i = i / 100
    n = int(input("Enter the number of months over which the bond will "
    "be repaid: "))
    repayment = (i * P) / (1 - (1 + i) **(-n))

    # Program prints the required result of the calculation.
    print(f"You have to repay the amount of money monthly is {repayment:2f}")

# If user enters invalid input, the program will print the message below.
else:
    print("Invalid input, please try again.")
