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
