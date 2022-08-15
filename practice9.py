#사전에서는 키의 중복이 허용되지 않는다. 사전의 경우에는 중괄호를 열고 닫고 한다.
#키는 3이고 밸류는 유재석이라는 데이터가 들어간거다. 100번키이고 밸류라는 조세호가 들어가있다.
cabinet = {3:"유재석",100:"조세호"}
print(cabinet[100])# 출력을 할때에는 앞에 있는 키값을 넣어주면 된다.

#또다른 방법으로 값을 가져올수 있다.
print(cabinet.get(3))

# 대괄호로 값을 가져왔을때 에러가 나면 프로그램을 종료시키는데
# 소괄호로 겟해서 가져오면 none이라는 글자가 나오면서 다음줄을 실행시킨다.


#사전 자료형 안에 키 값이 있는지 확인하는 방법
print(3 in cabinet) #값이 있으면 true
print(5 in cabinet) #값이 없으면 false이다.

#새손님이 와서 키값을 할당
print(cabinet)
#cabinet["C-20"] = "조세호";# 이미 사용중이라면 업데이트가 된다.


#떠나간 손님
#del cabinet["C-20"]
print(cabinet)

#지금 총 사용중인 키의 출력
print(cabinet.keys())

#value 값만 출력하고 싶다.
print(cabinet.values())

# key 와 value의 값을 쌍으로 출력하려면
print(cabinet.items())

# 목욕탕 폐점한다. 모든 캐비넷을 비운다.
cabinet.clear()
print(cabinet)
