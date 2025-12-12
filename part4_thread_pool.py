#Mijanur Rahman- 2212342642
import concurrent.futures
import time
import random
import threading

# Simulate a task (example workload)
def process_task(task_id):
    print(f"Task {task_id} starting on thread {threading.current_thread().name}")
    time.sleep(random.uniform(0.5, 1.5))  # simulate heavy work
    print(f"Task {task_id} completed")
    return task_id


if __name__ == "__main__":
    # Sequential Execution
    print("Sequential Execution:\n")

    start_time = time.time()
    for i in range(10):
        process_task(i)
    sequential_time = time.time() - start_time

    print(f"\nSequential Time: {sequential_time:.2f} seconds\n")


    # Parallel Execution Using Thread Pool
    print("Parallel Execution:\n")

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Run tasks in parallel
        results = list(executor.map(process_task, range(10)))

    parallel_time = time.time() - start_time

    print(f"\nParallel Time: {parallel_time:.2f} seconds")
    print(f"Speedup: {sequential_time / parallel_time:.2f}x")
