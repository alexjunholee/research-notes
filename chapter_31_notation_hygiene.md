# Ch.31 — 표기 위생

ch15가 *문장 안에서 수식이 박히는 법*을 다뤘다면, 이 챕터는 *논문 전체에서 표기가 일관되는 법*을 다룬다. 같은 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html)의 27 rules가 출처다. 일관성은 한 문장 안의 문제가 아니라 *논문 전체*의 문제이므로 별도 챕터에 둔다.

reviewer가 같은 기호를 두 번 다른 의미로 받으면 *의도된 차이인지 오타인지* 추측해야 한다. 이 추측이 working memory를 갉아 든다. 표기 위생은 글의 일관성을 만드는 작업이 아니라, 독자의 인지 부담을 낮추는 도구다.

학생들이 가장 자주 빠지는 결함은 raw symbol을 매번 타이핑하는 패턴이다. macro 없이 본문 곳곳에 $\mathbf{R}$을 직접 친 paper에서, 한 곳만 $R$로 깜박해도 reviewer 입장에서 *오타인지 의도인지* 모호해진다. 그래서 표기 위생은 *글쓴이의 꼼꼼함*에 의존하지 않고 *도구로 강제*하는 쪽에 가깝다.

---

## 31.1 Notation table — 한 곳에 한 번

🔴 **Method 도입에 notation table 한 컷.** 본문에 등장하는 모든 기호가 그 표 안에서 한 번 정의되어야 한다 — ch10 §2와 같은 권고. 본문에 흩뿌려진 정의는 reviewer가 *처음 등장한 곳*을 backtrack하게 만든다.

🟡 **표 구성 4 column.**

| Symbol | Meaning | Dimension/Unit | First introduced |
|---|---|---|---|
| $\mathbf{T}_k$ | sensor pose at time $k$ | $SE(3)$ | §3.1 |
| $\mathbf{r}_i$ | reprojection residual for measurement $i$ | $\mathbb{R}^2$ | §3.2 |
| $\lambda$ | regularization weight | scalar | §3.3 |

🟡 **표 위치.** Method 도입의 마지막 paragraph 직전 또는 직후. 수식이 본격적으로 등장하기 전에. 표 자체가 *수식 진입 전*에 reviewer의 working memory를 *준비*시킨다.

🔴 **한 기호의 두 의미 금지.** $R$이 회전·residual·reward로 동시에 쓰이는 paper가 흔하다. ch15 §1 R8과 같은 권고. notation table이 이 점을 *명시적*으로 잡아 두는 도구.

---

## 31.2 LaTeX 매크로 — 강제력 있는 통일

🟡 **모든 반복 기호를 매크로로.** raw symbol을 매번 타이핑하는 대신 매크로 정의 한 줄에 모든 사용을 묶어 둔다. 그러면 한 곳 수정으로 전 논문 적용이 가능해진다.

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

🔴 **매크로 부재의 비용.** 회전을 $\mathbf{R}$에서 $R$로 바꾸고 싶으면 매크로 정의 한 줄만 수정하면 끝나는 한편, raw symbol을 본문에 직접 친 paper는 search-and-replace로도 *모든 곳을 잡았다*고 보장이 안 된다. 한 곳만 깜박한 결함이 그대로 reviewer에게 도달한다.

🟡 **매크로 그룹화.** Lie group, bold vector, 통계, dataset 이름(`\KITTI`, `\TUM`) 등 그룹별로 묶어 두면 본문에서 *어떤 곳에 어떤 매크로*를 쓰는지 잡기 쉬워진다.

---

## 31.3 Dimension 일관성 — 단위와 차원

🔴 **모든 물리량에 단위 표기.** runtime이 ms인지 s인지, drift가 m인지 %인지가 본문·표·figure 모든 곳에서 같아야 한다. 같은 metric의 단위가 표마다 다르면 reviewer가 매번 변환을 시도한다.

🟡 **SI 권고.** 본문 첫 등장 시 명시 — `runtime ($\mathrm{ms}$)`, `drift ($\mathrm{m}$)`. 표·figure 축 라벨에도 단위. 단위가 빠진 figure는 ch12 §2의 desk reject 사유와 같은 결함.

🟡 **차원 명시.** vector 차원($\mathbb{R}^3$), matrix 차원($\mathbb{R}^{m \times n}$)이 처음 등장 시 명시. 본문에서 dimension이 *추측*되어야 하면 그 자체가 결함이다. notation table의 dimension column이 이 부분을 잡아 둔다.

---

## 31.4 Index 일관성 — 변수와 도메인

🔴 **Index 변수의 의미 일관.** 한 논문 안에서 $i$가 한 곳에서 measurement, 다른 곳에서 frame이면 reviewer가 추측해야 한다. $i$가 measurement이면 한 논문 안에서 항상 measurement.

🟡 **권장 default.** 분야별로 차이가 있지만 로보틱스·CV에서 자주 쓰이는 default는 다음과 같다.

- $i$ — measurement / observation
- $j$ — landmark / keypoint / track
- $k$ — time / frame
- $n$ — count (총 개수)

한 논문 안에서 일관되면 default를 따르지 않아도 된다. 다만 default와 *반대로* 쓰면 (예: $k$를 measurement로) reviewer가 분야 관행에 맞춰 추측하다 부담이 누적된다.

🟡 **합의 도메인 명시.** $\sum_{i=1}^N$이면 *N이 무엇의 카운트인가*가 prose에서 한 번. ch15 §3 잔차·loss 정의와 같은 권고. 인덱스 변수만 던져 두면 독자가 *어떤 집합 위에서의 합인지* 추측하게 둔다.

---

## 31.5 분야별 default convention

분야별로 자리잡힌 default가 있다. 그 default를 그대로 쓰면 reviewer 인지 부담이 가장 낮다.

**로보틱스/SLAM**: $\mathbf{T} \in SE(3)$ 변환, $\mathbf{R} \in SO(3)$ 회전, $\boldsymbol{\xi} \in \mathfrak{se}(3)$ Lie algebra, $\mathbf{p}$ point, $\mathbf{x}$ state, $\mathbf{z}$ measurement.

**CV**: $\mathbf{x}$ image coordinate, $\mathbf{X}$ world coordinate, $\mathbf{K}$ intrinsic, $\mathbf{P}$ projection.

**ML/통계**: $\theta$ parameter, $p(\cdot)$ distribution, $\mathcal{L}$ loss, $\mathcal{D}$ dataset.

새로운 표기가 default와 *충돌*하면 — 예를 들어 $\mathbf{T}$를 transform이 아니라 *training set*으로 쓰는 패턴 — reviewer 입장에서 분야 관행에 맞춰 추측한 의미가 본문 의미와 어긋난다. 이 어긋남을 발견할 때마다 working memory가 한 번씩 reset된다. 결국 default와 충돌하지 않는 곳에서만 새 표기를 쓰는 쪽이 마찰이 적다.

---

## 31.6 흔한 실수 5종

🔴 **한 기호 두 의미.** $R$이 회전·residual 동시 사용. 가장 자주 잡히는 결함.

🔴 **Notation table 부재.** 본문에 흩뿌려진 정의. 정의 위치를 backtrack해야 함.

🔴 **단위 누락.** 표·figure 축에 단위가 없음. ch12 §2의 desk reject 결함.

🔴 **Index 변수 재배정.** $i$의 의미가 섹션마다 바뀜.

🟡 **매크로 부재.** raw symbol 매번 타이핑. 한 곳만 어긋난 결함이 살아남음.

---

## 31.7 자기 진단

자기 manuscript에 다음 두 작업을 돌려 본다.

1. **Notation 추출.** 본문에 등장하는 모든 수학 기호를 한 페이지에 추출해 본다. 같은 기호가 두 의미로 쓰이는 곳이 있는가. notation table에 빠진 기호가 있는가.
2. **단위 추출.** 모든 표·figure의 축 라벨과 cell 값을 추출. 단위가 빠진 곳이 있는가. 같은 metric의 단위가 표마다 다른가.

두 작업 모두 *manuscript가 안정된 뒤*에 한 번 돌리는 작업이다. drafting 단계에서 매번 점검하면 작업 흐름이 깨진다. Stage 4 editing 또는 submit 직전에 한다.

ch15가 수식 *문법*을 다뤘다면 ch16은 수식 *위생*을 다뤘다. 두 챕터가 같은 Knuth 출처에서 나오지만, 한쪽은 *문장 안*에서 한쪽은 *논문 전체*에서 작동하므로 분리해 둔다.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1, §4, §5 — 수학 표기 통일 (ch15에서 일부 흡수, ch16에서 위생 layer 격상). notation table 작성·매크로 그룹·dimension/index 일관성 권고·분야 default convention·흔한 실수 5종은 자체.

다음: [Ch.17 — 수정과 rebuttal](./chapter_32_revision_rebuttal.md)