# #파일 입출력
# score_file = open("score.txt","w",encoding="utf-8")# 오픈을 쓰고 파일이름,"w"가 의미하는건 이 파일을 wrate 쓰겠다라는 의미 마지막으로 인코딩 써줌
# print("수학 : 0",file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()
# # 파일을 열었으면 항상 닫아줘야 한다.
#스코어파일을 쓰는 목적으로 쓰고 "w"


score_file = open("score.txt","a",encoding="utf8")#a를 쓰는거 어팬드 뒤에 이어쓰는 느낌 하는 느낌?
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

