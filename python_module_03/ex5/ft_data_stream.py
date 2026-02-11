import random
import time
from typing import Generator


def game_event_stream(
        count: int) -> Generator[dict[str, str | int], None, None]:
    players: list[str] = ['alice', 'bob', 'charlie']
    actions: list[str] = ['killed monster', 'found treasure', 'leveled up']

    for i in range(1, count + 1):
        event: dict[str, str | int] = {
            'id': i,
            'player': random.choice(players),
            'level': random.randint(1, 20),
            'action': random.choice(actions)
        }
        yield event


def process_game_events() -> tuple[int, int, int, int, float]:
    total_events: int = 0
    high_level: int = 0
    treasure_events: int = 0
    level_up_events: int = 0

    start_time: float = time.time()

    for event in game_event_stream(1000):
        total_events += 1

        if total_events <= 3:
            print(f"Event {event['id']}: Player {event['player']} \
(level {event['level']}) {event['action']}")
        if event['level'] > 10:
            high_level += 1
        if event['action'] == 'found treasure':
            treasure_events += 1
        if event['action'] == 'leveled up':
            level_up_events += 1

    if total_events > 3:
        print("...")

    return (total_events, high_level, treasure_events, level_up_events,
            time.time() - start_time)


def fibonacci_sequence() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    for _ in range(10):
        yield a
        a, b = b, a + b


def prime_number() -> Generator[int, None, None]:
    i: int = 0
    n: int = 2

    def is_prime(n: int) -> bool:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    while i < 5:
        if is_prime(n):
            yield n
            i += 1
        n += 1


def demonstration_generator() -> None:
    print("Fibonacci sequence (first 10): ", end="")
    i = 0
    for n in fibonacci_sequence():
        if i < 9:
            print(n, end=", ")
        else:
            print(n)
        i += 1
    print("Prime numbers (first 5): ", end="")
    i = 0
    for n in prime_number():
        if i < 4:
            print(n, end=", ")
        else:
            print(n)
        i += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")

    print("Processing 1000 game events...\n")
    (total_events, high_level, treasure_events,
     level_up_events, processing_time) = process_game_events()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    demonstration_generator()
