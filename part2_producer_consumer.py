#Mijanur Rahman- 2212342642
import threading
import time
import queue

# Shared basket (thread-safe queue)
basket = queue.Queue(maxsize=5)   # basket capacity = 5

# Producer → Baker
def baker(name, items=10):
    for i in range(items):
        bread = f"Bread-{i} by {name}"
        basket.put(bread)  # Waits automatically if basket is full
        print(f"{name} baked {bread}")
        time.sleep(0.5)    # simulate baking time
    print(f"{name} finished baking.")


# Consumer → Customer
def customer(name, items=10):
    for _ in range(items):
        bread = basket.get()  # Waits automatically if basket is empty
        print(f"{name} bought/eaten {bread}")
        time.sleep(0.8)       # simulate eating time
    print(f"{name} finished buying.")


# Main Execution
if __name__ == "__main__":

    # Create baker threads (producers)
    baker1 = threading.Thread(target=baker, args=("Baker-1",))
    baker2 = threading.Thread(target=baker, args=("Baker-2",))

    # Create customer threads (consumers)
    customer1 = threading.Thread(target=customer, args=("Customer-1",))
    customer2 = threading.Thread(target=customer, args=("Customer-2",))

    # Start threads
    baker1.start()
    baker2.start()
    customer1.start()
    customer2.start()

    # Wait for completion
    baker1.join()
    baker2.join()
    customer1.join()
    customer2.join()

    print("\nSimulation finished successfully!")
