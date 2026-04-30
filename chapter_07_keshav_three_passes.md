# Ch.7 — Keshav 3-pass 방법

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)이 §1에서 적은 문장 중 자주 인용되는 한 줄은 "각 패스는 고유한 목적이 있고, 다음 패스는 이전 패스 위에서만 의미가 있다"이다. 한 번에 다 읽으려는 충동을 가장 큰 적으로 둔다.

Ch.1에서 다룬 모드 분류가 *왜 읽는가*에 답한다면, 3-pass는 *어떻게 단계적으로 읽는가*에 답한다. 핵심은 *increasing detail*. 패스마다 디테일이 한 단계 깊어지고, 각 패스 끝에 "여기서 멈출지"의 결정 게이트가 붙는다. Keshav가 자주 환기하는 점은 모든 논문에 3패스를 완주하지 않는다는 것이고, 다수는 1st pass 끝에서 멈춘다.

L2 reader 입장의 위안이 하나 필요하다. 한국어권 글쓴이 [엄태웅 작가](https://gradschoolstory.chkwon.net)가 「영어 못해도 논문 잘 읽는 법」에서 적은 한 줄이 거기에 놓인다.

> *"지금도 영어를 못하며, 앞으로도 못할 것이다. 그래도 논문은 읽는다."*

영어 능력의 결핍을 인정한 채로 들어가는 패스가 Keshav 3-pass의 한국 독자용 시작점이다. 다만 영어 디테일에 막혀 멈추는 것과, 패스 절차에 따라 의도적으로 *건너뛰는* 것은 다르다. 후자가 Keshav가 가리키는 쪽이다.

---

## 7.1 1st pass — Bird's eye (5–10분)

같은 패스를 한국어 voice로 풀어낸 글이 [엄태웅 작가 G1](https://gradschoolstory.chkwon.net)의 4단계 절차다. abstract → conclusion → 그림·표 → introduction 순서로 훑는다. Keshav §2.1과 *실질적으로 동일한 절차*다. 들어가는 곳(abstract·conclusion·heading·figure)과 안 들어가는 곳(본문 디테일)이 같다. 차이는 voice뿐이다.

> *"초록은 출발 비디오여행의 영화 하이라이트다."*
>
> *"표·그림은 영어만 남은 사막에 한 줄기 오아시스다."*
>
> *"서론은 주옥같은 다음 논문들을 소개받는 보물창고다."*

세 비유가 1st pass에서 읽는 곳의 *기능*을 정확히 짚는다. abstract는 논문 전체의 압축 요약, figure는 영어 본문을 넘기는 시각 단축, introduction의 reference는 다음 논문 목록의 큐레이션이다.

Keshav §2.1은 1st pass를 "bird's-eye view"로 적는다. 다섯에서 십 분 안에 끝내는 패스다.

읽는 곳은 정해져 있다. title, abstract, intro, 각 section·subsection 헤딩, conclusion, 그리고 reference 목록을 한 번 훑는 정도다. 본문 단락, 수식, figure caption의 디테일에는 들어가지 않는다.

이 패스의 출력은 5 Cs — Category, Context, Correctness, Contributions, Clarity — 다섯 칸짜리 요약이다 (Ch.3에서 시트로 다룬다). 5 Cs를 채운 직후 stop / defer / proceed 셋 중 하나를 결정한다. 5분 안에 5 Cs가 다 채워지지 않으면 두 갈래다. 글쓴이가 abstract를 망쳤거나, 읽는 쪽 배경이 부족하다. 둘 다 멈춤 신호로 받는다.

---

## 7.2 2nd pass — Grasp content (한 시간 이내)

Keshav §2.2는 2nd pass를 "내용을 잡는" 패스로 적는다. 상한 한 시간. 본문을 정독하되 증명 디테일은 건너뛰고, figure와 graph는 면밀히 본다. 엄태웅 작가가 같은 단계에서 적은 "수식 디테일을 모르고 넘어가도 OK, 입출력과 필요성만 잡는다"는 Keshav §2.2의 "ignore proof details"와 같은 명제다. 출처는 다르지만 권고가 일치한다. 한국 L2 reader가 자기 영어 부족을 진단 신호로 오인하는 일이 잦아, 두 출처를 함께 둔다. Keshav가 §2.2에서 적은 quotable 중 하나는 "축 라벨과 오차막대 같은 사소한 디테일이 졸속한 연구와 탁월한 연구를 가른다"이고, 그래서 axis 라벨, 단위, error bar, significance 표기를 caption만이 아니라 plot 자체에서 확인하라는 권고가 붙는다.

모르는 reference를 만나도 그 자리에서 추적하지 않는다. 마킹만 하고 다음 단계로 넘긴다. ref 추적은 lit survey 단계의 일이다 (Ch.4에서 자세히).

이 패스의 출력은 본문의 main thrust + supporting evidence를 한 단락으로 적은 요약이다. 한 시간이 넘어가면 배경이 부족하다는 신호이고, 그러자면 모르는 ref 한두 편에 1st pass를 한 후 본 논문의 2nd pass로 복귀하는 편이 자연스럽다.

---

## 7.3 3rd pass — Virtual re-implementation (4–5시간 / 숙련자 한 시간 안팎)

Keshav §2.3은 3rd pass를 "to virtually re-implement the paper"로 적는다. quotable로 자주 떼어 인용되는 문장은 "3패스의 핵심은 논문을 머릿속으로 재구현해 보는 것이다"이다.

방법은 정해져 있다. 저자가 깐 가정과 같은 가정에서 출발해, 같은 결론에 도달할 방법을 *읽는 쪽이 직접* 설계한다. 그러고 나서 저자의 선택과 비교한다. 일치하지 않는 부분이 곧 implicit assumption, 약점, 빌려올 기법이다.

이 패스의 출력은 가정 목록, 약점 목록, 그리고 다른 작업에 빌려올 기법 목록이다. Reviewer 모드에 들어갈 작정이라면 3rd pass가 사실상 필수인 만큼 (Ch.5에서 자세히), 신입 박사과정에게는 4–5시간이 권장 분량이고, 같은 분야를 오래 본 숙련자에게는 한 시간 안팎으로 줄어든다고 Keshav는 적는다.

---

## 7.4 패스별 input / skip / output 정리

| Pass | Input | Skip | Output | 시간 |
|------|-------|------|--------|------|
| 1 | title·abstract·heading·conclusion·refs glance | 본문·수식·figure 디테일 | 5 Cs + stop/defer/proceed | 5–10분 |
| 2 | 본문·figure·graph (axis·error bar 포함) | 증명 디테일·미상 ref 추적 | 한 단락 요약 | ≤ 1시간 |
| 3 | 전체 + 가정 점검 + 재구현 시도 | (없음) | 가정·약점·기법 목록 | 4–5시간 (숙련자 ~1시간) |

Keshav가 §2 마지막에 환기하는 점은 패스 사이의 의존성이다. 1st pass 없이 2nd pass에 바로 들어가면 본문 어디에 시간을 쓸지 잡히지 않고, 2nd pass 없이 3rd pass에 들어가면 재구현할 핵심이 잡히지 않는다. 그래서 패스를 건너뛰지 않는 권고가 그 의존성에서 나온다.

---

## 7.5 시간 예산을 넘는 경우의 진단

각 패스의 시간 예산을 넘기면, 그 자체가 진단 신호다. 1st pass가 10분 안에 안 끝나면 두 갈래로 나뉜다. abstract의 broad-narrow-broad가 무너졌거나 (Ch.1에서 다룬 신호), 분야 배경이 부족하다. 2nd pass가 한 시간을 넘으면 ref 한두 편의 1st pass 후 복귀하는 편이 낫다. 3rd pass는 시간 예산보다 *재구현 막힘 지점*이 신호다. 막힌 지점은 대개 implicit assumption이다.

시간을 늘리는 것보다 *왜 늘어났는가*를 적는 편이 낫다.

---

## 7.6 AI-assisted reading — 2nd pass의 시간 단축 layer

3-pass 절차 위에 한 layer가 더 얹혀 있는 시점이다. 1st pass에서 abstract와 conclusion을 읽은 직후 PDF를 AI에 던지고 *contribution을 3줄로*, *related work에서 가장 자주 비교되는 baseline은 무엇인가*, *Eq. 5를 단계별로 유도해 달라* 같은 질문을 거는 패턴이 있다. 2nd pass의 정독 단계에서 본문 어디에 시간을 쓸지 좌표가 더 빨리 잡히고, 한 시간 상한 안에서 ref 한두 편의 1st pass에 쓸 시간이 그만큼 확보된다. Semantic Scholar의 관련 논문 추천을 받고, 추천 논문 사이의 차이점을 AI에 비교 정리시키는 작업도 같은 layer에 들어간다.

> AI 요약만 믿어서는 안 되는 부분이 따로 있다. 논문의 subtle한 가정, limitation 섹션의 뉘앙스, 실험 세팅의 세부 사항은 직접 읽어야 한다.

읽는 쪽이 직접 들어가야 하는 것(가정·limitation·실험 세팅)과 AI에 위임 가능한 것(요약·baseline 정리·유도 단계 보조)이 같은 절차의 두 layer로 갈라진다. (이전에 robotics-practice ch19 § 19.7에 정리된 내용으로, 분야 layer cameo로 가져옴.)

---

**출처.** [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §1·§2.1·§2.2·§2.3. [엄태웅 작가 G1 「영어 못해도 논문 잘 읽는 법」](https://gradschoolstory.chkwon.net) — 4단계 절차의 한국어 voice·인용 박스. robotics-practice ch19 § 19.7.1 — AI-assisted reading layer cameo (분야 layer 인용).

다음: [Ch.3 — 5 Cs 체크리스트](./chapter_08_five_cs.md)
