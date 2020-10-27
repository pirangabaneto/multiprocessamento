import threading
import multiprocessing
import socket


def fn():
    '''since all 3 functions were identical you can just use one ...'''
    x = 0
    while x < 10000000:
        if (x == 9999999):
            print("chegou ao topo")
        x += 1


def TEST_THREADS():
    new_thread1 = threading.Thread(target=fn, args=())
    new_thread2 = threading.Thread(target=fn, args=())
    new_thread3 = threading.Thread(target=fn, args=())
    new_thread1.start()
    new_thread2.start()
    new_thread3.start()
    new_thread1.join()
    new_thread2.join()
    new_thread3.join()


def TEST_NORMAL():
    fn()
    fn()
    fn()


def TEST_MULTIPROCESSING():
    threads = []
    for i in range(len(dados_conecao)):
        threads.append(multiprocessing.Process(target=escolherServidor, args=(i,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()



def escolherServidor(n):
    global dados_conecao
    ClientMultiSocket = socket.socket()
    servidor = dados_conecao[n]

    host = str(servidor[0])
    port = servidor[1]

    ClientMultiSocket.connect((host, port))

    ClientMultiSocket.recv(1024)
    ClientMultiSocket.close()



if __name__ == "__main__":
    '''It is very important to use name == __main__ guard code with threads and multiprocessing'''
    import timeit

    dados_conecao = [['127.0.0.1', 2001], ['127.0.0.2', 2002], ['127.0.0.3', 2003]]

    print("Time to Run 1x: %0.2fs" % (timeit.timeit(fn, number=1),))
    print("NORMAL:%0.2fs" % (timeit.timeit(TEST_NORMAL, number=1),))
    print("Threaded: %0.2fs" % (timeit.timeit(TEST_THREADS, number=1),))
    print("Multiprocessing: %0.2fs" % (timeit.timeit(TEST_MULTIPROCESSING, number=1),))