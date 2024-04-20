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


def displayQuestion(currentQuestion):
    print(currentQuestion["question"])
    for i in range(len(currentQuestion["answers"])):
        print(currentQuestion["answers"][i])
    print()
    
def mainLoop():
  addQuestion("What is Clash Royale?", ["a: A game", "b: A book", "c: A car"], "a")
  addQuestion("How old is Clash Royale?", ["a: 54 years", "b: 2 years", "c: 8 years"], "c")
  addQuestion("Where is Clash Royale played on?", ["a: Computer", "b: Mobile", "c: Console"], "b")
  
  for currentQuestion in questions:
    displayQuestion(currentQuestion)
    getUserChoice(currentQuestion)
    
    if answerIsCorrect(currentQuestion["correctAnswer"], currentQuestion["userAnswer"]):
      print("That's correct!")

    else:
      print("That's incorrect!")
      print("The correct answer is", currentQuestion["correctAnswer"])
    
    print()

print()
mainLoop()