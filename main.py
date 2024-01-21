import aiohttp
import asyncio
import time
# https://ngl.link/api/submit

username = "cottonfarmer112"
question = "cottonfarmer112"

data = {
    "username": username,
    "question": question,
    "deviceId": "e6baa765-afad-4885-a06f-13b5d54d7ce7"
}

async def request():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url="https://ngl.link/api/submit", data=data):
                print("sent")
    except Exception as e:
        print(e)

async def main():
    tasks = [request() for _ in range(10)]
    # Use asyncio.gather to run all the tasks concurrently
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
end = time.time()

print("Took {} seconds to send".format(end - start))
