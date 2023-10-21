#bai 6_1

#setup
# actor = {"name": "John Cleese", "rank": "awesome"}

# #function to modify
# def get_last_name():
#     try:
#         return actor["last_name"]
#     finally:
#         return "N/A"

# #test code
# get_last_name()
# print("All exceptions caught! Good job!")
# print("The actor's last name is %s" %get_last_name())

#bai 6_2

# def do_stuff_with_number(n):
#     print(n)

# def catch_this():
#     the_list = (1,2,3,4,5)

#     for i in range(20):
#         try:
#             do_stuff_with_number(the_list[i])
#         except IndexError:
#             do_stuff_with_number(0)

# catch_this()

#bai 6_3
try:
    print(a)
except NameError:
    print("Biến 'a' chưa được định nghĩa")


