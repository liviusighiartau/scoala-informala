def pop_element_from_tuple_slicing(my_tuple: tuple, index=None):
    my_tuple = my_tuple[:index] + my_tuple[index + 1:]
    return my_tuple


def pop_element_from_tuple_convert_to_list(my_tuple: tuple, index):
    tuple_to_list = list(my_tuple)
    tuple_to_list.pop(index)
    return tuple(tuple_to_list)

