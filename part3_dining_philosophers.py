import threading
import time
import random

# Create 3 forks (locks)
forks = [threading.Lock() for _ in range(3)]

def philosopher(phil_id):
    left_fork = phil_id
    right_fork = (phil_id + 1) % 3

    for i in range(3):  # Each philosopher eats 3 times
        print(f"Philosopher {phil_id} is thinking...")
        time.sleep(random.uniform(1, 2))

        print(f"Philosopher {phil_id} is hungry...")

        # Deadlock prevention: always pick the lower-numbered fork first
        first = min(left_fork, right_fork)
        second = max(left_fork, right_fork)

        print(f"Philosopher {phil_id} tries to pick fork {first}")
        with forks[first]:
            print(f"Philosopher {phil_id} picked up fork {first}")

            print(f"Philosopher {phil_id} tries to pick fork {second}")
            with forks[second]:
                print(f"Philosopher {phil_id} picked up fork {second}")

                # Eating
                print(f"Philosopher {phil_id} is eating...")
                time.sleep(random.uniform(1, 2))
                print(f"Philosopher {phil_id} finished eating.")

        # After context managers, forks are released automatically

    print(f"Philosopher {phil_id} left the table.")


# Main Execution
if __name__ == "__main__":
    threads = []

    for i in range(3):
        t = threading.Thread(target=philosopher, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nDining Philosophers simulation finished successfully!")
