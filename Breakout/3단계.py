# #3-1
# import gym
# import cv2 #3-1
# # env = gym.make("BreakoutDeterministic-v4", render_mode="human")
# env = gym.make("BreakoutNoFrameskip-v4", render_mode="human") #3-1
#
# observation = env.reset()
# print(type(observation))
# print('obs.shaep=', (observation.shape))
# print(observation)
#
# stageNum=1
# while True:
#     action = env.action_space.sample()
#     print('action=', action)
#     observation, reward, terminated, truncated = env.step(action)
#     print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)
#
#     if terminated==True:
#         stageNum+=1
#         env.reset()
#         print('스테이지가 끝났습니다.',stageNum)
#         if stageNum>3:
#             break
#
# env.close()
#
# #3-2
# import gym
# import cv2
# # env = gym.make("BreakoutDeterministic-v4", render_mode="human")
# env = gym.make("BreakoutNoFrameskip-v4", render_mode="human")
#
# observation = env.reset()
# print(type(observation))
# print('obs.shaep=', (observation.shape))
# print(observation)
#
# action=0#3-2
# stageNum=1
# while True:
#     action = env.action_space.sample()
#     print('action=', action)
#     observation, reward, terminated, truncated = env.step(action)
#     print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)
#
#     key_code=cv2.waitKey(10)#3-2
#     print("key_code=",key_code)#3-2
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
#
# #3-3
# import gym
# import cv2
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
#     shape=(210,160)#가로세로 모양 #3-3
#     img=cv2.resize(observation,shape,interpolation=cv2.INTER_CUBIC)#3-3
#     cv2.imshow('Frame',img)
#
#     key_code=cv2.waitKey(10)#3-2
#     print("key_code=",key_code)#3-2
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

#3-4 cv2의 키보드 기능 이용하기 (최종)
import gym
import cv2#3
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


