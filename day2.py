#Tip Calculator

print("Welcome to the Tip calculator!\n")
total_amount= input("What's the total amount to be paid? $ ")
percent_tip = input("What's the percent of the bill you want to tip? ")
num_people = int(input("How many people to split the bill between? "))
total_as_float=float(total_amount)
percent_value=int(percent_tip)/100
amount_per_person= round(((total_as_float+(percent_value*total_as_float))/num_people),2)
print(f"The amount each person has to pay is $ {amount_per_person}")
