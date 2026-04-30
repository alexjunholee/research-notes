# Ch.24 — Related Work: 분류와 비판의 자리

ch08의 Introduction이 *왜 이 논문이 존재하는가*에 답한다면, Related Work는 그 주변에 *누가 무엇을 시도했는가*에 답한다. 두 섹션이 함께 reviewer의 1차 verdict를 받는다. 두 섹션의 분담이 무너지면 한쪽이 *분야 분위기*만 늘어놓는 결함으로 수렴한다.

학생들이 가장 자주 빠지는 결함은 Related Work를 *연도순 인용 나열*로 채우는 것이다. "Smith et al. 2018 did A. Lee et al. 2019 did B. ..." 식으로 단락이 흐르면 reviewer 입장에서 *어떤 차원에서 비교하는가*가 안 보인다. 본인 방법이 어디에 위치하는지가 끝까지 안 잡히고, 이 결함이 단일 reject 사유로 잡힌다.

ch01 §1의 *reject의 complement* 관점이 여기에 직결된다. laundry 목록과 핵심 baseline 누락은 reject 사유로 가장 자주 잡히는 두 결함.

---

## 24.1 분류 axis — laundry 목록 회피

**Related Work의 골격은 분류 axis다.** 본인이 정한 axis 위에 prior work를 *위치*시키는 작업이 Related Work의 본 작업이다. axis가 잡히지 않은 채 인용을 나열하면 그것이 곧 laundry 목록.

**Axis 후보.** 분야마다 다르지만 로보틱스·CV에서 자주 등장하는 axis는 다음 네 종류다.

- 입력 modality — LiDAR · RGB · RGB-D · IMU 융합
- 표현 방식 — sparse · dense · neural field
- 학습 의존도 — geometric · learned · hybrid
- 적용 scenario — 실내 · 야외 · 동적 환경

**이차원 표.** axis 둘로 표를 잡는 것이 분야의 표준 적용 사례는다. 행이 한 axis(예: modality), 열이 다른 axis(예: 학습 의존도). 본인 방법이 표 위에서 *비어 있던 칸*에 들어가면 paper gap이 시각적으로 드러난다. ch08 §2의 paper gap이 표의 한 칸으로 보인다.

이차원 표를 Related Work 섹션에 한 컷 박는 패턴이 분야 reviewer 입장에서 가장 빠르게 *분류 완성도*를 받는다. 표 없이 본문만으로 axis를 전달하면 reviewer가 axis를 *추출*해야 한다.

---

## 24.2 비판의 강도 — 정확하되 정중히

**비판은 *방법의 한계*에 한정한다.** 저자에 대한 비난·저평가 금지. "Smith et al.'s approach is naive"는 reviewer 입장에서 *저자 비난*으로 읽힌다. "Smith et al.'s approach assumes static environments"가 *방법의 한계*에 한정한 표현이다.

**Vague phrasing 금지.** "may suffer from", "is limited in some scenarios", "could be improved" 같은 표현은 reject 사유로 가장 자주 잡히는 결함. 어떤 dataset의 어떤 시퀀스에서 어떤 metric이 얼마나 깨지는지 *수치*로 박는다.

> ❌ Method X may suffer from drift in long sequences.
>
> ✓ Method X reports 8.3% drift on KITTI sequence 09 (length 1700m), compared to 1.1% on shorter sequences.

✓ 쪽은 *어떤 sequence에서 얼마의 drift*가 박혀 있다. reviewer가 이 한 줄을 받으면 비판의 *근거*가 함께 들어온다.

**비판이 강할수록 근거가 강해야.** 본인 실험 또는 prior work의 보고된 한계를 인용. 근거 없이 비판이 강하면 reviewer가 *본인 방법의 우위를 만들기 위한 비뚤음*으로 의심한다.

---

## 24.3 핵심 baseline 누락의 비용

**본인 방법과 가장 가까운 baseline을 빠뜨리면 단일 reject 사유.** ch01 §1의 reject complement 축에서 가장 자주 잡히는 결함이다. Related Work에 등장하지 않은 baseline은 실험 섹션에서도 등장하지 않는 패턴이 함께 따라온다.

**최소선.** 본 분야에서 인용 많은 5편(분야 합의의 anchor)과 최근 1-2년 SOTA 3-5편이 기본. 두 그룹 다 다뤄야 reviewer가 *완성도*를 받는다. 한 그룹만 다루면 *고전 무시* 또는 *최신 무관심*으로 비뚤어 보인다.

**본인 lab self-citation 편중.** 본인 lab 논문만 골라 인용하는 패턴이 외부 reviewer 입장에서 *분야 합의*가 비뚤어 보이는 결함. self-citation은 *전체의 30% 미만*이 안전선.

분야별 사례는 [robotics-practice ch20 § 20.8.1](https://alexjunholee.github.io/robotics-practice/guide.html#2081-논문-쓰기-link)의 분야별 baseline catalog에 링크로 둔다. SLAM·detection·segmentation 분야별 핵심 5편 + 최근 SOTA 3편 목록이 그 링크에 있다.

---

## 24.4 흔한 실수 4종

**Laundry 목록.** 연도순 인용 나열. 분류 axis 부재. reviewer가 *어떤 차원에서 비교하는가*를 추출 못 함.

**핵심 baseline 누락.** 본인 방법과 1차 비교 대상이 빠짐. desk reject 사유.

**과대 비교.** "we outperform all prior work"를 Related Work에서 선언. 결과 섹션의 몫을 미리 가져온 형태. ch04 §5의 *content와 conclusion 스케일이 섞인다* 결함과 같은 축.

**Self-citation 편중.** 본인 lab 논문만 골라 인용. 분야 합의가 비뚤어 보임.

---

## 24.5 ch08과의 분담

ch08의 Introduction에서 paper gap이 한 줄로 박혔다면, Related Work는 그 paper gap의 *주변*을 본격적으로 펼친다. 두 섹션의 분담이 다음과 같이 작동한다.

| 항목 | Introduction (ch08) | Related Work (ch09) |
|---|---|---|
| 길이 | 1-2 단락 | 1-2 페이지 |
| 인용 수 | 5-10편 | 30-50편 |
| 골격 | gap funnel 3-tier | 분류 axis 이차원 |
| 비판 | 한 줄, 빈틈 명시만 | 본격, 수치 근거 |
| 본인 방법 | 한 문장 contribution | 표 위의 한 칸 |

이 분담이 무너지는 가장 흔한 패턴이 Introduction에 prior work 30편을 인용하는 결함이다. ch08 §6의 흔한 실수 *Background가 textbook 분량*과 같은 결함. Related Work를 별도 섹션으로 분리하지 않고 Introduction에 합치면 양쪽이 함께 무너진다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) — paragraph 층위 흐름 (간접). 분야 standard 관점 — 이차원 axis 표·SOTA + 인용 5편 minimum. [robotics-practice ch20 § 20.8.1](https://alexjunholee.github.io/robotics-practice/guide.html#2081-논문-쓰기-link) — 분야별 baseline catalog. 흔한 실수 4종, 비판 강도 권고, 이차원 axis 표 합성은 이 장에서 정리했다.

다음: [Ch.10 — 방법 섹션](./chapter_25_method.md)
