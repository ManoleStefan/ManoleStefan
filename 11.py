import asyncio
import sys

async def 1n(future, x):
    res = 0
    for i in range(1, x + 1):
        res += i
    future.set_result(f'1 = ={res}')
async def 2n(future, x):
    res = 0
    for i in range(1, x + 1):
        res += i
    future.set_result(f'2 ={res}')
async def 3n(future, x):
    res = 0
    for i in range(1, x + 1):
        res += i
    future.set_result(f'3 ={res}')
async def 4n(future, x):
    res = 0
    for i in range(1, x + 1):
        res = res + i
    future.set_result(f'4 = {res}')
def got_result(future):
    print(future.result())

if __name__ == '__main__':
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = n2 + 1
    n4 = n3 + 1
    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()
    future3 = asyncio.Future()
    future4 = asyncio.Future()
    tasks = [1n(future1, n1), 2n(future2, n2),3n(future3,n3),4n(future4,n4)]
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)
    future3.add_done_callback(got_result)
    future4.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
