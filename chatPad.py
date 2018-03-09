import usb

vendor = 0x045E
product = 0x028E

dataSize = 12
timeOut = 1000

dev = usb.core.find(idVendor=vendor, idProduct=product)

if dev is None:
    raise ValueError('butts.')
