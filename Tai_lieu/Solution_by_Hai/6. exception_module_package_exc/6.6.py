# read csv using csv.reader
import csv

count = 0
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        count += 1
        # print(line)

print(count)
