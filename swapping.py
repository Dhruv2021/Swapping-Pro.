def swapping ():
    file1=input("Enter File 1 Name= ")
    file2=input("Enter File 2 Name= ")
    with open(file1,"r") as data1:
        a=data1.read()

    with open(file2,"r") as data2:
        b=data2.read()
    
    with open(file1,"w") as data1:
        data1.write(b)

    with open(file2,"w") as data2:
        data2.write(a)

swapping()
      