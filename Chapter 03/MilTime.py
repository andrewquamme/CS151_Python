## Program to convert military time to civilian time

# Get military time as input
milTime = input("Enter a military time (0000 to 2359): ")

# Split entered time into hours and minutes
hours = int(milTime[:2])
minutes = int(milTime[2:])

# Set am/pm
if hours < 12:
    ampm = " am."
else:
    ampm = " pm."

# Hours can only be 1-12, but military time has 00
# as well as 13-23 that need to be changed

if hours == 00:         # 00 hours is 12
    hours = 12
elif hours > 12:        # subtract 12 from hours over 12
    hours = hours - 12  
else:                   # hours from 1-12 stay the same
    hours = hours

# Check for minutes of 0 and change to 00 so time doesn't print as 12:0
if minutes == 0:
    minutes = "00"

# Output the results
print("Civilian time is " + str(hours) + ":" + str(minutes) + ampm)

# Give user time to read results before program terminates
input("Press ENTER to continue")
