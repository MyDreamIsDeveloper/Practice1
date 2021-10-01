# 클래스 생성

class Person:
  def __init__(self, name, age): #init = initialize
    self.name = name
    self.age = age

# self는 this와 같은 기능 같음
  def say_hello(self, to_name):
    print("안녕 " + to_name + ", 나는 " + self.name)

  def status(self):
    print("이름:" + self.name + " / 나이:" + str(self.age))

A = Person("A", 10)
B = Person("B", 20)
C = Person("C", 30)

A.say_hello("철수")
B.say_hello("영희")
C.say_hello("미영")
print("")
A.status()
B.status()
C.status()

# 클래스 상속
class Police(Person):
  def arrest(self, to_arrest):
    print("체포:" + to_arrest)

class Programmer(Person):
  def program(self, to_program):
    print("프로그래밍:" + to_program)

A = Person("A", 10)
B = Police("B", 20)
C = Programmer("C", 30)