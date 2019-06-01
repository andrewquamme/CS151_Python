# Project: CS151 Assignment Week 2
# Student Name: Andrew Quamme
# Purpose: In this assignment we will practice using lists and tuples

# Declare the menus     
listBreakfastMenu = ['eggs', 'hashbrowns', 'sausages', 'toast']     
listLunchMenu = ['grilled cheese', 'hotdogs', 'fries','hamburger']     
listDinnerMenu =  [ 'steak', 'salad', 'chicken', 'mashed potatos', 'rice']

# Print out one item from each of the lists above.
print(listBreakfastMenu[0], listLunchMenu[2], listDinnerMenu[4])

# Print out all items from all three lists. 
print(listBreakfastMenu)
print(listLunchMenu)
print(listDinnerMenu)

# Using the lists you have just created, try out at least 3 of the methods
# from Table 2.5 on page 58

# Reverse lunch menu
listLunchMenu.reverse()
print(listLunchMenu)

# Count number of dinner menu items
print("Number of dinner items: ", len(listDinnerMenu))

# Add pancakes to breakfast menu
listBreakfastMenu.append('pancakes')
print(listBreakfastMenu)

# Take a slice of one of the lists above
print(listBreakfastMenu[1:3])

# Demonstrate how split is used
listHours = "9am - 11am,11:30am - 3:00pm,4:30pm - 10:00pm".split(",")
print(listHours)

# Demonstrate how join is used
print("Restauraunt Hours: " + ", ".join(listHours))

#Create a tuple and demonstrate the use of at least two methods using this tuple
tupleContact = ("1234 Main St", "Anytown", "WA", "90210", "253-555-1212")
street, city, state, zip, phone = tupleContact
print("Located at " + street + ", " + city + ", " + state + "  " + zip)
print("Call us at " + tupleContact[4])


