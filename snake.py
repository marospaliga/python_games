import algoplay as play
import time
import asyncio

# Initialize start time or counters
start_time = time.time()
a = False

@play.repeat_forever
async def do():
    global a
    if not a:
        print("First function is about to sleep for 7 seconds")
        await asyncio.sleep(7)
        print("First function is called second")
        a = True
    else:
        print("First function is about to sleep for 3 seconds")
        await asyncio.sleep(3)
        print("First function is called first")
        a = False

@play.repeat_forever
async def another_do():
    global a
    if not a:
        print("Second function is about to sleep for 0.5 seconds (first)")
        await asyncio.sleep(0.5)
        print("Second function is called first")
        a = True
    else: 
        print("Second function is about to sleep for 0.5 seconds (second)")
        await asyncio.sleep(0.5)
        print("Second function is called second")
        a = False

print("test2")


# Start the program
play.start_program()
