import keyboard
import csv
import time

global numOfKeyStrokes  #In order to compare each elemtn's letter one by one with keystroke
numOfKeyStrokes = 0

def keyStroke():
 temp = keyboard.read_key()
 time.sleep(0.1)
 global numOfKeyStrokes
 numOfKeyStrokes += 1
 return temp

def init(): 
 f = open('./DataBase.csv')
 data = csv.reader(f)
 getKeyStroke = [] 
 matchingFlag = False

 while True: # looping in order to keep getting keystrokes
  global numOfKeyStrokes
  getKeyStroke.append(keyStroke())
  print(getKeyStroke)
  print("numOfKeyStrokes ", numOfKeyStrokes)
  for word in data: # each row is an each cell in a csv file
   matchingFlag = False
   for char in range(numOfKeyStrokes):  # each x is an each letter in an each cell
    print("word[9][char]==getKeyStroke[numOfKeyStrokes-1]", word[9][char].lower(),",",getKeyStroke[numOfKeyStrokes-1])
    if word[9][char].lower() == getKeyStroke[numOfKeyStrokes-1]:
     print("char matched")
     matchingFlag = True
     break
    else: 
     matchingFlag = False
     break
   if matchingFlag == True : print(word[9])

 f.close()

init()

