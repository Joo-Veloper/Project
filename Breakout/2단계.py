## 2단계 각 함수들의 리턴값의 의미
##2-1
# import gym
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# env.reset()
# while True:
#     action=env.action_space.sample()#0-Noop,1-FIRE,2-RIGHT,3-LEFT
#     print('action=',action)
#     env.step(action)
# env.close()

##2-2 observation =게임의 환경변수
# import gym
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# observation=env.reset()#2-2
# print(type(observation))#2-2
# print('obs.shape=',(observation))#2-2 #게임장의 가로크기=210, 세로크기=160, 각셀당 색상수=3
# print(observation)#2-2
# while True:
#     action=env.action_space.sample()#0-Noop,1-FIRE,2-RIGHT,3-LEFT
#     print('action=',action)
#     env.step(action)
# env.close()

##2-3
# import gym
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# observation=env.reset()
# print(type(observation))
# print('obs.shaep=',(observation))
# print(observation)
# while True:
#     action=env.action_space.sample()
#     print('action=', action)  # 2-3
#     observation, reward, terminated, truncated = env.step(action)  # 2-3
#     print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)  # 2-3
#
# env.close()

##2-4
# import gym
#
# env = gym.make("BreakoutDeterministic-v4", render_mode="human")
# observation = env.reset()
# print(type(observation))
# print('obs.shaep=', (observation))
# print(observation)
# while True:
#     action = env.action_space.sample()
#     print('action=', action)
#     observation, reward, terminated, truncated = env.step(action)
#     print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)
#
#     if terminated==True:#2-4
#         print('스테이지가 끝났습니다.')#2-4
#         break#2-4
#
# env.close()

#2-5 환경변수확인 2단계 (최종)
import gym

env = gym.make("BreakoutDeterministic-v4", render_mode="human")
observation = env.reset()
print(type(observation))
print('obs.shape=', (observation))
print(observation)

stageNum=1##2-5
while True:
    action = env.action_space.sample()
    print('action=', action)  # 2-3
    observation, reward, terminated, truncated = env.step(action)  # 2-3
    print("observateion=", observation, 'reward=', reward, 'terminated=', terminated, 'truncated=', truncated)  # 2-3

    if terminated==True:
        stageNum+=1##2-5
        env.reset()##2-5
        print('스테이지가 끝났습니다.',stageNum)
        if stageNum>3:##2-5
            break

env.close()