questions = []
# userAnswer = None
score = 0
# currentQuestion = None



def addQuestion(question, answersAr, correctAnswer):
    questions.append({"question":question, "answers":answersAr, "correctAnswer":correctAnswer, "userAnswer":""})


def answerIsCorrect(correctAnswer, userAnswer):
    if correctAnswer == userAnswer:
        return True
    else:
        return False

def getUserChoice(currentQuestion):
    # userAnswer = input("Please select either a, b, or c")
    currentQuestion["userAnswer"] = input("Please select either a, b, or c: ")


def displayQuestion(questionIndex):
    currentQuestion = questions[questionIndex]
    print(currentQuestion["question"])
    for i in range(len(currentQuestion["answers"])):
        print(currentQuestion["answers"][i])
    print()

addQuestion("What is Clash Royale?", ["a: A game", "b: A book", "c: A car"], "a")

displayQuestion(0)
getUserChoice(questions[0])



print()
