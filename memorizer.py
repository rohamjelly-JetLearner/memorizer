from tkinter import *

root=Tk()
root.geometry('500x500')
frame=Frame(root)
frame.pack(side=TOP,pady=20)
add_f=Frame(root)
add_f.place(x=300,y=250)
list_f=Frame(root)
list_f.pack(side=LEFT,padx=30,pady=67)
open=Button(frame,text='OPEN',command=None)
delete=Button(frame,text='DELETE',command=None)
save=Button(frame,text='SAVE',command=None)
open.pack(side=LEFT,padx=35)
delete.pack(side=LEFT,padx=35)
save.pack(side=LEFT,padx=35)
add_e=Entry(add_f)
add=Button(add_f,text='ADD',command=None)
add_e.pack(side=TOP,pady=50)
add.pack(side=TOP,pady=50)
listbox=Listbox(list_f,bg='red')
scrollbar=Scrollbar(list_f,orient='vertical')
listbox.pack(side=LEFT)
scrollbar.pack(side=LEFT,fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for i in range(100):
    listbox.insert(END,'hello'+str(i))





root.mainloop()