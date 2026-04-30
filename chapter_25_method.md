# Ch.25 — 방법 섹션

[Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9의 readership 순서에서 Method는 가장 적게 읽히는 섹션이다. 다만 그 적은 readership에 *재현성·정확성·공정성*에 대한 reviewer 검증이 집중된다. Method는 읽힐 때 작동한다 — 읽힐 준비가 안 되어 있으면 곧 reject 사유로 굳는다.

학생들이 가장 자주 빠지는 결함은 Method를 *시간순 lab notebook*으로 쓰는 것이다. ch04 §1의 chronological structure 결함과 같은 결, "처음에 X를 시도했는데 안 돼서 Y로 갔고, Y가 또 한계가 있어서 Z에 도달했다"가 본문에 그대로 나오는 패턴. 이 구조는 lab notebook에는 적합하지만 Method에는 main failure mode다.

---

## 25.1 Results-driven structure — 결과를 받기 위한 골격

🔴 **Method 섹션의 골격은 Results 섹션의 골격을 거꾸로 받는다.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V·§VI의 강한 권고. Results의 각 figure·table을 만든 procedure가 Method의 각 sub-section으로 이어진다.

이 frame이 작업 순서를 정한다. Results outline을 먼저 잡고, 그 outline에서 Method outline을 *역으로 추출*한다. ch11에서 다룰 main result table·ablation table·qualitative figure 각각이 Method 어느 sub-section과 짝지어지는지가 outline 단계에서 결정된다.

🟡 **Method의 sub-heading.** ch05의 claim style은 Method에서는 살짝 약화된다. "Section 3.1 Feature Extraction"보다 "Section 3.1 Multi-scale BEV feature extraction"이 정보 밀도가 높지만, Results의 sub-heading만큼 *결과*가 박힐 곳은 아니다. 명사·기법명 위주로.

---

## 25.2 Notation table — 추적 가능한 표기

🔴 **Method 도입에 notation table 한 컷.** 본문에 등장하는 모든 기호가 그 표 안에서 한 번 정의되어야 한다. 본문에 흩뿌려진 정의는 reviewer가 *처음 등장한 자리*를 backtrack하게 만든다.

🟡 **표 구성.** 다음 네 column이 default다.

| Symbol | Meaning | Dimension/Unit | First introduced |
|---|---|---|---|
| $\mathbf{T}_k$ | sensor pose at time $k$ | $SE(3)$ | §3.1 |
| $\mathbf{r}_i$ | reprojection residual for measurement $i$ | $\mathbb{R}^2$ | §3.2 |
| $\lambda$ | regularization weight | scalar | §3.3 |

🔴 **한 기호의 두 의미 금지.** $R$이 회전행렬·residual·reward로 동시에 쓰이는 논문이 흔하다. 한 기호 한 의미가 ch15 §1 R8에서 다룬 원칙이고, 강제력 있는 통일은 ch16의 매크로 위생에서 본격적으로 다룬다.

---

## 25.3 Algorithm pseudocode — 재현성을 받는 도구

🟡 **본 알고리즘은 pseudocode로.** algorithm2e LaTeX 환경이 분야 표준 — 자세한 LaTeX 도구는 [robotics-practice ch20 § 20.8.5](https://github.com/jhlee9633/robotics-practice/blob/main/ch20.md)에 link로 위임.

🟡 **Pseudocode 구조.**

- **Input** 한 줄. *어떤 데이터·어떤 hyperparameter*를 받는가.
- **Output** 한 줄. *어떤 결과·어떤 형태*로 반환하는가.
- **본문 step** 줄별로. 본문 수식이 등장하는 step에는 식 번호로 cross-reference.

🟡 **계산 복잡도.** pseudocode 끝 또는 caption에 명시. $O(N)$인지 $O(N \log N)$인지 $O(N^2)$인지가 빠지면 reviewer가 *언급되지 않은 곳*에서 의심한다. runtime 보고가 빠른데 complexity가 안 적혀 있으면 *정말 빠른가*가 검증 불가로 남는다.

---

## 25.4 Hyperparameter table — 변인의 명시

🔴 **Hyperparameter는 모두 표로.** 본문에 흩뿌리면 reviewer가 추적 못 한다. "we use learning rate 1e-4 ... batch size 32 ... 그리고 또 ..."가 본문에 분산되어 있는 패턴이 가장 자주 결함으로 잡힌다.

🟡 **표 구성.** parameter · 값 · 의미 · 변경 시 영향 (sensitivity). 마지막 column이 ablation 섹션과 직결한다 — ch11의 ablation 표가 sensitivity column을 *검증한다*.

🟡 **Dataset별로 다른 hyperparameter.** dataset × parameter 이차원 표로. 한 hyperparameter가 dataset에 따라 다르면 *어떤 dataset에서 어떤 값이 default인가*가 명시되어야 한다.

---

## 25.5 흔한 실수 5종

🔴 **시간순 흐름.** "처음에 X 시도, 실패, Y로 변경, 또 실패, Z 도달". lab notebook이지 Method가 아니다.

🔴 **Notation 흩뿌리기.** 본문에서 처음 등장한 자리에서만 정의. 다시 찾으려면 backtrack해야 한다. notation table 부재의 결함과 같은 축.

🔴 **Hyperparameter 본문 흩뿌리기.** 표 부재. reviewer가 셀 수 없다.

🔴 **Pseudocode 부재.** 본문 수식만으로 알고리즘 재현 시도. step 순서·loop 구조가 모호해진다.

🟡 **계산 복잡도 누락.** runtime 보고는 있는데 complexity가 없으면 reviewer가 *왜 빠른가*를 못 받는다.

---

## 25.6 ch11과의 짝짓기

Method의 each sub-section이 Results의 each sub-section과 짝지어진 형태에 도달하면, 두 섹션의 일관성이 reviewer 1차 검증을 통과하는 첫 조건으로 잡힌다. 짝짓기가 어긋나는 두 패턴이 가장 자주 결함으로 잡힌다.

- **Method에는 있는데 Results에는 없는 component.** "we use multi-scale fusion"이 Method §3.2에 있는데 Results의 어느 figure에서도 검증되지 않은 결함. ablation 부재로 이어진다 — ch11 §3.
- **Results에는 있는데 Method에는 없는 component.** Results §4에서 ablation 표에 "w/o geometric prior" row가 등장했는데 Method에는 geometric prior 정의가 없는 결함. notation·정의 누락.

두 패턴 모두 outline 단계에서 Method ↔ Results 짝짓기를 명시적으로 해 두면 사라진다. outline 4-5회차에서 각 sub-section 옆에 *짝* 표시를 다는 작업이 분야 reviewer가 작동하는 1차 검증을 *미리* 통과시키는 일이다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V·§VI — Method 작성·write the methods first. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 5·6 — results-driven structure. 분야 standard — notation table·pseudocode·hyperparameter table. [robotics-practice ch20 § 20.8.5](https://github.com/jhlee9633/robotics-practice/blob/main/ch20.md) — booktabs·algorithm2e LaTeX (link). 흔한 실수 5종과 짝짓기 진단은 자체.

다음: [Ch.11 — 결과·논의](./chapter_26_results_discussion.md)
