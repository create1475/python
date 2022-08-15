
# score_file = open("score.txt","r",encoding="utf8")# r 이 의미하는건 모든 파일을 다 불러오는거다.
# print(score_file.read()) # 한번에 모든 파일을 읽는거다.
# score_file.close()


# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="")# 이건 한줄을 읽어오는거다. 그리고 커서를 다음줄로 이동  end 는 줄바꿈 안하고 싶을때 쓴다.
# print(score_file.readline(),end="")# 이건 한줄을 읽어오는거다. 그리고 커서를 다음줄로 이동
# print(score_file.readline(),end="")# 이건 한줄을 읽어오는거다. 그리고 커서를 다음줄로 이동
# print(score_file.readline(),end="")# 이건 한줄을 읽어오는거다. 그리고 커서를 다음줄로 이동
# score_file.close()


# # 몇줄인지 모를때 처리하는법
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
  
# score_file.close()

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list형태로 저장하는것
for line in lines:
    print(line,end="")

score_file.close()

