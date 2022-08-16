# with --
# import pickle
# 

# with open("profile.pickle","rb") as profile_file:   # 앞예제에서 만든 프로파일.피클 파일을 여는데 열때는 읽기형식인 r로 열고 피클이니까 b적어죽
#   # 이 파일 정보를 profile_file에 저장하는거다.
#   print(pickle.load(profile_file))  #피클.로드를 통해서 프로파일이라는 내용을 읽어올수 있는거다.

# #with 문은 close할것없이 자동으로 탈출해준다.



# 피클을 사용하지 않고 with를 활용해서 파일을 쓰고 읽는걸 하는것 
#with open("study.txt","w",encoding="utf8") as study_file: # study라는 텍스트 파일을 w형식으로 불러오고 그걸 study_file 에 관한 변수에 저장 
#   study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf-8") as study_file: # 파일 쓰는 거 읽는거 두문장으로 가능함 매번 import안해줘서 편리함은 있다.
    print(study_file.read())
    