import time
from threading import Thread

def process_file(file):
    time.sleep(5)
    with open(file,"r") as f:
        file_content=f.read()
        lines=file_content.splitlines()
        words=file_content.split()
        print(f"{file} - Lines: {len(lines)},Words: {len(words)}")

def sequential_processing(files):
    start_time = time.perf_counter()
    for file in files:
        process_file(file)

    end_time = time.perf_counter()
    print(f"\nSequential execution time: {end_time - start_time:.6f} seconds")

def threaded_process(files):
    threads=[]
    start_time = time.perf_counter()
    for file in files:
        t=Thread(target=process_file,args=(file,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    end_time=time.perf_counter()
    print(f"Total execution time: {end_time - start_time}")

def main():
    files = ["Day 09 - Threading, Multiprocessing & Async/file1.txt",
            "Day 09 - Threading, Multiprocessing & Async/file2.txt",
              "Day 09 - Threading, Multiprocessing & Async/file3.txt"]

    print("=== Sequential ===")
    sequential_processing(files)

    print("\n=== Multithreaded ===")
    threaded_process(files)

main()

