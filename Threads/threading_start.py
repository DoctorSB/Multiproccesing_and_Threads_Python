import time
import threading


def get_data(data):
    while True:
        print(f'{threading.current_thread().name} - {data}')
        time.sleep(5)

 # get_data без скобок - это ссылка на функцию, а не вызов функции
 # после str(time.time()) идет запятая, потому что функция принимает аргументы, а не кортеж
thr = threading.Thread(target=get_data, args=(
    str(time.time()),), name="Thread_1")
thr.start()

for i in range(100):
    print(f'{threading.current_thread().name} - {i}')
    time.sleep(1)
    if i % 10 == 0:
        print("Количество активных потоков: ",
              threading.active_count(), end="\n")
        print("Все потоки запущенные в этот момент: ",
              threading.enumerate(), end="\n")
        print("Работает ли поток thr: ", thr.is_alive(), end="\n")
