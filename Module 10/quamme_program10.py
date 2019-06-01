"""Andrew Quamme
CityUniversity of Seattle CIS151
Chapter 6.1 exercise 30
"""


def main():
    """Prompts a user for a state capital to remove from the list.
    If it's in the list, it gets deleted.
    If not, an error message is given. Repeats until Ctrl+C is pressed.
    """

    while True:
        try:
            capital_to_remove = input("Enter a state capital to "
                                      "delete (Ctrl+C to close): ")
            state_capitals.remove(capital_to_remove.title())
            print(capital_to_remove.title() + " deleted.")
        except KeyboardInterrupt:       # Used to end loop
            print("\nGoodbye!")
            exit()
        except:                         # If entered name is not in list
            print("Not a state capital.")

state_capitals = ["Olympia", "Salem", "Sacramento", "Columbus", "Lincoln",
                  "Denver", "Lansing", "Boston", "Tallahassee", "Austin",
                  "Oklahoma City", "Honolulu", "Juneau", "Salt Lake City",
                  "Santa Fe", "Bismarck", "Pierre", "Charleston",
                  "Richmond", "Trenton", "Saint Paul", "Springfield",
                  "Indianapolis", "Frankfort", "Nashville", "Atlanta",
                  "Montgomery", "Jackson", "Raleigh", "Columbia",
                  "Augusta", "Montpelier", "Concord", "Hartford",
                  "Providence", "Cheyenne", "Helena", "Topeka",
                  "Des Moines", "Harrisburg", "Annapolis", "Jefferson City",
                  "Phoenix", "Carson City", "Albany", "Madison", "Dover",
                  "Boise", "Little Rock", "Baton Rouge"]

main()
