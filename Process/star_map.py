import multiprocessing


def end_func(result):
    # result - это список значений, которые возвращает функция map_async
    print("Процесс завершился " + str(result))


def get_value(x, y, z):
    name = multiprocessing.current_process().name
    print(f"Процесс {name} получил значение {x, y, z}")
    return x, y, z


if __name__ == "__main__":
    # Создаем пул процессов с помощью контекстного менеджера 'with'.
    # Количество процессов в пуле устанавливается равным удвоенному количеству ядер процессора.
    with multiprocessing.Pool(multiprocessing.cpu_count() * 2) as pool:
        # нужно передавать аргументы в виде кортежа
        pool.starmap_async(
            get_value, [(1, 2, 3), (4, 5, 6)], callback=end_func)
        # при использовании map_async необходимо использовать метод close() и join()
        pool.close()
        pool.join()
