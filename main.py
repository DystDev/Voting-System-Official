
import os
import time
import csv
import getpass

results = {}
votersDict = {}
daysDictHandler = {}
currentDayResults = {}
currentDay = 1
extraFunctions = "CORRUPT, SAVE, LOAD, RETURN, END, SET, VOTERS, NEWDAY, DAYS"
password = "VOTING101"

def setup():
  global password
  # Adding own Candidates to app
  newCand = ""
  cont = False
  print("-- Voting System: First time setup --\n")
  print("Step 1: Configure Candidates \n")
  while cont == False:
    # Loops until CONT is said
    newCand = input("Enter candidate name here, use CONT to continue: ")
    # Checks if name is valid
    
    if newCand == "CONT":
      cont = True
      continue
    if newCand.isprintable() == False or newCand == "" or newCand in results.keys():
      print("Please choose a valid candidate name")
    else:
      # Adds a new dictionary value with the name and votes value 0
      results[newCand] = 0
      print("Added " + newCand + " as a candidate.")
    
  # Creates a iterable list of the candidates
  
  
  # Makes a readable list of names to be shown to user at voting screen
  
  os.system("clear")
  print("-- Voting System: First time setup --\n")
  print("Step 2: Set Admin Password \n")
  password = getpass.getpass(prompt='Enter password for admin panel: ', stream=None)
  os.system("clear")


setup()

def vote(vote):
  global results
  global votersDict
  global currentDayResults
  candidates = ""
  candidatesList = list(results.items())
  for x in range(len(candidatesList)):
    candidates += candidatesList[x][0] + ", "
  # Checks if vote is in the created dictionary of candidates
  candidates = candidates.rstrip(" ")
  candidates = candidates.rstrip(",")
  if vote not in results.keys() and vote != "ADMIN":
    print("Please make sure you vote for " + candidates)
    return
  if vote == "ADMIN":
    adminauth()
    return
  else:
    results[vote] += 1
    try:
      currentDayResults[vote] += 1
    except KeyError:
      currentDayResults[vote] = 1
  name = input("Please enter your name: ")
  votersDict[name] = vote
  # Shows user the vote they counted, waits once second, then clears for next vote
  print("Vote for " + vote + " counted")
  time.sleep(1)
  os.system("clear")


  # Debug line here
  # print("DEBUG: " + usrVote + " has " + str(results[usrVote]) + " votes")

def adminauth():
  guesses = 0
  auth = False
  while auth == False and guesses < 3:
    lockGuess = getpass.getpass(prompt='Enter password for admin panel: ', stream=None)
    if lockGuess == password:
      print("Authorised")
      auth = True
    elif lockGuess == "":
      print("Please enter a password into the field.")
    else:
      print("Unauthorised - Password Incorrect")
      guesses += 1
  if auth == False:
    print("Too many incorrect guesses, please try again later")
    return
  else:

    adminpanel()
    return

def adminpanel():
  returnToApp = False
  os.system("clear")
  print("-- VOTING SYSTEM ADMIN PANEL -- \n")
  while returnToApp != True:
    adminFunc = input("Please choose a function from " + extraFunctions + ": ").lower()
    if adminFunc != "return" and adminFunc != "end":
      if adminFunc.upper() in extraFunctions:
        eval(adminFunc + "()")
    
    elif adminFunc == "return":
      returnToApp = True
    
    elif adminFunc == "end":
      returnToApp = True
      end()

    

    else:
      print("Please choose a valid function")
  os.system("clear")
    
def corrupt():
  global results
  global currentDayResults
  ready = False
  while ready == False:
    # Loops until ready
    candToCorrupt = input("Enter candidate name here to corrupt: ")
    # Checks if name is valid
    if candToCorrupt in results.keys():
      ready = True
    else:
      print("Please choose a candidate in the election")
    # Adds 1000000 votes to the candidate
  results[candToCorrupt] += 1000000
  try:
    currentDayResults[vote] += 1
  except KeyError:
    currentDayResults[vote] = 1000000
  print("Completed.")

def voters():
  votersResult = ""
  votersList = list(votersDict.items())
  for x in range(len(votersList)):
    votersResult += votersList[x][0] + ": " + str(votersList[x][1]) + "\n"
  print(votersResult)
  

def save():
  resultsList = list(results.items())
  votersList = list(votersDict.items())
  newData = []
  with open("votes.txt", "w") as file:
    db = csv.writer(file)
    for result in resultsList:
      newData.append(result[0])
      newData.append(result[1])
      db.writerow(newData)
      newData = []
    file.close()
    db = ""
  with open("voters.txt", "w") as file:
    db = csv.writer(file)
    for result in votersList:
      newData.append(result[0])
      newData.append(result[1])
      db.writerow(newData)
      newData = []
    file.close()
    db = ""
  with open("days.txt", "w") as file:
    db = csv.writer(file)
    newData.append(currentDay)
    newData.append(currentDayResults)
    newData.append(daysDictHandler)
    db.writerow(newData)
    newData = []
    file.close()
    db = ""
  print("Completed.")

def load():
  global results
  global votersDict
  global currentDay
  global currentDayResults
  global daysDictHandler
  results = {}
  
  with open("votes.txt", "r") as file:
    info = csv.reader(file)    
    for row in info:
      results[row[0]] = int(row[1])
    file.close()
    info = ""
  with open("voters.txt", "r") as file:
    info = csv.reader(file)
    for row in info:
      votersDict[row[0]] = row[1]
    file.close()
    info = ""
  with open("days.txt", "r") as file:
    info = csv.reader(file)
    for row in info:
      currentDay = row[0]
      currentDayResults = row[1]
      daysDictHandler = row[2]
    file.close()
    info = ""
  print("Completed.")

def newday():
  global daysDictHandler
  global currentDayResults
  global currentDay
  daysDictHandler["Day " + str(currentDay)] = currentDayResults
  currentDayResults = {}
  currentDay += 1
  

def days():
  daysDictHandler["Day " + str(currentDay)] = currentDayResults
  dayPrintable = ""
  daysList = list(daysDictHandler.items())
  for day in daysList:
    dayPrintable += str(day[0]) + ": \n"
    dayResultList = list(day[1].items())
    for result in dayResultList:
      dayPrintable += "  " + str(result[0]) + ": " + str(result[1]) + "\n"
  print(dayPrintable)


def setResult():
  global results
  ready = False
  value = "NAN"
  while ready == False:
    # Loops until ready
    candToSet = input("Enter candidate name here to set value to: ")
    
    # Checks if name is valid
    if candToSet in results.keys():
      ready = True
      
    else:
      print("Please choose a candidate in the election")
    # Adds 1000000 votes to the candidate
  while value.isnumeric() == False:
    value = input("Enter value to set candidates vote to: ")
  value = int(value)
  results[candToSet] = value
  print("Completed.")

    
def end():
  os.system("clear")
  # Will hold the highest votes found so far
  maxVotes = 0
  # String to hold readable list of winners
  winners = ""
  # Iterable list of the results
  resultList = list(results.items())

  print("Conclusion of Voting: \n")
  # Iterates through all results' votes and updates max votes to result
  for x in range(len(results)):
    votes = resultList[x][1]
    if votes >= maxVotes:
      
      maxVotes = votes
  
  # Iterates through results again and if the votes is the same as the max, saves the candidate as winner (allows for duplicates)
  for x in range(len(results)):
    newVotes = resultList[x][1]
    if newVotes == maxVotes:
      winners += str(resultList[x][0]) + ", "
    # Formatted string to show candidate's votes
    print("{} got {} votes".format(resultList[x][0],resultList[x][1]))
  # Will show all winners
  print("\nWinner(s) are {}with {} votes".format(winners, maxVotes))
  time.sleep(5)
  x = input("Press ENTER to reset...")
  print("Resetting...")
  time.sleep(1)
  reset()


# Not sure about this method. It works, but the text is in red. I have no idea why. It's difficult for me to break out of the ADMIN panel. I'll have another crack later.

def reset():
  os.system('clear')
  os.system('python main.py')

# Will keep asking for votes until conclusion
while True:
  
  candidates = ""
  candidatesList = list(results.items())
  for x in range(len(candidatesList)):
    candidates += candidatesList[x][0] + ", "
  candidates = candidates.rstrip(" ")
  candidates = candidates.rstrip(",")
  resultsList = list(results.items())
  vote(input("Enter a vote: " + candidates + ": "))
  


