#!/usr/bin/env python3
"""
a coroutine that takes no arguments
"""

import asyncio
import random


async def async_generator():
    """ loops 10 times async wait 1 sec then yield random num"""
    i = random.uniform(0, 10)
    await asyncio.sleep(1)
    yield i
