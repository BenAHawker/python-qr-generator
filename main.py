from tkinter import *;
from tkinter import ttk
from src import templates as t;
from src import gencode as c;

tlist = []
for i in t.getTemplates():
    tlist += [i.replace('.pdf','')]

class TemplateBar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)

def getSelected(tbar):
    value = list(tbar.state())
    res = dict(zip(tlist, value))
    return res

def main():
    root = Tk()
    root.title('QR Generator')
    root.iconphoto(False,PhotoImage(file="./assets/img/icon.png"))
    root.config(padx=10,pady=10)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(0,weight=3)

    separator = ttk.Separator(root,orient=HORIZONTAL)
    

    # code_xbm = c.createQR()
    # code_bmp = BitmapImage(data=code_xbm)
    # code_bmp.config(foreground="black")
    # code_bmp.config(background="white")
    # label = Label(image=code_bmp)


    tbar = TemplateBar(root, tlist)
    tbar.config(relief=GROOVE, bd=2)
    tbarlbl = Label(root,text='Select Template',justify=LEFT)


    # Grid Layout
    separator.grid(row=0,column=0,sticky=EW)
    tbarlbl.grid(row=1,column=0,sticky = W)
    tbar.grid(row=2,column=0)
    
    # label.grid(row=2,column=0)

    root.mainloop()

if __name__ == '__main__':
    main()



    



