def return_string_from_list(my_list: list):
    my_list_updated = [
        element
        for element in my_list
        if type(element) is str]
    return my_list_updated


# my_list = ['I', 'am', 'a', 1, 'list', 'of', 5, 'strings']
# print(return_string_from_list(my_list))
