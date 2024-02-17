##4단계 컬러게임 화면을 흑백으로
##4-1 흑백처리 루틴
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

    key_code=cv2.waitKey(10)#3-2`
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
