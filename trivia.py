import csv
import random

def loadTrivia(filename):
  with open (filename) as fd:
    readcsv = csv.reader(fd, delimiter=',')
    data = list(readcsv)
    print (len(data))

  return data

def randomQuestion(questionsarray):
  # How it's written in Javascript 
  # Math.floor(Math.random() * Baeman.length
  index = random.randint(0,len(questionsarray))
  return questionsarray[index]


if __name__ == "__main__":
  questions = loadTrivia('carmillaservertrivia.csv')
  selectedquestion = randomQuestion(questions)
  print(selectedquestion)
  category = selectedquestion[0]
  q = selectedquestion[1]

  #selectedqdict = {}

  # This needs to be multiple choice so that user only has to select a, b, c, d


  correctans = selectedquestion[2]


  ansb = selectedquestion[3]
  ansc = selectedquestion[4]
  ansd = selectedquestion[5]

  ansbank = [correctans, ansb, ansc, ansd]
  # Put answers in another array, scramble
  # Match with a, b, c, or d

  random.shuffle(ansbank)

  ansdict = {}
  ansdict['a'] = ansbank[0]
  ansdict['b'] = ansbank[1]
  ansdict['c'] = ansbank[2]
  ansdict['d'] = ansbank[3]

  print("The category is: " + category)
  print("Question: " + q)

  print("Choose one: ")
  print(ansbank)

  userans = input()

  if ansdict[userans].lower() == correctans.lower():
    print("Correct")
  else:
    print ("\nFake fan...")
    print ("The correct answer is: " + correctans)

