# 좋은 서론은 분야가 겪는 문제에서 시작한다

**출처**: Vizzo, Guadagnino, Mersch, Wiesmann, Behley, Stachniss, 2023 — KISS-ICP: In Defense of Point-to-Point ICP — Simple, Accurate, and Robust Registration If Done the Right Way, IEEE Robotics and Automation Letters

---

## 발췌

초록 첫 세 문장:

> Robust and accurate pose estimation of a robotic platform, so-called sensor-based odometry, is an essential part of many robotic applications. While many sensor odometry systems made progress by adding more complexity to the ego-motion estimation process, we move in the opposite direction. By removing a majority of parts and focusing on the core elements, we obtain a surprisingly effective system that is simple to realize and can operate under various environmental conditions using different LiDAR sensors.

서론 둘째 단락의 첫 문장과 셋째 단락의 둘째·셋째 문장(가운데 생략):

> This paper returns to the roots: classical point-to-point ICP, introduced 30 years ago by Besl and McKay. … Our design uses neither sophisticated feature extraction techniques, learning methods, nor loop closures. The same parameter set works in various challenging scenarios such as highway drives of robot cars with many dynamic objects, drone flights, handheld devices, segways, and more.


---

## 한국어 의역

로봇의 자세를 강건하고 정확하게 추정하는 일, 곧 센서 기반 odometry는 여러 로봇 응용에 꼭 필요하다. 많은 odometry 시스템은 ego-motion(자기 움직임) 추정 과정에 복잡한 요소를 더하며 발전해 왔지만, 우리는 반대 방향으로 간다. 부품 대부분을 덜어 내고 핵심 요소에 집중해서, 구현하기 쉬우면서도 놀랄 만큼 잘 동작하는 시스템을 얻었다. 이 시스템은 여러 LiDAR 센서로 여러 환경에서 동작한다. 이 논문은 30년 전 Besl과 McKay가 제안한 고전적인 point-to-point ICP로 돌아간다. … 정교한 feature 추출 기법도, 학습 방법도, loop closure도 쓰지 않는다. 동적 물체가 많은 고속도로를 달리는 차량, 드론 비행, 손에 든 장치, segway 같은 까다로운 상황에서 같은 parameter 집합이 그대로 동작한다.

---

## 분석 — 왜 이 표현이 좋은가

초록 첫 문장은 센서 기반 odometry가 여러 로봇 응용에 꼭 필요한 부분이라고 짚는다("essential part of many robotic applications"). 둘째 문장은 기존 시스템들이 걸어온 방향을 adding more complexity로 요약한 다음, 문장 끝의 we move in the opposite direction에서 저자들의 방향을 밝힌다. 셋째 문장의 removing a majority of parts는 그 방향을 실제로 무엇을 했는지로 보여 준다. 그 뒤의 surprisingly effective와 simple to realize가 결과를 말한다. 문제, 기존 방법, 저자들의 선택이 세 문장 안에 차례로 들어 있다.

이 순서가 매끄럽게 읽히는 까닭은 문장 끝, 곧 강조 위치(stress position)에 강조할 말이 있기 때문이다. 둘째 문장 끝의 opposite direction이 다음 문장을 끌어내고, 셋째 문장에서는 그 방향이 removing a majority of parts라는 행동이 된다. 셋째 문장 끝의 different LiDAR sensors는 적용 범위를 말한다. Gopen과 Swan이 문장 단위로 설명한 reader expectation이 단락 전체에서 작동하는 예다.

부제 In Defense of Point-to-Point ICP(point-to-point ICP를 옹호하며)의 태도는 본문에도 이어진다. 저자들은 새 기법을 발명했다고 내세우지 않고, 오래된 기법을 제대로 쓰면 충분하다고 주장한다. 서론 둘째 단락 첫 문장 This paper returns to the roots: classical point-to-point ICP, introduced 30 years ago by Besl and McKay가 이 태도를 한 줄로 말한다. returns to the roots(뿌리로 돌아간다)라는 표현 덕분에 30년 된 알고리즘을 다시 쓰는 일이 근본으로 돌아가는 선택으로 읽힌다. 자기의 단순한 baseline을 옹호하고 싶은 후배가 빌려 쓸 만한 어조다.

초록 첫 세 문장은 Mensh와 Kording이 규칙 3에서 권한 context-content-conclusion(CCC) 순서로도 읽을 수 있다. 첫 문장이 분야를 정의하는 context이고, 둘째 문장이 기존 방향과 저자들의 방향을 대비하는 content이며, 셋째 문장이 단순한 시스템으로 충분하다는 conclusion이다. Ch.19에서 다룬 CCC가 실제 논문의 한 단락에 적용된 예다.

초록은 분야의 문제를 부풀리지 않는다. LiDAR odometry를 풀리지 않은 거대한 난제라고 하지 않고, 여러 로봇 응용에 필요한 부분이라고 담담하게 적는다. 제목, 부제, 초록 첫 두 문장, 서론 둘째 단락이 모두 같은 태도를 유지한다.

서론은 여섯 단락이다. 발췌한 두 단락 뒤의 넷째 단락은 주요 기여와 핵심 구성 요소(motion prediction, 공간 downsampling, robust kernel, adaptive threshold)를 밝히고, 다섯째 단락은 세 가지 핵심 주장을 내놓는다. 마지막 여섯째 단락은 공개 구현의 주소를 알려 준다. 다음 섹션 순서를 안내하는 문장은 없다. 서론 전체의 구성은 Ch.23 §23.5에서 다룬다.

---

## 따라 쓰기 — 자기 분야에 적용

시스템 논문의 서론 첫 단락을 쓸 때 이 순서를 빌려 볼 수 있다. "[분야의 과제]는 [응용]에 꼭 필요하다. 최근 연구는 [복잡한 도구 A, B, C]를 더해 왔다. 이 논문은 [단순한 baseline]을 제대로 쓰면 충분함을 보인다." 이 틀에 자기 분야의 명사를 넣으면 도입 단락의 첫 초고가 나온다. KISS-ICP의 we move in the opposite direction은 둘째 문장 안에서 방향 전환을 절 하나로 처리했다. 마지막 문장 끝에 무엇을 두어야 contribution이 가장 또렷한지 먼저 정하고, 그 낱말이 끝에 오도록 문장을 짜 본다.

분량도 따라 해 볼 만하다. KISS-ICP 초록은 문제와 기존 방법에 한 문장씩 쓰고, 나머지 문장을 저자들의 방법과 결과에 쓴다. 자기 baseline을 정면으로 옹호하고 싶다면 In Defense of …, returns to the roots, we move in the opposite direction 같은 구문을 참고한다.

---

## 출처
- `vizzo-2023-kiss` — Vizzo, I., Guadagnino, T., Mersch, B., Wiesmann, L., Behley, J., Stachniss, C., 2023. KISS-ICP: In Defense of Point-to-Point ICP — Simple, Accurate, and Robust Registration If Done the Right Way. IEEE Robotics and Automation Letters 8(2): 1029-1036. arXiv:2209.15397.

---
