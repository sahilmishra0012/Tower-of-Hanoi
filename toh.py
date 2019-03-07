
def toh(a,fro,to,aux):
    if(a==1):
        print("Move disk 1 from peg ",fro," to peg ",to)
        return
    toh(a-1,fro,aux,to)
    print("Move disk 1 from peg ",fro," to peg ",to)
    toh(a-1,aux,to,fro)

def main():
	x=int(input("Enter number of disks"))
	toh(x,'A','B','C')

if __name__=='__main__':
    main()
