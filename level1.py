import subprocess
import optparse
import re

parser = optparse.OptionParser() # create a parser object
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address") # add options to the parser
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address") # add options to the parser
(options, arguments) = parser.parse_args() # parse the arguments

if not options.interface:
    parser.error("[-] Please specify an interface, use --help for more info")
elif not options.new_mac:
    parser.error("[-] Please specify a new MAC address, use --help for more info")
elif not options.interface or not options.new_mac:
    parser.error("[-] Please specify an interface and a new MAC address, use --help for more info")


subprocess.call("ifconfig " + options.interface + " down" , shell=True) # turn off the interface
subprocess.call("ifconfig " + options.interface + " hw ether " + options.new_mac + "" , shell=True) # change the MAC address
subprocess.call("ifconfig " + options.interface + " up", shell=True) # turn on the interface
print(f"MAC Address Changed to: {options.new_mac} for interface {options.interface}")  # Display the new MAC address and interface

ifconfig_results = subprocess.check_output("ifconfig " + options.interface , shell=True).decode('UTF-8')
mac_changed = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

if options.new_mac == mac_changed[0]:
    print("MAC address was successfully changed to: " + options.new_mac)
else:
    print("MAC address was not changed.")
