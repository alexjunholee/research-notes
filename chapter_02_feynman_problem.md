# Ch.2 — 문제 정의는 답보다 먼저 좁혀진다

분야 좌표는 Ch.1에서 그렸다. 리뷰 한 편과 인용 그래프, hypothesis placeholder 한 줄까지가 그 결과물이다. 좌표가 잡힌 학생이 다음으로 마주하는 막힘은 모양이 다르다. 어드바이저가 "SLAM 정확도를 높여 보자"라고 말했는데, 그 한 문장에서 어디로 가야 손이 움직이는지 보이지 않는 단계다. 분야 지도가 있다고 풀어야 할 문제까지 자동으로 정해지지는 않는다.

이 장은 그 단계에서 문제를 작업 가능한 단위로 좁히는 절차를 본다. 연구 실패의 가장 흔한 원인은 정확한 답을 틀린 질문에 찾으려는 시도이고, 좁히기 절차가 그 함정을 피하는 도구다. Ch.1에서 비어 있는 채로 보관해 둔 hypothesis placeholder가 이 장에서 처음으로 작업 가능한 problem statement로 끌어올려진다.

---

## 2.1 문제를 먼저 적는다

[권창현 교수](https://gradschoolstory.chkwon.net/changhyun/%ec%97%b0%ea%b5%ac%ec%9d%98-%eb%b9%84%eb%b2%95-%ed%8c%8c%ec%9d%b8%eb%a7%8c-%ec%95%8c%ea%b3%a0%eb%a6%ac%ec%a6%98/)가 「연구의 비법: 파인만 알고리즘」에서 다시 꺼낸 Feynman의 3-step algorithm은 농담처럼 짧다.

> 1. Write down the problem.
> 2. Think real hard.
> 3. Write down the solution.

세 줄짜리 알고리즘은 농담처럼 보이지만 농담이 아니다. 신입생이 가장 자주 막히는 곳은 두 번째 줄이 아니라 첫 번째 줄이다. 풀어야 할 문제가 한 줄로 적히지 않은 채 "think real hard"로 넘어가면, 그 생각은 어디에도 착륙하지 못한 채 한 학기를 떠다닌다. 두 번째 줄이 두 번째에 놓인 데에는 의미가 있다. 문제가 적힌 다음에야 생각이 시작된다는 순서다.

세 줄을 같은 날 한 번에 쓰지 않아도 된다. 첫 줄을 적은 시점과 두 번째 줄에 도달하는 시점, 그리고 마지막 줄까지가 며칠·몇 주·몇 달 단위로 떨어진다. 첫 줄만 적힌 채로 한 주가 지나가는 것은 오히려 정상이다. 그 한 주가 두 번째 줄을 가능하게 한다.

> **문제를 쓰지 않으면 생각이 시작되지 않는다.** Feynman 3-step의 첫 줄이 비어 있으면 두 번째 줄도 비어 있다.

---

## 2.2 정확한 답 vs 옳은 질문

권창현 교수가 같은 글에서 든 두 비유가 이 함정을 압축한다.

> 디버깅을 해 본 사람은 알 것이다. 어디서 버그가 났는지 정확히 짚어내기만 하면, 고치는 일은 그 다음 일이다. 정작 어려운 것은 "어디가 문제냐"를 한 줄로 적는 일이다. 잘못된 자리를 정확하게 고쳐 봐야 프로그램은 여전히 안 돈다.
>
> 지진이 났다고 하자. "물자를 어떻게 운송할 것인가"는 거대한 주제지만 그 자체로는 풀 수 없다. "어느 도로가 끊겼고, 어느 창고에 무엇이 남아 있고, 어느 마을이 며칠째 고립되었는가"까지 좁혀져야 비로소 한 사람의 손이 움직일 수 있는 작업이 된다.

두 비유는 같은 곳을 가리킨다. 거대한 objective(SLAM 정확도, 물자 운송)는 작업의 방향만 준다. 작업의 단위는 되지 못한다. 단위가 되려면 측정 가능한 조건과 검증 가능한 가설로 좁혀져야 한다. 정확한 답을 틀린 질문에 찾으면 결과는 "잘 작동하는 것 같지만 의미가 없는 솔루션"으로 끝난다. 좁혀지지 않은 채로 출발한 연구가 1년 뒤 마주치는 가장 흔한 풍경이다.

권창현 교수는 그 진단을 한 줄로 정리한다.

> 연구는 답을 찾는 과정이 아니라 문제를 찾는 과정이다.

이 한 줄의 함의는 강하다. 처음 적은 problem statement는 마지막까지 같은 채로 남지 않는다. 좋은 문제는 작업 중에 좁아지고, 좁아지면서 모양을 바꾼다. 1년 뒤의 problem statement가 출발 시점의 problem statement와 다른 문장일 가능성이 높고, 그게 정상이다.

> **문제는 마지막에 정의된다.** 시작 지점의 problem statement는 placeholder이고, 작업 중에 진짜 문제가 발견된다.

---

## 2.3 hypothesis placeholder와의 봉합

권창현 교수의 "write down the problem"과 [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §3.3의 hypothesis placeholder는 같은 명제의 두 표현이다. 문제를 쓰는 행위는 곧 그 문제가 풀렸을 때 보일 가상의 답을 미리 그리는 행위다. Whitesides가 outline에 적어두라고 한 한 문장이 이를 직격한다.

> Simply indicate where missing data will go, how you think (hypothesize) they will look, and how you will interpret them if your hypothesis is correct.

데이터가 없으면 그 자리에 가설이 맞을 때 데이터가 어떻게 보일지를 미리 적어 둔다. 그 가상 데이터와 실제 데이터의 거리가 곧 실험의 to-do 목록이 된다. 문제를 한 줄로 적는 일도 같은 작업으로 수렴한다. "X 조건에서 Y가 Z로 측정될 것이다"라고 적는 순간, 그 문장은 가상의 결과를 품은 problem statement로 굳는다.

placeholder는 틀려도 된다. 시작점일 뿐이고 작업 중에 내용이 바뀌는 게 정상이다. Ch.1 진입 단계에서 한 줄 stub로 잡아 둔 placeholder ("X subfield에서 Y가 아직 안 풀렸고 Z 방향을 보고 싶다")가 이 장의 좁히기 절차를 거쳐 작업 가능한 problem statement 한 단락으로 끌어올려진다. 이후 [Part 2 ch02 (outline-first)](./chapter_17_outline_first.md)에서 이 problem statement가 outline 7-슬롯 안의 introduction 자리로 들어가, 가상 데이터를 품은 항목으로 다시 자란다. 같은 placeholder가 진입 → 문제 정의 → outline drafting의 세 층위를 가로지른다.

---

## 2.4 SLAM worked example — 좁히기 절차

좁히기가 어떻게 이루어지는지를 한 사례로 본다. 출발은 어드바이저가 던진 흔한 한 줄, "SLAM 정확도를 높이고 싶다"이다. 이 문장은 objective는 있지만 problem statement는 아니다. 무엇을, 어떤 조건에서, 어떻게 측정해 좋아졌다고 말할지가 비어 있다.

1차 좁히기는 현상 단위로 내려간다. "loop closure 실패가 잦다." 정확도라는 막연한 단어가 어떤 모듈이 어떤 식으로 깨지는지로 옮겨졌다. 2차 좁히기는 조건과 측정을 끼운다. "indoor low-light 시퀀스에서 ORB feature 탐지 수가 정상 조명 대비 30% 수준까지 떨어진다." loop closure 실패라는 현상이 그것이 왜 자주 일어나는지의 한 후보(전단의 feature 탐지)와 어디서 일어나는지의 한 조건(indoor low-light)으로 묶였고, 이 단계에서야 ablation 실험과 baseline 비교가 가능해진다. 3차 좁히기는 메커니즘 가설로 들어간다. "feature가 빈약한 프레임에서 초기 pose estimate가 흔들려 뒤따르는 ICP refinement가 local minima로 수렴한다." 측정 가능한 입력(프레임당 feature 수)과 측정 가능한 결과(ICP의 수렴점)가 인과 한 줄로 묶이고, 그제야 한 학생의 손이 움직일 수 있는 작업이 된다.

좁히기의 단위는 세 종류다. **constraint**(어떤 조건에서 — indoor low-light), **objective**(무엇을 — 프레임당 feature 수와 ICP 수렴점의 인과), **test condition**(어떻게 검증 — feature 수 임계값 sweep으로 ICP 수렴점 변화 측정). 세 슬롯이 모두 채워지지 않은 problem statement는 아직 좁혀지지 않았다. 좁힐수록 작업 가능해지고, 작업 가능해지면 솔루션이 뒤따라온다.

> 좁히기는 보통 3-4회. 한 번에 너무 좁히면 일반화가 깨지고, 너무 넓게 두면 작업이 시작되지 않는다.

> problem statement는 한 단락 이내로 적는다. 한 단락을 넘으면 아직 좁히지 못한 것이고, 두 problem이 섞여 있을 가능성이 높다.

좁히기의 절차는 모두에게 같다. 다만 그 절차를 기록하는 양식은 사람마다 다르다. 다음 섹션에서 그 양식을 본다.

---

## 2.5 personal style

좁히기의 algorithm은 모두에게 동일하다. 다만 그 algorithm을 적는 방식은 자기 것이다. [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §10이 그 점을 한 줄로 적었다.

> Get a personal style that works for you.

같은 챕터(§43)에 더 강한 표현이 한 번 더 등장한다. "the style has to be your own. You will write things that someone else will never write." Knuth의 함의는 단순하다. problem statement를 적는 양식, 가상 데이터를 그리는 다이어그램, constraint·objective·test를 분리해 두는 기호 체계 — 이런 도구는 학습 가능한 자기 도구고, 한 번 정착하면 5년이 지나도 같은 형태로 유지된다.

한 학생이 자기 problem statement 양식을 5년 안에 정착시키는 편이 권장 방향이다. 양식이라는 단어가 거창하게 들리지만, 실은 노트 한 페이지의 상단에 어떤 항목을 어떤 순서로 적는지, 좁히기 단계마다 어떤 기호로 표시하는지의 사소한 합의다. 그 사소한 합의가 일관되게 유지되면, 6개월 뒤 본인이 그 노트를 다시 봤을 때 그 시점의 자기 생각이 즉시 복원된다. 일관성이 곧 도구다.

> Knuth §10의 personal style은 problem statement 양식에도 적용된다. 자기 노트 양식을 5년 안에 정착시키는 게 권장 방향이다.

---

Ch.1에서 stub로 잡아 둔 hypothesis placeholder가 이 장의 좁히기 절차를 거쳐 한 단락짜리 problem statement로 자랐다. 그 단락이 본인 종이 위에 적힌 시점에서 학생의 화법이 바뀐다. "잘 안 되네요"가 "이 조건에서 이렇게 해볼까요"로 바뀐다. 그 전환이 일어나는 시점이 곧 주제의 주도권이 어드바이저에서 학생으로 넘어오는 시점이다. 다음 챕터에서 그 전환을 본다.

---

**출처.** [권창현 교수 G7 「파인만 알고리즘」](https://gradschoolstory.chkwon.net/changhyun/%ec%97%b0%ea%b5%ac%ec%9d%98-%eb%b9%84%eb%b2%95-%ed%8c%8c%ec%9d%b8%eb%a7%8c-%ec%95%8c%ea%b3%a0%eb%a6%ac%ec%a6%98/), [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767), [Knuth et al. 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html).

다음: [Ch.3 — 주도권의 이동: 교수 제안에서 내 주제로](./chapter_03_ownership_shift.md)
