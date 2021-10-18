import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed


@asyncio.coroutine
def say_hello_to():
    for i in range(100000):
        yield i



with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    future = executor.submit(say_hello_to)
    # print(type(future))
    t =  asyncio.wrap_future(future)
    # futures.append(future)

    print(t)

    # for future in as_completed(futures):
    #     print(future.result())

