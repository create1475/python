def open_account(): #함수를 정의할때는 def를 쓰고 뒤에 함수이름을 적고 가로열고닫고 콜론으로 닫는다
  print("새로운 계좌가 생성되었습니다.")


open_account()



# 전달값과 반환값
def deposit(balance, money):    # 전달하려는 값은 가로사이에 집어넣으면 된다.
  print("입금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance + money))

  #반환을 할때는 리턴을 쓰고 

  return balance + money

def withdraw(balance, money):
    if balance >= money:
      print("출금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance - money))
      return balance - money

    else:
        print("출금이 완료되지 않았습니다. 잔액은{0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance,money): #저녁에 출금 
  commission = 100   #수수료 값 백원
  return balance, balance - money - commission   # 두개의 값을 리턴해서 함수에 넣어준다.

balance = 0  # 처음 계좌에는 돈이 없다.
balance = deposit(balance,1000);  # 뒤에 쓰는건 발란스에 들어가는 금액이다.
balance = withdraw(balance,2000)
balance = withdraw(balance , 500)

commission,balance = withdraw_night(balance , 500)
print("수수료는  {0} 원이며,잔액은 {1} 원 입니다.".format(commission , balance))
print(balance)

#출금 이부분 전체로 다시하기..


