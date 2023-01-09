#!/usr/bin/env python3
"""
async coroutine takes an int arg, waits random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for random delay"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

