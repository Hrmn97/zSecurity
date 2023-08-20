#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")

parser.parse_args()

interface = raw_input("interface > ")
new_mac = raw_input("new MAC > ")
print ("[+] Changing the MAC Address for " + interface + " to " + new_mac)



#subprocess.call("ifconfig " + interface + " down", shell=True)
#subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
#subprocess.call("ifconfig " + interface + " up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
