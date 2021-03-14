import keyboard
import csv
import time

global indexNum  #In order to compare each elemtn's letter one by one with keystroke
indexNum = -1

def keyStroke():
 temp = keyboard.read_key()
 time.sleep(0.1)
 global indexNum
 indexNum += 1
 return temp

def init(): 
 f = open('./DataBase.csv')
 data = csv.reader(f)
 getKeyStroke = [] 
 matchingFlag = False
 global indexNum

 while True: # looping in order to keep getting keystrokes
  getKeyStroke.append(keyStroke())
  print(getKeyStroke)
  print("getKeyStroke: ", getKeyStroke[indexNum])
  for row in data: # each row is an each cell in a csv file
   matchingFlag = False
   print("range(indexNum): ", range(indexNum+1))
   print("indexNum: ", indexNum)
   for x in range(indexNum+1):  # each x is an each letter in an each cell
    print("row[9][indexNum]:", row[9][indexNum])
    print("row[9][x]:", row[9][x])
    if row[9][x].lower() == getKeyStroke[indexNum]:
     matchingFlag = True
     break
    else: 
     matchingFlag = False
     break
   if matchingFlag == True : print(row[9])
 f.close()

init()

