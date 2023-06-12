import time
import threading

counter = 0
# Отличие RLock от Lock в том, что разблокировка может произойти только в том потоке, который ее и заблокировал
locker = threading.RLockLock()


def increment_counter():
    global counter
    while True:
        # блокируем доступ к облсати
        locker.acquire()
        counter += 1
        time.sleep(1)
        print(counter)
        # разблокируем доступ к области
        locker.release()

    # пример написания кода с помощью контекстного менеджера with
    # with locker:
    #     counter += 1
    #     time.sleep(1)
    #     print(counter)


for _ in range(10):
    t = threading.Thread(target=increment_counter)
    t.start()
