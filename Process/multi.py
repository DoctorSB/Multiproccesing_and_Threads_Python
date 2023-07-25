import time
import multiprocessing


def func():
    for _ in range(100):
        print(f"{multiprocessing.current_process().name} - {time.ctime()}")
        time.sleep(1)

# Обязательно нужно вызывать только в __main__


if __name__ == "__main__":
    # Создаем процесс и запускаем его
    pr = multiprocessing.Process(target=func, name="Process-1")
    pr.start()
    # Дальнейший код будет выполняться только после завершения процесса
    pr.join()
    print('Main process continues to run in foreground')
    # для остановки процесса используем метод terminate()
    time.sleep(5)
    pr.terminate()

    prc = []
    for i in range(5):
        prc.append(multiprocessing.Process(target=func, name=f"Process-{i}"))
        prc[i].start()

    for i in prc:
        i.join()
