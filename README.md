# ARP spoof
Program for spoofing ARP requests to enable MITM attacks, works on LINUX\
Goal: Network packet manipulation\
\
\
How it works:\
Periodically sends out falsified ARP packets to manipulate the mac-address and the default gateway of the targeted host then routes them through the user's machine\
\
WARNING:\
Enable IP forwarding so the script won't pwn the targets' internet access\
\
Dependencies:\
sudo pip3 install scapy
