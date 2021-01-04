import datetime

"""

1: calculate_age:
-ask the user for the birth year
-calculate (apox) the age of the user
note:
year = int(input())

2: calculate_tip:
-tip = 15%
-ask for the total
-calculate the tip 

"""


#imports

#global vars

#functions
def calculate_age():
    birth_year = int(input("Enter your birth year:"))

    current_year = datetime.date.today().year

    age_year = current_year - birth_year

    print ("Your age is: ", age_year)


def calculate_tip():
    meal=float(input("Enter price of meal:"))
    tip =float(input("How much do you want to tip, in decimal form? "))
    total = meal * tip

    print("You should give ", total, "for tip")    



#instructions