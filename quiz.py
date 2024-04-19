questions = []
userAnswer = None
score = 0

def addQuestion(question, answersAr, correctAnswer):
    questions.append({"question":question, "answers":answersAr, "correctAnswer":correctAnswer})
    

def answerIsCorrect(correctAnswer):
    if correctAnswer == userAnswer:
        return True
    else:
        return False
    
def getUserChoice():
    userAnswer = input("Please select either a, b, or c")
    
addQuestion("What is Clash Royale?", ["a: A game", "b: A book", "c: A car"], "a: A game")

print(questions)