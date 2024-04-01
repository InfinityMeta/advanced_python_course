from multiprocessing import Queue, Pipe, Process
import logging
import time
import codecs

from utils import task_3_log_file

logging.basicConfig(
    filename=task_3_log_file,
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S",
)


def a(a_queue, a_conn):
    while True:
        if not a_queue.empty():
            text = a_queue.get()
            text = text.lower()
            a_conn.send(text)
            time.sleep(5)


def b(b_conn, main_queue):
    while True:
        if b_conn.poll():
            text = b_conn.recv()
            text = codecs.encode(text, "rot_13")
            logging.info(f"Processed text: {text}")
            main_queue.put(text)


if __name__ == "__main__":
    a_queue = Queue()
    main_queue = Queue()
    b_conn, a_conn = Pipe()

    process_a = Process(target=a, args=(a_queue, a_conn))
    process_b = Process(target=b, args=(b_conn, main_queue))

    process_a.start()
    process_b.start()

    while True:
        text = input("Enter text for processing:")
        logging.info(f"Enter text for processing: {text}")
        a_queue.put(text)
