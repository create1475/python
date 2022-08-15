#세트(set)  집합   중복이 안된고 순서가 없다.
#중복이 안되고 순서가 없다.

#중괄호는 사전에서 썻다 사전에서는 키와 밸류를 썻다.
my_set = {1,2,3,4,5,5,5,5,5,5}
print(my_set)

java = {"유재석" , "김태호","양세형"}
python = set(["유재석", "박명수"])#리스트로 먼저 만들고 그다음 셋으로 설정가능하다.

#자바와 파이썬 둘다 가능한사람
print(java & python)
print(java.intersection(python)) # 이것도 교집합 값을 뽑는거다.


#합집합을 뽑자 자바도 할수있고 파이썬도 할수있는 개발자를 뽑자.

print(java | python)
print(java.union(python))

#차집합  자바는 할줄알지만 파이썬은 할줄 모르는사람
print(java - python)
print(java.difference(python))

#파이썬 할줄아는사람이 늘어남 
python.add("김태호")
print(python)

#자바를 까먹음 자바를 할줄모른다는 의미
java.remove("김태호")
print(java)