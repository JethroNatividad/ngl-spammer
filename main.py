import aiohttp
import asyncio
import time
import uuid
import random

# https://ngl.link/api/submit
times = 500

async def send_message(username, questions):
    try:
        async with aiohttp.ClientSession() as session:
            random_device_id = uuid.uuid4()
            random_question = random.choice(questions)
            data = {
                "username": username,
                "question": random_question,
                "deviceId": random_device_id
            }
            async with session.post(url="https://ngl.link/api/submit", data=data):
                print(f"Sent {random_question} to @{username} as {random_device_id}")
    except Exception as e:
        print(e)

async def main():
        badwords = [line.strip() for line in open('bad.txt', 'r')]
        username = "cottonfarmer112"
        tasks = [send_message(username, badwords) for _ in range(times)]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()

seconds = end - start
print(f"Took {seconds} seconds to send {times} messages.")
