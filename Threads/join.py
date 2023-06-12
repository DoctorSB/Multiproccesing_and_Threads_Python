import time
import threading


def get_data(data, value):
    for _ in range(value):
        print(f'{threading.current_thread().name} - {data}')
        time.sleep(1)


thr_list = []

for i in range(5):
    thr = threading.Thread(target=get_data, args=(
        str(time.time()), i,), name=f"Thread_{i}")
    thr_list.append(thr)
    thr.start()

for i in thr_list:
    i.join()  # ждем завершения потока
