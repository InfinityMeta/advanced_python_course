import math
import time
import numpy as np
import matplotlib.pyplot as plt
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils import (
    task_2_threading_log_file,
    task_2_threading_savepic_file,
    CPU_NUM,
    integrate_seg,
)


def integrate(f, a, b, n_jobs=1, n_iter=1e8, n_split=100):
    points = np.linspace(0, n_iter, n_split, dtype=np.int64)
    pair_of_points = zip(points, points[1:])
    step = (b - a) / n_iter
    acc = 0
    futures = []
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        for seg_start, seg_end in pair_of_points:
            futures.append(
                executor.submit(
                    integrate_seg,
                    f=f,
                    a=a,
                    seg_start=seg_start,
                    seg_end=seg_end,
                    step=step,
                )
            )
        for future in as_completed(futures):
            acc += future.result()

    return acc


if __name__ == "__main__":
    logging.basicConfig(
        filename=task_2_threading_log_file,
        level=logging.INFO,
        format="%(levelname)s: %(asctime)s %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S",
    )

    durs = []

    logging.info("Threading experiment starts")

    for i in range(1, CPU_NUM * 3 + 1):
        start = time.time()
        integrate(math.cos, 0, math.pi / 2, n_jobs=i)
        dur = time.time() - start
        logging.info(f"n_jobs: {i}, time: {dur:.4f}s")
        durs.append(dur)

    plt.plot(list(range(1, CPU_NUM * 3 + 1)), durs)
    plt.xlabel("n_jobs")
    plt.ylabel("time")
    plt.title("Integration: threading")
    plt.grid(True)
    plt.savefig(task_2_threading_savepic_file)
