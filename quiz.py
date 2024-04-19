questions = []
userAnswer = None
score = 0
currentQuestion = None

def addQuestion(question, answersAr, correctAnswer):
    questions.append({"question":question, "answers":answersAr, "correctAnswer":correctAnswer})
    

def answerIsCorrect(correctAnswer):
    if correctAnswer == userAnswer:
        return True
    else:
        return False
    
def getUserChoice():
    userAnswer = input("Please select either a, b, or c")
    
def displayQuestion(questionIndex):
    currentQuestion = questions[questionIndex]
    print(currentQuestion["question"])
    for i in range(len(currentQuestion["answers"])):
        print(currentQuestion["answers"][i])
    print()
            
addQuestion("What is Clash Royale?", ["a: A game", "b: A book", "c: A car"], "a: A game")

displayQuestion(0)