"""TBD"""

from random import randint


def get_random_seed() -> int:
    """Get a random seed. Must be between 0 and 2**32 - 1"""
    return randint(0, 2 ** 32 - 2)
