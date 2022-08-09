python = "Python is Amazing"
print(python.lower())#모든 문자를 소문자로 출력한다.
print(python.upper())#모든 문자는 대문자로 출력한다.
print(python[0].isupper)#0인덱스에 있는 문자가 대문자인지 확인한다. 맞으면 true 아니면 false
print(len(python))# 파이썬 전체 문자열의 길이를 반환해줌
print(python.replace("Python" , "java"))#파이썬문자를 자바문자로 바꾼다.

index = python.index("n")#인덱스 자리 n자리 찾아줘라 그자리 번지수를 찾아줘라
print(index)

index = python.index("n", index + 1)#뒤에서부터 그니까 n이 5 니까  index+1이 의미하는것은 n이란 문자를(5)에 있는거 다음부터 찾아라 
print(index)

print(python.find("java"))

print(python.find("n"))# 만약  find해서 단어가 없으면 -1이 나온다.
#print(python.index("java"))# 이건 오류다 왜나하면 java라는 단어가 없으니 그냥 끝낸다 그래서 여기서 실행문이 끝나니까 이걸 find로 바꾸고 실행해야 다음행이 실행된다.
print("hi")
print(python.count("n"))#이건 파이썬이란 단어안에 n이라는 글자가 몇번 등장하는지 찾아주는 역활을 한다.



# \n:줄바꿈


print("저는 \"나노코딩\"입니다.")

# \r은 커서를 맨 앞으로 이동
print("red Apple\rpine")

 # \b 는 백스페이스 역활을 한다.

sss = "http://naver.com"
print(sss)
aaa = sss.replace("http://naver.com","naver.com")

print(aaa)
aaa = aaa[:5]
print(aaa)

ccc = aaa[:3]
print(ccc)

ddd = len(aaa)
print(ddd)

eee=aaa.count("e")
print(eee)

print(ccc,ddd,eee,"!")
#그지같이 만들었구만....ㅋㅋㅋㅋ
#첫걸음은 위대하다.


