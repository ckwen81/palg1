from datetime import datetime
import read_from_file_or_net as rf

my_file = "GOOGL.csv"

container_csv_text = rf.read_any_text_file(my_file)
csv_text = container_csv_text.strip()
csv_file = csv_text.split('\n')

csv_file_lists = []
for string in csv_file:
    csv_file_lists.append(string.split(','))

data =[]

for row in csv_file_lists[1:]:
    tradeDay = datetime.strptime(row[0], '%Y-%m-%d')
    price = float(row[5])
    vol = int(row[6])
    data.append([tradeDay, price, vol])


a = "2004-04-01"
b = "2004-04-02"
a_datetime = datetime.strptime(a, '%Y-%m-%d')
b_datetime = datetime.strptime(b, '%Y-%m-%d')

print( (a_datetime.year == b_datetime.year) & (a_datetime.month == b_datetime.month))

