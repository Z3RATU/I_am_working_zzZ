import time
import random

def main():
    text = open('./log2',mode='r')
    while(True):
        tell = text.tell()
        for line in text.readlines():
            random_f = random.random()
            random_f = random_f/3
            print(line[:-1])
            time.sleep(random_f)
        text.seek(tell)

if __name__ == '__main__':
    main()
