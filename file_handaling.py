import os

path = "C:/heet/text"
print("1. For Read")
print("2. For Write")
print("3. For Create")
print("4. For Remove")
print("5. For Append")


choice =  input("Enter Your Choice:")


if choice == '1':
    if os.path.exists(path):
        f1 = open(path,'r')
        print(f1.read())
    else:
        print("File does not exist....")

elif choice == '2':
    if os.path.exists(path):
        f1 = open(path,'w')
        f1.write("Hello this is file handaling.....")    
        print("File has been written.....")    
    else:
        print("File does not exist....")
        
elif choice == '3':
        if os.path.exists(path):
            print("File already exist.....")
        else:
            f1 = open(path,'x')
            print("File is created....")
    
elif choice == '4':
    if os.path.exists(path):
        os.remove(path)
        print('File removed....')
    else:
         print("File does not exist....")   
elif choice == '5':
        if os.path.exists(path):
             f1 = open(path,'a')
             f1.write("My Name Is Heet...")
             print("File Apeended....")
        else:
            print("File does not exist....")

else:
    print('Invalid input....') 