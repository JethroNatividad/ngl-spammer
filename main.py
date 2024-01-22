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
                'Host': 'ngl.link',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://ngl.link',
                'Connection': 'keep-alive',
                'Referer': f'https://ngl.link/{username}',
                'Cookie': f'cf_clearance={cf_clearance}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers',
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