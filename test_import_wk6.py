import read_from_file_or_net as rf

my_file = "hnr1.abc"
my_url = "http://193.1.33.31:88/pa1/gettysburg.txt"

file_result = rf.read_any_text_file(my_file)
if file_result:
    # todo do stuff with file
    pass

url_result = rf.get_stuff_from_net(my_url)
if url_result:
    # todo do stuff with url
    pass


print(file_result)
print("=-"*30)
print(url_result)