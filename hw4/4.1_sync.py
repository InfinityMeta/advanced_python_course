import time
import logging

from utils import fib, N, task_1_log_file


if __name__ == "__main__":
    logging.basicConfig(
        filename=task_1_log_file,
        level=logging.INFO,
        format="%(levelname)s: %(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S",
    )
    start = time.time()
    for _ in range(10):
        fib(N)
    dur = time.time() - start
    logging.info("Synchronous regime:")
    logging.info(f"Time to compute {N}th fibonacci number: {dur:.4f}s")
