import re
class IPv4:
    def __init__(self,addr:str,mask:str):
        self.addr=self.validate_format(addr)
        self.mask=self.validate_format(mask)

    def validate_format(self,value:str) -> list[int]:
        if not isinstance(value,str):raise TypeError
        # check the format with a regex (xxx.xxx.xxx.xxx) where x is any digit
        pattern=re.compile(r"^(\d{1,3}\.){3}\d{1,3}$") # ipv4 regex pattern
        if not pattern.match(value):
            raise ValueError
        # check if values are in 0,255 range and assing it to a 4 index table
        if(all(0<= int(part) <=255 for part in value.split("."))):
            return [int(part) for part in value.split(".")]
        else: raise ValueError
    def show_addr_and_mask(self):
        print(f"address: {self.addr}")
        print(f"mask {self.mask}")

    def ipToNumber(ipv4:list[int]):
        pass
    

