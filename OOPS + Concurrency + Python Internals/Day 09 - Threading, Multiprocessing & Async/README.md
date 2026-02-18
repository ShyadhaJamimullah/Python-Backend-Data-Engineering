## Python Concurrency & Parallelism Tasks

This repository contains two Python tasks demonstrating concurrent and parallel processing techniques:

**1. Multi-File Processor –** Compare sequential vs multithreaded file processing.

**2. Parallel Downloader –** Download multiple files asynchronously using ```asyncio``` and ```aiohttp```.

### Task 1: Multi-File Processor

A console app that reads multiple text files and counts lines and words, demonstrating sequential vs multithreaded execution.

**Key Concepts**

- Sequential file processing vs multithreading.
- Thread creation using Python’s ```threading.Thread```.
- Measuring execution time for performance comparison.
- Basic file I/O.

**Features**

- Counts lines and words in multiple files.
- Shows time difference between sequential and threaded execution.

### Task 2: Parallel Downloader

A Python program to download multiple files concurrently using asynchronous programming.

**Key Concepts**

- Asynchronous tasks with ```asyncio```.
- HTTP requests using ```aiohttp``` for non-blocking downloads.
- Creating and running multiple tasks concurrently with ```asyncio.gather```.
- Persistent storage in a ```downloads``` folder.

**Features**

- Reads URLs from a text file (```links.txt```).
- Downloads all files in parallel.
- Prints download start and finish messages for each file.
- Measures total execution time for all downloads.

### What I Learned

- Difference between sequential, multithreaded, and asynchronous execution.
- How to improve performance for I/O-bound tasks.
- Using Python’s threading module and asyncio module effectively.
- Measuring execution time for performance comparison.
- Managing multiple files and downloads safely.

