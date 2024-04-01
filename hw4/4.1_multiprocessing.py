import time
import logging
from multiprocessing import Process

from utils import fib, N, task_1_log_file


if __name__ == "__main__":
    logging.basicConfig(
        filename=task_1_log_file,
        level=logging.INFO,
        format="%(levelname)s: %(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S",
    )

    processes = []

    start = time.time()
    for i in range(10):
        processes.append(Process(target=fib, args=(N,), daemon=True))
        processes[i].start()

    for i in range(10):
        processes[i].join()

    dur = time.time() - start
    logging.info("Multiprocessing regime:")
    logging.info(f"Time to compute {N}th fibonacci number: {dur:.4f}s")
