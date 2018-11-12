#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wwl

import socket
from multiprocessing import Process

from concurrent.futures import ProcessPoolExecutor


def task(c,addr):
    while True:
        try:
            data = c.recv(1024)
            print(data.decode('utf-8'))
            if not data:
                c.close()
                break
            c.send(data.upper())
        except Exception:
            print('连接断开')
            c.close()
            break


if __name__ == '__main__':
    server = socket.socket()
    server.bind(('127.0.0.1', 65534))
    server.listen(5)

    # 创建一个进程池
    pool = ProcessPoolExecutor()

    while True:
        c, addr = server.accept()
        p = Process(target=task, args=(c, addr))
        p.start()
        pool.submit(task, c, addr)
