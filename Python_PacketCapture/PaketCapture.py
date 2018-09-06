from scapy.all import*  

count = 0
protocols = {1:'ICMP', 6:'TCP', 17:'UDP'}

def sniffing():
    sniff(prn=showPacket, timeout=int(time))

def showPacket(packet):
    global count
    src_ip = packet[0][1].src  
    dst_ip = packet[0][1].dst  
    proto = packet[0][1].proto

    if proto in protocols:  
        print("protocol: %s: src: %s -> dst: %s" %(protocols[proto], src_ip, dst_ip))
        count += 1
        print(count)
  
time = input()
sniffing()
