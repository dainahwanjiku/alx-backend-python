#!/usr/bin/env python3
"""
a function that takes an int and returns asyncio.task
"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """returns asyncio.Task"""
    task = create_task(wait_random(max_delay))
    return task
