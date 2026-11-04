# Ch.25 — 방법 섹션

[Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)은 rule 9에서 제목, 초록, 그림을 보는 사람이 논문의 나머지를 읽는 사람보다 훨씬 많고, Method 섹션을 읽는 사람이 가장 적다고 했다. 이 장은 Method까지 읽는 독자를 결과를 재현하거나 비교가 공정했는지 따지려는 사람으로 보고 쓴다. 이 독자에게 필요한 정보가 빠지면 주장(claim)의 근거가 약해진다.

Method를 연구 노트처럼 시간순으로 쓰면 최종 방법의 논리가 가려진다. "처음에 X를 시도했는데 안 돼서 Y로 갔고, Y에도 한계가 있어서 Z에 이르렀다" 같은 과정은 연구 노트에 남긴다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)는 2.4절에서 초심자가 처음의 실패부터 마지막 성공까지 실험 과정을 시간순으로 늘어놓곤 한다고 지적하고, 중요한 결과부터 쓰라고 했다. Method에는 재현에 필요한 최종 절차와 그 절차를 고른 근거를 논리 순서로 쓴다.

---

## 25.1 Results-driven structure — 결과에 맞춘 골격

**Method의 순서는 Results의 순서를 따른다.** Whitesides는 개요에 들어갈 항목을 적으면서(2.3절 항목 7) Experimental 섹션의 소제목을 Results 섹션의 순서에 맞춰 적으라고 했다. Mensh와 Kording도 rule 7에서 control과 method는 전체 논리에 필요한 자리에 들어간다고 했다. Results의 그림과 표를 만든 절차가 Method의 서브섹션이 된다.

그래서 Results의 개요(outline)를 먼저 잡고, 그 개요를 거슬러 가며 Method의 개요를 만든다. Ch.26의 주요 결과 표, ablation 표, 정성 비교 그림이 각각 Method의 어느 서브섹션에 대응하는지는 개요 단계에서 정한다.

**Method의 소제목.** "Section 3.1 Feature Extraction"보다 "Section 3.1 Multi-scale BEV feature extraction"에 정보가 더 많다. 다만 Method 소제목에는 [Ch.20](./chapter_20_subheadings_and_conclusions.md)의 주장형 소제목처럼 결과를 넣을 수 없으니, 명사와 기법 이름으로 쓴다.

---

## 25.2 Notation table — 기호를 찾아볼 수 있는 표

**기호가 많으면 Method 앞부분에 notation table(기호 표)을 둔다.** 핵심 기호를 표에서 한 번 정의하고, 본문에서 처음 나올 때도 뜻을 알 수 있게 쓴다. 기호가 몇 개뿐이면 본문에서 정의하는 것으로 충분하다.

**표 구성.** 아래 네 열은 예시다. 학회·학술지 템플릿과 기호 수에 맞춰 줄인다.

| Symbol | Meaning | Dimension/Unit | First introduced |
|---|---|---|---|
| $\mathbf{T}_k$ | sensor pose at time $k$ | $SE(3)$ | §3.1 |
| $\mathbf{r}_i$ | reprojection residual for measurement $i$ | $\mathbb{R}^2$ | §3.2 |
| $\lambda$ | regularization weight | scalar | §3.3 |

**한 기호에는 한 뜻만 준다.** 로보틱스 논문에서는 $R$ 하나가 회전행렬, residual, reward를 함께 가리키기도 한다. 한 기호에 한 뜻만 주는 원칙은 [Ch.30 R8](./chapter_30_math_and_proofs.md)에서, 이 원칙을 LaTeX 매크로로 지키는 방법은 [Ch.31](./chapter_31_notation_hygiene.md)에서 다룬다.

---

## 25.3 Algorithm pseudocode — 재현을 돕는 의사코드

**단계의 순서, 분기, 반복이 방법의 핵심이면 pseudocode(의사코드)를 넣는다.** LaTeX에서는 `algorithm2e` 패키지를 흔히 쓴다. 학회·학술지 템플릿이 정한 환경이 있으면 그것을 따르고, 정해진 것이 없으면 [robotics-practice ch20 §20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#208-연구-실전)의 도구 목록을 참고한다.

**Pseudocode 구조.**

- **Input** 한 줄. 어떤 데이터와 hyperparameter를 받는지 적는다.
- **Output** 한 줄. 무엇을 어떤 형태로 돌려주는지 적는다.
- **단계** 한 줄에 하나씩. 본문 수식을 쓰는 단계에는 식 번호를 붙인다.

**계산 복잡도.** 입력 크기에 따라 비용이 어떻게 늘어나는지 분석할 수 있으면 pseudocode 뒤나 본문에 적는다. 이론적 복잡도와 실제 실행 시간(runtime)은 따로 적는다. 빠르다고 주장한다면 하드웨어, 구현, 입력 크기, 측정 방법도 함께 적는다. 복잡도를 분석할 수 있는데 runtime만 보고하면 심사위원은 왜 빠른지 짐작해야 한다.

---

## 25.4 Hyperparameter table — 설정값을 한곳에

**재현에 필요한 hyperparameter는 한곳에서 찾을 수 있게 한다.** 수가 많으면 표나 공개 config 파일로 모으고, 핵심 값은 본문에서도 설명한다. "we use learning rate 1e-4 … batch size 32 …" 같은 값이 여러 곳에 흩어져 있으면 어떤 설정으로 결과를 냈는지 따라가기 어렵다.

**표 구성.** parameter, 값, 뜻, 값을 바꿨을 때의 영향(sensitivity)을 적는다. 마지막 열의 근거는 Ch.26의 ablation 표에서 보인다.

**Dataset마다 값이 다른 hyperparameter.** dataset을 행에, parameter를 열에 놓은 표로 정리한다. 어떤 dataset에서 어떤 값을 기본으로 썼는지가 드러나야 한다.

---

## 25.5 Ch.26의 Results와 맞추기

Method의 서브섹션마다 대응하는 Results의 서브섹션이 있으면 심사위원은 두 섹션이 서로 맞는지 쉽게 확인할 수 있다. 두 섹션이 어긋나는 흔한 경우는 다음과 같다.

- **Method에는 있는데 Results에는 없는 구성 요소.** Method §3.2에 "we use multi-scale fusion"이라고 썼는데 Results의 어느 그림에서도 그 효과를 검증하지 않은 경우다. 대개 ablation이 빠져 있다([Ch.26 §26.2](./chapter_26_results_discussion.md)).
- **Results에는 있는데 Method에는 없는 구성 요소.** Results §4의 ablation 표에 "w/o geometric prior" 행이 있는데 Method에는 geometric prior의 정의가 없는 경우다. 정의나 기호가 빠진 것이다.

개요 단계에서 Method의 서브섹션마다 대응하는 Results 항목을 옆에 적어 두면 두 경우를 일찍 찾을 수 있다.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7(control과 method는 논리에 필요한 자리에), rule 9(Method를 읽는 사람이 가장 적다). [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 2.3절 항목 7(Experimental 소제목을 Results 순서에 맞추기), 2.4절(시간순으로 쓰지 말고 중요한 결과부터). [robotics-practice ch20 §20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#208-연구-실전) — LaTeX 도구 예시. notation table, pseudocode, hyperparameter table의 구성은 이 장에서 정리했다.

다음: [Ch.26 — 결과와 논의](./chapter_26_results_discussion.md)
