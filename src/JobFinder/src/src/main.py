"""
    Author: Timothy Brantley II
"""
import asyncio
import logging
from request_builder import run
from data import save
import grequests

logger = logging.getLogger(__name__)

def init():
    # logging.config.fileConfig('logging_config.ini')
    pass

@asyncio.coroutine
def process_request_Save(rs):
    k = grequests.map(rs)
    save('Table', k)

@asyncio.coroutine
def process_as_results_come_in():
    requests = [req for req in run()]
    print("Going to save requests")
    process_request_Save(requests)

@asyncio.coroutine
def process_get_status():
    count = len([c for c in run()])
    print("{0} URLS processed".format(count))

def main():
    init()
    loop = asyncio.get_event_loop()
    print("Starting Event Loop")
    loop.run_until_complete(process_as_results_come_in())
    # loop.run_until_completed(process_get_status())
    try:
        loop.run_forever()
    finally:
        loop.close()

if __name__ == "__main__":
    main()
