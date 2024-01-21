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
            async with session.post(url="https://ngl.link/api/submit", data=data):
                print(f"Sent {random_question} to @{username} as {random_device_id}")
    except Exception as e:
        print(e)


async def spam(username, count):
        messages = [line.strip() for line in open('messages.txt', 'r')]
        tasks = [send_message(username, messages) for _ in range(count)]
        await asyncio.gather(*tasks)

@click.command()
@click.option('--username', prompt='NGL Username',
              help='The username to spam.')
@click.option('--count', prompt='Spam count', type=int, help='n times to spam.')
def main(username, count):

    start = time.time()
    asyncio.run(spam(username, count))
    end = time.time()

    seconds = end - start
    print(f"Took {seconds} seconds to send {count} messages.")

f = Figlet(font='slant')
print(f.renderText('NGL SPAMMER'))
main()