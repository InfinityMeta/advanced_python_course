import time
import logging
from threading import Thread

from utils import fib, N, task_1_log_file


if __name__ == "__main__":
    logging.basicConfig(
        filename=task_1_log_file,
        level=logging.INFO,
        format="%(levelname)s: %(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S",
    )

    threads = []

    start = time.time()
    for i in range(10):
        threads.append(Thread(target=fib, args=(N,), daemon=True))
        threads[i].start()

    for i in range(10):
        threads[i].join()

    dur = time.time() - start
    logging.info("Threading regime:")
    logging.info(f"Time to compute {N}th fibonacci number: {dur:.4f}s")
