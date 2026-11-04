# Ch.31 — 표기 위생

[Ch.30](./chapter_30_math_and_proofs.md)에서는 문장 안에 수식을 넣는 법을 다뤘다. 이 장에서는 논문 전체에서 표기를 일관되게 지키는 법을 다룬다. 두 장 모두 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1의 27개 항목에서 출발한다.

같은 기호가 다른 뜻으로 쓰이면 심사위원은 일부러 그렇게 쓴 것인지 오타인지 따져 봐야 한다. 그만큼 내용을 따라갈 힘이 줄어든다. 표기를 깔끔하게 관리하면 독자의 부담이 준다.

기호를 쓸 때마다 직접 입력하다 실수가 생기기도 한다. 매크로 없이 본문 곳곳에 $\mathbf{R}$을 직접 입력하다 보면 한 곳만 $R$로 적기 쉽다. 그러면 심사위원은 그것이 오타인지 의도인지 알 수 없다. 표기는 도구로 묶어 관리하는 편이 낫다.

---

## 31.1 Notation table: 기호를 한곳에 모은 표

**기호가 많다면 Method 앞부분에 notation table을 둔다.** [Ch.25 §25.2](./chapter_25_method.md)와 같은 권고이고, 표의 예시도 그 절에 있다. 예시의 네 열 가운데 필요한 것만 고른다.

**표 위치.** Method 앞부분이 아니어도, 독자가 기호를 처음 여럿 만나는 대목보다 앞이면 된다.

**한 기호에는 한 뜻만 준다.** $R$을 회전, residual, reward에 한꺼번에 쓰는 논문이 있다. [Ch.30 R8](./chapter_30_math_and_proofs.md)에서도 같은 것을 권했다. notation table을 만들면 이런 겹침이 눈에 띈다.

---

## 31.2 LaTeX 매크로로 표기 묶기

**자주 쓰고 나중에 바뀔 수 있는 표기를 매크로로 정의한다.** 기호를 매번 직접 입력하지 않고 매크로 한 줄로 정의해 두면, 그 한 줄만 고쳐 논문 전체에 반영할 수 있다. 한 번만 쓰는 기호까지 매크로로 바꾸면 TeX 원본이 오히려 읽기 어려워진다.

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

**매크로가 없으면 고치기 어렵다.** 회전 표기를 $\mathbf{R}$에서 $R$로 바꾸려면 매크로 정의 한 줄만 고치면 된다. 기호를 본문에 직접 입력한 논문은 찾아 바꾸기로 모든 곳을 고쳤는지 확신하기 어렵다. 한 곳을 놓치면 그대로 심사위원 눈에 띈다.

**매크로를 종류별로 묶는다.** Lie group, 굵은 vector, 통계, dataset 이름(`\KITTI`, `\TUM`)처럼 종류별로 묶어 두면 어떤 매크로가 있는지 찾기 쉽다.

---

## 31.3 단위와 차원

**모든 물리량에 단위를 적는다.** runtime이 ms인지 s인지, drift가 m인지 %인지가 본문과 표, 그림에서 모두 같아야 한다. 같은 metric의 단위가 표마다 다르면 심사위원은 표를 볼 때마다 단위를 환산해야 한다.

**단위를 적는 법.** 본문에서 처음 나올 때 `runtime ($\mathrm{ms}$)`, `drift ($\mathrm{m}$)`처럼 밝히고, 표와 그림의 축에도 적는다. 분야나 학회가 SI 단위를 요구하는지도 확인한다.

**차원을 밝힌다.** vector의 차원($\mathbb{R}^3$)과 matrix의 차원($\mathbb{R}^{m \times n}$)을 처음 나올 때 적는다. 독자가 본문에서 차원을 짐작해야 한다면 고쳐야 할 곳이다. notation table에 차원 열을 두면 빠뜨리지 않는다.

---

## 31.4 인덱스와 그 범위

**인덱스 변수는 한 뜻으로 쓴다.** 한 논문에서 $i$가 어떤 곳에서는 measurement를, 다른 곳에서는 camera view를 가리키면 심사위원은 어느 쪽인지 따져 봐야 한다. $i$를 measurement 인덱스로 정했다면 논문 끝까지 그 뜻으로 쓴다. Knuth도 point 14에서 특별한 이유가 없다면 같은 것을 가리키는 인덱스를 곳마다 바꾸지 말라고 했다.

**관례의 예.** 분야와 논문마다 다르지만 로보틱스와 CV에서는 흔히 이렇게 쓴다.

- $i$ — measurement / observation
- $j$ — landmark / keypoint / track
- $k$ — time / frame
- $n$ — count (총 개수)

한 논문 안에서 일관되기만 하면 이 예를 따르지 않아도 된다. 관례를 따르는 것보다 기호가 처음 나올 때 뜻과 범위를 함께 적는 것이 먼저다.

**합의 범위를 밝힌다.** $\sum_{i=1}^N$이라고 썼다면 $N$이 무엇의 개수인지 본문에서 한 번 밝힌다. Ch.30 §30.3의 잔차·loss 정의에서도 같은 것을 권했다.

---

## 31.5 분야별 기본 관례

분야마다 널리 쓰는 표기가 있다. 아래는 자주 보이는 예일 뿐 표준을 모두 모은 목록은 아니다.

**로보틱스/SLAM**: $\mathbf{T} \in SE(3)$ 변환, $\mathbf{R} \in SO(3)$ 회전, $\boldsymbol{\xi} \in \mathfrak{se}(3)$ Lie algebra, $\mathbf{p}$ point, $\mathbf{x}$ state, $\mathbf{z}$ measurement.

**CV**: $\mathbf{x}$ image coordinate, $\mathbf{X}$ world coordinate, $\mathbf{K}$ intrinsic, $\mathbf{P}$ projection.

**ML/통계**: $\theta$ parameter, $p(\cdot)$ distribution, $\mathcal{L}$ loss, $\mathcal{D}$ dataset.

새 표기가 관례와 부딪치면 독자가 헷갈린다. 예를 들어 $\mathbf{T}$로 training set을 가리키면, $\mathbf{T}$를 좌표 변환으로 읽어 온 심사위원은 볼 때마다 뜻을 바꿔 읽어야 한다. 새 기호는 널리 쓰는 관례와 겹치지 않게 고른다.

---

## 31.6 자기 진단

자기 원고에서 다음을 점검한다.

1. **기호 뽑아 보기.** 본문에 나오는 수학 기호를 모두 한 페이지에 뽑아 본다. 같은 기호를 두 뜻으로 쓴 곳이 있는지, notation table에 빠진 기호가 있는지 본다.
2. **단위 뽑아 보기.** 모든 표의 셀 값과 그림의 축 라벨을 뽑는다. 단위가 빠진 곳이 있는지, 같은 metric의 단위가 표마다 다른지 본다.

원고 전체를 훑는 점검은 원고가 어느 정도 굳은 뒤에 한다. 초고를 쓰는 동안에는 기호 목록을 함께 고쳐 나가고, 마지막 교정에서 빠진 것과 겹치는 것을 다시 확인한다.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 point 11(변수는 처음 나올 때 정의한다), point 14(한 표기를 두 대상에 쓰지 않고, 같은 대상에는 같은 표기를 쓴다). notation table, 매크로, 단위·차원·인덱스 점검은 이 장에서 이 두 항목을 넓혀 정리했다. 분야별 표기는 관례의 예일 뿐 지켜야 할 규정은 아니다.

다음: [Ch.32 — 개정과 답변서](./chapter_32_revision_rebuttal.md)
