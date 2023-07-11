##12
##12-1
# import gym
# import cv2
# import numpy as np #4-1
#
# def get_crosspt(x11,y11,x12,y12,x21,y21,x22,y22):#9-1
#     if x12==x11 or x22==x21:#9-1
#         print('data x=0')#9-1
#         return -1,-1#9-1
#     m1=(y12-y11)/(x12-x11)#9-1
#     m2=(y22-y21)/(x22-x21)#9-1
#     if m1==m2:#9-1
#         print('parallel')#9-1
#         return-1,-1#9-1
#     cx=(x11*m1-y11-x21*m2+y21)/(m1-m2)#9-1
#     cy=m1*(cx-x11)+y11#9-1
#
#     return cx,cy
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
# que=[]#8-1
# hori_cx,hori_cy=0,0 #10-1
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
#     ##8-1 공의 방향 구하기
#     if xCenter !=0 or yCenter !=0:#8-1
#         que.append((xCenter,yCenter))#8-1
#
#     if len(que)>=6:#8-1
#         q=que.pop(0)#8-1
#     #     print('que=',q)#8-1
#     #     print(que[0],que[1],que[2],que[3],que[4])#8-1
#     #     print('q[0]:(',que[0][0],que[0][1],')')#8-1
#     #     print('q[4]:(',que[4][0],que[4][1],')')#8-1
#
#     #8-2 우하 좌하, 우상 좌상 4개로만 구분
#     #8-2 아래로 내려오는 공, Y방향이 증가
#     # if len(que)>=5:#8-2
#     #     if que[0][0]-que[4][0]>0:#8-2
#     #         print('올라가는공',end='')#8-2
#     #         action=0#8-2
#     #     if que[0][0]-que[4][0]<0:#8-2
#     #         print('내려가는',end='')#8-2
#     #         if que[0][1]-que[4][1]>0:#8-2
#     #             print('좌향 공',end='')#8-2
#     #             action=3#8-2
#     #         elif que[0][1]-que[4][1]<0:#8-2
#     #             print('우향 공',end='')#8-2
#     #             action=2#8-2
#     #         else:#8-2
#     #             print('가운데 공',end='')#8-2
#     #             action=0#8-2
#     #     else:#8-2
#     #         print('수평유지중',end='')#8-2
#     #         action=0#8-2
#
#     ##8-3 공의 중점을 구하고 큐에저정된 데이터를 선분으로 그리기,예상 경로/방향 그리기
#         cv2.line(img4, (que[0][1], que[0][0]), (que[4][1], que[4][0]), (255, 255, 255), thickness=1)
#     #8-3 공 주변에 테두리 그리기
#         cv2.rectangle(img4,(yCenter-4,xCenter-3),(yCenter+4,xCenter+3),(128,128,128),1)
#
#         # img44=cv2.resize(img4,(480,480),interpolation=cv2.INTER_NEAREST)
#         # cv2.imshow('Frame4',img44)
#
#         x12=que[0][1]#9-1
#         y12=que[0][0]#9-1
#         x11=que[4][1]#9-1
#         y11=que[4][0]#9-1
#
#         x21=1#9-1 #수평선
#         y21=71#9-1
#         x22=189#9-1
#         y22=72#9-1
#         if x11>5:#9-1
#             hori_cx, hori_cy=get_crosspt(x11, y11, x12, y12, x21, y21, x22, y22)#9-1
#             if hori_cx != -1 and hori_cy!=-1:#9-1
#                 cv2.rectangle(img4, (int(hori_cx)-4,int(hori_cy)-3),(int(hori_cx)+4,int(hori_cy)+3),(128,128,128),1)#9-1
#                 cv2.line(img4, (yCenter, xCenter), (int(hori_cx), int(hori_cy)), (255, 255, 255), thickness=1)#9-1
#                 img44=cv2.resize(img4,(480,480),interpolation=cv2.INTER_NEAREST)#9-1
#
#         #img44=cv2.resize(img4,480,480),interpolation=cv2.INTER_NEAREST)#9-1
#         cv2.imshow('Frame4',img44)#9-1
#     ##7-1막대위치 구하기
#     barImage=img2[144:147,10:200]#7-1
#     cv2.imshow('Bar Image',barImage)#7-1
#
#     ##7-2 점들의 숫자값을 출력해보고 숫자가 낮은 것은 if문에서 제거함(텍스트 출력 루틴)
#     # for i in range(3):#7-2
#     #     for j in range(1,189):#7-2
#     #         if barImage[i,j]>=100:#7-2
#     #             print('1',end='')#7-2
#     #         else:#7-2
#     #             print('.',end='')#7-2
#     #     print()#7-2
#     # print()#7-2
#     #7-3 막대위치 중심
#     barXCenter = 0  # 7-3
#     barYCenter = 0  # 7-3
#     countGerm = 0  # 7-3
#
#     for i in range(3):  # 7-3
#         for j in range(1, 189):  # 7-3
#             if barImage[i, j] >= 100:  # 7-3
#                 barXCenter += i  # 7-3
#                 barYCenter += j  # 7-3
#                 countGerm += 1  # 7-3
#     if countGerm > 0:  # 7-3
#         barXCenter = barXCenter // countGerm  # 7-3
#         barYCenter = barYCenter // countGerm  # 7-3
#         print('barXCenter=', barXCenter, 'barYCenter=', barYCenter)  # 7-3
#     else:  # 7-3
#         print('막대없음')  # 7-3
#
#     #12 벽면에 부딪히는 경우에 대한 처리
#     if hori_cx<0:
#         print('원래 hori_cx=:',hori_cx,end="")
#         hori_cx=abs(hori_cx)
#         print('horiz<=0',barXCenter,'hori_cx=',hori_cx,'dir=',dir['left'],'action=',action)
#     if hori_cx>189:
#         print('원래 hori_cx=:',hori_cx,end="")
#         hori_cx=hori_cx-2*(hori_cx-189)
#         print('horiz>189=',barXCenter,'hori_cx=',hori_cx,'dir=',dir['right'],'action=',action)
#
#
#     ## 10-1
#     ##11-1
#     ##공의 예상 위치에 막대 이동하기
#     ##공의 예상 위치 근처에서 막대 흔들림 방지
#     dir={'noop':0,'fire':1, 'right':2,'left':3}#10-1
#     if barYCenter>hori_cx and abs(barYCenter-hori_cx)>=10:#11-1
#         action=dir['left']#10-1
#     elif barYCenter < hori_cx and abs(barYCenter-hori_cx)>=10:#11-1
#         action=dir['right']#10-1
#     else:#10-1
#         action=dir['noop']#10-1
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

#12-2
import gym
import cv2
import numpy as np #4-1

def get_crosspt(x11,y11,x12,y12,x21,y21,x22,y22):#9-1
    if x12==x11 or x22==x21:#9-1
        print('data x=0')#9-1
        return -1,-1#9-1
    m1=(y12-y11)/(x12-x11)#9-1
    m2=(y22-y21)/(x22-x21)#9-1
    if m1==m2:#9-1
        print('parallel')#9-1
        return-1,-1#9-1
    cx=(x11*m1-y11-x21*m2+y21)/(m1-m2)#9-1
    cy=m1*(cx-x11)+y11#9-1

    return cx,cy
# env = gym.make("BreakoutDeterministic-v4", render_mode="human")
env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")

observation = env.reset()
#print(type(observation))
#print('obs.shaep=', (observation.shape))
#print(observation)

action=0#3-2
stageNum=1
que=[]#8-1
hori_cx,hori_cy=0,0 #10-1
inPlay=False#12
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


    if countGerm>0:#12-2
        xCenter=xCenter//countGerm#12-2
        yCenter=yCenter//countGerm#12-2
        #print('xCenter=',xCenter,'yCenter=',yCenter)#12-2
        inPlay=True#12-2
    else:#12-2
        #print('공없음')
        inPlay=False#12-2
    ##8-1 공의 방향 구하기
    if xCenter !=0 or yCenter !=0:#8-1
        que.append((xCenter,yCenter))#8-1

    if len(que)>=6:#8-1
        q=que.pop(0)#8-1
    #     print('que=',q)#8-1
    #     print(que[0],que[1],que[2],que[3],que[4])#8-1
    #     print('q[0]:(',que[0][0],que[0][1],')')#8-1
    #     print('q[4]:(',que[4][0],que[4][1],')')#8-1

    #8-2 우하 좌하, 우상 좌상 4개로만 구분
    #8-2 아래로 내려오는 공, Y방향이 증가
    # if len(que)>=5:#8-2
    #     if que[0][0]-que[4][0]>0:#8-2
    #         print('올라가는공',end='')#8-2
    #         action=0#8-2
    #     if que[0][0]-que[4][0]<0:#8-2
    #         print('내려가는',end='')#8-2
    #         if que[0][1]-que[4][1]>0:#8-2
    #             print('좌향 공',end='')#8-2
    #             action=3#8-2
    #         elif que[0][1]-que[4][1]<0:#8-2
    #             print('우향 공',end='')#8-2
    #             action=2#8-2
    #         else:#8-2
    #             print('가운데 공',end='')#8-2
    #             action=0#8-2
    #     else:#8-2
    #         print('수평유지중',end='')#8-2
    #         action=0#8-2

    ##8-3 공의 중점을 구하고 큐에저정된 데이터를 선분으로 그리기,예상 경로/방향 그리기
        cv2.line(img4, (que[0][1], que[0][0]), (que[4][1], que[4][0]), (255, 255, 255), thickness=1)
    #8-3 공 주변에 테두리 그리기
        cv2.rectangle(img4,(yCenter-4,xCenter-3),(yCenter+4,xCenter+3),(128,128,128),1)

        # img44=cv2.resize(img4,(480,480),interpolation=cv2.INTER_NEAREST)
        # cv2.imshow('Frame4',img44)

        x12=que[0][1]#9-1
        y12=que[0][0]#9-1
        x11=que[4][1]#9-1
        y11=que[4][0]#9-1

        x21=1#9-1 #수평선
        y21=71#9-1
        x22=189#9-1
        y22=72#9-1
        if x11>5:#9-1
            hori_cx, hori_cy=get_crosspt(x11, y11, x12, y12, x21, y21, x22, y22)#9-1
            if hori_cx != -1 and hori_cy!=-1:#9-1
                cv2.rectangle(img4, (int(hori_cx)-4,int(hori_cy)-3),(int(hori_cx)+4,int(hori_cy)+3),(128,128,128),1)#9-1
                cv2.line(img4, (yCenter, xCenter), (int(hori_cx), int(hori_cy)), (255, 255, 255), thickness=1)#9-1
                img44=cv2.resize(img4,(480,480),interpolation=cv2.INTER_NEAREST)#9-1

        #img44=cv2.resize(img4,480,480),interpolation=cv2.INTER_NEAREST)#9-1
        cv2.imshow('Frame4',img44)#9-1
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
    dir = {'noop': 0, 'fire': 1, 'right': 2, 'left': 3}  # 10-1

    #12-1  벽면에 부딪히는 경우에 대한 처리
    if inPlay==True:#12-2
        if hori_cx<0:#12-1
            print('원래 hori_cx=:',hori_cx,end="")
            hori_cx=abs(hori_cx)
            print('horiz<=0',barXCenter,'hori_cx=',hori_cx,'dir=',dir['left'],'action=',action)
        if hori_cx>189:
            print('원래 hori_cx=:',hori_cx,end="")
            hori_cx=hori_cx-2*(hori_cx-188)
            print('horiz>189=',barXCenter,'hori_cx=',hori_cx,'dir=',dir['right'],'action=',action)
        if barYCenter>hori_cx and abs(barYCenter-hori_cx)>=10:
            action=dir['left']
        elif barYCenter < hori_cx and abs(barYCenter - hori_cx) >= 10:  # 11-1
            action = dir['right']  # 10-1
        else:  # 10-1
            action = dir['noop']  # 10-1
    else:
        action=dir['noop']
    ## 10-1
    ##11-1
    ##공의 예상 위치에 막대 이동하기
    ##공의 예상 위치 근처에서 막대 흔들림 방지
    if barYCenter>hori_cx and abs(barYCenter-hori_cx)>=10:#11-1
        action=dir['left']#10-1
    elif barYCenter < hori_cx and abs(barYCenter-hori_cx)>=10:#11-1
        action=dir['right']#10-1
    else:#10-1
        action=dir['noop']#10-1


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