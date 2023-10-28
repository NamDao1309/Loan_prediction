# 3.11
amount = 100000000  # Số tiền gốc ban đầu
interest_rate = 0.03  # Lãi suất
periods = 10  # Số kỳ hạn

for i in range(1, periods+1):
    interest = amount * interest_rate
    amount += interest
    print(f"Kỳ hạn {i}: {amount:.2f} VND")

