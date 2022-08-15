#반복문 for 
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in[1,2,3,4,5,]:# for in은 공식이다.
#   print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(5):#0,1,2,3,4까지 주어진다.
  print("대기번호 : {0}".format(waiting_no))  


for waiting_no in range(1,6):#이건 1부터 6직전까지 그러니 5까지 나온다.
  print("대기번호 : {0}".format(waiting_no))  




starbuck=["아이언맨","토르","아이엠그루트"]
for customer in starbuck:
  print("{0}, 커피가 준비되었습니다.".format(customer))
  
