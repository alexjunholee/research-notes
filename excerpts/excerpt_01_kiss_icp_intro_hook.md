# 좋은 서론은 분야의 통증에서 시작한다

**출처**: Vizzo, Guadagnino, Mersch, Wiesmann, Behley, Stachniss, 2023 — *KISS-ICP: In Defense of Point-to-Point ICP — Simple, Accurate, and Robust Registration If Done the Right Way*, IEEE Robotics and Automation Letters

---

## 발췌

Abstract 도입부:

> Robust and accurate pose estimation of a robotic platform, so-called sensor-based odometry, is an essential part of many robotic applications. While many sensor odometry systems made progress by adding more complexity to the ego-motion estimation process, we move in the opposite direction. By removing a majority of parts and focusing on the core elements, we obtain a surprisingly effective system that is simple to realize and can operate under various environmental conditions using different LiDAR sensors.

Introduction body가 같은 3-beat를 반복:

> This paper returns to the roots: classical point-to-point ICP, introduced 30 years ago by Besl and McKay. … Our design uses neither sophisticated feature extraction techniques, learning methods, nor loop closures. The same parameter set works in various challenging scenarios such as highway drives of robot cars with many dynamic objects, drone flights, handheld devices, segways, and more.


---

## 한국어 의역

로봇의 자세를 정확하고 강건하게 추정하는 일, 즉 센서 기반 odometry는 수많은 로봇 응용의 본질적 구성요소다. 대다수 odometry 시스템은 ego-motion 추정 파이프라인에 복잡함을 *더해* 발전해 왔지만, 우리는 반대 방향으로 간다. 부품을 *덜어내고* 핵심에만 집중함으로써, 다양한 LiDAR 센서와 다양한 환경에서 동작하는 놀랄 만큼 단순하고 효과적인 시스템을 얻는다. 이 논문은 30년 전 Besl과 McKay가 제안한 *고전적 point-to-point ICP*로 돌아간다. feature 추출, 학습 모듈, loop closure 어느 것도 쓰지 않는다. 같은 parameter 집합이 자율주행 고속도로, 드론, 핸드헬드, segway 모두에서 동작한다.

---

## 분석 — 왜 이 표현이 좋은가

논문의 abstract와 introduction이 함께 도입의 정석을 보여 준다. 짧은 폭 안에 분야 통증, 기존 방법의 누적된 복잡함, 자신들의 단순한 해법이 차례로 놓인다. abstract 첫 문장은 LiDAR odometry가 모바일 로보틱스의 핵심 기능임을 짚는다("essential part of many robotic applications"). 두 번째 문장이 기존 방향성을 한 호흡으로 요약한다 — *adding more complexity*. 그리고 같은 문장 끝에 반전 동사가 등장한다 — *we move in the opposite direction*. 이 한 문장 안에 통증·기존 흐름·우리의 자세가 모두 들어 있다. 다음 문장의 *removing a majority of parts*가 그 자세를 행동으로 풀어내고, 마지막에 contribution 형용사 *surprisingly effective*, *simple*이 강조 자리에 놓인다.

3-beat가 깔끔히 작동하는 이유는 강조 위치(stress position)에 강조거리가 정확히 놓여 있기 때문이다. 두 번째 문장의 끝, 독자가 가장 오래 기억하는 위치에 *opposite direction*이 놓여 다음 문장의 동력을 만든다. 그 다음 문장의 끝에는 *simple to realize* 등 contribution claim이 정확히 자리 잡는다. 한 문장의 stress position이 다음 문장의 topic position으로 이어지는 old-before-new 사슬이 단락 전체를 끌고 간다. Gopen과 Swan이 말한 reader expectation의 단락 단위 적용이 살아 있는 사례다.

부제 *In Defense of Point-to-Point ICP*가 본문 어조에 그대로 살아 있다. "옹호한다(in defense of)"는 표현은 *우리가 새로 발명했다*가 아니라 *기존의 단순한 도구가 부당하게 평가절하되었다*는 자세를 선언한다. introduction 본문의 *This paper returns to the roots: classical point-to-point ICP, introduced 30 years ago by Besl and McKay*가 같은 자세를 한 줄로 압축한다. "returns to the roots"라는 표현이 30년 된 알고리즘을 다시 꺼내드는 행위를 *후퇴*가 아닌 *복귀*로 프레이밍한다. 후배가 자신의 단순한 baseline을 옹호하고 싶을 때 빌릴 수 있는 어조다. 도전적이지만 점잖다.

이 단락 그 자체가 mini-CCC다. abstract 첫 문장에 context(분야 정의)가 깔리고, 두 번째에 content의 *반전*이 채워지며, 세 번째 이후에 conclusion(단순한 해법으로 충분함)이 닫힌다. Mensh와 Kording이 rule 3에서 권한 단락 단위 CCC가 abstract 첫 단락에서 그대로 구현된다. 가이드 Part 2 ch04에서 다룬 CCC fractal이 in-the-wild에서 어떻게 작동하는지 보여 주는 가장 깔끔한 사례 중 하나다.

한 가지 더. 이 hook은 분야 통증을 *과장하지 않는다*. "LiDAR odometry는 풀리지 않은 거대 난제다"라 외치지 않고, 로봇 응용의 흔한 구성요소라 담담히 적는다("essential part of many robotic applications"). 후배 글쓰기에서 흔히 보이는 over-claiming — "이 분야는 위기에 처해 있다" 류 — 의 반대 방향이다. 통증이 작아 보일수록 "그런데 우리는 더 단순한 해법을 들고 왔다"는 contribution이 선명해진다. 통증의 크기와 contribution의 크기는 *비례*가 아니라 *비대칭*으로 짜는 편이 효과적이다. KISS-ICP는 이 비대칭이 제목, 부제, abstract 첫 두 문장, introduction 첫 단락에 일관되게 흐른다.

---

## 따라 쓰기 — 자기 분야에 적용

이 패턴은 시스템 논문 인트로 첫 단락의 3-beat 골격이다. "[분야 task]는 [응용]의 핵심이다. 최근 연구는 [복잡한 도구 A, B, C]를 더해 왔다. 이 논문은 [단순한 baseline]을 올바르게만 하면 충분함을 보인다." — 세 문장으로 압축된 이 골격에 자기 도메인의 명사를 끼워 넣으면 도입 단락의 1차 초고가 나온다. KISS-ICP의 *we move in the opposite direction*은 두 번째 문장에서 자세 전환을 한 절(clause)로 처리한 좋은 사례다. 강조 자리에 들어갈 단어를 먼저 정한 뒤 — 마지막 문장의 끝에 무엇을 두어야 contribution이 가장 또렷한가 — 거꾸로 문장을 짜는 것이 한 가지 작업 순서다.

3-beat 안에서 통증을 과장하지 않는 것이 또 한 축이다. 통증 한 줄, 복잡함 한 줄, 우리 해법 두세 줄. 이 분량 비율이 단순함을 contribution으로 내세우는 논문에서 잘 작동한다. 통증을 길게 쓰면 독자는 "그래서 위기가 정말 있나"를 의심한다. 짧게 쓰면 contribution이 들어설 자리가 넓어진다. 자기 baseline을 *옹호*하는 입장이라면 *In Defense of …* / *returns to the roots* / *we move in the opposite direction* 같은 구문 변형을 부제와 본문 양쪽에 걸어 두면 자세가 단단해진다.

---

## 출처
- `vizzo-2023-kiss` — Vizzo, I., Guadagnino, T., Mersch, B., Wiesmann, L., Behley, J., Stachniss, C., 2023. *KISS-ICP: In Defense of Point-to-Point ICP — Simple, Accurate, and Robust Registration If Done the Right Way.* IEEE Robotics and Automation Letters 8(2): 1029-1036. arXiv:2209.15397.

---
