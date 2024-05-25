import struct

def Hash_Function(Key):
    return Key%10

def Create_File():
    ef = open("Employee.dat","wb")
    format = 'i20sf'
    size = struct.calcsize(format)
    for i in range(10):
        ef.write(struct.pack(format,-1,b'                    ',0.0))
    print("File Successfully created")
    ef.close()

def DisplayAllRecords():
    Format = 'i20sf'
    size = struct.calcsize(Format)
    ef = open("Employee.dat","rb")
    for i in range(10):
        Record = ef.read(size)
        ID,Name,Salary = struct.unpack(Format,Record)
        print("Employee ID : ",ID)
        print("Employee Name : ",Name.decode().strip())
        print("Employee Salary : ",Salary)
    ef.close()

def AddRec():
    EmployeeID = int(input("Enter Employee ID : "))
    EmployeeName = input("Enter Employee Name : ")
    EmployeeSalary = float(input("Enter Employee Salary : "))

    format = 'i20sf'
    size =struct.calcsize(format)

    HashKey = Hash_Function(EmployeeID)

    try:
        ef = open("Employee.dat","r+b")
    except:
        Create_File()
        ef = open("Employee.dat","r+b")

    ef.seek(HashKey*size)
    Record = ef.read(size)
    Id,Name,Salary = struct.unpack(format,Record)
    if Id == EmployeeID:
        print("Record already exists")
    elif Id == -1:
        ef.seek(HashKey*size)
        ef.write(struct.pack(format,EmployeeID,EmployeeName.encode(),EmployeeSalary))
    else:
        while Id != -1:
            Record = ef.read(size)
            Id,Name,Salary = struct.unpack(format,Record)
            if  ef.tell() == size *10:
                ef.seek(0)

        ef.seek(ef.tell()-size)
        ef.write(struct.pack(format,EmployeeID,EmployeeName.encode(),EmployeeSalary))
    ef.close()

def SearchRecord():
    SearchID = int(input("Enter Employee ID to search : "))
    HashKey = Hash_Function(SearchID)
    Format = 'i20sf'
    size = struct.calcsize(Format)
    ef = open("Employee.dat","rb")
    ef.seek(HashKey*size)
    Record = ef.read(size)
    ID,Name,Salary = struct.unpack(Format,Record)
    if ID == SearchID:
        print("Employee ID : ",ID)
        print("Employee Name : ",Name.decode().strip())
        print("Employee Salary : ",Salary)
    elif ID != SearchID:
        count = 0
        while ID != SearchID:
            Record = ef.read(size)
            ID,Name,Salary = struct.unpack(Format,Record)
            count += 1

            if count == 10:
                print("Record does not exist")
                break

            if ef.tell() == 10*size:
                ef.seek(0)
        if ID == SearchID:
            print("Employee ID : ",ID)
            print("Employee Name : ",Name.decode().strip())
            print("Employee Salary : ",Salary)

    ef.close()

def UpdateRecord():
    UpdateID = int(input("Enter Employee ID to search : "))
    HashKey = Hash_Function(UpdateID)
    Format = 'i20sf'
    size = struct.calcsize(Format)
    ef = open("Employee.dat","r+b")
    ef.seek(HashKey*size)
    Record = ef.read(size)
    ID,Name,Salary = struct.unpack(Format,Record)
    if ID == UpdateID:
        print("Employee ID : ", ID)
        print("Employee Name : ", Name.decode().strip())
        print("Employee Salary : ", Salary)
        NewEmployeeName = input("Enter New Employee Name or leave blank to use previous Name : ")
        if NewEmployeeName == "":
            NewEmployeeName = Name.decode()
        NewEmployeeSalary = input("Enter New Employee Salary or leave blank to use previous Salary : ")
        if NewEmployeeSalary == "":
            NewEmployeeSalary = Salary
        ef.seek(HashKey*size)
        ef.write(struct.pack(Format,ID,NewEmployeeName.encode(),float(NewEmployeeSalary)))
        print("Record Updated Successfully")
    else:
        count = 0
        while ID != UpdateID:
            Record =ef.read(size)
            ID,Name,Salary = struct.unpack(format,Record)
            count += 1

            if count == 10:
                print("Record does not exist")
                break

            if ef.tell() == 10*size:
                ef.seek(0)
        if ID == UpdateID:
            print("Employee ID : ", ID)
            print("Employee Name : ", Name.decode().strip())
            print("Employee Salary : ", Salary)
            NewEmployeeName = input("Enter New Employee Name or leave blank to use previous Name : ")
            if NewEmployeeName == "":
                NewEmployeeName = Name
            NewEmployeeSalary = input("Enter New Employee Salary or leave blank to use previous Salary : ")
            if NewEmployeeSalary == "":
                NewEmployeeSalary = Salary
        ef.seek(ef.tell()-size)
        ef.write(struct.pack(Format,ID,NewEmployeeName.encode(),float(NewEmployeeSalary)))
        print("Record Updated Successfully")

    ef.close()

def DeleteRecord():
    DeleteID = int(input("Enter Employee ID to search : "))
    HashKey = Hash_Function(DeleteID)
    Format = 'i20sf'
    size = struct.calcsize(Format)
    ef = open("Employee.dat","r+b")
    ef.seek(HashKey*size)
    Record = ef.read(size)
    ID,Name,Salary = struct.unpack(Format,Record)
    if ID == DeleteID:
        print("Employee ID : ", ID)
        print("Employee Name : ", Name.decode().strip())
        print("Employee Salary : ", Salary)
        choice = input("Do You want to delete Record? Press Y for Yes and N for No")
        if choice == "Y":
            ef.seek(HashKey*size)
            ef.write(struct.pack(Format,0,b'',0.0))
            print("Record Deleted Successfully")
    else:
        count = 0
        while ID != DeleteID:
            Record =ef.read(size)
            ID,Name,Salary = struct.unpack(format,Record)
            count += 1

            if count == 10:
                print("Record does not exist")
                break

            if ef.tell() == 10*size:
                ef.seek(0)
        if ID == DeleteID:
            print("Employee ID : ", ID)
            print("Employee Name : ", Name.decode().strip())
            print("Employee Salary : ", Salary)
            choice = input("Do You want to delete Record? Press Y for Yes and N for No")
            if choice == "Y":
                ef.seek(ef.tell()-size)
                ef.write(struct.pack(Format,0,b'',0.0))
                print("Record Deleted Successfully")

    ef.close()

choice = 0
while choice != 7:
    print("1 : Create file")
    print("2 : Display All Records")
    print("3 : Add Record")
    print("4 : Search Record")
    print("5 : Update Record")
    print("6 : Delete Record")
    print("7 : Exit Program")
    choice = int(input("Enter you choice : "))
    if choice == 1:
        Create_File()
    elif choice == 2:
        DisplayAllRecords()
    elif choice == 3:
        AddRec()
    elif choice == 4:
        SearchRecord()
    elif choice == 5:
        UpdateRecord()
    elif choice == 6:
        DeleteRecord()
    elif choice == 7:
        print("Exitting...")
    else:
        print("Invalid choice")




