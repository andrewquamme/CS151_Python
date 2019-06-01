#Take hours worked and hourly rate and calculate gross pay

#Get hours worked and hourly rate
hoursWorked = eval(input("Enter hours worked: "))
hourlyRate = eval(input("Enter hourly pay rate: "))

#Calculate gross pay with OT for over 40 hours
if hoursWorked <= 40:
    grossPay = (hoursWorked * hourlyRate)
else:
    grossPay = (40 * hourlyRate) + (1.5 * hourlyRate * (hoursWorked - 40))

print("Gross pay is ${0:.2f}".format(grossPay))

input("Press ENTER to continue")
