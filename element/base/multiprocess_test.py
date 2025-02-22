import multiprocessing
import time


def dance():
    for i in range(3):
        time.sleep(i)
        print(f'dance {i}')

def sing():
    for i in range(3):
        time.sleep(i)
        print(f'sing {i}')

if __name__ == '__main__':
    multiprocessing.freeze_support()
    dance_process  = multiprocessing.Process(target=dance)
    #设置为守护进程
    dance_process.daemon =True
    dance_process.start()

    sing_process  = multiprocessing.Process(target=sing)
    sing_process.start()
    # 子进程销毁
    # sing_process.terminate()
    sing_process.join()
    dance_process.join()