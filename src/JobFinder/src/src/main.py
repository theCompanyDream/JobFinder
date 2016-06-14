"""
    Author: Timothy Brantley II

    TODO: Make these asynchronous
"""
# import asyncio
import logging
from request_builder import run
from data import save
import asyncio
import signal
import aiohttp
import sys
import json
import random

eLoop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=eLoop)

async def request_get(url, params):
    wait_time = random.randint(1, 60)
    yield from asyncio.sleep(wait_time)
    async with client.get(url, params=params) as response:
        assert response.status == 200
        logging.debug(response)
        return await response.read()

async def process_as_results_come_in():
    for url, req in run():
        response = await request_get(url, req)
        result = json.loads(response.decode('utf-8'))
        # logging.debug(result['results'])
        save("Jobs", *result['results'])

def signal_handler(signal, frame):
    eloop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
logging.debug("Starting Event Loop")
eLoop.run_until_complete(process_as_results_come_in())
try:
    eLoop.run_forever()
finally:
    eLoop.close()

# if __name__ == "__main__":
#     main()
