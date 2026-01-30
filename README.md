# MAC Address Changer

A simple Python tool to change your network interface's MAC address for educational purposes.

## What is a MAC Address?

A **MAC (Media Access Control) address** is a unique identifier assigned to network interfaces for communications at the data link layer of a network segment. It's a 48-bit (6-byte) address typically represented as six groups of two hexadecimal digits, separated by colons or hyphens (e.g., `00:1A:2B:3C:4D:5E`).

**Key characteristics:**
- **Unique**: Each network interface has a unique MAC address
- **Hardware-based**: Assigned by the manufacturer
- **Persistent**: Remains the same across reboots
- **Used for**: Network identification and communication at the data link layer

## How to Change MAC Address Manually

### On Linux (using ifconfig)

1. **Check current MAC address:**
   ```bash
   ifconfig eth0
   # or
   ip link show eth0
   ```

2. **Bring the interface down:**
   ```bash
   sudo ifconfig eth0 down
   ```

3. **Change the MAC address:**
   ```bash
   sudo ifconfig eth0 hw ether 00:11:22:33:44:55
   ```

4. **Bring the interface back up:**
   ```bash
   sudo ifconfig eth0 up
   ```

5. **Verify the change:**
   ```bash
   ifconfig eth0
   ```

### On Linux (using ip command)

```bash
# Check current MAC
ip link show eth0

# Change MAC address
sudo ip link set dev eth0 down
sudo ip link set dev eth0 address 00:11:22:33:44:55
sudo ip link set dev eth0 up

# Verify
ip link show eth0
```

## How to Use This Tool

### Prerequisites

- Python 3.x
- Linux operating system
- `ifconfig` command available (part of `net-tools` package)

### Installation

1. Clone or download this repository
2. Make sure you have the required dependencies

If `ifconfig` is not available, install it:
```bash
sudo apt-get update
sudo apt-get install net-tools
```

### Usage

```bash
python3 main.py -i [interface] -m [new_mac_address]
```

### Parameters

- `-i` or `--interface`: Network interface to change (e.g., eth0, wlan0)
- `-m` or `--mac`: New MAC address in format XX:XX:XX:XX:XX:XX

### Examples

```bash
# Change eth0 MAC address
sudo python3 main.py -i eth0 -m 00:11:22:33:44:55

# Change wlan0 MAC address
sudo python3 main.py -i wlan0 -m aa:bb:cc:dd:ee:ff

# Show help
python3 main.py --help
```

### Example Output

```
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

MAC Address Changed to: 00:11:22:33:44:55 for interface eth0
[ + ] MAC address was successfully changed to: 00:11:22:33:44:55
```

## Important Notes

⚠️ **Warning**: This tool is for educational purposes only. Changing MAC addresses may:
- Violate terms of service of some networks
- Be illegal in some jurisdictions
- Affect network connectivity
- Require administrator/root privileges

### Requirements

- **Root privileges**: You need to run this tool with `sudo` or as root
- **Valid interface**: Make sure the interface exists and is active
- **Valid MAC format**: Use proper MAC address format (XX:XX:XX:XX:XX:XX)

### Troubleshooting

**Common issues:**

1. **Permission denied**:
   ```bash
   sudo python3 main.py -i eth0 -m 00:11:22:33:44:55
   ```

2. **Interface not found**:
   - Check available interfaces: `ifconfig -a` or `ip link show`
   - Make sure the interface name is correct

3. **Invalid MAC address**:
   - Use format: XX:XX:XX:XX:XX:XX
   - Each pair should be hexadecimal (0-9, A-F)

## Legal Disclaimer

This tool is provided for educational purposes only. The author is not responsible for any misuse or damage caused by this tool. Use at your own risk and ensure you comply with all applicable laws and regulations in your jurisdiction.

## Author

**Created by:** cat0x01
**GitHub:** [https://github.com/cat0x01](https://github.com/cat0x01)