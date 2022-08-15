absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11): #student 라는 객체에 range해서 1부터 10까지 출력
    if student in absent: # 만약 학생중에 결석한 사람이 있다면
     continue
    elif student in no_book:
      print("오늘수업 여기까지 .{0}는 교무실로 따라와".format(no_book))
    break

#왜 이거는 출력이 안되냐 짜쯩나게 빡치네

print("{0}, 책을 읽어봐.".format(student))


