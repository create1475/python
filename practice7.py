# #리스트--순서를 가지는 객체의 집합

# #지하철 칸 별로 10명 20명 30명이 있다.
# #  subway1 = 10
# #  subway2 = 20
# #  subway3 = 30

# from re import sub


# subway = [10,20,30]#이게 리스트이다.
# print(subway)

# subway = ["유재석","조세호","강호동"]
# print(subway)

# #조세호가 몇번째 인덱스에 있는지 찾아라
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음칸에 탔다.
# #append 는 뒤에 더하다 의미이다. 맨뒤자리에 하하를 추가한다.

# subway.append("하하")
# print(subway)

# #정형돈씨를 유재석과 조세호 사이에 넣으려고한다. 공식은 인설트 쓰고 자리 쓰고 넣을값을 쓴다.

# subway.insert(1,"졍형돈")
# print(subway)

# #지하철에 있는 사람을 한명씩 꺼냄 pop는 뒤에서부터 한명씩 뺀다.
# print(subway.pop())
# print(subway)

# #같은 이름의 사람이 몇명있는지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬도 가능합니다.
