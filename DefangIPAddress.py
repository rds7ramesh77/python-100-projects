#python program for Defang IP Address
#To convert an IP address to a defang IP address, we need to replace "." with "[.]".

def ip_address(address):
    newAddress=""
    splitAddress=address.split(".")
    separator="[.]"
    
    newAddress=separator.join(splitAddress)
    return newAddress

ipaddress=ip_address("192.10.10.3")
print(ipaddress)