from multiprocessing import Process, Event
import time

event = Event()


def print_func():
    print("Процесс запущен")
    while True:
        event.wait()
        print("Процесс завершен")
        time.sleep(1)


def test_event():
    while True:
        print("Событие установлено")
        time.sleep(5)
        event.set()
        print("Событие сброшено")
        time.sleep(5)
        event.clear()


if __name__ == "__main__":
    Process(target=test_event).start()
    Process(target=print_func).start()
    
