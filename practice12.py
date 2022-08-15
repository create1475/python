#자료구조의 변경
menu = {"커피","우유","주스"}#집합으로 먼저 만들어본다
print(menu,type(menu))#이걸 실행하면 set형이된다. 이걸 다른걸로 바꿔볼꺼다. 이건 중괄호


menu = list(menu)
print(menu,type(menu))#이렇게 감싸서 형식이 리스트 형으로 바뀌었다.이건 대괄호

menu = tuple(menu)
print(menu,type(menu))# 이건 소괄호로 바뀐다.

menu = set(menu)
print(menu,type(menu))#다시 셋으로 바꾼거다.




