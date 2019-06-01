'''
Andrew Quamme
CityU CIS-151
Chapter 7.2 exercise 10 (p 304)
Modify program in example 2 to only show PF students who pass
'''

import student

def main():
    listOfStudents = obtainListOfStudents()  # students and grades
    displayResults(listOfStudents)

def obtainListOfStudents():
    listOfStudents = []
##    ## This section used for quick loading of students
##    st = student.PFstudent("Andrew", 96,96)
##    listOfStudents.append(st)
##    st = student.PFstudent("Brianna", 96,96)
##    listOfStudents.append(st)
##    st = student.LGstudent("Casey", 96,96)
##    listOfStudents.append(st)
##    st = student.PFstudent("Demi", 45,45)
##    listOfStudents.append(st)
    carryOn = 'Y'
    while carryOn == 'Y':
        name = input("Enter student's name: ")
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter student's grade on final exam: "))
        category = input("Enter category (LG or PF): ")
        if category.upper() == "LG":
            st = student.LGstudent(name, midterm, final)
        else:
            st = student.PFstudent(name, midterm, final)
        listOfStudents.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfStudents

def displayResults(listOfStudents):
    print("\nNAME\tGRADE")
    listOfStudents.sort(key = lambda x: x.getName())  # Sort students by name.
    for pupil in listOfStudents:
        if isinstance(pupil, student.PFstudent) and pupil.calcSemGrade() == "Pass":
            # If object is of class PFstudent and has a passing grade
            print(pupil)
main()


