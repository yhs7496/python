from scapy.all import*

count = 1
protocols = {1:'ICMP', 6:'TCP', 17:'UDP'}

def sniffing():
    print("Sniffing Start")
    pcap_file = sniff(prn=showPacket, timeout=int(sniffing_time), filter=str(protocol_type))
    wrpcap("Packet.pcap", pcap_file)

def showPacket(packet):
    global count
    # IP
    src_ip = packet[IP].src  
    dst_ip = packet[IP].dst  
    proto = packet[IP].proto
    ttl = packet[IP].ttl
    
    # TCP
    sport = packet[TCP].sport
    dport = packet[TCP].dport
    seq = packet[TCP].dport
    ack = packet[TCP].ack

    if proto in protocols:  
        if proto == 6:
            print("packet number: %s protocol: %s" %(count, protocols[proto]))
            print("src: %s -> dst: %s TTL: %s" %(src_ip, dst_ip, ttl))
            print("sport: %s dport: %s" %(sport, dport))
            print("seq: %s ack: %s" %(seq, ack))

        else:
            print("packet number: %s protocol: %s" %(count, protocols[proto]))
            print("src: %s -> dst: %s TTL: %s" %(src_ip, dst_ip, ttl))
        count += 1
    else:
        print("지원하지 않는 프로토콜입니다.")
         
protocol_type = input("Protocol Type: ")         
sniffing_time = input("Sniffing Time: ")
sniffing()

