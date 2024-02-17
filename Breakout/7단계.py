##7단계 막대 위치 구하기
##7-1
# import gym
# import cv2
# import numpy as np #4-1
# # env = gym.make("BreakoutDeterministic-v4", render_mode="human")
# env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")
#
# observation = env.reset()
# #print(type(observation))
# #print('obs.shaep=', (observation.shape))
# #print(observation)
#
# action=0#3-2
# stageNum=1
# while True:
#     #action = env.action_space.sample()
#     print('action=', action)
#     observation, reward, terminated, truncated = env.step(action)
#     #print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)
#
#     action=0 #3-4
#
#     shape=(210,160)#가로세로 모양 #3-3
#     img=cv2.resize(observation,shape,interpolation=cv2.INTER_CUBIC)#3-3
#     cv2.imshow('Frame',img)
#
#     ###4-1흑백으로 처리하는 루틴
#     frame=img.astype(np.uint8)#4-1
#     img2=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)#4-1
#
#     img22=cv2.resize(img2,(480,480),interpolation=cv2.INTER_NEAREST)#4-1
#     cv2.imshow("Frame2",img22)#4-1
#
#     ###5-1필요부분만 잘라내기
#     ###주변 떼어내고 순전히 필드만 나타낸 범위
#     img3 = img2[24:148, 10:200]  # 5 테두리 없이 필요부분만 잘라내기#5-1
#     img3=cv2.resize(img3,(480,480),interpolation=cv2.INTER_NEAREST)#5-1
#     cv2.imshow("Frame3",img3)#5-1
#
#     img4 = img2[71:148, 10:200]  # 5-2
#     img44 = cv2.resize(img4, (480, 480), interpolation=cv2.INTER_NEAREST)  # 5-2
#     cv2.imshow("Frame4", img44)  # 5-2
#
#     #공의 위치 구하기#6-1
#     # for i in range(73):#6-1
#     #     for j in range(1,189):#6-1
#     #         if img4[i,j]!=0:#6-1
#     #             print('x',end='')#6-1
#     #         else:#6-1
#     #             print('.',end='')#6-1
#     #     print()#6-1
#
#     xCenter=0#6-2
#     yCenter=0#6-2
#     countGerm=0#6-2
#
#     #공의 위치 구하기 #6-2
#     for i in range(1,73):#6-2
#         for j in range(1,189):#6-2
#             if img4[i,j]>=100:#6-2
#                 xCenter+=i#6-2
#                 yCenter+=j#6-2
#                 countGerm+=1#6-2
#     if countGerm>0:#6-2
#         xCenter=xCenter//countGerm#6-2
#         yCenter=yCenter//countGerm#6-2
#         print('xCenter=',xCenter,'yCenter=',yCenter)#6-2
#
#     ##7-1막대위치 구하기
#     barImage=img2[144:147,10:200]#7-1
#     cv2.imshow('Bar Image',barImage)#7-1
#
#
#     key_code=cv2.waitKey(10)#3-2
#     print('key_code=',key_code)#3-2
#
#     if key_code==ord('a') or key_code==ord('A'):#3-2
#         print('A key pressed')#3-2
#         action=3#3-2
#     elif key_code==ord('d')or key_code==ord('D'):#3-2
#         print('D key pressed')#3-2
#         action=2#3-2
#     elif key_code==ord('s')or key_code==ord('S'):#3-2
#         print('S key pressed')#3-2
#         action=1#3-2
#
#     if key_code & 0xFF==27:#3-2
#         break#3-2
#
#     if terminated==True:
#         stageNum+=1
#         env.reset()
#         print('스테이지가 끝났습니다.',stageNum)
#         if stageNum>3:
#             break
#
# env.close()

##7-2
# import gym
# import cv2
# import numpy as np #4-1
# # env = gym.make("BreakoutDeterministic-v4", render_mode="human")
# env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")
#
# observation = env.reset()
# #print(type(observation))
# #print('obs.shaep=', (observation.shape))
# #print(observation)
#
# action=0#3-2
# stageNum=1
# while True:
#     #action = env.action_space.sample()
#     print('action=', action)
#     observation, reward, terminated, truncated = env.step(action)
#     #print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)
#
#     action=0 #3-4
#
#     shape=(210,160)#가로세로 모양 #3-3
#     img=cv2.resize(observation,shape,interpolation=cv2.INTER_CUBIC)#3-3
#     cv2.imshow('Frame',img)
#
#     ###4-1흑백으로 처리하는 루틴
#     frame=img.astype(np.uint8)#4-1
#     img2=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)#4-1
#
#     img22=cv2.resize(img2,(480,480),interpolation=cv2.INTER_NEAREST)#4-1
#     cv2.imshow("Frame2",img22)#4-1
#
#     ###5-1필요부분만 잘라내기
#     ###주변 떼어내고 순전히 필드만 나타낸 범위
#     img3 = img2[24:148, 10:200]  # 5 테두리 없이 필요부분만 잘라내기#5-1
#     img3=cv2.resize(img3,(480,480),interpolation=cv2.INTER_NEAREST)#5-1
#     cv2.imshow("Frame3",img3)#5-1
#
#     img4 = img2[71:148, 10:200]  # 5-2
#     img44 = cv2.resize(img4, (480, 480), interpolation=cv2.INTER_NEAREST)  # 5-2
#     cv2.imshow("Frame4", img44)  # 5-2
#
#     #공의 위치 구하기#6-1
#     # for i in range(73):#6-1
#     #     for j in range(1,189):#6-1
#     #         if img4[i,j]!=0:#6-1
#     #             print('x',end='')#6-1
#     #         else:#6-1
#     #             print('.',end='')#6-1
#     #     print()#6-1
#
#     xCenter=0#6-2
#     yCenter=0#6-2
#     countGerm=0#6-2
#
#     #공의 위치 구하기 #6-2
#     for i in range(1,73):#6-2
#         for j in range(1,189):#6-2
#             if img4[i,j]>=100:#6-2
#                 xCenter+=i#6-2
#                 yCenter+=j#6-2
#                 countGerm+=1#6-2
#     if countGerm>0:#6-2
#         xCenter=xCenter//countGerm#6-2
#         yCenter=yCenter//countGerm#6-2
#         print('xCenter=',xCenter,'yCenter=',yCenter)#6-2
#
#     ##7-1막대위치 구하기
#     barImage=img2[144:147,10:200]#7-1
#     cv2.imshow('Bar Image',barImage)#7-1
#
#     ##7-2 점들의 숫자값을 출력해ㅂ고 숫자가 낮은 것은 if문에서 제거함(텍스트 출력 루틴)
#     # for i in range(3):#7-2
#     #     for j in range(1,189):#7-2
#     #         if barImage[i,j]>=100:#7-2
#     #             print('1',end='')#7-2
#     #         else:#7-2
#     #             print('.',end='')#7-2
#     #     print()#7-2
#     # print()#7-2
#
#     key_code=cv2.waitKey(10)#3-2
#     print('key_code=',key_code)#3-2
#
#     if key_code==ord('a') or key_code==ord('A'):#3-2
#         print('A key pressed')#3-2
#         action=3#3-2
#     elif key_code==ord('d')or key_code==ord('D'):#3-2
#         print('D key pressed')#3-2
#         action=2#3-2
#     elif key_code==ord('s')or key_code==ord('S'):#3-2
#         print('S key pressed')#3-2
#         action=1#3-2
#
#     if key_code & 0xFF==27:#3-2
#         break#3-2
#
#     if terminated==True:
#         stageNum+=1
#         env.reset()
#         print('스테이지가 끝났습니다.',stageNum)
#         if stageNum>3:
#             break
#
# env.close()

##7-3 바의 위치 중점계산(최종)
import gym
import cv2
import numpy as np #4-1
# env = gym.make("BreakoutDeterministic-v4", render_mode="human")
env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")

observation = env.reset()
#print(type(observation))
#print('obs.shaep=', (observation.shape))
#print(observation)

action=0#3-2
stageNum=1
while True:
    #action = env.action_space.sample()
    print('action=', action)
    observation, reward, terminated, truncated = env.step(action)
    #print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)

    action=0 #3-4

    shape=(210,160)#가로세로 모양 #3-3
    img=cv2.resize(observation,shape,interpolation=cv2.INTER_CUBIC)#3-3
    cv2.imshow('Frame',img)

    ###4-1흑백으로 처리하는 루틴
    frame=img.astype(np.uint8)#4-1
    img2=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)#4-1

    img22=cv2.resize(img2,(480,480),interpolation=cv2.INTER_NEAREST)#4-1
    cv2.imshow("Frame2",img22)#4-1

    ###5-1필요부분만 잘라내기
    ###주변 떼어내고 순전히 필드만 나타낸 범위
    img3 = img2[24:148, 10:200]  # 5 테두리 없이 필요부분만 잘라내기#5-1
    img3=cv2.resize(img3,(480,480),interpolation=cv2.INTER_NEAREST)#5-1
    cv2.imshow("Frame3",img3)#5-1

    img4 = img2[71:148, 10:200]  # 5-2
    img44 = cv2.resize(img4, (480, 480), interpolation=cv2.INTER_NEAREST)  # 5-2
    cv2.imshow("Frame4", img44)  # 5-2

    #공의 위치 구하기#6-1
    # for i in range(73):#6-1
    #     for j in range(1,189):#6-1
    #         if img4[i,j]!=0:#6-1
    #             print('x',end='')#6-1
    #         else:#6-1
    #             print('.',end='')#6-1
    #     print()#6-1

    xCenter=0#6-2
    yCenter=0#6-2
    countGerm=0#6-2

    #공의 위치 구하기 #6-2
    for i in range(1,73):#6-2
        for j in range(1,189):#6-2
            if img4[i,j]>=100:#6-2
                xCenter+=i#6-2
                yCenter+=j#6-2
                countGerm+=1#6-2
    if countGerm>0:#6-2
        xCenter=xCenter//countGerm#6-2
        yCenter=yCenter//countGerm#6-2
        print('xCenter=',xCenter,'yCenter=',yCenter)#6-2



    ##7-1막대위치 구하기
    barImage=img2[144:147,10:200]#7-1
    cv2.imshow('Bar Image',barImage)#7-1

    ##7-2 점들의 숫자값을 출력해보고 숫자가 낮은 것은 if문에서 제거함(텍스트 출력 루틴)
    # for i in range(3):#7-2
    #     for j in range(1,189):#7-2
    #         if barImage[i,j]>=100:#7-2
    #             print('1',end='')#7-2
    #         else:#7-2
    #             print('.',end='')#7-2
    #     print()#7-2
    # print()#7-2
    #7-3 막대위치 중심
    barXCenter = 0  # 7-3
    barYCenter = 0  # 7-3
    countGerm = 0  # 7-3

    for i in range(3):  # 7-3
        for j in range(1, 189):  # 7-3
            if barImage[i, j] >= 100:  # 7-3
                barXCenter += i  # 7-3
                barYCenter += j  # 7-3
                countGerm += 1  # 7-3
    if countGerm > 0:  # 7-3
        barXCenter = barXCenter // countGerm  # 7-3
        barYCenter = barYCenter // countGerm  # 7-3
        print('barXCenter=', barXCenter, 'barYCenter=', barYCenter)  # 7-3
    else:  # 7-3
        print('막대없음')  # 7-3


    key_code=cv2.waitKey(10)#3-2
    print('key_code=',key_code)#3-2

    if key_code==ord('a') or key_code==ord('A'):#3-2
        print('A key pressed')#3-2
        action=3#3-2
    elif key_code==ord('d')or key_code==ord('D'):#3-2
        print('D key pressed')#3-2
        action=2#3-2
    elif key_code==ord('s')or key_code==ord('S'):#3-2
        print('S key pressed')#3-2
        action=1#3-2

    if key_code & 0xFF==27:#3-2
        break#3-2

    if terminated==True:
        stageNum+=1
        env.reset()
        print('스테이지가 끝났습니다.',stageNum)
        if stageNum>3:
            break

env.close()