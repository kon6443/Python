import keyboard

def keyStrokes():
 print(keyboard.read_key())

def init():
 while True: 
  keyStrokes()

init()

