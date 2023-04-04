#!/usr/bin/env python3
'''expressing coroutine using asyncio and random modules
'''
import asyncio
import random, typing


async def async_generator() -> typing.Generator[float, None, None]:
  '''The coroutine loops and yields
  '''
  i = 0
  while(i < 10):
    await asyncio.sleep(1)
    yield random.uniform(0, 10)
    i += 1
