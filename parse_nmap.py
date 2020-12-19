import sys
import xml.etree.ElementTree as ET

def usage():
    print("python3 parse_nmap.py <filename.xml>")

def print_list(l):
    for o in l:
        print(o)

def make_urls(addresses, hostnames, ports):
    for addr in addresses:
        for port in ports:
            if port=="80":
                print("http://" + addr)
            elif port=="443":
                print("https://" + addr)
            else:
                print("https://" + addr + ":" + port)
    for hostname in hostnames:
        for port in ports:
            if port=="80":
                print("http://" + hostname)
            elif port=="443":
                print("https://" + hostname)
            else:
                print("http://" + hostname + ":" + port)
                print("https://" + hostname + ":" + port)

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(-1)
    filename = sys.argv[1]
    tree = ET.parse(filename)
    root = tree.getroot()
    
    for child in root:
        if child.tag == "host":
            addresses = []
            hostnames = []
            ports = []
            for subchild in child:
                if subchild.tag == "address":
                    addr = subchild.attrib['addr']
                    addresses.append(addr)
                if subchild.tag == "hostnames":
                    for subsubchild in subchild:
                        if subsubchild.tag == "hostname":
                            hostname = subsubchild.attrib['name']
                            hostnames.append(hostname)
                if subchild.tag == "ports":
                    for subsubchild in subchild:
                        if subsubchild.tag == "port":
                            for subsubsubchild in subsubchild:
                                if subsubsubchild.tag == "state":
                                    if subsubsubchild.attrib['state'] == "open":
                                        portid = subsubchild.attrib['portid']
                                        ports.append(portid)
                

            #print_list(addresses)
            #print_list(hostnames)
            #print_list(ports)
            make_urls(addresses, hostnames, ports)
                #for port in ports:
                    #if port == "80":
                    #    print("http://" + addr)
                    #elif port == "443":
                    #    print("https://" + addr)
                    #else:
                    #    print("https://" + addr + ":" + port)
            #for hostname in hostnames:
            #    for port in ports:
            #        if port == "80":
            #            print("http://" + hostname)
            #        elif port == "443":
            #            print("https://" + hostname)
            #        else:
            #            print("https://" + hostname + ":" + port)

if __name__=='__main__':
    main()

