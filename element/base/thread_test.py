import  threading
import time

lock = threading.Lock()
def sing(song: str):
    lock.acquire()
    current_thread = threading.current_thread()
    print("sing:",current_thread)
    for i in range(3):
        print(f"sing...{song}")
        time.sleep(i)
    lock.release()

if __name__ == '__main__':
    sing_t = threading.Thread(target=sing,args=("11111",))
    sing_t1 = threading.Thread(target=sing,args=("22222",))
    sing_t.start()
    sing_t1.start()
    # sing_t.join()

    print("all done.")

