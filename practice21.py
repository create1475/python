#표준 입출력

# print("python" + "java")# +를 썻을때는 줄이 다 붙어서 나온다
# print("python" , "java",sep=",")#sep값을 ,로 했을때는 출력값 사이에 ,가 들어간다.
# print("python" , "java",sep=",",end="?")#sep값을 ,로 했을때는 출력값 사이에 ,가 들어간다.
# print("무엇이 더 재미있을까요?")
# # 프린트문 두개가 한줄에 연결되서 나온다  end 의미는 원래는 줄바꿈이였는데 물음표를 넣어주면 뒤에있는 문장이 연달아서 한문장으로 출력


# import sys
# print("python", "java", file=sys.stdout)# out 은 표준 출력으로 찍히는거고
# print("python", "java", file=sys.stderr)# err 은 표준 에러로 출력되는거다.


# scores = {"수학":0 , "영어":50, "코딩": 100}
# for subject,score in scores.items():  # .items는 키와 밸류값을 쌍으로 보내준다.
#   #print(subject,score)
#   print(subject.ljust(8),str(score).rjust(4),sep=":") # 왼쪽으로 정렬하는데 8칸을 공간을 확보하고 왼쪽으로 정렬 

#                                                               #스코어 부븐은 정렬을 하는데 오른쪽 정렬하는데 4칸의 공간을 확보하고 출력한다.


#은행 대기 순번표
#001 002 003 004 005 이렇게 되어있다.
# for number in range(1,21):
#   print("대기번호: "  + str(number).zfill(3))   # 이건 3공간을 확보하고 출력하는 뜻인데 값이 없을때는 빈공간은 0을 채워 넣는건다.

answer = input("아무 값이나 입력하세요 : " )
print("입력하신 값은 " + answer + "입니다.")   # 이건 스트링 형으로 받는다.사용자 형태로 입력을 받으면 항상 문자열로 받는다.
