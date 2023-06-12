import time
import threading


def get_data(data):
    for _ in range(5):
        print(f'{threading.current_thread().name} - {data}')
        time.sleep(1)

# При создании потока можно указать, что он будет демоном
# Демон - это поток, который не ждет завершения работы других потоков
# Если все потоки в программе - демоны, то программа завершится, как только завершится поток main
# Если хотя бы один поток не демон, то программа будет ждать завершения всех потоков
# По умолчанию потоки не демоны


thr = threading.Thread(target=get_data, args=(
    str(time.time()),), daemon=True, name="Thread_1")

# thr.setDaemon(True)  # можно указать демонство потока и так
thr.start()
print('Finish')
