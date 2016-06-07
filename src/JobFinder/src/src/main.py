"""
    Author: Timothy Brantley II

    TODO: Make these asynchronous
"""
# import asyncio
import logging
from request_builder import run
from data import save
import requests

logger = logging.getLogger(__name__)

def init():
    # logging.config.fileConfig('logging_config.ini')
    pass

def process_request_Save(rs):
    for result in rs:
        print(result)
        save('Job', result.json())

def process_as_results_come_in():
    process = run()
    requests = [next(process) for req in range(0,1)]
    logging.debug("Going to save requests")
    process_request_Save(requests)

def process_get_status():
    count = len([c for c in run()])
    print("{0} URLS processed".format(count))

def main():
    init()
    process_as_results_come_in()
    # loop = asyncio.get_event_loop()
    # print("Starting Event Loop")
    # loop.run_until_complete(process_as_results_come_in())
    # loop.run_until_completed(process_get_status())
    # try:
    #     loop.run_forever()
    # finally:
    #     loop.close()

if __name__ == "__main__":
    main()
