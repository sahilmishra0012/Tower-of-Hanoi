import  tkinter

class rectangle():
    def __init__(self,name):
        c=tkinter.Canvas(name)
        c.create_rectangle(50,0,100,50,fill='red')
        c.pack()
        

def main():
    m=tkinter.Tk()
    rectangle(m)
    m.mainloop()

if __name__=='__main__':
    main()