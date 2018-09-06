import asyncio

@asyncio.coroutine
def func5():
    while True:
        print("I am func5")
        yield from asyncio.sleep(1)

@asyncio.coroutine
def func6():
    while True:
        print("I am func6")
        yield from asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait([func5(),func6()])
    loop.run_until_complete(tasks)
