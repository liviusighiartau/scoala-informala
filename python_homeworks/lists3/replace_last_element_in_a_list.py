def replace_last_element_in_list(my_list: list, replacer='last'):
    my_list_updated = [
        replacer
        if index == len(my_list) - 1
        else element
        for index, element in enumerate(my_list)
    ]
    return my_list_updated
