questions = []

def addQuestion(question, answersAr, correctAnswer):
    questions.append({"question":question, "answers":answersAr, "correctAnswer":correctAnswer, "userAnswer":""})


def answerIsCorrect(correctAnswer, userAnswer):
    if correctAnswer == userAnswer:
        return True
    else:
        return False

def getUserChoice(currentQuestion):
    currentQuestion["userAnswer"] = input("Please select either a, b, or c: ")


def displayQuestion(currentQuestion):
    print(currentQuestion["question"])
    for i in range(len(currentQuestion["answers"])):
        print(currentQuestion["answers"][i])
    print()
    
def mainLoop():
  score = 0
  addQuestion("What are the UN SDGs?", ["a: A set of Goals to help improve the world.", "b: A book wirtten UN members", "c: A singular goal developed by the United States"], "a")
  addQuestion("When were these goals made?", ["a: 2012", "b: 1994", "c: 2015"], "c")
  addQuestion("How many SDGs are there?", ["a: 100", "b: 17", "c: 9"], "b")
  addQuestion("As of 2023, which country is leading in their progress of completing the SDGs?", ["a: Sweden", "b: Finland", "c: America"], "b")
  addQuestion("What is SDG 9?", ["a: industry, infrastructure, and innovation", "b: lowering Carbon Dioxide emmisions", "c: lowering plastic production"], "a")
  addQuestion("Which country is doing the worst with these goals as of 2023?", ["a: Somalia", "b: China", "c: South Sudan"], "c")
  addQuestion("How many countries, of the 197, are participating in the completion of the SDGs?", ["a: 197", "b: 193", "c: 177"], "b")
  addQuestion("What does SDG stand for?", ["a: Sustainable Development Goal", "b: Sustainable Devotion Goal", "c: Solving Difficulties Goal"], "a")
  addQuestion("Which of these SDGs have we made the most progress to?", ["a: SDG 9", "b: SDG 2", "c: SDG 7"], "a")
  addQuestion("Which of these SDGs have we made the least progress to?", ["a: SDG 7", "b: SDG 9", "c: SDG 2"], "c")
  
  for currentQuestion in questions:
    displayQuestion(currentQuestion)
    getUserChoice(currentQuestion)
    
    if answerIsCorrect(currentQuestion["correctAnswer"], currentQuestion["userAnswer"]):
      print("That's correct!")
      score+=1

    else:
      print("That's incorrect!")
      print("The correct answer is", currentQuestion["correctAnswer"])
    
    print()

  print("Congratulations, you have", score, "out of", len(questions), "points!")

print()
mainLoop()