"""
Q: Which are the methods which have not been presented?
A: copy() - Return a shallow copy of the list. Equivalent to a[:]
A: count(x) - Return the number of times x appears in the list
A: index(x[, start[, end]]) - Return zero-based index in the list of the
first item whose value is x
A: reverse() - Reverse the elements of the list in place.
A: sort(key=None, reverse=False) - Sort the items of the list in place (the arguments
can be used for sort customization, see sorted() for their explanation)
"""

color = ['orange', 'blue', 'red', 'green', 'black', 'brown', 'grey', 'black', 'green', 'green']

color_ = color.copy() + ['purple']
print("My list contains these elements: " + repr(color_) + ".")

print("My list has " + str(color_.count('green')) + " of green.")

print("Red is on position " + str(color_.index('red')) + ".")

color_.reverse()
print("This is what you see when you look at it backwards " + str(color_) + ".")


def number_of_letters(color_element):
    return len(color_element)


color_.sort(key=number_of_letters)
print(color_)
