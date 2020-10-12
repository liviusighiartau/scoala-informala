

def uppercase(fnc):

    def inner_func(expression: str):
        return fnc(expression).upper()

    return inner_func


@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet('Liviu'))


def safe_divide(fnc):

    def inner_func(num1: int, num2: int):
        try:
            return fnc(num1, num2)
        except ZeroDivisionError:
            return "Division by 0 cannot be performed!"
        except Exception:
            return "Operation cannot be performed, please try again!"

    return inner_func


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


print(divide(10, 5))
print(divide(8, 0))

print_registry = []


def register(fnc):

    print_registry.append(fnc.__name__)
    return fnc


@register
def greet(name):
    return "Greetings {}!".format(name)


@register
def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


greet('Liviu')
say_hello('Liviu')
say_goodbye('Liviu')

print(print_registry)
