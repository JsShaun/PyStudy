
from concurrent.futures import ThreadPoolExecutor, as_completed



def say_hello_to(name):
    for i in range(100000):
        pass
    return f'Hi, {name}'

names = ['John', 'Ben', 'Bill', 'Alex', 'Jenny']

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []
    for n in names:
        future = executor.submit(say_hello_to, n)
        print(type(future))
        futures.append(future)

    for future in as_completed(futures):
        print(future.result())

#########################################################

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(say_hello_to, names)

for r in results:
    print(r)