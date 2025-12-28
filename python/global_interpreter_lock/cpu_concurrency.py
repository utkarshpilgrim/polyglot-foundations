import hashlib, threading, multiprocessing as mp, os, time

def cpu_work(n=10**7):
    data= b"benchmark"
    for _ in range(n): 
        hashlib.sha256(data).digest() 

if __name__ == "__main__": 
    start = time.time()
    procs = os.cpu_count()

    threads = [threading.Thread(target=cpu_work) for _ in range(procs)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Threads: {time.time() - start:.1f}s")

    start = time.time()
    processes = [mp.Process(target=cpu_work) for _ in range(procs)]
    for p in processes: p.start()
    for p in processes: p.join()
    print(f"Processes: {time.time() - start:.1f}s")