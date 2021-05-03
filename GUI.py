from tkinter import *
from program import *

root =Tk()
root.title("Name Picker")
root.iconbitmap('icon.ico')
root.geometry()

active = 1
Radiobutton(root, text='yes', variable=active, value=1).grid(row=0,column=1)
Radiobutton(root, text='no', variable=active, value=0).grid(row=0,column=2)

label_active=Label(root, text ="would you like activity to be a fator?")
label_active.grid(row=0,column=0)

label_slots=Label(root, text ="how many slots left?")
label_slots.grid(row=1,column=0)

#entry_active = Entry(root,text=active)
#entry_active.grid(row=0,column=1)

entry_slots = Entry(root, width=10)
entry_slots.grid(row=1,column=1)


def rec_input(flag):
    #flag=int(entry_active.get())
    slot=int(entry_slots.get())

    name,date,time,active = imp_data()
    keys,Dict = make_dict(date,time,name)
    selected = instant_draw(flag,slot,keys,active)
    
    for i in range(len(selected)):
        print(Dict[selected[i]], end=' ')
        names=Label(root,text=Dict[selected[i]]).grid(row=3+i,column=0)
                
    
runbutton = Button(root, text="pick names", command=lambda:rec_input(active))
runbutton.grid(row=2,column=0)


root.mainloop()