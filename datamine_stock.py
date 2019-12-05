from datetime import datetime
import read_from_file_or_net as rf

my_file = "GOOGL.csv"

container_csv_text = rf.read_any_text_file(my_file)
csv_text = container_csv_text.strip()
csv_file = csv_text.split('\n')

csv_file_lists = []
for string in csv_file:
    csv_file_lists.append(string.split(','))

data = []

for row in csv_file_lists[1:]:
    tradeDay = datetime.strptime(row[0], '%Y-%m-%d')
    price = float(row[5])
    vol = int(row[6])
    data.append([tradeDay, price, vol])

'''Function calAverage iterates through the data tuple using for_mthyear as a parameter to calculate for month using 
%Y-%m as part of the datetime library and Year for %Y.  There are no check or error handling at the moment for any date 
formats other than dates in the following format YYYY-MM-DD and it assumes that the csv file is listed in ascending order 
using the tradeday as the key
'''
def calAverage(data, for_mthyear):
    base_date = datetime.strftime(data[0][0], for_mthyear)
    average_data = []
    vprice = 0
    volume = 0

    for date in data:
        checkdate = datetime.strftime(date[0], for_mthyear)

        if checkdate == base_date:
            vprice += date[1]*date[2]
            volume += date[2]

        elif checkdate != base_date:
            average = vprice / volume
            average_data.append([base_date, average])
            base_date = checkdate
            vprice = 0
            volume = 0
            vprice = date[1]*date[2]
            volume = date[2]

        if date is data[-1]:
            average = vprice / volume
            average_data.append([base_date, average])
    return average_data

def main():
    monthly_avg = calAverage(data, for_mthyear='%Y-%m')
    monthly_avg = sorted(monthly_avg, key=lambda tup: tup[1])
    print(monthly_avg)


    yearly_avg = calAverage(data, for_mthyear='%Y')
    yearly_avg = sorted(yearly_avg, key=lambda tup: tup[1])
    print(yearly_avg)

    print("\n Worst 6 Years")
    print("----------------")
    for year in  yearly_avg[:6]:
        print(f"{year[0]} : {year[1]:<.2f}")

    print("\n Worst 6 months")
    print("----------------")
    for month in monthly_avg[:6]:
        print(f"{month[0]} : {month[1]:<.2f}")

    '''Since it is already sorted we are going to select the last six items (best 6)' \
     in the list using the [begin:end:step]'''

    print("\n Best 6 months")
    print("----------------")
    for month in yearly_avg[-1:-7:-1]:
        print(f"{month[0]} : {month[1]:<.2f}")

    print("\n Best 6 Years")
    print("----------------")
    for year in yearly_avg[-1:-7:-1]:
        print(f"{year[0]} : {year[1]:<.2f}")




if __name__ == '__main__':
    main()

