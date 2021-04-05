import csv
import time
import keyboard


def search_strs():
    search_str = ""
    while True:
        time.sleep(0.1)
        key_press = keyboard.read_key()
        if key_press == "backspace" and search_str:
            search_str = search_str[:-1]
        elif len(key_press) == 1 and ('a' <= key_press <= 'z'):
            search_str += keyboard.read_key()
        else:
            continue
        yield search_str


def init():
    words = []
    with open('./DataBase.csv') as f:
        data = csv.reader(f)
        for row in data:
            for word in row:
                if word == row[9]: 
                    words.append(word.strip().lower()) #  removing every empty strings left and right side of the element

    for search_str in search_strs():
        for word in words:
            #print(word)
            if word[:len(search_str)] == search_str:
                print(word)


if __name__ == '__main__':
    init()

