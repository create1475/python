# 기본값

# def profile(name, age ,main_lang):
#     print("이름 : {0} \t 나이 : {1}\t 주사용언어:{2}." \
#       .format(name,age,main_lang)) # 줄바꿈을 할때는 한칸 띄우고 역슬래쉬 박으면 이줄은 한줄이에요 라는 의미이다.

# profile("유재석", 20 , "파이썬")
# profile("김태호", 20 , "자바")


#같은 학교 같은학년 같은 반 수업.

def profile(name, age=17 ,main_lang="파이썬"):
    print("이름 : {0} \t 나이 : {1}\t 주사용언어:{2}." \
      .format(name,age,main_lang)) # 줄바꿈을 할때는 한칸 띄우고 역슬래쉬 박으면 이줄은 한줄이에요 라는 의미이다.

profile("유재석")
profile("김태호")