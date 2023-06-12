import time
import threading


def func():
    while True:
        print("Timer thread")
        time.sleep(1)


# создаем таймер, который будет запускать функцию func каждые 10 секунд
thr = threading.Timer(5, func)
# без демонизации потока программа не завершится, пока не завершится поток таймера
thr.setDaemon(True)
thr.start()

for _ in range(10):
    print("Main thread")
    time.sleep(1)

thr.cancel()  # остановить таймер если он не был запущен или он демон
