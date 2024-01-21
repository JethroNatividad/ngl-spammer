import aiohttp
import asyncio
import time
import uuid
import random
from pyfiglet import Figlet
import click

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
            async with session.post(url="https://ngl.link/api/submit", data=data) as response:
                print("Status:", response.status)
                if response.status != 200:
                    print(f"Error sending '{random_question}' to @{username}.")
                else:
                    print(f"Sent '{random_question}' to @{username}.")
                return response.status
    except Exception as e:
        print(e)


async def spam(username, count):
        messages = [line.strip() for line in open('messages.txt', 'r')]

        start = time.time() 
        tasks = [send_message(username, messages) for _ in range(count)]
        results = await asyncio.gather(*tasks)
        end = time.time()

        # Count the number of success status
        success = results.count(200)
        seconds = end - start
        print(f"\nTook {seconds} seconds to send {success} messages.")
        
@click.command()
@click.option('--username', prompt='NGL Username',
              help='The username to spam.')
@click.option('--count', prompt='Spam count', type=int, help='n times to spam.')
def main(username, count):
    asyncio.run(spam(username, count))

f = Figlet(font='slant')
print(f.renderText('NGL SPAMMER'))
main()