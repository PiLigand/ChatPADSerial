import tkinter

class GUIWindow:
    def __init__(self):
        self.root = tkinter.Tk()

        tkinter.Label(self.root, text="Product ID: ").grid(row=0, column=0, sticky=tkinter.W)
        tkinter.Label(self.root, text="Vendor ID: ").grid(row=1, column=0, sticky=tkinter.W)

        tkinter.Label(self.root, text="Incoming Data").grid(row=4, column=0, sticky=tkinter.W)
        tkinter.Label(self.root, text="Outgoing Data").grid(row=8, column=0, sticky=tkinter.W)


        self.root.mainloop()
