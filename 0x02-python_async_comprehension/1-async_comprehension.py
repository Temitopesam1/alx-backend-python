#!/usr/bin/env python3
'''expressing coroutine using async comprehension
'''
import asyncio
import random, typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
  '''The coroutine collect random numbers and returns them
  '''
  result = [i async for i in async_generator()]
    return result