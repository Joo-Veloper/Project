##1-1(실행되는지 확인)
# import gym
#
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# env.reset()
# env.close()

##1-2 time를 이용한 sleep (3초간 기다렸다가 종료)
# import gym
# import time #1-2
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# env.reset()
# env.close()
# time.sleep(3) #1-2

##1-3 step함수사용(오른쪽 작동후 끝)
# import gym
# import time
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# env.reset()
# env.step(2)#1-3
# env.close()
# time.sleep(3)

##1-4 한번에 명령구조가 아닌 순환구조를 가져야한다.
# import gym
# import time
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# env.reset()
# while True: #1-4
#     env.step(2)
# env.close()
# time.sleep(3)

##1-5 게임 시작 명령
# import gym
# import time
# env=gym.make("BreakoutDeterministic-v4",render_mode="human")
# env.reset()
# env.step(1)#1-5
# while True:
#     env.step(3)
# env.close()
# time.sleep(3)

##1-6 #공이 나오게 하는 함수(동작은 하지만 제어 불가 가장 기본형태)1단계atari Break-step1
import gym
env=gym.make("BreakoutDeterministic-v4",render_mode="human")
env.reset()
while True:
    env.step(env.action_space.sample())
env.close()
