# Ch.22 — 제목과 초록

한 reviewer가 한 학회에서 받는 manuscript 5-10편 중 다수가 *제목만으로* 1차 분류된다. 그 분류를 통과한 paper는 다음 단계에서 abstract 한 paragraph 안에서 verdict의 큰 뼈대를 받는다. 제목과 초록은 본문에 도달하기 위한 *입장권*이다.

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §IV가 둘을 한 묶음으로 다룬 이유도 이 비대칭에서 나온다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 1과 rule 5가 각각 제목과 초록의 골격을 정의해 둔다. ch01 §6의 readership-weighted budget이 둘에 가장 큰 시간 비중을 할당하라고 권하는 것도 같은 이유다.

---

## 22.1 Title — contribution 한 문장

**제목은 한 문장으로 압축한 contribution이다.** Mensh-Kording rule 1의 정식화. 본인 논문이 분야에 *무엇을 더했는가*가 제목 한 줄로 추출되어야 한다.

**동사가 들어가야 contribution이 산다.** "BEV-based Loop Closure"는 명사구일 뿐이다. 그 명사구가 *무엇을 했는가*는 본문을 읽어야 알 수 있다. "BEV-based loop closure halves recall failures on KITTI"는 동사·숫자·대상이 박혀 있다. ch05 §3의 헤딩 작성 절차와 같은 축.

**길이 권고는 12-15 단어.** 너무 짧으면 contribution이 압축되지 않은 상태로 남고, 너무 길면 인덱싱·인용·자동화 분류기에서 손실이 생긴다. 분야 관행과 venue 한도 안에서.

**Keyword density.** contribution과 직결되는 keyword 2-3개가 제목에 들어가야 한다. 검색·인덱싱·자동 추천이 이 keyword를 입력으로 받는다.

---

## 22.2 Abstract — full CCC self-contained

**Abstract는 자기 안에서 닫혀야 한다.** Mensh-Kording rule 5가 *key fits its lock* 비유로 박았다. 결과(key)가 정확히 갭(lock)에 들어맞아야 abstract가 완성된다. ch04 §3에서 다룬 self-contained 조건과 같은 축.

**다섯 칸이 한 paragraph 안에 들어간다.**

1. **Field gap** — 분야 전체의 큰 빈틈 한 줄.
2. **Paper gap** — 본 논문이 메우는 정확한 자리 한 줄.
3. **Approach** — 그 자리를 어떻게 메우는가 한두 줄.
4. **Result** — 핵심 숫자. *수치 하나*가 강하게 박혀야 reviewer가 verdict의 뼈대를 받는다.
5. **Implication** — 분야에 무엇을 의미하는가 한 줄.

**외부 참조 금지.** "Fig. 3 shows …", "in Sec. 4 we …" 같은 본문 참조가 abstract에 들어가면 self-contained 조건이 깨진다. abstract만 떼어 *별도 manuscript*로 읽혔을 때 자족적이어야 한다.

**길이 권고는 150-250 단어.** venue별 한계 안에서. 너무 짧으면 다섯 칸이 압축 안 되고, 너무 길면 reviewer 입장에서 *본문을 미리 보는* 글이 된다.

---

## 22.3 작성 순서 — 본문이 안정된 뒤

**Abstract는 맨 마지막에 쓴다.** Whitesides §IV의 강한 권고. 본문이 흔들리는 동안 abstract를 깎으면 lock이 흔들리는 동안 key를 깎는 일. 본문 outline 4-5회차가 안정된 뒤, 그제서야 abstract 작업의 첫 칸이 열린다.

제목도 같은 시점에 있다. outline iteration 1-3회차에서는 placeholder로 남아 있어도 된다. claim style로 다듬는 작업은 본문 결론이 안정된 뒤에야 의미가 자란다 — ch05 §3의 작성 절차와 같은 관점.

**시간 배분.** ch01 §6의 readership-weighted budget을 그대로 따른다 — 제목에 한 시간, abstract에 두세 시간이 권장 비율이다. 본문 한 섹션에 8-10시간을 들이는 학생이 abstract에 30분을 쓰는 패턴이 흔하다. 그 비율이 reject 사유의 비율과 거의 정확히 반대로 작동한다.

---

## 22.4 arXiv 시대 — 자동화 pipeline의 first filter

[김기섭 교수 「연구길의 초입에서」](https://gsk1m.github.io/productivity/2024/05/25/entering-research.html)가 같은 문제를 *arXiv 자동화*의 관점으로 적었다.

> *"제목이 입력 pipeline의 first filter다. arXiv·alphaxiv·Google Scholar의 자동 추천·검색 분류기가 제목·초록 token을 보고 paper를 push할지 말지 결정한다."*

이 진단이 §1·§2의 권고에 한 층위를 더 얹는다. reviewer만이 first filter가 아니라는 입장이다. 자동화 분류기가 제목의 keyword density를 입력으로 받아 *어디로 push할지*를 결정한다. contribution keyword와 분야 keyword가 제목에 들어가야 자동화 층위를 통과한다.

**Abstract의 첫 1-2 문장은 자동 요약기·LLM 추천기의 입력 slice.** 그 첫 두 문장에 paper gap과 contribution이 와야 자동화 추천에서 *왜 이 paper가 추천되는가*가 살아남는다. abstract의 마지막에 contribution을 두고 첫 문장을 *분야 일반론*으로 시작하는 패턴이 가장 자주 손실되는 결함.

자동화 층위는 분야 reviewer가 작동하는 층위와 *방향이 같다*. 둘 다 first filter에서 contribution keyword와 paper gap을 본다. 자동화에 맞추는 작업이 reviewer에 맞추는 작업과 정렬된다.

---

## 22.5 흔한 실수 4종

**제목이 명사구만.** "A New Method for Loop Closure"는 동사가 없어 contribution이 *암시*만 된다. reviewer가 본문을 읽어야 contribution이 추출되는 결함.

**Abstract가 본문 도입처럼.** context만 길게 늘이고 result number가 들어가지 않는 패턴. *수치 하나*가 abstract에 박히지 않으면 self-contained 조건이 깨진다.

**Abstract에 외부 참조.** 본문의 figure·section을 가리키는 reference가 들어가면 곧 self-contained 위반.

**제목에 두 contribution.** 첫 논문이면 contribution이 한 줄로 압축되지 않은 시점. ch01 §1의 *하나의 논문에는 하나의 메시지* 권고와 같은 관점. contribution 둘이 제목에 동시에 박히면 두 곳에서 reject 사유가 자란다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §IV — abstract 작성 순서·자기완결성. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 1 (제목 = contribution 한 문장) + rule 5 (abstract = key fits its lock). [김기섭 교수 「연구길의 초입에서」](https://gsk1m.github.io/productivity/2024/05/25/entering-research.html) — arXiv 자동화·제목 first filter. 흔한 실수 4종은 이 장에서 정리했다.

다음: [Ch.8 — Introduction 해부](./chapter_23_introduction.md)
