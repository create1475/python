# #키워드값 
# def profile(name, age ,main_lang):
#   print(name,age ,main_lang)


# profile(name="유재석" ,age= 20 ,main_lang= "파이썬")
# profile(main_lang="자바" , age = 25 , name = "김태호")



# #가변인자를 이용한 함수 호출
# def profile(name,age,lang1, lang2,lang3,lang4,lang5):
#     print("이름 : {0} \t 나이 {1}\t".format(name,age), end = " ")  # 앤드를 적어주면 줄바꿈을 하지 않고 바로 이어서 다름 프린트문을 출력해준다.
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재석" , 20 , "python", "java","c","C++","c#")



# 만약에 또 다른 사람의 가변인자를 가져야 한다면. 총 6개의 언어가 필요하니까 lang6까지 적어야 하는 상황이 온다 그떄 쓰는게 가변인자이다.
def profile(name, age, *language):  #난 이게 왜 에러가 뜨지?
    print("이름 : {0} \t 나이 {1}\t".format(name,age), end= " ")  #앤드를 적어주면 줄바꿈을 하지 않고 바로 이어서 다름 프린트문을 출력해준다.
    for lang in language:
     print(lang, end=" ")
    print()
      


profile("유재석" , 20 , "python", "java","c","C++","c#")
profile("김태호" , 25 , "kotlin", "swift",)


