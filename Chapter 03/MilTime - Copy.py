#Program to convert military time to civilian time

milTime = input("Enter a military time (0000 to 2359): ")

hours = int(milTime[0:2])
minutes = int(milTime[2:5])

#set am/pm to am
ampm = " am."

#12 is 12 pm
if hours == 12:
    ampm = " pm."

#00 is 12 am
elif hours == 00:
    hours = 12
    ampm = " am."

#hours greater than 12: subtract 12 and set am/pm to pm    
elif hours > 12:
    hours = hours - 12
    ampm = " pm."

#if/else to account for minutes of :00
if minutes == 0:
    minutes = "00"
else:
    minutes = str(minutes)

print("Civilian time is " + str(hours) + ":" + minutes + ampm)

input("Press ENTER to continue")
