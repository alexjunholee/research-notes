# Ch.18 — 시간 배분과 피드백 루프

Method 섹션을 두 달 다듬은 학생이 reviewer로부터 abstract만 보고 reject된 코멘트를 받는 일은 흔하다. 가장 많이 읽히는 부분과 가장 많이 다듬은 부분이 어긋난 결과다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)의 rule 9와 rule 10이 이 어긋남을 정면으로 다룬다.

---

## 18.1 가장 많이 읽히는 것에 가장 많이 투자한다

논문 한 편이 받는 독자 수를 거칠게 풀어 보면 다음과 비슷하다. 1000명이 title을 보고, 그중 100명이 abstract로 내려가고, 다시 50명이 figure 1까지 내려간다. method까지 도달하는 인원은 5명 안팎이다. Mensh-Kording rule 9는 글쓰기 시간을 이 깔때기에 비례해 배분하라고 적었다.

시간 우선순위는 다음 순서로 잡힌다.

> Title > Abstract > Figure(특히 Fig 1) > Outline > Introduction > Results > Discussion > Method > Related Work

Method가 가장 적게 읽히는 부분이라는 사실이 Method를 *부정확하게* 써도 된다는 뜻은 아니다. 정확성은 유지하되 윤문에 시간을 쓰지 말라는 권고에 가깝다. Method의 목적은 재현이지 설득이 아니다.

---

## 18.2 비율 가이드

논문 한 편의 글쓰기 시간을 100%로 보면 다음 비율이 작업 가능한 출발점 하나다.

| 항목 | 비율 |
|---|---|
| Title + Abstract | 15-20% |
| Figures (특히 Fig 1과 main result figure) | 25-30% |
| Outline iteration ([Ch.2](./chapter_17_outline_first.md)) | 15-20% |
| Introduction | 15% |
| Results & Discussion | 10-15% |
| Method + 부록 | 5-10% |

한국 대학원생에게서 흔히 잡히는 패턴은 Method에 50% 이상이 들어가고 Title·Abstract·Figure에 합쳐 10%가 들어가는 정반대 비율이다. 학부 글쓰기 훈련의 후유증인 부분이 있다. 학부 시험 답안에서는 풀이 과정이 점수를 받았다. 논문은 다르다 — 풀이 과정은 결과를 정당화하는 보조 자료로 들어간다.

---

## 18.3 Test reader 프로토콜

rule 10은 "reduce, reuse, recycle"의 reduce 쪽에 무게를 둔다. 같은 사람에게 여러 번 보여 주지 말라는 권고다. 한 번 본 사람의 머릿속에는 이미 *글쓴이가 의도한 구조*가 박혀 있고, 두 번째 읽기에서는 그 구조를 채워 넣으면서 읽는다. 신선한 독자가 잡아내는 결함을 두 번째 reader는 잡지 못한다.

단계별로 reader를 분리한다.

- **Outline 단계** — 같은 분야 동료 1명. 구조가 말이 되는지를 검증한다.
- **초고 단계** — 다른 세부 분야 동료 1명. gap funnel이 자기 분야 밖에서도 작동하는지 검증한다.
- **수정 단계** — 비전공 대학원생 1명. abstract만 보여 주고 "이 논문이 무엇을 푸는지 한 문장으로 말해 달라"고 요청한다.

reader에게 던지는 질문이 *닫힌 질문*("이 부분 괜찮아?")이면 답변도 닫힌 채로 돌아온다. *재구성 요청*("이 논문이 무슨 문제를 푸는지 한 문장으로 말해 주세요")이 진단에 훨씬 정보가 많다.

---

## 18.4 "Non-specific feedback"의 진단

reader에게서 막연한 답("좋네요", "뭔가 어렵다", "잘 모르겠다")이 돌아오면 *큰 그림 실패* 신호다. 단어 수준이 아니라 구조 수준에서 결함이 있다는 뜻이다. 이 경우 단어를 고치는 대응이 가장 흔한 함정이다. 단어를 다듬어도 구조가 그대로면 다음 reader도 같은 막연한 답을 돌려준다.

진단 분기는 다음과 같다.

- "abstract만 보고 무슨 논문인지 모르겠다" — Title·Abstract 전면 재작업. [ch07](./chapter_22_title_abstract.md)에서 다룬다.
- "왜 이게 중요한지 모르겠다" — Introduction의 gap funnel 결함. [ch08](./chapter_23_introduction.md)에서 진단법을 다룬다.
- "Method는 알겠는데 결과가 와닿지 않는다" — Results의 declarative subheading 결함. [ch11](./chapter_26_results_discussion.md)에서 처방한다.

각 분기는 *구조 단위의 재작업*을 요구한다. 단어 수준에서 멈추면 같은 reject가 반복된다.

---

## 18.5 피드백 루프의 빈도와 cooldown

Outline iteration 사이 24시간 cooldown은 [Ch.2 §3](./chapter_17_outline_first.md)에 적었다. 같은 원리가 초고 → 수정 사이에도 작동한다 — 최소 48시간을 권한다. 그제서야 글쓴이의 머리가 *직전에 쓴 문장의 잔상*에서 풀려난다.

마감 직전에 *새로운 reader*를 투입하지는 않는다. 신선한 reader는 신선한 결함을 잡아내지만, 마감 시점에 그 결함을 모두 처리할 시간이 없다. 처리하지 못한 결함은 글쓴이의 머리에 남아 공황을 만든다. 마감 일주일 전부터는 *이미 한 번 본 reader*에게 같은 글을 다시 보여 줘서 마이너 결함만 잡는 방식이 안전하다.

---

## 18.6 점검 가능한 부분

이 장의 권고 중 일부는 체크리스트로 반복 점검할 수 있다. 섹션별 수정 횟수의 불균형, abstract보다 Method만 계속 고치는 패턴, 피드백이 단어 수준에만 머무는 패턴은 §1 우선순위 위반의 신호다. 단락 수준 결함은 비교적 빨리 보이지만, 섹션·논문 스케일의 결함은 반드시 reader를 바꿔 다시 봐야 한다.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9 (시간 배분), rule 10 (피드백 루프). [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) (cooldown 정신 차용). 비율 수치, 단계별 reader 분리, 진단 분기, 마감 cooldown은 이 장에서 정리했다.

다음: [Ch.4 — CCC: 단락·섹션·논문의 fractal](./chapter_19_ccc.md)
