import multiprocessing

# различия между Lock и RLock
# Lock - может быть разблокирован любым процессом
# RLock - может быть разблокирован только тем процессом, который его заблокировал
lock = multiprocessing.Lock()
# lock = multiprocessing.RLock()  # Recursive lock


def get_value(l):
    l.acquire()
    pr_name = multiprocessing.current_process().name
    print(f"{pr_name} got the lock")
    l.release()


# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target=get_value, args=(lock,), name="Process-1")
#     p2 = multiprocessing.Process(target=get_value, args=(lock,))
#     p1.start()
#     p2.start()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=get_value, args=(lock,))
    p2 = multiprocessing.Process(target=get_value, args=(lock,))
    p1.start()
    p2.start()
    # ИСПОЛЬЗОВАТЬ join() ОБЯЗАТЕЛЬНО
    p1.join()
    p2.join()
