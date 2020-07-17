import socket


from getmac import get_mac_address as gma

# functions for getting ip address
def ip_and_hostname():
    
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    print("Your hostname is ",host_name)
    print("Your ip Address is ",ip)
ip_and_hostname()

# functions for getting mac address
def mac_address():
    print("\nYour Mac Adress is ",gma().upper())
mac_address()


#
