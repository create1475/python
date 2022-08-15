#튜플은 내용변경이나 추가가 불가능하다. 하지만 속도는 리스트보다 빠르다 변경되지 않는 값을 사용할때 쓰인다.

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

#메뉴에 생선가스를 추가하고 싶다.

# name = "김종국"
# age = 20
# hoddy = "코딩"
# print(name,age ,hoddy)


(name,age,hoddy) = "김종국",20,"코딩" 
print(name,age,hoddy)
