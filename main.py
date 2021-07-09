from tkinter import *;
from src import templates as t;

tlist = []
for i in t.getTemplates():
    tlist += [i.replace('.pdf','')]

class Checkbar(Frame):
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

    tbar = Checkbar(root, tlist)
    tbar.config(relief=GROOVE, bd=2)
    tbarlbl = Label(root,text='Select Template',justify=LEFT)


    # Grid Layout
    tbarlbl.grid(row=0,column=0,sticky = W)
    tbar.grid(row=1,column=0)


    root.mainloop()

if __name__ == '__main__':
    main()



    



