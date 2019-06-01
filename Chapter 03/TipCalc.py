#Program to calculate tip for a server in restaurant

#Get amount of bill
bill=eval(input("Enter amount of bill: "))

#tip is 15% of bill with a $2 minimum
tip=bill*.15

if tip < 2:
    tip=2

print("Tip is ${0:.2f}".format(tip))

input("Press ENTER to continue")
