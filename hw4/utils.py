N = 37

CPU_NUM = 12

task_1_log_file = "./artefacts/4.1_logs.txt"
task_2_threading_log_file = "./artefacts/4.2_threading_logs.txt"
task_2_threading_savepic_file = "./artefacts/4.2_threading.png"
task_2_multiprocessing_log_file = "./artefacts/4.2_multiprocessing_logs.txt"
task_2_multiprocessing_savepic_file = "./artefacts/4.2_multiprocessing.png"
task_3_log_file = "./artefacts/4.3_logs.txt"


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def integrate_seg(f, a, seg_start, seg_end, step):
    acc = 0
    for i in range(seg_start, seg_end + 1):
        acc += f(a + i * step) * step
    return acc
