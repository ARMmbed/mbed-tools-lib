# https://gist.github.com/cevaris/79700649f0543584009e
import contextlib
import itertools
import sys
import threading
import time


class Spinner:
    spinner_cycle = itertools.cycle(['\\', '|', '/', '-'])

    def __init__(self):
        self.stop_running = threading.Event()
        self.spin_thread = threading.Thread(target=self.init_spin)

    def start(self):
        self.spin_thread.start()

    def stop(self):
        self.stop_running.set()
        self.spin_thread.join()

    def init_spin(self):
        while not self.stop_running.is_set():
            sys.stdout.write(next(self.spinner_cycle))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\b')
            sys.stdout.write(' ')
            sys.stdout.flush()
            sys.stdout.write('\b')


@contextlib.contextmanager
def spinner():
    spinner = Spinner()
    spinner.start()
    yield
    spinner.stop()
