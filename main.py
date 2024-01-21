import aiohttp
import asyncio
import time
import uuid

# https://ngl.link/api/submit

username = "cottonfarmer112"
question = "cottonfarmer112"

async def request():
    try:
        async with aiohttp.ClientSession() as session:
            data = {
                "username": username,
                "question": question,
                "deviceId": uuid.uuid4()
            }
            async with session.post(url="https://ngl.link/api/submit", data=data):
                print("sent")
    except Exception as e:
        print(e)

async def main():
    tasks = [request() for _ in range(100)]
    # Use asyncio.gather to run all the tasks concurrently
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
end = time.time()

print("Took {} seconds to send".format(end - start))
