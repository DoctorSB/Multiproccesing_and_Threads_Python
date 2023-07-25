import multiprocessing


def end_func(result):
    # result - это список значений, которые возвращает функция map_async
    print("Процесс завершился")
    print(result)


def get_value(value):
    name = multiprocessing.current_process().name
    print(f"Процесс {name} получил значение {value}")
    return value


if __name__ == "__main__":
    # Создаем пул процессов с помощью контекстного менеджера 'with'.
    # Количество процессов в пуле устанавливается равным удвоенному количеству ядер процессора.
    with multiprocessing.Pool(multiprocessing.cpu_count() * 2) as pool:

        # Применяем функцию 'get_value' к каждому элементу списка 'list(range(100))' с использованием пула процессов.
        # Функция map автоматически распределяет вычисления между процессами в пуле.
        # pool.map(get_value, list(range(100)))
        pool.map_async(get_value, list(range(100)), callback=end_func)
        # при использовании map_async необходимо использовать метод close() и join()
        pool.close()
        pool.join()
