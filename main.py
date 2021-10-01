# dict 연습

x = dict()
y = {}

print(x)
print(y)

x = {
  "name": "철수",
  "age": 20,
}

# dict는 Key와 Value로 구성, Map과 유사한 기능으로 보임
print(x["name"])
print(x["age"])

print(x.keys()) # x의 Key 전체 출력
print(x.values()) # x의 Value 전체 출력

for n in x: # dict의 모든 key-value 출력
  print(n + ":" + str(x[n]))