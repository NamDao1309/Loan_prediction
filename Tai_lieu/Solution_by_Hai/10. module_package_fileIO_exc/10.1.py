def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Đọc nội dung file INPUT.txt
with open("INPUT.txt", "r") as input_file:
    lines = input_file.readlines()
    count = int(lines[0])
    numbers = list(map(int, lines[1].split()))

# Lọc các số nguyên tố từ mảng numbers
prime_numbers = [num for num in numbers if is_prime(num)]

# Ghi các số nguyên tố vào file KETQUA.txt
with open("KETQUA.txt", "w") as output_file:
    output_file.write(" ".join(map(str, prime_numbers)))
