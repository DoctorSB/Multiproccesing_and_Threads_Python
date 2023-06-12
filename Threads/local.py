import time
import threading

data = threading.local()


# threading.local() - создает объект, который хранит данные в потоке
# Это значит, что каждый поток будет иметь свою копию этого объекта
# Это удобно, когда в разных потоках нужно хранить разные данные
# Например, в одном потоке хранить данные о пользователе, а в другом о товарах
# В этом примере мы создаем объект data, который хранит данные в потоке
# И в двух потоках мы меняем значение этого объекта
# И в каждом потоке мы получаем свое значение
# Это значит, что в потоке 1 мы получим 1, а в потоке 2 мы получим 2
# Но функция get_data() будет получать значение из своего потока
def get_data():
    print(data.value)


def thread_1():
    data.value = 1
    get_data()


def thread_2():
    data.value = 2
    get_data()

# Можно обойтись без создания функции get_data() и вызывать data.value внутри потоков
# def thread_1():
#     data.value = 1
#     print(data.value)
#
# def thread_2():
#     data.test = []
#     print(data.test)
# При этом ошибки из-за отсутствия атрибута value не будет, потому что мы его создали в потоке


threading.Thread(target=thread_1).start()
threading.Thread(target=thread_2).start()
