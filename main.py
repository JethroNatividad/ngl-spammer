import aiohttp
import asyncio
import time
import uuid

# https://ngl.link/api/submit
times = 10

async def send_message(username, question):
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
    username = "cottonfarmer112"
    question = "cottonfarmer112"
    tasks = [send_message(username, question) for _ in range(times)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()

seconds = end - start
print(f"Took {seconds} seconds to send {times} messages.")
