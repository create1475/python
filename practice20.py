#지역변수 전역변수

gun = 10

def checkpoint(solidiers):

  global gun  # 이건 전역 공간에 있는 gun사용 
  gun = gun - solidiers
  print("[함수 내]  남은 총 : {0}".format(gun))


  def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내]  남은 총 : {0}".format(gun)) # 
    return gun # 리턴을 던짐으로써 건의 값이 바뀐다.

print("[전체 총]  남은 총 : {0}".format(gun))
checkpoint(2)
print("[남은총]  남은 총 : {0}".format(gun))


#전역변수는 잘 사용하지 않음
