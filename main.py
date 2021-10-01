# 먼저 이름과 나이를 받아온다.
# 나이가 10살 미만이면 "안녕" 을 출력한다.
# 나이가 10살 이상, 20살 미만이면 "안녕하세요" 를 출력한다.
# 그 외에는 "안녕하십니까" 를 출력한다.

def getStatus(name, age):
  if age < 10:
    print("안녕")
  elif age >= 10 and age < 20:
    print("안녕하세요")
  else:
    print("안녕하십니까")

getStatus("김철수", 8)
getStatus("김미영", 14)
getStatus("김순자", 41)