import socket
import platform
import psutil
import netifaces
 
# Function to get the default gateway
def get_default_gateway():
    gateways = netifaces.gateways()
    default_gateway = gateways.get('default', {}).get(netifaces.AF_INET, [None])[0]
    return default_gateway
 
# System Information
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
system_info = platform.uname()
 
print("Your Computer Name is:", hostname)
print("Your Computer IP Address is:", IPAddr)
 
# Get and print the default gateway
default_gateway = get_default_gateway()
print("Your Default Gateway is:", default_gateway)