import tkinter
import usb

class GUIWindow:

    def __init__(self):
        self.root = tkinter.Tk()

        self.frameBG = tkinter.Frame(self.root, bg="red", relief=tkinter.SUNKEN)

        tkinter.Label(self.frameBG, text="Product ID: ").grid(row=0, column=0, sticky=tkinter.W)
        tkinter.Label(self.frameBG, text="Vendor ID: ").grid(row=1, column=0, sticky=tkinter.W)
        tkinter.Label(self.frameBG, text="Incoming Data").grid(row=4, column=0, sticky=tkinter.W)
        tkinter.Label(self.frameBG, text="Outgoing Data").grid(row=8, column=0, sticky=tkinter.W)

        tkinter.Button(self.frameBG, text="Send", command=self.sendPacket).grid(row=9, column=0)
        tkinter.Button(self.frameBG, text="Read", command=self.readPacket).grid(row=5, column=0)
        tkinter.Button(self.frameBG, text="Link", command=self.linkDevice).grid(row=0, column=3)
        tkinter.Button(self.frameBG, text="Device Info", command=self.devInfo).grid(row=2, column=3)

        self.textStatus = tkinter.Text(self.frameBG, height=1, width=20).grid(row=1, column=3)
        self.textVendor = tkinter.Text(self.frameBG, height=1, width=20).grid(row=0, column=1)
        self.textProduct = tkinter.Text(self.frameBG, height=1, width=20).grid(row=1, column=1)
        self.textRead = tkinter.Text(self.frameBG, height=3, width=35).grid(row=4, column=1, rowspan=3, columnspan=3)
        self.textWrite= tkinter.Text(self.frameBG, height=3, width=35).grid(row=8, column=1, rowspan=3, columnspan=3)

        self.frameBG.pack()
        self.root.mainloop()

    def sendPacket(self):
        print ("Sending packet")
        if self.dev is None:
            raise ValueError("Device not found")

    def readPacket(self):
        print ("Reading packet")
        if self.dev is None:
            raise ValueError("Device not found")

    def linkDevice(self):
        print ("Linking device")
        vendor = int(self.textVendor.get(INDEX1="0.0", INDEX2=tkinter.END), 16)
        product = int(self.textProduct.get(INDEX1="0.0", INDEX2=tkinter.END), 16)
        self.dev = usb.core.find(idVendor=vendor, idProduct=product)
        if self.dev is None:
            raise ValueError("Device not found")

    def devInfo(self):
        print ("Reporting Device Info")
        if self.dev is None:
            raise ValueError("Device not found")
        self.textRead.delete(INDEX1="0.0", INDEX2=tkinter.END)

        manu = self.dev.iManufacturer
        prod = self.dev.iProduct
        ser = slef.dev.iSerialNumber

        self.textRead.insert(index=tkinter.END, chars="Manufacturer: %s  ; Product: %s  ; Serial: %s" % (manu, prod, ser))




#============= Main Run ===============
