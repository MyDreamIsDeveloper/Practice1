# tuple 연습

x = tuple()
y = ()

print(x)
print(y)

# List와 동일하게 선언할 수 있으며 비슷한 기능을 가지고 있음
x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

# List와 지원하는 기능을 이용 할 수 있음
print(x + y)
print('a' in y)
print(z.index(1))

# 하지만 이미 선언한 값을 변경 할 수 없음
# 자바의 Enum과 비슷한 매커니즘으로 보임
# x[0] = 10 : Error