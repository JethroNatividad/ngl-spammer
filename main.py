import aiohttp
import asyncio
import time
import uuid

# https://ngl.link/api/submit

username = "cottonfarmer112"
question = "cottonfarmer112"
times = 10

async def request():
    try:
        async with aiohttp.ClientSession() as session:
            random_device_id = uuid.uuid4()
            data = {
                "username": username,
                "question": question,
                "deviceId": random_device_id
            }
            async with session.post(url="https://ngl.link/api/submit", data=data):
                print(f"Sent {question} to @{username} as {random_device_id}")
    except Exception as e:
        print(e)

async def main():
    tasks = [request() for _ in range(times)]
    # Use asyncio.gather to run all the tasks concurrently
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
end = time.time()

seconds = end - start
print(f"Took {seconds} seconds to send {times} messages.")
