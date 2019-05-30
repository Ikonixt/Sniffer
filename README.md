# ARP spoof
for spoofing ARP requests to enable MITM attacks, works on LINUX\
Goal: Practice packet manipulation\
\
\
How it works:\
Periodically sends out falsified ARP packet to manipulate the mac-address of the target host and the default gateway and routes them through the machine\
\
WARNING:\
Enable IP forwarding so the script won't pwn the targets' internet access\
\
Dependencies:\
sudo pip3 install scapy
