# Serial Text Filing
class stRec:
    def __init__(self):
        self.stName = None
        self.stClass = None
        self.stFee = None
TempArr = [stRec() for i in range(10)]
Temp2Arr = [stRec() for i in range(10)]
def AddFieldwise():
    sf = open("StudentFile.txt","wt")
    Name = input("Enter Student Name to write in File or leave Blank to end")
    while Name != "":
        Class = input("Enter Class to write in File")
        Fee = str(input("Enter fee to write in File"))

        sf.write(Name + "\n")
        sf.write(Class + "\n")
        sf.write(Fee + "\n")

        Name = input("Enter name to write in File or Leave blank to end")

    sf.close()

def DisplayFieldWise():
    try:
        sf = open("StudentFile.txt","rt")
        NameRead = sf.readline()
        while NameRead != "":
            ClassRead = sf.readline()
            FeeRead = sf.readline()

            print("Name : ",NameRead,end="")
            print("Class : ",ClassRead,end="")
            print("Fee : ",FeeRead)
            NameRead = sf.readline()
        sf.close()
    except:
        print("File Doesn't exist")

def SearchFieldWise():
    Found = False
    SearchName = input("Enter Name to Search")
    try:
        sf = open("StudentFile.txt","rt")
        NameRead = sf.readline()
        while NameRead != "":
            ClassRead = sf.readline()
            FeeRead = sf.readline()

            if SearchName == NameRead.strip():
                Found = True
                print("Name : ",NameRead,end="")
                print("Class : ",ClassRead,end="")
                print("Fee : ",FeeRead)
            NameRead = sf.readline()
        sf.close()
        if not Found:
            print(SearchName," is not found")
    except:
        print("file not found")

def DeleteFieldWise():
    Found = False
    DeleteName = input("Enter Name of the Student to delete")
    count = 0
    try:
        sf = open("StudentFile.txt","rt")
        NameRead = sf.readline()
        while NameRead != "":
            ClassRead = sf.readline()
            FeeRead = sf.readline()

            if DeleteName != NameRead.strip():
                TempArr[count].stName = NameRead.strip()
                TempArr[count].stClass = ClassRead.strip()
                TempArr[count].stFee = FeeRead.strip()
            else:
                Found = True
            NameRead = sf.readline()
            count += 1
        sf.close()
        if not Found:
            print("Name not Found")
        sf = open("StudentFile.txt","wt")
        count = 0
        while TempArr[count].stName != None:
            sf.write(TempArr[count].stName + "\n")
            sf.write(TempArr[count].stClass + "\n")
            sf.write(TempArr[count].stFee + "\n")
            count += 1
        sf.close()
    except:
        print("File Doent Exist")

def EditFieldWise():
     Found = False
     count = 0
     EditName = input("Enter Name of the Student to edit")
     try:
        sf = open("StudentFile.txt","rt")
        NameRead = sf.readline()
        while NameRead != "":
            ClassRead = sf.readline()
            FeeRead = sf.readline()

            if EditName != NameRead.strip():
                Temp2Arr[count].stName = NameRead.strip()
                Temp2Arr[count].stClass = ClassRead.strip()
                Temp2Arr[count].stFee = FeeRead.strip()
            elif EditName == NameRead.strip():
                Found = True
                NewName = input("Enter new name or leave blank to use previous name")
                if NewName == "":
                    NewName = NameRead.strip()
                NewClass = input("Enter new class or leave blank to use Previous class")
                if NewClass == "":
                    NewClass = ClassRead.strip()
                NewFee = input("Enter new Fee or leave blank to use Previous Fee")
                if NewFee == "":
                    NewFee = FeeRead.strip()
                Temp2Arr[count].stName = NewName
                Temp2Arr[count].stClass = NewClass
                Temp2Arr[count].stFee = NewFee
            NameRead = sf.readline()
            count += 1
        sf.close()
        if not Found:
            print("Name doesn't exit")
        sf = open("StudentFile.txt","wt")
        count = 0
        while Temp2Arr[count].stName != None:
            sf.write(Temp2Arr[count].stName + "\n")
            sf.write(Temp2Arr[count].stClass + "\n")
            sf.write(Temp2Arr[count].stFee + "\n")
            count += 1
        sf.close()
     except:
         print("File doesn't exit")
print(TempArr[0].stName)
choice = 0
while choice != 6:
    print("1 : Add Field wise Record")
    print("2 : Display Record")
    print("3 : Search Record")
    print("4 : Delete Record")
    print("5 : Edit Record")
    print("6 : Exit")
    choice = int(input("Enter Your Choice"))
    if choice == 1:
        AddFieldwise()
    elif choice == 2:
        DisplayFieldWise()
    elif choice == 3:
        SearchFieldWise()
    elif choice == 4:
        DeleteFieldWise()
    elif choice == 5:
        EditFieldWise()
    elif choice == 6:
        print("Exitting....")
    else:
        print("invalid choice")
