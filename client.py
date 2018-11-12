#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Wwl

from multiprocessing import  process
import socket

client = socket.socket()

client.connect(('127.0.0.1', 65534))

while True:
    msg = input('>>>>:')
    if not msg:continue
    client.send(msg.encode('utf-8'))

    data =client.recv(1024)
    print(data.decode('utf-8'))


