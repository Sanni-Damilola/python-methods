def get_all_list_methods():
    count = 0
    for method in dir(list):
        count += 1
        print(count, method)


get_all_list_methods()


