import random
import itertools
import math
from typing import Union

from fastapi import FastAPI
random.seed(10)


def heavy_compute():
    list1=[random.randint(1, 100) for i in range(10000)]
    list2=[random.randint(1, 10) for i in range(100)]

    two_lists=[list1,list2]
    permutation = itertools.product(*two_lists) # I obtain the permutation ty Cyttorak
    result=[math.factorial(x[0]+x[1]) for x in permutation] # The complex operation (factorial of the sum)
    return result

app = FastAPI()

@app.get("/compute")
async def hello():
    file_name = "/tmp/test.txt"
    try:
        with open(file_name, "w+") as f:
            import time
            start_time = time.time()
            heavy_compute()
            time_spent = time.time() - start_time
            response = f"Time spent in compute() function: {time_spent} seconds"
            response = response + "\n test rolling update"
            f.write(response)
            return response + "\n"
    except Exception as e:
        return "open file failed"


@app.get("/health")
async def health():
    return "OK"
       