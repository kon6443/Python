import keyboard
import csv

def keyStroke():
 temp = keyboard.read_key()
 return temp

def init(): 
 f = open('./DataBase.csv')
 data = csv.reader(f)
 indexNum = 0  #In order to compare each elemtn's letter one by one with keystroke

 while True:
  #print("while indexNum: ", indexNum) # testing while loop
  getKeyStroke = keyStroke()
  for row in data:
   #print("for indexNum: ", indexNum) # testing for loop
   if row[9][indexNum].lower() == getKeyStroke :
    print(row[9])
  indexNum += 1
 f.close()

init()

