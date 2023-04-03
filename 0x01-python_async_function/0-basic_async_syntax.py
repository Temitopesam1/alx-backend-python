#!/usr/bin/env python3
'''Expressing coroutine using asyncio and random module
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number delay.
    '''
    delay: float = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
