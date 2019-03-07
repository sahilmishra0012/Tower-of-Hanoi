import  tkinter

class rectangle():
    def __init__(self,name,w,x,y,z,color):
        
        name.create_rectangle(w,x,y,z,fill=color)#20,10,10,500,fill='grey'
        name.pack()
        

def main():
    m=tkinter.Tk()
    c=tkinter.Canvas(m)
    stick1=rectangle(c,50,10,40,200,'grey')
    stick2=rectangle(c,150,10,140,200,'grey')
    stick3=rectangle(c,250,10,240,200,'grey')
    rectangle(c,80,200,10,190,'red')
    rectangle(c,70,190,20,180,'red')
    rectangle(c,60,180,30,170,'red')
    m.mainloop()

if __name__=='__main__':
    main()