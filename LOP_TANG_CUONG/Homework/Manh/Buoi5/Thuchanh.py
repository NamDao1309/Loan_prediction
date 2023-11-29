#bai 6.1
actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name(): 
 try:
     return actor["last_name"]
 except KeyError:
     print("Khong tim thay ten")
     
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())


#bai 6.4
def do_stuff_with_number(n):
 print(n)
 
def catch_this():
 the_list = (1, 2, 3, 4, 5)
 for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: 
       # do_stuff_with_number(0)
       print("Khong tim thay phan tu")
       
catch_this()

#bai 6.3
try:
    print(a)
except NameError:
    print("Bien a chua duoc dinh nghia.")

#bai 6.6
import csv 
path_file = "Buoi5.27.11.2023/New Text Document.txt"
read_file = csv.reader(path_file)

def count_lines(read_file):
        return len(list(read_file))

print(f'The number of lines in file is {count_lines(read_file)}.')



