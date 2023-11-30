# def show_employee(name, salary=9000):
#      print("Name:", name, "salary:", salary)
#      show_employee("Ben", 12000)
#      show_employee("Jessa")
# name = input("Nhap ten: ")
# print(show_employee(name, salary=9000))

# Bai 5.1
def liet_ke_ham():
    tach = ham.split()
    for n in tach:
        print(n)
ham = int(input("Nhap ham func1( )"))
print(liet_ke_ham())