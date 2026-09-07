# Ch.22 — 제목과 초록

심사위원에게 배정되는 원고 수와 심사 workflow는 venue마다 다르다. 다만 [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)의 1st pass처럼 제목·초록·서론을 먼저 읽는 독자가 많다. 제목과 초록은 독자가 본문에 들어가기 전에 논문의 큰 틀을 전해야 한다.

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §IV가 둘을 한 묶음으로 다룬 이유도 이 비대칭에서 나온다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 1과 rule 5가 각각 제목과 초록의 골격을 정의해 둔다. Ch.16 §16.6의 readership-weighted budget이 둘에 가장 큰 시간 비중을 할당하라고 권하는 것도 같은 이유다.

---

## 22.1 제목 — 기여를 담은 한 문장

**제목은 논문의 기여를 한 문장으로 압축한다.** Mensh-Kording rule 1은 본인 논문이 분야에 무엇을 더했는지가 제목 한 줄에 드러나야 한다고 적었다.

**제목에서 기여의 방향이 보여야 한다.** "BEV-based Loop Closure"는 주제만 말한다. "BEV-based loop closure halves recall failures on KITTI"처럼 동사·효과·대상을 넣으면 결과형 제목이 된다. 여기 제시된 수치는 제목의 작성 문형을 예시하기 위한 가상 데이터다. 분야 관행상 명사구 제목을 쓰더라도 무엇을 새로 보였는지가 드러나는지 확인한다.

**길이는 venue 규정과 명료성으로 정한다.** 모든 분야에 통하는 12-15단어 규칙은 없다. 기여를 식별하는 데 필요한 말은 남기고, 검색 결과에서 잘려도 뜻이 무너지지 않게 앞부분을 다듬는다.

**Keyword 선택.** contribution과 직결되는 핵심 용어를 제목에 넣는다. 검색·인덱싱에 쓰이는 실제 분야 용어를 고르되, 정해진 개수나 같은 단어의 반복을 목표로 삼지 않는다.

---

## 22.2 초록 — 완결된 CCC

**초록은 자기 안에서 닫혀야 한다.** Mensh-Kording rule 5는 key fits its lock이라는 비유를 썼다. 결과(key)가 정확히 갭(lock)에 들어맞아야 초록이 완성된다. Ch.19 §19.3의 자기완결성과 같은 축에 있다.

**다섯 칸이 한 단락 안에 들어간다.**

1. **Field gap** — 분야 전체의 큰 빈틈 한 줄.
2. **Paper gap** — 본 논문이 메우는 정확한 자리 한 줄.
3. **Approach** — 그 자리를 어떻게 메우는가 한두 줄.
4. **Result** — 핵심 결과. 정량 연구라면 대표 수치를 넣고, 이론·질적 연구라면 검증된 중심 결론을 넣는다.
5. **Implication** — 분야에 무엇을 의미하는가 한 줄.

**외부 참조를 두지 않는다.** "Fig. 3 shows …", "in Sec. 4 we …" 같은 본문 참조가 초록에 들어가면 자기완결성이 깨진다. 초록만 떼어 독립된 원고로 읽어도 자족적이어야 한다.

**길이는 venue의 word limit를 따른다.** 150-250단어는 여러 분야에서 흔히 볼 수 있는 작업 범위일 뿐 보편 규칙이 아니다. 다섯 칸을 빠짐없이 담되 같은 맥락을 되풀이하지 않는다.

---

## 22.3 작성 순서 — 본문이 안정된 뒤

**초록은 맨 마지막에 쓴다.** Whitesides §IV의 권고다. 본문이 흔들리는 동안 초록을 깎는 일은 lock이 흔들리는 동안 key를 깎는 것과 같다. 본문 outline 4-5회차가 안정된 뒤에야 초록 작업을 시작할 수 있다.

제목도 같은 시점에 있다. outline iteration 1-3회차에서는 placeholder로 남아 있어도 된다. claim style로 다듬는 작업은 본문 결론이 안정된 뒤에야 의미가 자란다 — Ch.20 §20.3의 작성 절차와 같은 관점.

**시간 배분.** Ch.16 §16.6의 readership-weighted budget을 따른다. 제목과 초록에 별도 작업 시간을 잡되, 원 출처는 제목 한 시간·초록 두세 시간 같은 고정값을 제시하지 않는다. 실제 기록에서 본문 한 섹션에는 오래 쓰면서 초록은 마감 직전에만 다듬었다면 다음 원고의 예산을 조정한다.

---

## 22.4 arXiv 시대 — 자동화 파이프라인의 첫 관문

[김기섭 교수 「연구길의 초입에서」](https://gsk1m.github.io/productivity/2024/05/25/entering-research.html)가 같은 문제를 arXiv 자동화의 관점으로 적었다. 이 절에서는 그 논점을 제목과 초록이 검색·추천·인덱싱 단계에서 먼저 노출된다는 말로 정리한다.

이 진단은 §1·§2의 권고에 검색·인덱싱 층위를 더한다. 서비스별 추천 알고리즘은 공개 범위가 다르므로 특정 token 수나 keyword density가 노출을 보장한다고 말할 수 없다. 다만 제목과 초록에 실제 분야 용어와 기여가 명료하게 들어가야 검색 결과에서도 논문을 식별할 수 있다.

**초록의 첫 1-2문장은 여러 색인 화면에서 독자에게 먼저 보이는 부분이다.** 첫 두 문장에서 field와 paper gap을 구체화하고, 접근과 결과가 이어질 자리를 만든다. 자동 요약기나 추천기가 정확히 어느 문장을 쓰는지는 서비스마다 다르므로 노출을 보장하는 공식처럼 다루지 않는다.

검색·인덱싱을 위해 기여와 분야 용어를 명료하게 쓰는 일은 사람 독자의 이해에도 도움이 된다. 다만 추천 알고리즘을 추측해 문장을 만드는 대신 사람에게 정확한 제목과 자족적인 초록을 쓰는 것을 기준으로 둔다.

---

## 22.5 흔한 실수 4종

**제목에서 기여가 모호함.** "A New Method for Loop Closure"는 어떤 점이 새로운지 드러나지 않아 contribution이 암시만 된다. 심사위원이 본문을 읽어야 contribution이 추출되는 결함.

**Abstract가 본문 도입처럼.** context만 길게 늘이고 핵심 결과가 들어가지 않는 패턴. 정량 연구라면 대표 수치가, 이론·질적 연구라면 중심 결론이 들어가야 자기 안에서 닫힌다.

**Abstract에 외부 참조.** 본문의 그림·section을 가리키는 reference가 들어가면 곧 self-contained 위반.

**제목에 두 contribution.** 첫 논문이면 contribution이 한 줄로 압축되지 않은 시점. Ch.16 §16.1의 하나의 논문에는 하나의 메시지 권고와 같은 관점. contribution 둘이 제목에 동시에 박히면 두 곳에서 reject 사유가 자란다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §IV — abstract 작성 순서·자기완결성. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 1 (제목 = contribution 한 문장) + rule 5 (abstract = key fits its lock). [김기섭 교수 「연구길의 초입에서」](https://gsk1m.github.io/productivity/2024/05/25/entering-research.html) — arXiv 자동화·제목 first filter. 제목과 초록 작성 시 자주 범하는 네 가지 실수는 실무 검토를 위해 본문에서 유형별로 분류했다.

다음: [Ch.23 — Introduction 해부](./chapter_23_introduction.md)
