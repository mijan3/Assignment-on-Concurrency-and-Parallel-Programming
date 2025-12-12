# Assignment-on-Concurrency-and-Parallel-Programming

# CSE 425 - Concurrency and Parallel Programming

This repository contains four programs demonstrating core concepts of Concurrency and Parallel Programming using Python.

# How to Run:
```bash
python part1_race_condition.py
```
```bash
python part2_producer_consumer.py
```
```bash
python part3_dining_philosophers.py
```
```bash
python part4_thread_pool.py
```

# Part 1 – Race Condition & Synchronization

This program demonstrates a race condition where several threads are incrementing a shared variable without synchronization.
The first version (no lock) produces an incorrect result due to lost updates.

In this version threading.Lock() is used so that the increments are atomic, hence the final value will be correct.

I have learned:

- What race conditions are

- Why synchronization is needed How locks avoid inconsistent results

# Part 2 – Producer–Consumer Problem

This part implements a bakery simulation using a thread-safe queue (queue.Queue).
Baker threads produce bread and place it in a basket, while customer threads consume bread.

The queue automatically handles waiting when the basket is full or empty, preventing overflow/underflow.

I learned:

- How threads communicate using queues

- Why queue.Queue is ideal for producer-consumer patterns

- How blocking operations ensure correct coordination


# Part 3 – Dining Philosophers (Deadlock Prevention)

This program simulates 3 philosophers sharing 3 forks.
Deadlock is prevented using ordered fork picking (always pick the lower-numbered fork first).

I learned:

- How deadlock happens in shared-resource programs

- How ordering or special rules avoid deadlock

- How synchronization controls resource access between threads

# Part 4 – Thread Pool & Parallel Tasks

This program compares sequential execution vs. parallel execution using a ThreadPoolExecutor.
Ten tasks are executed first one-by-one, then using a pool of 4 threads.

Parallel execution finishes significantly faster.

I learned:

- How thread pools simplify parallelism

- How concurrency improves performance

- How to measure execution time and speedup

