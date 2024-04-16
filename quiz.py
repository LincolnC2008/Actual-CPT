questions = []
userAnswer = None
score = 0

def addQuestion(question, answersAr, correctAnswer):
    questions.push({"question":question, "answers":answersAr, "correctAnswer":correctAnswer})
    
addQuestion()

def answerIsCorrect(correctAnswer):
    if correctAnswer == userAnswer:
        return True
    else:
        return False