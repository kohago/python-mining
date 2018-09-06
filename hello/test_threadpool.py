import time
import concurrent.futures

def func3():
    while True:
        print("I am func3!")
        time.sleep(1)

def func4():
    while True:
        print("I am func4!")
        time.sleep(1)

if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(func3)
    executor.submit(func4)
