age = float(input("Enter your age: "))
rhr = float(input("Enter your resting heart rate: "))
thr = int(.7*(220-age)+(.3*rhr))
print("Training heart rate:",thr,"beats/min")
