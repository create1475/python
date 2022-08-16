# # 마린 :공격유닛 ,군인, 총을 쏠수있음

# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력{0},공격력{1}\n".format(hp,damage))


# #탱크 = 공격유닛 탱크 포를 쏠수있는데 일반모드가 시즈모즈가 있다.
# tank_name="탱크"
# tank_hp = 150
# tank_damage=35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력{0},공격력{1}\n".format(tank_hp,tank_damage))

# def attack(name,location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다.[공격력{2}]".format(\
#       name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)      



# #만약에 탱크가 한마리 더 추가된다면?

# tank2_name="탱크"
# tank2_hp = 150
# tank2_damage=35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력{0},공격력{1}\n".format(tank2_hp,tank2_damage))




# from ctypes.wintypes import HPALETTE
# from unicodedata import name


# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력{0},공격력{1}".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",150,35)
# tank = Unit("탱크",150,35)



# wraith1 = Unit("레이스",80,5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))# ..이걸로 클래스 내부에 있는걸 접근할수 있다.

# wraith2 = Unit("레이스",80,5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))



class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 {2}]".format(\
            self.name,location,self.damage))#여기는 location앞에 self적지 않는다.셀프는 자기자신을 의미 클래스 내에서는 항상 self를 무조건 적는다. location은 전달받은 값을 쓴다는 의미이다.
    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재체력은{1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} :파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")
firebat1.damaged(25)#두번 공격받는다고 가정
firebat1.damaged(25)


#메딕 의무병을 의미

#class AttackUnit:
#    def __init__(self, name, hp, damage):
#           self.name = name
#           self.hp = hp
#           self.damage = damage
#
#class Unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#두개의 클래스에서 name 와hp가 같이 있으니까 상속이란걸 쓸수있다.

#상속받는 방법 
#class AttatckUnit(unit):  이게 파이썬 상속받는 방법

#부모클래스 두개 이상 상속받는걸 다중상속이라고 한다.

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다.[속도 : {2}]".format(name,location,self.flying_speed))

class FlyableAttackunit(AttackUnit,Flyable):#이건 콤마로 구분하면서 다중상속 받는 방법
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,damage)
        Flyable.__init__(self,flying_speed)#이거 두개가 한것은 어택유닛과 플라이어블 클래스를 상속받아서 초기화를 해준것이다.


valkyrie = FlyableAttackunit("발키리",200,6,5)
valkyrie.fly(valkyrie.name,"3시")
