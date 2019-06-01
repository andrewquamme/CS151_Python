## Andrew Quamme
## Assignment 8
## Exercise #32 (Quiz Grades) on Page 293 of the textbook
## Class needed for quiz_grades.py

class Quizzes:
    """Class for name and quiz scores and calculating the average score"""

    def __init__(self, name = "", quiz_scores = []):
        # Initialize instance of Quizzes and set quiz scores
        self._name = name
        self._quiz_scores = quiz_scores
        
    def calc_average(self):
        # Drop the lowest quiz score and calculate the average score
        scores = self._quiz_scores
        scores.sort
        del scores[-1]
        average_score = sum(scores)/len(scores)
        return str(average_score)

    def __str__(self):
        # Return quiz average as the state of 
        return self._name + "\t\t" + self.calc_average()
