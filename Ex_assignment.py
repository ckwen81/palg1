def get_text_file_from_net(text_url):
    """Takes a URL of a text file that is on the web as
        a string and returns the text file as a string
        using the Request Library."""
    try:
        import requests
        retrieve = requests.get(text_url)
        text_file_str = retrieve.text
        return text_file_str
    except Exception as err:
        print(f"Error trying to retrieve the file from the net: {err}")
        return None


# 1. Download the Google share price data for the net and put it into a .csv file
container_csv_text = get_text_file_from_net("http://193.1.33.31:88/pa1/GOOGL.csv")
csv_text = container_csv_text.strip()  # strips whitespace from the end of the text

# 2. Create a list in which each element will be a string i.e. a line of text from the .csv file
csv_rows = csv_text.split('\n')

# 3. Create a list of lists. The elements of (2.) separated by the comma in the string
csv_rows_lists = []
for string in csv_rows:
    csv_rows_lists.append(string.split(','))

# 4. Make a final list whose elements will be the data we need i.e. 'Year', 'Month', 'Adj. Close', 'Volume'
data = []
for row in csv_rows_lists[1:]:
    yr = int(row[0][:4])
    mth = int(row[0][:4] + row[0][5:7])
    vol = int(row[6])
    price = float(row[5])
    data.append([yr, mth, price, vol])

# 5. Initialize the variables we need to use in the calculations
# NB: 'run' means a variable that is a running total

prev_yr = data[0][0]
run_p_by_v_yr = (data[0][2] * data[0][3])
run_v_yr = data[0][3]
avg_p_yr = run_p_by_v_yr / run_v_yr

prev_mth = data[0][1]
run_p_by_v_mth = (data[0][2] * data[0][3])
run_v_mth = data[0][3]
avg_p_mth = run_p_by_v_mth / run_v_mth

avg_Monthly_Price_list = []
avg_Yearly_Price_list = []

# 6. Loop through each date and calculate the answers required
#   date[0] is YEAR
#   date[1] is MONTH
#   date[2] is ADJ CLOSE PRICE
#   date[3] is VOLUME
for date in data[1:]:
    # 6.1. if the year and month of this date equal the year and month of the previous date
    if date[0] == prev_yr and date[1] == prev_mth:
        # 6.1.1. update the average yearly price
        run_p_by_v_yr += date[2] * date[3]
        run_v_yr += date[3]
        avg_p_yr = run_p_by_v_yr / run_v_yr
        prev_yr = date[0]
        # 6.1.2. and update the average monthly price
        run_p_by_v_mth += date[2] * date[3]
        run_v_mth += date[3]
        avg_p_mth = run_p_by_v_mth / run_v_mth
        prev_mth = date[1]
        # 6.1.3. check if this is the last date in data
        if date is data[-1]:
            avg_Monthly_Price_list.append([avg_p_mth, prev_mth])
            avg_Yearly_Price_list.append([avg_p_yr, prev_yr])

    # 6.2. if the year of this date equals the previous year but the month of this date is different to previous month
    elif date[0] == prev_yr and date[1] != prev_mth:
        # 6.2.1. update the average yearly price
        run_p_by_v_yr += date[2] * date[3]
        run_v_yr += date[3]
        avg_p_yr = run_p_by_v_yr / run_v_yr
        prev_yr = date[0]
        # 6.1.2. Add the Average Adj. Close Price of the previous month to the list
        avg_Monthly_Price_list.append([avg_p_mth, prev_mth])

        run_p_by_v_mth = date[2] * date[3]
        run_v_mth = date[3]
        avg_p_mth = run_p_by_v_mth / run_v_mth
        prev_mth = date[1]
        # 6.1.3. check if this is the last date in data
        if date is data[-1]:
            avg_Monthly_Price_list.append([avg_p_mth, prev_mth])
            avg_Yearly_Price_list.append([avg_p_yr, prev_yr])

    # 6.3. if the rear of this date is NOT equal to the year of the previous date
    elif date[0] != prev_yr:
        # 6.3.1. Add the Average Adj. Close Price of the previous month and year to their respective lists
        avg_Monthly_Price_list.append([avg_p_mth, prev_mth])
        avg_Yearly_Price_list.append([avg_p_yr, prev_yr])
        # 6.3.2. Re-initialize the yearly variables
        run_p_by_v_yr = date[2] * date[3]
        run_v_yr = date[3]
        avg_p_yr = run_p_by_v_yr / run_v_yr
        prev_yr = date[0]
        # 6.3.3. Re-initialize the monthly variables
        run_p_by_v_mth = date[2] * date[3]
        run_v_mth = date[3]
        avg_p_mth = run_p_by_v_mth / run_v_mth
        prev_mth = date[1]
        # 6.3.4. check if this is the last date in the data
        if date is data[-1]:
            avg_Monthly_Price_list.append([avg_p_mth, prev_mth])
            avg_Yearly_Price_list.append([avg_p_yr, prev_yr])


# 7. Output the desired results
#  7.1. The Yearly desired results
avg_Yearly_Price_list.sort()
print("Average Adj. Close - Worst 6 Years")
print("------------------------------------")
for year in avg_Yearly_Price_list[:6]:
    print(f"{year[1]}: {year[0]:<.2f}")
print("\nAverage Adj. Close - Best 6 Years")
print("------------------------------------")
for year in avg_Yearly_Price_list[-1:-7:-1]:
    print(f"{year[1]}: {year[0]:<.2f}")

#  7.2. The Monthly desired results
avg_Monthly_Price_list.sort()
print("\nAverage Adj. Close - Worst 6 Months")
print("------------------------------------")
for month in avg_Monthly_Price_list[:6]:
    print(f"{month[1]}: {month[0]:<.2f}")
print("\nAverage Adj. Close - Best 6 Months")
print("------------------------------------")
for month in avg_Monthly_Price_list[-1:-7:-1]:
    print(f"{month[1]}: {month[0]:<.2f}")