import re
from functools import reduce
class IPv4:
    def __init__(self,addr:str):
        self.addr,self.mask=self.validate(addr)

    def validate(self,value:str) -> (list[int],list[int]):
        if not isinstance(value,str): # checks if value is string
            raise TypeError("IP must be a string.")
        pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$") # ipv4 pattern: aaa.aaa.aaa.aaa/aa where a is a number
        if not pattern.fullmatch(value): #check the regex
            raise ValueError("Invalid IP format.")
        address,cidr=value.split("/")
        cidr=int(cidr) # converting to int has to be done for later use, regex checks if its a number already

        parts=[int(part) for part in address.split(".")] # if all correct, splits the value in 4 parts
        if not all(0<=part<=255 for part in parts): # checks if all 4 parts are between 0 and 255
            raise ValueError("IP octects must be between 0 and 255.")
        if not 0<cidr<32:
            raise ValueError("Mask must be between 0 and 32.")

        mask = self.cidr_to_mask(cidr)
        return parts,mask
    

    def cidr_to_mask(self,cidr): # takes a value between 0-32 and returns a table of size 4 with a valid ipv4 mask
        bits = '1'*cidr+'0'*(32-cidr) # string of 1's followed by 0's with size 32
        return [int(bits[i:i+8],2) for i in range (0,32,8)] # converting to a table [x,x,x,x]
    
    def octets_to_int(self,octets): # takes 4 octects in a table and returns it in bits as a string
        return reduce(lambda x,y: x|y,[x<<i*8 for i,x in enumerate(octets)])


    def show_info(self):
        informations = [ # holds strings with rows of info
                f"IP Address: {".".join(str(i) for i in self.addr)}",
                f"Mask: {".".join(str(i) for i in self.mask)}",
                f"IP Address in bits: {self.octets_to_int(self.addr)}",
                f"Mask in bits: {self.octets_to_int(self.mask)}"
               ] 
        width=max(len(i) for i in informations) # calculates max width of all rows
        
        # prints the info in an ASCII border
        print("+" + "-" * (width+2) + "+")
        for row in informations:
            print("| " + row.ljust(width)+" |")
        print("+" + "-" * (width+2) + "+")


    def ipToNumber(ipv4:list[int]):
            pass
        

