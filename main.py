from classes.IPv4 import IPv4
def main():
    s = input("Podaj adres ip: ")
    ip=IPv4(s)
    ip.show_info()


if __name__=="__main__":
    main()

