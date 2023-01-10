#!/usr/bin/env python3
"""
a coroutine that takes no arguments
"""

import asyncio
import random


async def async_generator() ->:
    """ loops 10 times async wait 1 sec then yield random num"""
    delay = random.uniform(0, 10)
    for i in range(0 to 10):
        yield i
    await asyncio.sleep(1)
    return delay
