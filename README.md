# Network Scanner App
==========================

### Description
This application is a simple network scanner developed in Python using the nmap library. The application allows you to identify devices connected to a network.

### Features
**Base IP Input:**
* The user inputs a base IP address along with its range (for example, 192.168.1.0/24), which allows scanning all devices within that subnet.

**Ping Scan:**
The application uses the -sn command from Nmap to perform a ping scan. This type of scan detects which devices are active on the network without performing a deep port scan.

**Connected Device Identification:**
After completing the scan, the code displays a list of all active hosts, including their IP addresses and, if available, the hostname of each device.

**Active Device Counter:**
The code counts and displays the total number of connected devices detected on the network.

**Informative Messages:**
A message is shown indicating whether no devices were found on the network.

### Requirements
Python 3.6+
Nmap: You must have Nmap installed on your operating system. You can download it from here: https://nmap.org/

### Python Libraries:
python-nmap: To interact with Nmap from Python.

### Contributions
If you want to contribute to the project, please fork the repository and send your pull requests. All suggestions are welcome.

License
This project is licensed under the MIT License. See the LICENSE file for more details.