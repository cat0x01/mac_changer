import subprocess
import optparse
import re
import colorama
colorama.init()
from colorama import Fore, Style


Banner = """

  __  __              _____ _                                 
 |  \/  |            / ____| |                                
 | \  / | __ _  ___ | |    | |__   __ _ _ __   __ _  ___ _ __ 
 | |\/| |/ _` |/ __|| |    | '_ \ / _` | '_ \ / _` |/ _ \ '__|
 | |  | | (_| | (__ | |____| | | | (_| | | | | (_| |  __/ |       
 |_|  |_|\__,_|\___| \_____|_| |_|\__,_|_| |_|\__, |\___|_|   
                 ______                        __/ |          
                |______|                      |___/           


[+] MAC Address Changer [+]
[+] Created by : cat0x01 [+]
[+] GitHub: https://github.com/cat0x01 [+]
[+] Note: This tool is for educational purposes only.
"""

print(Fore.GREEN +  Banner)

parser = optparse.OptionParser() # create a parser object
parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address") # add options to the parser
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address") # add options to the parser
(options, arguments) = parser.parse_args() # parse the arguments

if not options.interface:
    parser.error(Fore.RED + "[-] Please specify an interface, use --help for more info")
elif not options.new_mac:
    parser.error(Fore.RED + "[-] Please specify a new MAC address, use --help for more info")
elif not options.interface or not options.new_mac:
    parser.error(Fore.RED + "[-] Please specify an interface and a new MAC address, use --help for more info")


subprocess.call("ifconfig " + options.interface + " down" , shell=True) # turn off the interface
subprocess.call("ifconfig " + options.interface + " hw ether " + options.new_mac + "" , shell=True) # change the MAC address
subprocess.call("ifconfig " + options.interface + " up", shell=True) # turn on the interface
print(f"MAC Address Changed to: {options.new_mac} for interface {options.interface}")  # Display the new MAC address and interface

ifconfig_results = subprocess.check_output("ifconfig " + options.interface , shell=True).decode('UTF-8')
mac_changed = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)

if options.new_mac == mac_changed[0]:
    print(Fore.GREEN + "[ + ] MAC address was successfully changed to: " + options.new_mac)
else:
    print(Fore.RED + "[ - ] MAC address was not changed.")
