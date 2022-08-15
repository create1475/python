# 무작위로 있는 숫자를 정렬하는 함수 sort

num_list = [1,4,2,5,3]
num_list.sort();
print(num_list);

# 순서뒤집기 가능
num_list.reverse()
print(num_list)

#값을 모두 지우고 싶다 하면
num_list.clear()
print(num_list)

# 다양한 자료형 함수와 함께 사용한다. 소문자 t를 사용하면 에러가 난다. 이유는 뭘까???
num_list = [1,4,2,5,3]
mix_list = ["조세호", 20, True]

#print(mix_list)
#리스트 확장  num_list 와 mix_list를 연결시킨다.
num_list.extend(mix_list)
print(num_list)


