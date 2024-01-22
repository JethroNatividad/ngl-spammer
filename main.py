import aiohttp
import asyncio
import time
import uuid
import random
from pyfiglet import Figlet
import click

async def send_message(username, questions, cf_clearance):
    try:
        async with aiohttp.ClientSession() as session:
            random_device_id = uuid.uuid4()
            random_question = random.choice(questions)
            data = {
                "username": username,
                "question": random_question,
                "deviceId": random_device_id
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                'Cookie': f'cf_clearance={cf_clearance}',
            }
            
            async with session.post(url="https://ngl.link/api/submit", data=data, headers=headers) as response:
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
        cf_clearance = open('clearance.txt', 'r').readline().strip()

        start = time.time() 
        tasks = [send_message(username, messages, cf_clearance) for _ in range(count)]
        results = await asyncio.gather(*tasks)
        end = time.time()

        # Count the number of success status
        success = results.count(200)
        seconds = end - start

        print(f"\nTook {seconds} seconds to send {success} out of {count} messages.")
        if success < count:
            print("Please add a new Cloudflare cookie. Follow the instructions on the README.md file.")
        
@click.command()
@click.option('--username', prompt='NGL Username',
              help='The username to spam.')
@click.option('--count', prompt='Spam count', type=int, help='n times to spam.')
def main(username, count):
    asyncio.run(spam(username, count))

print(Figlet(font='slant').renderText('NGL SPAMMER'))
main()