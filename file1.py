
import os

print("Enter 1 to add data.")
print("Enter 2 to update .")
print("Enter 3 to delete.")
print("Enter 4 to show complete data.")
print("Enter 5 to search data.")

inp=int(input("your input is : "))

def extra():
    if(inp==1):
        add()
    if(inp==2):
        update()
    
def add():
    
        f=open("file1.log","a") #opening the file
                                            #and apending data instead of write the data
        n=int(input("how many entries do u want to make : "))
        for i in range(n):
            roll=input("Enter the roll no : ")
            name=input("Enter he name : ")

            add=input("Enter the address : ")
            f=open("file1.log","a") #opening the file
                                            #and apending data instead of write the data
        
            f.write(roll)
            f.write(";")
            f.write(name)
            f.write(";")
            f.write(add)
            f.write(".")
        f.close()
        

 

def showall():
    f=open("file1.log","r")
    s=f.read()
    s=s.replace(";","\t")
    s=s.replace(";","\t")
    s=s.replace(".","\n")
    print(s)


def search():
    search=input("enter the number to be searched : ")
    flag=0

    with open("file1.log", "r") as my_file:
        for line in my_file:
            string = line.split(".")
            for line in string:
                string=line.split(";")
                
                for line in string:
                #print(line)
                    if(string[0]==search):
                        print("Number has been found")
                        flag=1
                        break
                    else:
                        flag=flag
        if(flag==0):
            print("file not found")
            
def update():
    f1=open("file1.log",'r')
    f2=open("file2.log",'w+')
    search=input("Enter the element to be searced : ")
    
    for line in f1:
        string = line.split(".")
        for line in string:
            string=line.split(";")
            if(string[0]==search):
                    name=input("Enter name : ")
                    address=input("enter adress:")
                    f2.write(search + ";")
                    f2.write(name+";")
                    f2.write(address+";")
            else:
                f2.write(line)
    f1.close()
    f2.close()
    os.remove("file1.log")
    os.rename(r'C:\Users\admin\Desktop\chir\file2.log',r'C:\Users\admin\Desktop\chir\file1.log')
        

def delete():
    delete=input("enter the number to be delete : ")
    
    f1=open("file2.log",'w+')
    with open("file1.log", "r",encoding='utf-8') as  f:
        for line in f:
            string = line.split(".")
            for line in string:
                string=line.split(";")
                #for line in string:
                #print(line)
                if(string[0] !=delete):
                    f1.write(line+'.')
                    #break
                        
    f1.close()
    os.remove("file1.log")
    os.rename(r'C:\Users\admin\Desktop\chir\file2.log',r'C:\Users\admin\Desktop\chir\file1.log')
    



            
if(inp == 1):
    add()
if(inp==4):
    #print("this part of the code has ben reached")
    showall()
if(inp==5):
        search()
if(inp==2):
        update()
if(inp==3):
    delete()
    

