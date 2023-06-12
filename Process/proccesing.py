import time
import multiprocessing

class Process(multiprocessing.Process):
    # Переопределяем метод run
    def run(self):
        print('Work')

if __name__ == "__main__":
    pr = Process()  
    pr.start()