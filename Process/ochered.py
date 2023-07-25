import random
import time
import multiprocessing

# Queue - это общая очередь, которая может быть использована несколькими процессами
# Значения в очереди хранятся в порядке FIFO (First In First Out - Первый пришел, первый ушел)
# их можно получить из любого процесса, который имеет доступ к очереди


def get_text(q):
    val = random.randint(0, 9)
    q.put(str(val))


q = multiprocessing.Queue()

pr_list = []

if __name__ == "__main__":
    for i in range(10):
        pr = multiprocessing.Process(target=get_text, args=(q,))
        pr_list.append(pr)
        pr.start()

    for pr in pr_list:
        pr.join()

    for elem in iter(q.get, None):
        print(elem)
