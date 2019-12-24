print("Enter 1 to add data.")
print("Enter 2 to update .")
print("Enter 3 to delete.")
print("Enter 4 to show complete data.")
print("Enter 5 to search data.")

inp=int(input("your input is : "))


    
def add():
    n=int(input("how many entries do u want to make : "))
    for i in range(n):
        roll=input("Enter the roll no : ")
        name=input("Enter he name : ")
        add=input("Enter the address : ")


        f1=open("file1.log","a") #opening the file
                                            #and apending data instead of write the data

        f1.write(roll)
        f1.write(":")
        f1.write(name)
        f1.write(";")
        f1.write(add)
        f1.write(".")
   
    f1.close()

 

def showall():
    f2=open("file1.log","r")
    s=f2.read()
    s=s.replace(":","\t")
    s=s.replace(";","\t")
    s=s.replace(".","\n")
    print(s)


def search():
    with open("file1.log", "r") as my_file:
        for line in my_file:
            string = line.split(".")
            for line in string:
                #print(line)
                string=line.split(";")
                print(string)
        
    

if(inp == 1):
    add()
if(inp==2):
    #print("this part of the code has ben reached")
    showall()
if(inp==5):
    search()
    
