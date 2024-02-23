# Breakout 예상 경로 스스로 동작

이 프로젝트는 Breakout 게임에서의 예상 경로를 여러 경우로 학습시킨 후, 자동으로 블록을 모두 깨뜨릴 때까지 동작하는 알고리즘을 개발하는 것을 목표로 합니다. 학습된 모델은 게임의 상태를 인식하고 최적의 행동을 예측하여, 자동으로 게임을 진행합니다.


<img src="https://github.com/Joo-Veloper/Project/assets/134623719/200e2d4b-ab7b-45ad-b621-47fd7b29c7b9" width="500">


# 환경 설정
본 프로젝트는 Python과 여러 외부 라이브러리를 사용합니다. 아래는 프로젝트를 시작하기 위해 필요한 환경 설정 단계입니다.
Python 가상 환경 생성 : 이 명령어는 atari라는 이름의 Python 가상 환경을 생성합니다. Python의 버전은 3.6.13으로 설정됩니다.
```
conda create -n atari python==3.6.13
```

필요한 라이브러리 설치:이러한 라이브러리들은 게임 환경을 구성하고, 이미지 처리 및 시각화를 위해 필요합니다.
```
pip install gym[atari]
pip install autorom[accept-rom-license]
pip install scikit-image
pip install pyqt5==5.15.6
pip install pyqtgraph==0.11.1
```

참고 문서
프로젝트 진행 중 필요한 추가 정보 및 상세한 설명은 다음 문서를 참조하십시오:

Gym Library Documentation -> https://www.gymlibrary.dev/
이 문서는 OpenAI Gym 라이브러리의 공식 문서로, 다양한 시뮬레이션 환경을 제공하고, 이를 활용한 강화학습 알고리즘 개발에 대한 가이드를 제공합니다.

실행 방법
환경 설정이 완료된 후, 개발한 알고리즘을 실행하여 Breakout 게임의 예상 경로를 학습시키고 자동으로 게임을 진행할 수 있습니다. 학습 과정과 결과를 관찰하며, 알고리즘의 성능을 평가하고 개선할 수 있습니다.



