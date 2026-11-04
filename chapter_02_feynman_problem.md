# Ch.2 — 문제 정의는 답보다 먼저 좁혀진다

Ch.1에서 리뷰 한 편과 인용 그래프로 분야 좌표를 잡고 hypothesis placeholder를 한 줄 적었다. 좌표를 잡은 다음에는 문제를 정하는 데서 막힌다. 지도교수가 "SLAM 정확도를 높여 보자"라고 했는데, 그 한 문장에서 무엇부터 손을 대야 할지 보이지 않는다. 분야 지도가 있어도 풀어야 할 문제는 따로 정해야 한다.

이때는 문제를 손댈 수 있는 크기로 좁혀야 한다. 틀린 질문에 정확한 답을 찾으려 하면 연구가 한참 돌아간다. Ch.1에서 비워 둔 hypothesis placeholder는 이 좁히기를 거쳐 처음으로 실제 작업에 쓸 problem statement가 된다.

---

## 2.1 문제를 먼저 적는다

[권창현 교수](https://gradschoolstory.chkwon.net/changhyun/%ec%97%b0%ea%b5%ac%ec%9d%98-%eb%b9%84%eb%b2%95-%ed%8c%8c%ec%9d%b8%eb%a7%8c-%ec%95%8c%ea%b3%a0%eb%a6%ac%ec%a6%98/)는 「연구의 비법: 파인만 알고리즘」에서 Feynman algorithm을 소개한다. 세 줄이 전부다.

> 1. Write down the problem.
> 2. Think real hard.
> 3. Write down the solution.

권창현 교수가 각주에 적었듯, 이 알고리즘은 동료 물리학자 Murray Gell-Mann이 Feynman을 두고 농담으로 한 말이다. 권창현 교수는 처음 접했을 때 황당하다고 여겼고, 대학원생 때는 2번에 감명을 받았다가, 결국 가장 감명 깊은 것은 1번이었다고 쓴다. 문제를 쓰려면 풀어야 할 문제가 정확히 무엇인지 알아야 하는데, 그런 경우가 드물기 때문이다. 풀 문제를 한 줄로 적지 못한 채 "think real hard"로 넘어가면, 한 학기 내내 생각만 하고 아무것도 정해지지 않는다. 생각은 문제를 적은 다음에 시작한다.

세 줄을 같은 날 다 쓸 필요는 없다. 첫 줄을 적는 날과 둘째 줄, 마지막 줄에 이르는 날은 며칠에서 몇 달까지 떨어져 있다. 첫 줄만 적어 두고 한 주를 보내는 것도 탐색의 일부다. 그 한 주 동안 생각한 것이 둘째 줄로 이어진다.

> **문제를 쓰지 않으면 생각이 시작되지 않는다.** Feynman algorithm의 첫 줄이 비어 있으면 둘째 줄도 비어 있다.

---

## 2.2 틀린 질문에 정확한 답을 찾는 함정

권창현 교수는 같은 글에서 *Financial Calculus*의 서문을 인용한다. 많은 사람이 "finding precise answers to the wrong questions", 곧 틀린 질문에 정확한 답을 찾느라 헛수고를 한다는 말이다. 그리고 예를 든다.

첫째는 지진이다. "대형 지진 발생 이후의 대처법"은 연구 분야는 될 수 있어도 문제는 아니다. "대형 지진 발생 이후의 적절한 구호 물자 운송방법"으로 좁혀도 아직 문제가 아니다. "A라는 빈도로 z 지역에서 구호 물자 수요가 생길 때, x 지역에서 z 지역으로 얼마나 자주 물자를 보내야 하는가"까지 와야 문제가 된다. 그래도 실제 수요가 A가 아닌 다른 빈도로 생긴다면 그 문제는 wrong question이다.

둘째는 버그다. 권창현 교수는 "결과가 제대로 나오지 않는다. 어떻게 제대로 나오게 할 수 있을까?"는 좋은 문제가 아니라고 쓴다. 어떤 결과는 맞고 어떤 결과는 틀리는지, 틀린 원인이 코드인지 알고리즘인지, 알고리즘이 풀려는 문제 자체가 잘못됐는지로 나누어 정의하고 열심히 생각하면 대부분 풀린다.

SLAM 정확도나 구호 물자 운송 같은 큰 objective는 방향을 알려 준다. 실제 작업으로 옮기려면 측정할 수 있는 조건과 검증할 수 있는 가설로 좁혀야 한다. 좁히지 않고 출발한 연구는 틀린 질문에 정확한 답을 찾는 쪽으로 흘러가기 쉽다. 그러면 결과는 잘 돌아가는 것 같지만 쓸모없는 해법으로 끝난다.

권창현 교수는 글 끝머리에 이렇게 적었다.

> 연구는 사실 답을 찾는 과정이 아니라 문제 혹은 질문을 찾는 과정이다.

좋은 문제는 작업하면서 좁아지고, 좁아지면서 모양이 바뀐다. 1년 뒤의 problem statement는 처음 적은 것과 다른 문장일 때가 많고, 그게 정상이다.

> **문제는 작업하면서 정해진다.** 처음 적은 problem statement는 placeholder이고, 진짜 문제는 작업 중에 드러난다.

---

## 2.3 hypothesis placeholder로 이어지는 길

Feynman algorithm의 "write down the problem"과 [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)의 outline도 문제를 먼저 적는 데서 출발하고, 여기에 나올 결과를 미리 그려 보는 일을 더한다. Whitesides는 outline을 설명하면서 이렇게 적었다.

> Simply indicate where missing data will go, how you think (hypothesize) they will look, and how you will interpret them if your hypothesis is correct.

아직 데이터가 없으면, 가설이 맞을 때 나올 데이터의 모양을 미리 적어 둔다. 미리 그린 데이터와 실제로 잰 값을 맞대 보는 일이 실험 계획의 뼈대가 된다. 문제를 한 줄로 분명하게 적는 일도 같다. "X 조건에서 Y가 Z로 측정될 것이다"라고 적으면, 그 문장은 예상 결과가 담긴 작업 가설이 된다.

placeholder는 틀려도 된다. 출발점일 뿐이고 작업하면서 내용이 바뀌는 게 정상이다. Ch.1에서 한 줄 stub으로 적어 둔 placeholder("X subfield에서 Y가 아직 안 풀렸고 Z 방향을 보고 싶다")는 좁히기를 거쳐 한 단락짜리 problem statement가 된다. [Ch.17 (outline-first)](./chapter_17_outline_first.md)에서는 이 problem statement가 outline의 introduction 자리에 들어가고, 미리 그린 데이터와 함께 다시 다듬어진다.

---

## 2.4 SLAM 예제로 보는 좁히기

아래 수치와 인과는 좁히는 형식을 보여 주려고 지어낸 예다. 특정 dataset이나 알고리즘의 성능을 보고한 값이 아니다. 출발점은 지도교수가 할 법한 말, "SLAM 정확도를 높이고 싶다"다. 이 문장에는 objective는 있어도 problem statement는 없다. 무엇을, 어떤 조건에서, 어떻게 재서 좋아졌다고 말할지가 비어 있다.

1차로 좁히면 현상이 나온다. "loop closure가 자주 실패한다." 정확도라는 막연한 말이 어느 모듈이 어떻게 깨지는지로 바뀌었다.

2차로 좁히면 조건과 측정 지표가 붙는다. "실내 저조도 시퀀스에서 ORB feature 검출 수가 정상 조명의 30% 수준까지 떨어진다." 이제 loop closure 실패에 원인 후보(앞단의 feature 검출)와 발생 환경(실내 저조도)이 붙었으니, ablation 실험과 baseline 비교를 설계할 수 있다.

3차로 좁히면 인과가 나온다. "feature가 적은 프레임에서 초기 pose 추정이 흔들리고, 뒤따르는 ICP refinement가 local minimum에 빠진다." 측정할 수 있는 입력(프레임당 feature 수)과 측정할 수 있는 결과(ICP가 수렴한 지점)가 하나의 인과로 이어져야 실제로 해 볼 수 있는 연구 과제가 된다.

좁힐 때 채울 칸은 constraint, objective, test condition이다. constraint는 어떤 조건에서인지(실내 저조도), objective는 무엇을 밝히는지(프레임당 feature 수와 ICP 수렴 지점의 인과), test condition은 어떻게 검증하는지(feature 수 임계값을 바꿔 가며 ICP 수렴 지점이 어떻게 변하는지 잰다)를 적는다. 한 칸이라도 비어 있으면 아직 덜 좁힌 problem statement다. 좁힐수록 손댈 곳이 분명해지고, 손댈 곳이 분명해지면 해법을 찾기 시작할 수 있다.

> 이 예에서는 세 번 좁혔다. 몇 번 좁힐지는 정해져 있지 않다. constraint, objective, test condition이 다 채워질 때까지 좁힌다. 다만 너무 좁히면 결과를 일반화하기 어려워진다.

> problem statement는 한 단락 안에 적는다. 한 단락을 넘으면 아직 덜 좁혔거나 문제 두 개가 섞여 있을 때가 많다.

---

## 2.5 자기 양식

좁히는 절차는 누구에게나 같아도, 그 절차를 적는 양식은 사람마다 다르다. [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html)의 §10에서 Knuth는 알고리즘을 어떻게 쓸지 고민한 이야기를 한다. 사람들이 "Knuth 스타일로 알고리즘을 쓰겠다"고 하고는 그가 가장 중요하게 여기는 관례를 무시해 완전히 망쳐 버린다며, 이렇게 말한다.

> So get a personal style that works for you.

마지막 강의를 정리한 §43에서도 비슷한 말을 한다. "the style has to be your own. You will write things that someone else will never write." problem statement를 적는 양식, 예상 데이터를 그리는 그림, constraint·objective·test condition을 나눠 적는 기호도 이렇게 익히고 고쳐 가며 쓰는 자기 도구다. 오래 쓸수록 다시 꺼내 쓰기 쉬워지지만, 연구 단계와 문제에 따라 모양은 바뀐다.

양식이라고 하면 거창하게 들리지만, 실제로는 노트 한 쪽 위에 어떤 항목을 어떤 순서로 적을지, 좁히는 단계마다 어떤 기호를 붙일지 정해 두는 정도다. 이를 꾸준히 지키면 나중에 노트를 다시 볼 때 그때 무슨 생각을 했는지 되살리기 쉽다. 양식이 작업과 맞지 않으면 항목을 바꿔 가며 다듬는다.

> 자기 노트 양식을 꾸준히 쓰되, 작업에 맞지 않는 부분은 고친다.

---

problem statement를 한 단락으로 적고 나면 지도교수에게 하는 말이 달라진다. "잘 안 되네요" 대신 "이 조건에서 이렇게 해 볼까요"라고 말하게 된다. 주제를 이끄는 사람이 지도교수에서 학생으로 바뀌기 시작하는 때가 이때다.

---

**출처.** [권창현 교수 「연구의 비법: 파인만 알고리즘」](https://gradschoolstory.chkwon.net/changhyun/%ec%97%b0%ea%b5%ac%ec%9d%98-%eb%b9%84%eb%b2%95-%ed%8c%8c%ec%9d%b8%eb%a7%8c-%ec%95%8c%ea%b3%a0%eb%a6%ac%ec%a6%98/), [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767), [Knuth et al. 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html).

다음: [Ch.3 — 주도권의 이동: 교수 제안에서 내 주제로](./chapter_03_ownership_shift.md)
