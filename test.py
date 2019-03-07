import  tkinter

m=tkinter.Tk()

c=tkinter.Canvas(m)
rect=c.create_rectangle(50,0,100,50,fill='red')
c.pack()
m.mainloop()
