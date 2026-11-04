import re
class IPv4:
    def __init__(self,addr:str,mask:str):
        self.addr=self.validate_ip(addr)
        self.mask=self.validate_mask(mask)

    def validate_ip(self,value:str) -> list[int]:
        if not isinstance(value,str): # checks if value is string
            raise TypeError("IP must be a string.")
        pattern = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$") # ipv4 pattern: aaa.aaa.aaa.aaa where a is a number
        if not pattern.fullmatch(value): #check the regex
            raise ValueError("Invalid IP format.")

        parts= [int(part) for part in value.split(".")] # if all correct, splits the value in 4 parts
        if not all(0<=part<=255 for part in parts): # checks if all 4 parts are between 0 and 255
            raise ValueError("IP octects must be between 0 and 255.")
        return parts
    

    def validate_mask(self,value:str)->list[int]:
        parts = self.validate_ip(value) # uses the validate_ip to get verified array of numbers

        binary_mask = ''.join(f'{part:08b}' for part in parts) # 08b means 0 filler 8 characters and 2 b is binary

        if '01' in binary_mask: # 1's in the mask must be continous.
            raise ValueError("Invalid subnet mask.")

        return parts

    def show_addr_and_mask(self):
        print(f"address: {self.addr}")
        print(f"mask {self.mask}")

    def ipToNumber(ipv4:list[int]):
            pass
        

