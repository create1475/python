print("나는 %d살 입니다" % 20)#%d 는 숫자이고

print("나는 %s을 좋아해요. " %"파이썬")#스트링형이다.

print("apple은 %c로 시작해요" %"A")# 캐릭터형이다.한글자만 입력가능
#%s는 거의다 출력된다.

print("나는 %s색과 %s색을 좋아해요." %('빨강','파랑') )#가로를 해놓으면 2개이상의 %를 넣을수있다.


#방법2
print("나는{}살입니다..".format(20))#점을 찍고 포멧을 쓰면 된다.
print("나는 {}색과{}색을 좋아한다.".format("빨강","파랑"))
print("나는 {0}색과{1}색을 좋아한다.".format("빨강","파랑"))#0인덱스 1인덱스 이렇게 들어가는거다.



#방법 3
print("나는 {age}살이며 ,{color}색을 좋아해요".format(age=20,color = "파랑"))

#방법4
age = 30
color = "빨강"
print(f"나는{age}이며,{color}색 을 좋아한다.")#프린트문 내에서 f로 시작한다. 그럼 위 변수 선언과 같은 방법을 사용할수있다.

#\n은 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

print("저는 \"나노코딩\"입니다.")#따옴표 쓸때 이렇게 써야한다.

#\\역슬래쉬 두번쓰면 문장내에서는  \가 표시된다.

#\r 커서를 맨앞에 가져다 놓는다.
print("red apple\rpine")

#\b:백스페이스(한 글자 출력)
print("red\bapple")

#\t 탭





