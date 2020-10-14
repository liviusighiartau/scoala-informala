class Person(object):

    def __init__(self, full_name, country, city, age, working_years):
        self.full_name = full_name
        self.country = country
        self.city = city
        self.age = age
        self.working_years = working_years

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def is_legal_to_open_account(self):
        if 18 <= self.age <= 63 and self.working_years > 1:
            message = f'''
            The user {self.full_name} who lives in {self.country}, {self.city} is legal to open a bank account.'''
            print(message)
            return True
        elif self.age > 63:
            message = f'''
            The user {self.full_name} who lives in {self.country}, {self.city} is too old to open a bank account.'''
            print(message)
            return False
        else:
            message = f'''
            The user {self.full_name} who lives in {self.country}, {self.city} is not legal to open a bank account.'''
            print(message)
            return False


person = Person('Liviu Sighiartau', 'Romania', 'Cluj-Napoca', 27, 3)


class Employee(Person):

    def __init__(
            self, full_name, country, city, age, sex,
            has_credits, has_deposits, no_of_late_payments, is_married, salary):
        self.has_credits = has_credits
        self.has_deposits = has_deposits
        self.no_of_late_payments = no_of_late_payments
        self.is_married = is_married
        self.salary = salary
        super().__init__(full_name, country, city, age, sex)

    def is_currently_employed(self):
        if self.salary != 0:
            return True
        else:
            return False

    def get_max_credit(self):
        if 1500 >= self.salary > 700 and self.no_of_late_payments == 0:
            credit_value = 10000
            # credit = {'credit_value': credit_value, 'credit_time_period': 60}
        elif 3000 > self.salary >= 1501 and self.no_of_late_payments == 0:
            credit_value = 40000
            # credit = {'credit_value': credit_value, 'credit_time_period': 60}
        else:
            credit_value = 100000

        return {'credit_value': credit_value, 'credit_time_period': 60}


employee = Employee('Liviu Sighiartau', 'Romania', 'Cluj-Napoca', 27, 3, True, True, 0, True, 7000)
print(employee.is_adult())
print(employee.is_legal_to_open_account())
print(employee.is_currently_employed())
print(employee.get_max_credit())


