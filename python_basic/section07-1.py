# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 클래스를 선언하고 변수에 할당(인스턴스화 시킴), 메모리에 올려서(페이로드) 사용
# 네임스페이스: 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수: 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수: 객체마다 별도로 존재, 인스턴스 생성 후 사용


class UserInfo:
    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("name: ", self.name)


# 네임스페이스
user1 = UserInfo("kim")
user1.user_info_p()
print(user1.name)
user2 = UserInfo("park")
user2.user_info_p()
print(user2.name)

print("user1", id(user1))
print("user2", id(user2))
print("user1:namespace", user1.__dict__)
print("user2:namespace", user2.__dict__)

# self의 이해


class SelfTest:
    def function1():  # self 인자가 없기 때문에 클래스에서 호출해야함 (클래스 메소드)
        print("function 1 called!!")

    def function2(self):  # 인스턴스 메소드
        print("self!", id(self))
        print("function 2 called!!")


self_test = SelfTest()
# self_test.function1() #에러
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

print("\n\n")
# 클래스 변수, 인스턴스 변수


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("kim")
user2 = WareHouse("park")
user3 = WareHouse("lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 네임스페이스, 클래스 변수 (공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(
    user1.stock_num
)  # 인스턴스 변수가 아니지만, 자신의 네임스페이스에 없으면 클래스의 네임스페이스를 찾아감 이 마저도 없으면 에러 발생
print(user2.stock_num)
print(user3.stock_num)

del user1  # 인스턴스를 지움
print(user2.stock_num)
