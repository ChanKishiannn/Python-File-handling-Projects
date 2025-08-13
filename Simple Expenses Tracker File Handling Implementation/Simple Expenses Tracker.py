database = "Tacker Database.txt"

open(database, "a").close()

def add_Income():
    income = input("Add your income: ")
    with open(database, "a") as f:
        f.write(income + "\n")
    print(f"The {income} Income Added Successfully")

def view_Income():
    with open(database, "r") as f:
        income.readlines()
    if income:
        print("========== My Income ========")
        for i, incomeList in enumerate(income, start=1):
            print(f"{i}. {incomeList.strip()}")
    else:
        print("\n Invalid! The database is Empty")
              
