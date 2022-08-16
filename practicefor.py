#출석번호 1,2,3,4 앞에 100을 붙이기로 함 -> 101,102,103,104 이렇게 할꺼임

# student = [1,2,3,4,5]
# print(student)

# student=[i+100 for i in student]#i에 100을 더한값을 스튜던트에 있는 i값에 100을 더해서 리스트로 바꿔서 student 에 넣어라

# print(student)



#학생 이름을 길이로 변환
student = ["iron_man","thor","i am groot"]
student = [len(i) for i in student]

print(student)

#학생이름을 대문자로 변환
student = ["iron_man","thor","i am groot"]
student = [i.upper() for i in student]#스튜던트 안에 있는 i를 가지고 i를 대문자로 바꾼다.

