# Ch.31 — 표기 위생

[Ch.30 — 수식·정리·증명](./chapter_30_math_and_proofs.md)이 문장 안에 수식을 넣는 법을 다뤘다면, 여기서는 논문 전체의 표기를 일관되게 유지하는 법을 다룬다. 두 논의 모두 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1의 27 points에서 출발한다.

심사위원이 같은 기호를 서로 다른 의미로 만나면 의도한 차이인지 오타인지 추측해야 한다. 이 추측이 작업 기억을 갉아먹는다. 표기 위생은 독자의 인지 부담을 낮춘다.

학생들이 가장 자주 빠지는 결함은 raw symbol을 매번 타이핑하는 패턴이다. macro 없이 본문 곳곳에 $\mathbf{R}$을 직접 입력하면, 한 곳만 $R$로 적어도 심사위원은 오타인지 의도인지 알기 어렵다. 표기 위생은 도구로 강제하는 편이 낫다.

---

## 31.1 Notation table — 한 곳에 한 번

**표기가 많다면 Method 도입에 notation table을 둔다.** 핵심 기호를 표와 본문 첫 등장 중 적절한 곳에서 정의한다. 기호가 몇 개뿐이라면 별도 표 없이 산문 정의로 충분하다. [Ch.25 §25.2](./chapter_25_method.md)와 같은 권고다.

**표는 다음 네 열에서 필요한 것을 고른다.** `First introduced`가 지면만 차지한다면 뺄 수 있다.

| Symbol | Meaning | Dimension/Unit | First introduced |
|---|---|---|---|
| $\mathbf{T}_k$ | sensor pose at time $k$ | $SE(3)$ | §3.1 |
| $\mathbf{r}_i$ | reprojection residual for measurement $i$ | $\mathbb{R}^2$ | §3.2 |
| $\lambda$ | regularization weight | scalar | §3.3 |

**표 위치.** 독자가 기호를 처음 많이 만나는 대목보다 앞에 둔다. 반드시 Method 도입의 마지막 단락일 필요는 없다.

**한 기호에 두 의미를 두지 않는다.** $R$이 회전·residual·reward로 동시에 쓰이는 논문이 흔하다. [Ch.30 R8](./chapter_30_math_and_proofs.md)과 같은 권고다. notation table로 이 문제를 명시적으로 확인할 수 있다.

---

## 31.2 LaTeX 매크로 — 강제력 있는 통일

**반복되고 바뀔 가능성이 있는 표기를 매크로로 정의한다.** raw symbol을 매번 타이핑하는 대신 매크로 정의 한 줄에 사용을 묶으면 한 곳을 수정해 논문 전체에 적용할 수 있다. 단발성 기호까지 모두 매크로로 만들면 오히려 원본을 읽기 어려워질 수 있다.

```latex
% 회전·변환 (Lie group)
\newcommand{\R}{\mathbf{R}}
\newcommand{\T}{\mathbf{T}}
\newcommand{\SE}[1]{SE(#1)}
\newcommand{\so}[1]{\mathfrak{so}(#1)}

% Bold vector
\newcommand{\xb}{\mathbf{x}}
\newcommand{\yb}{\mathbf{y}}
\newcommand{\zb}{\mathbf{z}}

% 통계
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
```

**매크로 부재의 비용.** 회전을 $\mathbf{R}$에서 $R$로 바꾸고 싶으면 매크로 정의 한 줄만 수정하면 끝나는 한편, raw symbol을 본문에 직접 친 논문은 search-and-replace로도 모든 곳을 잡았다고 보장이 안 된다. 한 곳만 깜박한 결함이 그대로 심사위원에게 도달한다.

**매크로 그룹화.** Lie group, bold vector, 통계, dataset 이름(`\KITTI`, `\TUM`) 등 그룹별로 묶어 두면 본문에서 어떤 곳에 어떤 매크로를 쓰는지 잡기 쉬워진다.

---

## 31.3 Dimension 일관성 — 단위와 차원

**모든 물리량에 단위 표기.** runtime이 ms인지 s인지, drift가 m인지 %인지가 본문·표·그림 모든 곳에서 같아야 한다. 같은 metric의 단위가 표마다 다르면 심사위원이 매번 변환을 시도한다.

**단위 권고.** 본문 첫 등장 시 `runtime ($\mathrm{ms}$)`, `drift ($\mathrm{m}$)`처럼 밝히고 표·그림 축에도 적는다. 분야·venue가 SI 사용을 요구하는지 확인한다. 단위가 빠지면 수치를 해석할 수 없다.

**차원 명시.** vector 차원($\mathbb{R}^3$), matrix 차원($\mathbb{R}^{m \times n}$)이 처음 등장 시 명시. 본문에서 dimension이 추측되어야 하면 그 자체가 결함이다. notation table의 dimension column이 이 부분을 잡아 둔다.

---

## 31.4 Index 일관성 — 변수와 도메인

**Index 변수의 의미 일관.** 한 논문 안에서 $i$가 한 곳에서는 measurement, 다른 곳에서는 camera view를 가리키면 심사위원이 추측해야 한다. $i$를 measurement index로 정했다면 논문 전체에서 그 뜻을 유지한다.

**관습의 예.** 분야와 논문마다 다르지만 로보틱스·CV에서 다음과 같은 선택을 볼 수 있다.

- $i$ — measurement / observation
- $j$ — landmark / keypoint / track
- $k$ — time / frame
- $n$ — count (총 개수)

한 논문 안에서 일관되면 이 예를 따르지 않아도 된다. 기호의 뜻을 첫 등장에 명시하고 domain을 함께 적는 것이 관습보다 우선한다.

**합의 도메인을 명시한다.** $\sum_{i=1}^N$이면 N이 무엇의 개수인지 산문에서 한 번 밝힌다. ch15 §3의 잔차·loss 정의와 같은 권고다. 인덱스 변수만 두면 독자가 어떤 집합 위에서의 합인지 추측해야 한다.

---

## 31.5 분야별 기본 관례

분야별로 널리 쓰이는 표기 관습이 있다. 아래는 자주 보이는 예이지 표준의 완전한 목록이 아니다.

**로보틱스/SLAM**: $\mathbf{T} \in SE(3)$ 변환, $\mathbf{R} \in SO(3)$ 회전, $\boldsymbol{\xi} \in \mathfrak{se}(3)$ Lie algebra, $\mathbf{p}$ point, $\mathbf{x}$ state, $\mathbf{z}$ measurement.

**CV**: $\mathbf{x}$ image coordinate, $\mathbf{X}$ world coordinate, $\mathbf{K}$ intrinsic, $\mathbf{P}$ projection.

**ML/통계**: $\theta$ parameter, $p(\cdot)$ distribution, $\mathcal{L}$ loss, $\mathcal{D}$ dataset.

새로운 표기가 기본과 충돌하면 — 예를 들어 $\mathbf{T}$를 transform이 아니라 training set으로 쓰면 — 심사위원이 분야 관행에 따라 추측한 의미와 본문 의미가 어긋난다. 이 어긋남을 발견할 때마다 작업 기억을 다시 정리해야 한다. 기본과 충돌하지 않는 곳에서만 새 표기를 쓰는 편이 마찰이 적다.

---

## 31.6 흔한 실수 5종

**한 기호 두 의미.** $R$이 회전·residual 동시 사용. 가장 자주 잡히는 결함.

**정의의 위치가 불명확함.** 표기가 많은데 notation table이나 첫 등장 정의가 없어 backtrack해야 함.

**단위 누락.** 표·그림 축에 단위가 없어 수치를 해석할 수 없음.

**Index 변수 재배정.** $i$의 의미가 섹션마다 바뀜.

**매크로 부재.** raw symbol 매번 타이핑. 한 곳만 어긋난 결함이 살아남음.

---

## 31.7 자기 진단

자기 원고에서 다음 두 가지를 점검한다.

1. **Notation 추출.** 본문에 등장하는 모든 수학 기호를 한 페이지에 추출해 본다. 같은 기호가 두 의미로 쓰이는 곳이 있는가. notation table에 빠진 기호가 있는가.
2. **단위 추출.** 모든 표·그림의 축 라벨과 셀 값을 추출한다. 단위가 빠진 곳이 있는가. 같은 metric의 단위가 표마다 다른가.

두 작업의 전체 sweep은 원고가 안정된 뒤에 수행한다. 초고 중에는 notation 목록을 함께 갱신하고, 마지막 교정에서 누락과 충돌을 다시 확인한다.

수식 문법은 문장 안에서 작동하고, 수식 위생은 논문 전체에서 작동한다. 둘은 같은 Knuth의 원칙에서 나왔지만 적용하는 층위가 다르다.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 point 11(변수 정의)·point 14(같은 대상에 일관된 표기) — notation table, 매크로, dimension/index 점검으로 확장했다. 분야별 표기 예는 강제 표준이 아니라 첫 선택을 돕는 관습 목록이다.

다음: [Ch.17 — 수정과 rebuttal](./chapter_32_revision_rebuttal.md)
