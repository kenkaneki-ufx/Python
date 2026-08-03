import os
n = input("[ 1. Create a new FILE\t\t\t  ]\n[ 2. copy FILE f1 Code to another FILE f2 ]\n[ 3. delete FILE\t\t\t  ]\n")
if n=='1':
    file = input('Enter file name: ')  
    try:
        with open(f'Python/{file}',"r") as f:
            print("Filename already exists")
    except FileNotFoundError:              
        with open(f'Python/{file}','w') as f:
            print(f"{file} file is created..")
    
elif n=='2':
    file1 = input('Enter file that copy from: ')
    file2 = input('Enter file that copy to: ')
    with open(f'Python/{file1}',"r") as f1:
        data = f1.read()           # [ copy file f1 Code to another file f2 ]
    with open(f'Python/{file2}',"w") as f2:
        f2.write(data)
    # os.remove(file1)

elif n=='3':
    file = input('Enter file to delete: ')     # [ delete file ]
    try:
        os.remove(f'Python/{file}')
        print(f"{file} file is deleted")
    except FileNotFoundError:
        print("File doesn't exist")

else:
    print("Enter valid choice: ")