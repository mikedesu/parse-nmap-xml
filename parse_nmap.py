import sys
import xml.etree.ElementTree as ET


def usage():
    print("python3 parse_nmap.py <filename.xml>")


def print_list(l):
    for o in l:
        print(o)


# grok-2-latest refactor: 2/28/2025
def make_urls(a, h, p):
    for x in a + h:
        for y in p:
            z = f'http{"s"if y=="443"else""}://{x}{":"+y if y not in["80","443"]else""}'
            print(z)
            if y not in ["80", "443"]:
                print(z.replace("http", "https"))


def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(-1)

    # grok-2-latest refactor: 2/28/2025
    f = sys.argv[1]
    r = ET.parse(f).getroot()
    for c in r:
        if c.tag == "host":
            a = [s.attrib["addr"] for s in c if s.tag == "address"]
            h = [
                x.attrib["name"]
                for s in c
                if s.tag == "hostnames"
                for x in s
                if x.tag == "hostname"
            ]
            p = [
                x.attrib["portid"]
                for s in c
                if s.tag == "ports"
                for x in s
                if x.tag == "port"
                and any(y.tag == "state" and y.attrib["state"] == "open" for y in x)
            ]
            make_urls(a, h, p)


if __name__ == "__main__":
    main()
