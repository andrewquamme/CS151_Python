## Program to calculate change.
## Takes input and calculates whole dollars and change

change = float(input("Enter amount of change: "))
change = int(change * 100)
dollars = change // 100
change %= 100
quarters = change // 25
change %= 25
dimes = change // 10
change %= 10
nickels = change // 5
change %= 5
pennies = change // 1

print("{0:<10s}{1:<5d}".format("Dollars:", dollars))
print("{0:<10s}{1:<5d}{2:<10s}{3:<5d}".format("Quarters:", quarters, "Dimes:",dimes))
print("{0:<10s}{1:<5d}{2:<10s}{3:<5d}".format("Nickels:", nickels, "Pennies:",pennies))
