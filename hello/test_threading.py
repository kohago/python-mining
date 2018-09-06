import time
import threading

def func1():
    while True:
        print("I am func1!")
        time.sleep(1)

def func2():
    while True:
        print("I am func2!")
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=func1)
    thread2 = threading.Thread(target=func2)
    thread1.start()
    thread2.start()
