import pandas as pd
import matplotlib.pyplot as plt

path = "Buoi18_DA.13.12.2023\sales_data.csv"
df = pd.read_csv(path)

# profitList = df['total_profit'].tolist()
# monthList = df['month_number'].tolist()
# plt.plot(monthList, profitList, label='Tổng lợi nhuận của tất cả các tháng',marker='o', color='r'
#         , markerfacecolor='k', linestyle='--', linewidth=3 )
# plt.xlabel('Month number')
# plt.ylabel('Profit in dollar')
# plt.title("Doanh thu công ty theo tháng")
# plt.xticks(monthList)
# plt.yticks([100000, 200000, 300000, 400000, 500000])

monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()

plt.bar([x-0.25 for x in monthList], faceCremSalesData, width=0.25, align='edge')
plt.bar([x+0.25 for x in monthList], faceWashSalesData, width=-0.25, align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()