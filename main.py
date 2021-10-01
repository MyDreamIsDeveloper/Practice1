# List 선언, 2가지의 방법

x = list()
y = []

print(x)
print(y)

x = [5,1,2,4] # List에 지정한 변수 채워넣기
print(sorted(x)) # 오름차순 정렬 후 출력
print(sum(x)) # List의 변수를 모두 더한 후 출력
print(x[0]) # List의 원하는 값 출력

for n in x:
  print(n)
  # x에 든 내용을 n에 넣어가며 출력
  # 자바의 for (String s : String[]) 와 유사한 기능이지만 type을 기재하지 않음.

print(x.index(2)) # List 안에 찾고자 하는 내용의 위치를 알려줌

if 5 in x: # List 조건문
  print("true")
else:
  print("false");