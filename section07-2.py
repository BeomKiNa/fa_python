# 클래스 상속, 다중 상속

# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class"""

    def __init__(self, type, color):
        self.type = type
        self.color = color

    def show(self):
        return "Car Class 'Show Moethod!'"


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, type, color):
        super().__init__(type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return "Car info : %s %s %s" % (self.car_name, self.type, self.color)


model1 = BmwCar("520d", "sedan", "red")
print(model1.color)  # Super
print(model1.type)  # Super
print(model1.car_name)  # Sub
print(model1.show())  # Super
print(model1.show_model())  # Sub
print(model1.__dict__)
print("\n")

# Method Overriding

model2 = BenzCar("220d", "suv", "black")
print(model2.show())  # Sub: Super의 show를 Overriding

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritance Info(상속 정보를 리스트 형태로)
print(BmwCar.mro())
print(BenzCar.mro())

# 다중 상속


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print(A.mro())
