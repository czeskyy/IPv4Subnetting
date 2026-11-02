from classes.IPv4 import IPv4
def main():
    ip=IPv4("192.168.0.1","255.255.255.0")
    ip.show_addr_and_mask()


if __name__=="__main__":
    main()

