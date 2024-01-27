def get_all_list_methods():
    count = 0
    for method in dir(list):
        if not "__" in method:
            count += 1
            print(count, method)

get_all_list_methods()


