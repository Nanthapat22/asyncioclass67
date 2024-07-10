from random import random
import asyncio
# rice
async def cook_rice():
    value = 1 + random()
    print(f'Cooking rice {value} sec')
    await asyncio.sleep(value)
    return (f'rice: {value}')
# noodle
async def cook_noodle():
    value = 1 + random()
    print(f'Cooking noodle {value} sec')
    await asyncio.sleep(value)
    return (f'noodle: {value}')
# curry
async def cook_curry():
    value = 1 + random()
    print(f'Cooking curry {value} sec')
    await asyncio.sleep(value)
    return (f'curry: {value}')
async def main():
    
    tasks = [
        asyncio.create_task(cook_rice(),name="rice"),
        asyncio.create_task(cook_noodle(),name="noodle"),
        asyncio.create_task(cook_curry(),name="curry")
    ]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first = done.pop()
    print(first.result())
    print (f"{len(pending)} tasks completed in time ")
    
# run
asyncio.run(main())
    