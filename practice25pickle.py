# pickle  프로그램상에서 사용하는 데이터를 파일 형태로 저장하는것 누군가에게 파일을 주면 누가 받아서 쓰면됨

import pickle
# profile_file = open("profile.pickle", "wb")# 파일을 열때는 쓰기 목적인 w   b는 바이너리 타입인데 피클을 쓰기 위해서는 항상 b를 써줘야한다.
# profile = {"이름:":"박명수", "나이": "30","취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile 에 있는 정보를 file에 저장            1저장할 내용 2 어떤 파알을 쓸껀지 
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  #   파일에 있는 내용을 그대로 가지고와서 데이터 형태로 불러와준다.
print(profile)
profile_file.close()
