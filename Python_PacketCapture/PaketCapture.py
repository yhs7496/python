from scapy.all import*
  
count = 1
protocols = {1:'icmp', 6:'tcp', 17:'udp'}
protocol_type = input("Protocol Type: ")
sniffing_time = input("Sniffing Time: ")

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
    length = packet[IP].len    
        
    if proto in protocols:  
        # ICMP 
        if proto == 1:
            message_type = packet[ICMP].type
            code = packet[ICMP].code
            
            print("packet number: %s protocol: %s" %(count, protocols[proto].upper()))
            print("src: %s -> dst: %s TTL: %s" %(src_ip, dst_ip, ttl))
            print("type: %s code: %s" %(message_type, code))
            print("\n")

        # TCP
        if proto == 6:
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            seq = packet[TCP].dport
            ack = packet[TCP].ack
            flag = packet[TCP].flags
            
            print("packet number: %s protocol: %s" %(count, protocols[proto].upper()))
            print("src: %s -> dst: %s" %(src_ip, dst_ip))
            print("TTL: %s Length: %s" %(ttl, length))
            print("sport: %s dport: %s" %(sport, dport))
            print("seq: %s ack: %s flag: %s" %(seq, ack, flag))
            print("\n")
        
        # UDP
        if proto == 17:
            print("packet number: %s protocol: %s" %(count, protocols[proto].upper()))
            print("src: %s -> dst: %s TTL: %s" %(src_ip, dst_ip, ttl))
            print("\n")
        count += 1

if protocol_type in protocols.values():
    sniffing()
    print("Finish Capture Packet")
    print("Total Packet: %s" %(count-1))    
else: 
    print("Unsupported format")

