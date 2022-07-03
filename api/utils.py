from random import random


def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement


def generate_ticker_name() -> list[str]:
    result = []
    result.extend([f'ticker_0{i}' for i in range(10)])
    result.extend([f'ticker_{i}' for i in range(10, 100)])
    return result
