# 25장 방법 섹션

서론과 Related Work에서 논문의 문제의식과 자리를 분명히 세웠다면, 이제 그 빈틈을 실제로 어떻게 해결했는지 구체적인 장치를 내보일 차례다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)의 rule 9에서 보았듯 Method는 논문에서 가장 적게 읽히는 섹션이다([18장 §18.1](./chapter_18_time_budget.md)). 하지만 역설적으로 Method까지 꼼꼼히 파고드는 소수의 독자는 실험을 직접 재현해 보려거나 비교가 공정했는지 따져 묻는 깐깐한 독자와 심사위원이다. 이 독자에게 꼭 필요한 정의와 설정이 빠져 있으면, 아무리 앞선 섹션이 매끄러워도 논문의 주장(claim)을 받치는 근거가 통째로 흔들린다.

Method를 쓸 때 가장 먼저 피해야 할 습관은 연구 노트처럼 시행착오를 시간순으로 늘어놓는 일이다. "처음에 X를 시도했는데 안 돼서 Y로 갔고, Y에도 한계가 있어서 Z에 이르렀다"와 같은 탐색의 역사는 연구 노트에 남겨 두면 된다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 역시 2.4절에서 이런 시간순 서술을 피하라고 당부한다([17장 §17.2](./chapter_17_outline_first.md)). Method에는 연구자가 거쳐 온 우회로가 아니라, 결과를 재현하는 데 필요한 최종 절차와 그 절차를 선택한 논리적 근거를 체계적인 순서로 적어야 한다.

---

## 25.1 Results-driven structure — 결과에 맞춘 골격

시간순이 아니라면 Method의 순서는 무엇을 기준으로 세워야 할까? 답은 단순하다. **Method의 순서는 Results의 순서를 따른다.** Whitesides는 개요 항목을 정리하면서(2.3절 항목 7) Experimental 섹션의 소제목을 Results 섹션의 순서에 맞춰 적으라고 권하고, Mensh와 Kording 역시 rule 7에서 control과 method는 전체 논리에 필요한 자리에 놓여야 한다고 설명한다. 결국 Results의 그림과 표를 만들어 낸 절차가 그대로 Method의 서브섹션이 되는 셈이다.

실무적으로는 Results의 개요(outline)를 먼저 잡은 뒤, 그 개요를 거슬러 올라가며 Method의 개요를 짠다. 26장에서 다룰 주요 결과 표, ablation 표, 정성 비교 그림이 각각 Method의 어느 서브섹션에서 설명한 구성 요소에 대응하는지 개요 단계에서 짝을 맞춰 두면 중간에 빠지거나 겉도는 절이 줄어든다.

골격이 잡히면 **Method의 소제목도 구체적으로 적는다.** "Section 3.1 Feature Extraction"처럼 뭉뚱그리기보다 "Section 3.1 Multi-scale BEV feature extraction"처럼 핵심 기법이 드러나게 적는 편이 훨씬 많은 정보를 준다. 물론 Method 소제목에는 [20장](./chapter_20_subheadings_and_conclusions.md)의 주장형 소제목처럼 실험 결과를 먼저 실을 수 없으니, 기법의 핵심과 대상을 정확히 담은 명사구로 정리한다.

---

## 25.2 Notation table — 기호를 찾아볼 수 있는 표

서브섹션마다 수식과 변수가 연달아 등장하는 논문에서는 독자가 앞뒤 페이지를 오가며 기호의 뜻을 다시 찾다가 흐름을 놓치기 쉽다. **기호가 많은 논문이라면 Method 앞부분에 notation table(기호 표)을 두어** 핵심 기호를 한 번에 정리해 두고, 본문에서 처음 등장할 때도 문맥 안에서 뜻을 한 번 더 짚어 준다. 물론 기호가 몇 개 안 되는 논문이라면 굳이 표를 만들지 않고 본문에서 바로 정의하는 편이 깔끔하다.

표를 둘 때는 아래 네 열을 기본 틀로 삼아 학회·학술지 지면과 기호 수에 맞게 간추려 쓴다.

| Symbol | Meaning | Dimension/Unit | First introduced |
|---|---|---|---|
| $\mathbf{T}_k$ | sensor pose at time $k$ | $SE(3)$ | §3.1 |
| $\mathbf{r}_i$ | reprojection residual for measurement $i$ | $\mathbb{R}^2$ | §3.2 |
| $\lambda$ | regularization weight | scalar | §3.3 |

표로 기호를 모아 두면 **한 기호에 한 뜻만 주는 원칙**을 지키기도 훨씬 수월해진다. 로보틱스 논문에서는 $R$ 하나가 회전행렬과 residual, reward를 동시에 가리켜 독자를 혼란에 빠뜨리는 일이 잦다. 표를 먼저 정리해 두면 이런 기호 충돌을 초고 단계에서 바로 걸러 낼 수 있다(→ [30장 R8](./chapter_30_math_and_proofs.md); [31장](./chapter_31_notation_hygiene.md)).

---

## 25.3 Algorithm pseudocode — 재현을 돕는 의사코드

수식만으로 파악하기 어려운 **단계의 순서나 분기, 반복 구조가 방법의 핵심이라면 pseudocode(의사코드)를 함께 싣는 편이 좋다.** LaTeX에서는 `algorithm2e` 패키지가 널리 쓰이지만, 투고하려는 학회나 학술지 템플릿이 따로 정한 환경이 있다면 그 규칙을 따른다.

독자가 코드를 옮겨 적듯 따라올 수 있게 의사코드에는 세 가지 요소를 빠뜨리지 않는다.

- **Input** — 알고리즘이 어떤 데이터와 hyperparameter를 받는지 한 줄에 명시한다.
- **Output** — 계산 끝에 무엇을 어떤 형태로 돌려주는지 한 줄로 밝힌다.
- **단계** — 한 줄에 한 동작씩 깔끔하게 적고, 본문 수식을 불러다 쓰는 줄에는 식 번호를 달아 본문과 연결한다.

의사코드를 실었다면 **계산 복잡도**도 빼놓지 말고 짚어 준다. 입력 크기가 커질 때 계산 비용이 어떻게 늘어나는지 이론적으로 분석할 수 있다면 의사코드 바로 뒤나 본문에서 밝히고, 실제 측정한 실행 시간(runtime)은 이와 구분해 따로 보고한다. 특히 방법이 빠르다고 주장하려면 사용한 하드웨어, 구현 환경, 입력 크기, 측정 방식까지 함께 적어야 설득력이 생긴다. 이론적 복잡도를 따질 수 있는데도 막연히 runtime 숫자만 적어 내면 심사위원은 왜 빠른지, 입력이 커져도 그 속도가 유지되는지 짐작에 기댈 수밖에 없다.

---

## 25.4 Hyperparameter table — 설정값을 한곳에

실제 구현과 재현의 성패는 종종 hyperparameter 한두 개에 달려 있다. **재현에 필요한 hyperparameter는 본문 문장 여기저기에 흩뿌리지 말고 한곳에서 바로 찾을 수 있게 모아야 한다.** "we use learning rate 1e-4 …"가 3.1절에 나오고 "batch size 32 …"가 4.2절 구석에 박혀 있으면, 독자는 어떤 조합으로 결과를 얻었는지 맞추느라 원고를 뒤적여야 한다. 설정값이 많다면 표나 공개 config 파일로 일괄 정리하되, 결과에 큰 영향을 주는 핵심 값만큼은 본문에서도 이유와 함께 설명한다.

Hyperparameter 표를 짤 때는 parameter 이름과 값, 의미에 더해 값을 바꾸었을 때 성능이 어떻게 변하는지(sensitivity)까지 함께 적어 두면 훨씬 유익하다. 그 민감도의 구체적 근거는 자연스럽게 26장의 ablation 표로 이어진다. 만약 **dataset마다 다른 값을 적용했다면** dataset을 행에, parameter를 열에 놓은 표로 정리해 어떤 benchmark에서 어떤 값을 기본값으로 썼는지 한눈에 드러낸다.

---

## 25.5 26장의 Results와 맞추기

§25.1에서 세운 Results 중심 골격이 원고 끝까지 살아남으려면, Method의 서브섹션과 Results의 서브섹션이 일대일로 맞물려 있는지 마지막으로 대조해야 한다. 두 섹션이 짝을 이루면 심사위원도 방법의 각 부품이 실제로 제 몫을 했는지 손쉽게 검증할 수 있다. 반대로 두 섹션이 어긋날 때 흔히 나타나는 불일치는 다음 두 가지다.

- **Method에는 있는데 Results에는 없는 구성 요소** — Method §3.2에서 "we use multi-scale fusion"이라고 한참 설명해 놓고, 정작 Results의 어느 그림이나 표에서도 그 효과를 따져 보지 않은 경우다. 대개 해당 요소의 ablation 실험이 빠져 있다([26장 §26.2](./chapter_26_results_discussion.md)).
- **Results에는 있는데 Method에는 없는 구성 요소** — Results §4의 ablation 표에는 "w/o geometric prior" 행이 버젓이 들어가 있는데, 정작 Method 본문에서는 geometric prior의 정의나 수식을 찾을 수 없는 경우다. 설명이나 기호 정의가 누락된 자리다.

개요를 짜는 단계에서부터 Method의 각 서브섹션 옆에 대응할 Results의 표와 그림을 적어 두면, 이런 어긋남을 실험과 집필이 끝나기 전에 일찍 잡아낼 수 있다. 이렇게 Method의 설계도와 기호, 설정값, 검증 대상이 빈틈없이 맞물려 준비되었다면, 이제 다음 장에서 그 설계가 실제 데이터 위에서 어떤 결과를 내고 무엇을 뜻하는지 Results와 Discussion으로 풀어낼 차례다.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7(control과 method는 논리에 필요한 자리에), rule 9(Method를 읽는 사람이 가장 적다). [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 2.3절 항목 7(Experimental 소제목을 Results 순서에 맞추기), 2.4절(시간순으로 쓰지 말고 중요한 결과부터). [robotics-practice 19장 §19.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#198-연구-실전) — LaTeX 도구 예시.

다음: [26장 결과와 논의](./chapter_26_results_discussion.md)