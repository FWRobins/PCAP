class Scanner:
    def scan(self):
        print("Scanning from Scanner")

class Printer:
    def printing(self):
        print("Printing from printer")

class Fax:
    def send(self):
        print("sending from Fax")
    def printing(self):
        print("printing from Fax")

class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

spf = MFD_SPF()
spf.scan()
spf.printing()
spf.send()
print(" ")
sfp = MFD_SFP()
sfp.scan()
sfp.printing()
sfp.send()
