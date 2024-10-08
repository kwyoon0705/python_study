def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")


my_car = Car(make="Hyundai", model="Genesis")
print(my_car.model)
