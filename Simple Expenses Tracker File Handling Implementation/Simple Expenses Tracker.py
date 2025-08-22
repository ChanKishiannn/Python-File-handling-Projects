database = "Tacker Database.txt"

open(database, "a").close()

def add_Income():
    income = input("Add your income: ")
    with open(database, "a") as f:
        f.write(income + "\n")
    print(f"The {income} Income Added Successfully")

def view_Income():
    with open(database, "r") as f:
        income = f.readlines()
    if income:
        print("========== My Income ========")
        for i, incomeList in enumerate(income, start=1):
            print(f"{i}. {incomeList.strip()}")
    else:
        print("\n Invalid! The database is Empty")

def delete_Income():
    with open(database, "r") as f:
        income = f.readlines()

    deleteIncome = input("Enter the Income you want to Delete: ")

    new_income = [incomeList for incomeList in income if incomeList.strip() != deleteIncome]

    if len(new_income) != len(income):
        with open(database, "w") as f:
            f.writelines(new_income)
        print("The Income was successully Deleted!")
    else:
        print("The Income was not found! Invalid Deletion")

def edit_Income():
    with open(database, "r") as f:
        income = f.readlines()

    incomeToBeReplace = input("Enter the Income you want to Replace: ")
    new_Income = input("Enter the new Income: ")

    found = False
    for i in range (len(income)):
        if income[i].strip() == incomeToBeReplace:
            task[i] = new_Income + "\n "
            found = true
            break

    if found:
        with open(database, "w") as f:
            f.writelines(income)
        print("Successfully Edit the new income: ")
    else:
        print("No similar income found! ")
    
userChoose = 0
while userChoose != 5:
    print("\n[1] Add Income")
    print("[2] Delete Income")
    print("[3] Edit Income")
    print("[4] View Income")
    print("[5] Exit")

    try:
        userChoose = int(input("Please Choose from the option: "))
    except errorMessage:
        print("Invalid Input! Please Try Again: ")
        continue

    if useChoose == 1:
        add_Income()
    elif useChoose == 2:
        delete_Income()
    elif useChoose == 3:
        edit_Income()
    elif useChoose == 4:
        view_Income()
    elif useChoose == 5:
        print("Exiting program! Thank youuu and Goodbye....")
    else:
        print("Invalid Input! PLease Try Again")
        
