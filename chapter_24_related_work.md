# Ch.24 — Related Work: 분류와 비판의 자리

Ch.23의 서론이 왜 이 논문이 존재하는가에 답한다면, Related Work는 그 주변에서 누가 무엇을 시도했는가에 답한다. 두 섹션이 함께 심사위원의 1차 판단을 받는다. 두 섹션의 분담이 무너지면 한쪽은 분야 분위기만 늘어놓게 된다.

Related Work를 연도순 인용 나열로만 채우면 어떤 차원에서 연구들을 비교하는지 보이지 않는다. "Smith et al. 2018 did A. Lee et al. 2019 did B. ..." 식으로 단락이 흐르면 본인 방법의 위치도 끝까지 잡히지 않는다. 이 결함 하나가 언제나 reject를 결정한다고 단정할 수는 없지만, novelty와 baseline coverage를 의심하게 만든다.

Ch.16 §16.1의 reject의 complement 관점이 여기에 직결된다. 나열식 목록과 핵심 baseline 누락은 심사에서 반복해서 점검되는 결함이다.

---

## 24.1 분류축 — 나열식 목록 피하기

**Related Work의 골격은 분류축이다.** 본인이 정한 축 위에 선행 연구를 위치시키는 것이 Related Work의 중심 작업이다. 축을 잡지 않은 채 인용을 나열하면 나열식 목록이 된다.

**분류축 후보.** 분야마다 다르지만 로보틱스·CV에서는 다음 네 종류가 자주 등장한다.

- 입력 modality — LiDAR · RGB · RGB-D · IMU 융합
- 표현 방식 — sparse · dense · neural field
- 학습 의존도 — geometric · learned · hybrid
- 적용 scenario — 실내 · 야외 · 동적 환경

**이차원 표.** 연구 수가 많고 두 축이 실제 차이를 설명한다면 행과 열로 분류표를 만들 수 있다. 이는 분야 표준이나 필수 형식이 아니라 사고 도구다. 본인 방법이 표에서 비어 있던 칸에 들어가면 paper gap 후보가 시각적으로 드러나지만, 빈 칸 자체가 연구 가치나 novelty를 증명하지는 않는다.

이차원 표가 분류를 더 명료하게 만든다면 Related Work에 넣는다. 축이 하나이거나 연구 수가 적다면 산문이 더 낫다. 표를 쓰든 산문을 쓰든 분류 기준과 본인 방법의 위치를 독자가 추측하게 두지 않는다.

---

## 24.2 비판의 강도 — 정확하되 정중히

**비판은 방법의 한계에 한정한다.** 저자에 대한 비난·저평가 금지. "Smith et al.'s approach is naive"는 심사위원 입장에서 저자 비난으로 읽힌다. "Smith et al.'s approach assumes static environments"가 방법의 한계에 한정한 표현이다.

**Vague phrasing 점검.** "may suffer from", "is limited in some scenarios", "could be improved"만으로 끝내면 한계의 범위를 알 수 없다. 출처가 보고한 dataset·조건·metric을 구체적으로 적되, 원 논문이 보고하지 않은 수치를 만들어 넣지 않는다.

> ❌ Method X may suffer from drift in long sequences.
>
> ✓ Method X reports $d_1$ drift on sequence A, compared with $d_2$ on the shorter sequences [citation].

✓ 쪽의 $d_1$, $d_2$, sequence 이름은 실제 출처에서 확인해 채운다. 조건과 수치, 인용을 함께 적어 비판의 근거를 추적할 수 있게 한다.

**비판이 강할수록 근거도 강해야 한다.** 본인 실험이나 선행 연구가 보고한 한계를 인용한다. 근거 없이 비판만 강하면 심사위원은 본인 방법의 우위를 만들기 위해 비교를 비튼 것은 아닌지 의심한다.

---

## 24.3 핵심 baseline 누락의 비용

**본인 방법과 가장 가까운 baseline을 빠뜨리면 novelty와 공정 비교가 흔들린다.** Related Work에 등장하지 않은 baseline은 실험 섹션에서도 빠질 수 있다. 누락이 심사 결과에 미치는 정도는 논문의 주장과 venue에 따라 다르지만, 왜 비교하지 않았는지는 설명해야 한다.

**Coverage 기준.** 고정된 5편·3-5편 최소선은 없다. 문제 정의를 만든 anchor, 가장 가까운 방법, 같은 benchmark의 강한 비교군, 최근의 직접 관련 연구가 빠지지 않았는지 claim별로 확인한다. 최신 연구의 범위는 검색 종료일을 적어 경계를 분명히 한다.

**본인 연구실 self-citation 편중.** 본인 연구실 논문만 골라 인용하면 분야의 범위를 비뚤게 제시할 수 있다. 모든 분야에 통하는 30% 안전선은 없다. 각 self-citation이 현재 주장에 직접 필요한지 확인하고, 독립 연구 그룹의 가장 가까운 선행 연구도 같은 기준으로 찾는다.

분야별 탐색의 출발점으로 [robotics-practice ch20 §20.8.1](https://alexjunholee.github.io/robotics-practice/guide.html#2081-논문-쓰기-link)의 baseline catalog를 링크해 둔다. 목록을 그대로 최소 인용 세트로 쓰지 말고, 검색 종료일과 본인 claim에 맞춰 공식 proceedings·논문에서 갱신한다.

---

## 24.4 흔한 실수 4종

**나열식 목록.** 인용을 연도순으로 나열하고 분류축을 두지 않으면, 심사위원은 어떤 차원에서 비교하는지 알 수 없다.

**핵심 baseline 누락.** 본인 방법의 1차 비교 대상이 빠지면 novelty와 공정 비교를 설득하기 어렵다.

**과대 비교.** "we outperform all prior work"를 Related Work에서 선언. 결과 섹션의 몫을 미리 가져온 형태. Ch.19 §19.5의 content와 conclusion 스케일이 섞이는 결함과 같은 축.

**Self-citation 편중.** 본인 연구실 논문만 골라 인용하면 분야 합의를 비뚤게 제시한 것으로 보인다.

---

## 24.5 Ch.23과의 분담

Ch.23의 Introduction에서 paper gap이 한 줄로 박혔다면, Related Work는 그 paper gap의 주변을 본격적으로 펼친다. 두 섹션의 분담이 다음과 같이 작동한다.

| 항목 | Introduction (Ch.23) | Related Work (Ch.24) |
|---|---|---|
| 길이 | paper gap을 여는 데 필요한 범위 | 분류와 위치를 설명하는 데 필요한 범위 |
| 인용 수 | 핵심 주장에 직접 필요한 인용 | 분류축의 주요 계열과 직접 비교군을 덮는 인용 |
| 골격 | gap funnel 3-tier | 분류축(필요하면 이차원 표) |
| 비판 | 한 줄, 빈틈 명시만 | 본격, 수치 근거 |
| 본인 방법 | 한 문장 contribution | 표 위의 한 칸 |

이 분담이 무너지는 가장 흔한 패턴이 Introduction에 prior work 30편을 인용하는 결함이다. Ch.23 §23.6의 흔한 실수인 Background가 textbook 분량인 것과 같은 결함이다. Related Work를 Introduction에 합칠 때도 문제 제기와 기존 연구 분류의 역할이 뒤섞이지 않도록 해야 한다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) — 단락 층위 흐름(간접). [robotics-practice ch20 §20.8.1](https://alexjunholee.github.io/robotics-practice/guide.html#2081-논문-쓰기-link) — 분야별 baseline 탐색의 출발점. 분류축·이차원 표·coverage 점검은 이 장의 작업 도구이며, 고정 인용 수나 self-citation 비율을 표준으로 두지 않는다.

다음: [Ch.25 — 방법 섹션](./chapter_25_method.md)
