# Ex1: Create a employee and dept database.
dept_db = {
    101: 'HRD',
    102: 'FINANCE',
    103: 'ACCOUNTS',
    104: 'SALES',
    105: 'ENGINEERING',
    106: 'SUPPORT'
}
employee_db = {
    1000: dict(name="Alex", doj='01-10-89', dept=103),
    1001: dict(name="Mary", doj='01-11-88', dept=101),
    1002: dict(name="John", doj='01-10-87', dept=104),
    1003: dict(name="David", doj='01-06-89', dept=105),
    1004: dict(name="Anne", doj='01-01-86', dept=106),
    1005: dict(name="Samson", doj='01-02-89', dept=101)
}


def search_employee_by_id(id):
    if id in employee_db:
        return employee_db[id], dept_db[employee_db[id]['dept']]
    return None


print(search_employee_by_id(1000))

# Ex2: Display products with price less or equal form user input
products = {
    'SMART WATCH': 550,
    'PHONE': 1000,
    'PLAYSTATION': 500,
    'LAPTOP': 1550,
    'MUSIC PLAYER': 600,
    'TABLET': 400
}

cost = int(input("Enter your budget: "))

print("You can buy: ", end="")
for key, value in products.items():
    if (value <= cost):
        print(key, end=", ")

# [Bài tập] Từ điển

word = input("Enter a word: ")
dictionary = {
    "hello": "xin chào",
    "how": "thế nào",
    "book": "quyển vở",
    "computer": "máy tính"
}
print(dictionary[word]) if word in dictionary else print("Not found in database")

# [Bài tập] Count number of occurrence of words in a given text.
def count_word(text):
    num_words = {}
    text_list = text.split()
    for word in text_list:
        word = word.lower().strip(",. ")
        if word in num_words:
            num_words[word] += 1
        else:
            num_words[word] = 1
    return num_words

message = "This is a test message. This message is to test the count_word function."
print(count_word(message))

# [Bài tập] Ứng dụng quản lý sản phẩm
prod_db = {
    1: dict(name="Iphone 12", price=1200),
    2: dict(name="Galaxy S21", price=1100),
    3: dict(name="Xperia 1", price=1000),
    4: dict(name="Mi 11", price=900),
    5: dict(name="Mate 40", price=800)
}

def get_info(prod_db, prod_id):
    if id in prod_db:
        return prod_db[prod_id]
    return None

def upd_info(prod_db, prod_id, new_info):
    if id in prod_db:
        prod_db[prod_id] = new_info
    else:
        prod_db.update({prod_id: new_info})

print(prod_db)

options = [{
    "1": "Thêm sản phẩm mới",
    "2": "Cập nhật sản phẩm",
    "3": "Xóa sản phẩm",
    "4": "Thoát khỏi ứng dụng",
}]
while (True):
    print("Chọn chức năng: ", options)
    option = int(input("Enter option: "))
    if option == 1:
        prod_id = int(input("Enter product ID: "))
        prod_name = input("Enter product name: ")
        new_prod = dict(name=prod_name)
        upd_info(prod_db, prod_id, new_prod)
    elif option == 2:
        prod_id = int(input("Enter product ID: "))
        prod_name = input("Enter new product name: ")
        upd_info(prod_db, prod_id, prod_name)
    elif option == 3:
        prod_id = int(input("Enter product ID: "))
        del prod_db[prod_id]
    elif option == 4:
        break
    else:
        print("Invalid option")
print(prod_db)
