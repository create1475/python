#if 분기

#weather = "맑아요"
# if(조건) : # 콜론으로 문장 끝을 낸다.
#     실행 명령문

# if(weather == "비"):
#   print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#   print("준비물 필요 없어요")




#input 사용자의 입력을 받는 문장 

# weather = input("오늘 날씨는 어때요.?")#input을 쓰면 사용자의 입력을 받아서 터미널에서 내가 입력하기를 기다린다. scanner문이랑 비슷하다고 생각하면 된다, 띄어쓰기 잘 생각하고 쓰자 

# if(weather == "비" or weather == "눈"):
#   print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#   print("준비물 필요 없어요")

#input 은 항상 문자열로 받는다. 이걸 int로 감싸줘야 한다.
temp = int(input("기온은 어때요?"))#기온은 숫자기때문에 숫자형으로 바꿔야 한다.

if 30 <= temp:
  print("너무 더워요 . 나가지 마세요")
elif 10 <= temp and temp < 30:
  print("괜찮은 편이에요")
else:
  print("너무 추우니까 나가지 마여 ")






  