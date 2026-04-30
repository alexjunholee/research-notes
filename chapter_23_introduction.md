# Ch.23 — Introduction 해부: gap funnel과 Whitesides 5요소

논문 1차 심사에서 reviewer가 verdict의 큰 뼈대를 잡는 곳 — Introduction이다. [Keshav (2007)](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)이 정리한 1st pass에서 reviewer가 읽는 페이지는 첫 한 장이고, 그 한 장의 대부분이 Introduction이다. 이 사실이 Introduction의 비중을 정한다. Introduction이 흔들리면 method가 정확해도 verdict는 reject 쪽으로 기운다.

학생들이 가장 자주 하는 실수는 Introduction을 *Related Work의 축약본*으로 채우는 것이다. 인용을 줄줄 늘어놓고, 끝에서 "we propose …"로 점프한다. 이 형식은 reviewer 입장에서 *왜 이 논문이 존재하는지*에 답을 못 얻은 채로 contribution 문장에 도달하게 만든다.

해소는 두 프레임을 겹쳐 쓰는 데서 시작한다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §III가 정리한 5요소 — 무엇이 들어가야 하는가의 자리표 — 와 [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 6의 gap funnel — 어떤 순서로 좁혀 가는가의 흐름표 — 두 가지를 겹친다.

---

## 23.1 Whitesides 5요소 — slot 점검

Whitesides가 §III에 박은 다섯 칸은 다음과 같다.

1. **Objectives** — 무엇을 했는가. 한 문장으로 답할 수 있어야 한다.
2. **Justification** — 왜 했는가. objective의 동기.
3. **Background** — 독자가 알아야 하는 *최소* 사전 지식. textbook이 아니라 footnote 분량.
4. **Reader guidance** — 이 논문에서 무엇을 만나게 되는지. "In Sec. 2 we describe …".
5. **Summary preview** — 핵심 결과의 한 줄. abstract와 다른 함의로 작동.

다섯 칸 모두를 첫 1-2 단락에 욱여넣으라는 것이 Whitesides의 권고다. 그가 §II에서 "first paragraph in full early"를 강조한 이유도 첫 두 단락의 정보 밀도가 높기 때문이다. Introduction의 나머지는 이 5요소의 *부연*이지 새 정보가 아니다.

5요소 점검은 reviewer 시점에서 reverse-read로 한다. 자기 Introduction 첫 두 단락에서 다섯 칸이 한 줄씩 추출되는가. 추출이 안 되는 칸이 있다면 그 칸이 비어 있다는 뜻이다. 그중 가장 자주 빠지는 칸 — Reader guidance다.

---

## 23.2 Gap funnel — 3-tier nesting

5요소가 정적인 자리표라면, gap funnel은 동적인 깔때기다. Mensh & Kording rule 6이 Introduction의 흐름을 세 계단의 빈틈으로 정의했다.

- **Field gap**. 분야 전체가 풀지 못한 큰 문제. 한 줄.
- **Subfield gap**. 그 분야의 specific 영역에서의 한계. 한두 줄.
- **Paper gap**. 본 논문이 정확히 메우는 빈틈. 한 줄.
- **→ 기여**. 그 빈틈을 어떻게 메웠는가.

핵심은 빈틈이 *좁아진다*는 사실이다. field gap은 broad하게 시작하고, paper gap에서 한 점으로 수렴한다. reviewer가 이 깔때기를 따라 내려오면서 "이 논문이 정확히 어디를 메우는가"를 자연스럽게 받는다.

학생들이 가장 흔하게 어기는 칸 — paper gap이다. subfield gap에서 곧장 contribution으로 점프하면 깔때기 한 단이 비고, reviewer는 "왜 *이 방법*으로 메웠는가"를 본문 어디서도 못 얻는다. 가장 좁은 단이 비면 깔때기 전체가 무너진다.

---

## 23.3 한국어 mirror — 엄태웅 작가 6단

같은 흐름을 한국어 설명로 풀어낸 글이 [엄태웅 작가 G2 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net)의 Introduction 6단이다.

> 1. 큰 문제 — 분야 전체가 푸는 문제.
> 2. 점진적 스코프 축소 — 그 분야 안에서 본 논문이 향하는 자리.
> 3. 선행 연구 — 그 자리에서 쌓인 시도들.
> 4. 한계 — 선행 연구가 풀지 못한 자리.
> 5. 본 연구 기여 — 한계를 메우는 본 논문의 시도.
> 6. 논문 구성 — 다음 섹션 안내.

이 6단이 §2의 gap funnel 3-tier(field → subfield → paper)와 §1의 Whitesides 5요소를 한 절차에 합친 한국어 적용 사례는다. 1·2·3·4가 gap funnel을 점진적으로 좁히고, 5가 contribution + summary preview를 채우고, 6이 Whitesides의 reader guidance 칸을 명시적으로 박는다. 한국어 문체가 빠뜨리지 않는 6번(논문 구성)이, 영어권 학생이 자주 누락하는 reader guidance와 정확히 같다.

엄태웅 작가가 같은 글에서 강조하는 비율이 *Intro에 노력의 40-50% 투자*다. 90%의 reviewer가 abstract와 Introduction에서 verdict의 큰 뼈대를 잡는다는 관찰이 그 비율의 근거다. ch01 §6에서 다룬 readership-weighted budget(Mensh-Kording R9)의 한국어 mirror로 읽으면 된다.

---

## 23.4 두 프레임의 매핑

5요소와 gap funnel은 경쟁이 아니라 중첩으로 작동한다.

| Whitesides 5요소 | Gap funnel 위치 |
|---|---|
| Background | Field gap + Subfield gap |
| Justification | Subfield gap → Paper gap |
| Objectives | Paper gap을 메우려는 시도의 명시 |
| Summary preview | 기여 |
| Reader guidance | (구조적 도움말, funnel과 별개 축) |

이 매핑이 작업 순서를 정한다. outline 단계에서 gap funnel로 *흐름*을 결정하고, draft 단계에서 5요소로 *칸*을 점검한다. 두 단계를 합치면 한쪽이 다른 쪽을 가린다.

---

## 23.5 사례 — KISS-ICP의 첫 단락

[KISS-ICP (Vizzo et al., RA-L 2023)](https://arxiv.org/abs/2209.15397)의 Introduction 첫 단락이 두 프레임을 한 호흡에 통과시킨다. field gap은 "LiDAR odometry는 풀린 문제처럼 보인다"로 열고, subfield gap은 "튜닝 지옥이다"로 좁힌다. 그러고는 paper gap이 "단순한 baseline이 부재하다"로 한 점에 모인다. 그 단락의 마지막 문장이 summary preview를 겸한다 — "we show that simple ICP is sufficient when carefully configured."

5요소도 같은 단락에서 다 채워진다. 칸도 정연하다. (a) objective는 "단순한 LiDAR odometry baseline 제시", (b) justification은 "단순함이 generality를 낳는다", (c) background는 ICP 계열의 기존 한계, (d) reader guidance는 다음 단락 시작에서, (e) summary preview는 첫 단락 마지막 문장에서.

발췌와 줄별 분석은 Part 3 [`kiss_icp_intro_hook.md`](./excerpts/excerpt_01_kiss_icp_intro_hook.md)에 있다.

---

## 23.6 흔한 실수 4종

**첫 문장이 trend 나열로 시작.** "Recently, deep learning has revolutionized …" 류. field gap이 아니라 *분야 분위기*로 시작하면 깔때기가 열리지 않는다. 첫 문장은 *문제*에서 연다.

**Background가 textbook 분량.** 3 단락 이상이면 background가 아니라 mini-survey다. Related Work 섹션이 따로 있다. Introduction의 background는 *paper gap을 이해하기 위한 최소량*만.

**Reader guidance 누락.** "In Sec. 2 we …" 한 단락이 통째로 빠진 Introduction이 흔하다. Whitesides가 5요소에 명시적으로 박아 둔 칸이다. 한 단락 또는 한 문장이라도 들어가야 한다.

**Objective와 기여이 같은 표현으로 반복.** 첫 단락의 objective 문장과 기여 절의 첫 항이 동일한 어구이면 둘 중 하나가 잉여다. objective는 *시도*를, contribution은 *결과*를 적는다.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 6 — gap funnel 3-tier nesting. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §II–§III — 5요소와 first-paragraph-in-full 권고. [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) — 1st pass에서 Introduction의 비중. [엄태웅 작가 G2 「논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net) — Introduction 6단과 *노력의 40-50% Intro 투자* 비율. 두 프레임의 연결과 KISS-ICP 적용은 본문에서 정리.

다음: [Ch.9 — Related Work: 분류와 비판의 자리](./chapter_24_related_work.md)
