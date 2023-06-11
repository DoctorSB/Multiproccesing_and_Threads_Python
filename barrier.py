import time
import threading
import random
from threading import current_thread

# барьер - это объект, который блокирует выполнение потоков до тех пор, пока не будут выполнены определенные условия
# например, если мы хотим, чтобы 5 потоков выполнили какую-то задачу, то мы можем использовать барьер
# и когда 5 потоков достигнут барьера, то они будут ждать пока остальные 5 потоков не достигнут барьера
# когда все 10 потоков достигнут барьера, то они будут выполнять задачу


def test(barrier):
    slp = random.randint(10, 15)
    print(f"{current_thread().name} запущен в {time.strftime('%H:%M:%S')}")
    time.sleep(slp)
    # тут может выполнятся загрузка данных

    # блокируем выполнение потоков до тех пор, пока не будут выполнены определенные условия
    barrier.wait()
    # а тут может выполнятся обработка/отправка данных
    print(f"{current_thread().name} преодолел барьер {time.strftime('%H:%M:%S')}")


bar = threading.Barrier(5)  # создаем барьер, который будет ждать 5 потоков
for i in range(10):
    threading.Thread(target=test, args=(bar,), name=f'Thr_{i}').start()
