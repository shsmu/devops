#!/usr/bin/env python
import xmlrpclib

def add_system(url, username, password, system):
    remote = xmlrpclib.Server(url)
    token = remote.login(username, password)
    system = system
    system_id = remote.new_system(token)
    remote.modify_system(system_id, "name", system['name'], token)
    remote.modify_system(system_id, "hostname", system['hostname'], token)
    remote.modify_system(system_id, "profile", system['profile'], token)
    remote.modify_system(system_id, "name_servers_search", system['name_servers_search'], token)
    remote.modify_system(system_id, "name_servers",system['name_servers'], token)
    remote.modify_system(system_id, "gateway", system['gateway'], token)
    remote.modify_system(system_id, "kernel_options", system['kernel_options'], token)
    remote.modify_system(system_id, "kickstart", system['kickstart'], token)
    remote.modify_system(system_id, "modify_interface", system['modify_interface'], token)
    remote.save_system(system_id, token)
    ret = remote.sync(token)
    print ret


if __name__ == '__main__':
    url = "http://192.168.1.254/cobbler_api"
    username = "cobbler"
    password = "cobbler"
    system = {}
    for i in range(10,12):
        system[i]={"name":"CKA-" + str(i) + ".sanyu.com",
              "hostname":"CKA-" + str(i) + ".sanyu.com",
              "profile":"CentOS-7-x86_64-Minimal-1804",
              "name_servers_search":"sanyu.com",
              "name_servers":"192.168.1.254",
              "gateway":"192.168.1.254",
              "kernel_options":"biosdevname=0 net.ifnames=0",
              "kickstart":"/var/lib/cobbler/kickstarts/cka.ks",
              "modify_interface":{
                 "macaddress-eth0"   : "00:00:00:00:00:" + str(i),
                 "ipaddress-eth0"    : "192.168.1." + str(i),
                 "Gateway-eth0"      : "192.168.1.254",
                 "subnet-eth0"       : "255.255.255.0",
                 "static-eth0"       : 1,
                 "dnsname-eth0"      : "CKA-" + str(i) + ".sanyu.com"
                }
              }
    for k in system:
        add_system(url=url, username=username, password=password, system=system[k])
