import random
import time
import multiprocessing

# Array - это общий массив, который может быть использован несколькими процессами
# При создании массива необходимо указать тип данных, которые будут храниться в массиве
# В данном случае это целые числа (integer)
# При создании массива необходимо указать его размер


def summ_value(array, locker, index):
    with locker:
        num = random.randint(0, 9)
        vtime = time.ctime()
        array[index] = num
        print(f"Array[{index}] = {num} at {vtime}")
        time.sleep(num)


arr = multiprocessing.Array("i", range(10))

lock = multiprocessing.Lock()


process = []

if __name__ == "__main__":
    for i in range(10):
        pr = multiprocessing.Process(target=summ_value, args=(arr, lock, i))
        process.append(pr)
        pr.start()

    for pr in process:
        pr.join()

    print(list(arr))
