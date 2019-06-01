

import quizzes

def main():
    keep_going = 'Y'
    list_of_scores = []
    student_grade = quizzes.Quizzes()
    while keep_going == 'Y':
        # Create a blank list to store objects, prompt for scores,
        # and append scores to the list
        scores = []
        name = input("Enter student name: ")
        scores.append(float(input("Enter grade on quiz 1: ")))
        scores.append(float(input("Enter grade on quiz 2: ")))
        scores.append(float(input("Enter grade on quiz 3: ")))
        scores.append(float(input("Enter grade on quiz 4: ")))
        scores.append(float(input("Enter grade on quiz 5: ")))
        scores.append(float(input("Enter grade on quiz 6: ")))
        # Great an instance of Quizzes obect and pass scores
        student_grade = quizzes.Quizzes(name, scores)
        list_of_scores.append(student_grade)    # Add object to list
        keep_going = input("Continue? Y/N ").upper()
    # Output results from list
    print("Name\t\tQuiz Average")
    for student in list_of_scores:
            print(student)
   
main()
