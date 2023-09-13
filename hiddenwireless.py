from scapy.all import *
import os

interface = "wlan0"

# Function to output probe requests, association requests, and/or probe responses
def h_packet(packet):
    if packet.haslayer(Dot11ProbeReq) or packet.haslayer(Dot11ProbeResp) or packet.haslayer(Dot11AssoReq):
        print "SSID identified " + packet.info

os.system("iwconfig " + interface + "mode monitor")

print "Sniffing traffic on interface " + interface
sniff(interface=interface, prn=h_packet)

