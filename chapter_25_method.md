# Ch.25 — 방법 섹션

[Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9은 Method보다 제목·초록·그림을 더 많은 독자가 본다고 지적한다. 다만 Method를 읽는 독자는 재현성·정확성·공정성을 세밀하게 검토할 수 있다. 필요한 정보가 빠지면 claim의 근거가 약해진다.

Method를 시간순 연구실 노트로 쓰면 최종 방법의 논리가 가려질 수 있다. "처음에 X를 시도했는데 안 돼서 Y로 갔고, Y가 또 한계가 있어서 Z에 도달했다"는 과정은 연구 노트에 남긴다. Method에서는 재현에 필요한 최종 절차와 선택 근거를 논리 순서로 배치한다.

---

## 25.1 Results-driven structure — 결과를 받기 위한 골격

**Method 섹션의 골격은 Results에 필요한 절차를 거슬러 짚어 구성한다.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V·§VI의 권고다. Results의 각 그림·표를 만든 절차가 Method의 각 서브섹션으로 이어진다.

이 관점에 따라 Results outline을 먼저 잡고, 그 outline에서 Method outline을 역으로 만든다. Ch.26에서 다룰 main result table·ablation table·qualitative figure 각각이 Method의 어느 sub-section과 짝지어지는지는 outline 단계에서 정한다.

**Method의 소제목.** Ch.20의 주장형 소제목은 Method에서 조금 약해진다. "Section 3.1 Feature Extraction"보다 "Section 3.1 Multi-scale BEV feature extraction"이 정보 밀도가 높지만, Results의 소제목만큼 결과가 들어갈 곳은 아니다. 명사와 기법명을 중심으로 쓴다.

---

## 25.2 Notation table — 추적 가능한 표기

**표기가 많다면 Method 도입에 notation table을 둔다.** 핵심 기호를 표에서 한 번 정의하고 본문 첫 등장에서도 뜻을 알 수 있게 쓴다. 기호가 몇 개뿐이라면 별도 표를 두지 않고 본문 산문 정의만으로 충분하다.

**표 구성.** 다음 네 열은 이 장이 제안하는 예시다. venue template와 기호 수에 맞춰 줄인다.

| Symbol | Meaning | Dimension/Unit | First introduced |
|---|---|---|---|
| $\mathbf{T}_k$ | sensor pose at time $k$ | $SE(3)$ | §3.1 |
| $\mathbf{r}_i$ | reprojection residual for measurement $i$ | $\mathbb{R}^2$ | §3.2 |
| $\lambda$ | regularization weight | scalar | §3.3 |

**한 기호의 두 의미 금지.** $R$이 회전행렬·residual·reward로 동시에 쓰이는 논문이 흔하다. 한 기호 한 의미는 [Ch.30 R8](./chapter_30_math_and_proofs.md)의 원칙이고, 강제력 있는 통일은 [Ch.31](./chapter_31_notation_hygiene.md)의 매크로 위생에서 다룬다.

---

## 25.3 Algorithm pseudocode — 재현성을 확보하는 도구

**단계 순서·분기·반복이 핵심이면 pseudocode를 제시한다.** `algorithm2e`는 실무에서 널리 활용되는 편리한 LaTeX 패키지다. venue template이 지정한 환경을 우선 따르고, 선택지가 열려 있으면 [robotics-practice ch20 §20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#2085-도구)의 예를 참고한다.

**Pseudocode 구조.**

- **Input** 한 줄. 어떤 데이터·어떤 hyperparameter를 받는가.
- **Output** 한 줄. 어떤 결과·어떤 형태로 반환하는가.
- **본문 step** 줄별로. 본문 수식이 등장하는 step에는 식 번호로 reference.

**계산 복잡도.** 입력 크기에 따른 비용을 의미 있게 분석할 수 있다면 pseudocode 뒤나 본문에 명시한다. 이론적 복잡도와 실제 runtime은 서로 다른 근거이므로 둘을 대신 쓰지 않는다. `빠르다`고 주장한다면 hardware·implementation·입력 크기와 측정 protocol도 함께 적는다.

---

## 25.4 Hyperparameter table — 변인의 명시

**재현에 필요한 hyperparameter를 한곳에서 찾게 한다.** 수가 많으면 표나 공개 config로 정리하고, 핵심 값은 본문에서도 설명한다. "we use learning rate 1e-4 ... batch size 32 ... 그리고 또 ..."가 여러 곳에 흩어지면 어떤 설정으로 결과를 냈는지 추적하기 어렵다.

**표 구성.** parameter · 값 · 의미 · 변경 시 영향(sensitivity)을 적는다. 마지막 열은 ablation 섹션과 직결된다. Ch.26의 ablation 표가 sensitivity 열을 검증한다.

**Dataset별로 다른 hyperparameter.** dataset × parameter 이차원 표로. 한 hyperparameter가 dataset에 따라 다르면 어떤 dataset에서 어떤 값이 기본인가가 명시되어야 한다.

---

## 25.5 흔한 실수 5종

**시간순 서술.** "처음에 X 시도, 실패, Y로 변경, 또 실패, Z 도달" 식의 서술은 연구실 노트에 가깝고 Method 섹션의 논리를 흐린다.

**Notation 흩뿌리기.** 본문에서 처음 등장한 자리에서만 정의. 다시 찾으려면 backtrack해야 한다. 기호가 많다면 notation table로 모아 찾게 한다.

**Hyperparameter 본문 흩뿌리기.** 표나 공개 config 등으로 모아 두지 않아 심사위원이 한눈에 파악할 수 없다.

**Pseudocode 부재.** 단계 순서·분기·반복이 핵심인데도 본문 수식만으로 재현을 시도하면 step 순서와 loop 구조가 모호해진다.

**계산 복잡도 누락.** 의미 있는 복잡도 분석이 가능한데 runtime만 보고하면 심사위원은 빠른 이유를 확인할 수 없다.

---

## 25.6 Ch.26과의 짝짓기

Method의 각 서브섹션이 Results의 서브섹션과 짝지어지면, 두 섹션의 일관성을 심사위원이 1차로 검증할 수 있다. 다음 두 패턴에서 짝이 가장 자주 어긋난다.

- **Method에는 있는데 Results에는 없는 component.** "we use multi-scale fusion"이 Method §3.2에 있는데 Results의 어느 그림에서도 검증되지 않은 결함. ablation 부재로 이어진다 — Ch.26 §26.2.
- **Results에는 있는데 Method에는 없는 component.** Results §4에서 ablation 표에 "w/o geometric prior" row가 등장했는데 Method에는 geometric prior 정의가 없는 결함. notation·정의 누락.

두 패턴은 outline 단계에서 Method ↔ Results 짝을 표시하면 일찍 발견할 수 있다. outline을 다듬는 후반부에 각 sub-section 옆에 대응하는 결과를 명기해 두면, 누락된 구성 요소나 검증 공백을 확실히 걸러낼 수 있다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V·§VI — Method 작성과 실험 절차 기록. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rules 7·9 — 결과 논리의 outline과 시간 배분. [robotics-practice ch20 §20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#2085-도구) — LaTeX 도구 예시. notation table·pseudocode·hyperparameter table은 필요에 따라 유연하게 선택하는 실무 서술 도구다.

다음: [Ch.26 — 결과·논의](./chapter_26_results_discussion.md)
