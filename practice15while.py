#while 

# customer = "토르"
# #토르라는 변수를 커스터머에 집어넣고
# index = 5
# #다섯번을 반복하기 위해 인덱스에 5를 집어넣는다.

# while index >= 1:
#   print("{0} , 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))#처음에는 {0}이 들어가는건 커스터머가 들어가고 {1}은 인덱스가 #몇번남았는지 확인하는거다
#   index -= 1 #인덱스는 한번씩 줄여나간다.
 
#   if index == 0: 
#     print("커피는 폐기처분되었습니다.")



# customer = "아이언맨"
# index = 1
# while True:
#   print("{0} , 커피가 준비되었습니다. 호출{1} 회".format(customer, index))
#   index += 1
# 이건 무한루프 입니다.

customer = "토르"
person = "Unknown"

while person != customer :# 이름이 토르가 아니니? 하면 안맞으니까 와일문 안으로 들어가지 않는다 계속 반복
  print("{0}, 커피가 준비 되었습니다.".format(customer))#이름이 토르면 와일문 안으로 들어와서 프린트문 출력
  person = input("이름이 어떻게 되세요?")


