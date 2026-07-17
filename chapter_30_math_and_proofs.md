# Ch.30 — 수식·정리·증명 쓰기

[Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html)은 독자가 수식이 들어간 단락을 어떻게 읽는지 관찰했다. 첫 독서에서는 수식을 훑어 넘기는 독자가 많다. 그래서 §1 point 13은 수식이 빠져도 산문이 흘러야 한다는 'blah' 테스트를 제시한다. 간단한 수식을 제외한 나머지를 'blah'로 바꾸어도 문장이 이어져야 한다는 뜻이다.

학생들이 가장 자주 어기는 곳이 여기다. displayed equation 다섯 줄을 연달아 놓고 between-equation prose는 한 줄도 쓰지 않은 derivation이 흔하다. 그러면 심사위원은 첫 독서에서 그 페이지를 통과하지 못한다. Nilsson이 §34에 적은 "쉽게 쓴 글일수록 읽기 어렵다"가 같은 문제를 가리킨다. 수식 사이의 산문은 공들여 다듬을수록 읽기 쉬워진다.

---

## 30.1 수식이 문장에 들어가는 법

**R1. 인접한 수식 사이에는 단어를 넣는다 (point 1).** 두 수식이 쉼표만으로 이어지면 어디서 한 수식이 끝나고 다음이 시작하는지 즉시 안 잡힌다.

> ❌ Consider $S_q$, $q < p$.
>
> ✓ Consider $S_q$, where $q < p$.

**R2. 문장은 수식으로 시작하지 않는다 (point 2).**

> ❌ $X$ denotes the rotation matrix.
>
> ✓ Let $X$ denote the rotation matrix.

문장 첫 자리에는 산문 단어를 둔다. ch14의 topic position 원칙과 같다.

**R3. 산문 안에 ∴ ⇒ ∀ ∃ 금지(point 3).** 논리 기호는 수식 안에서만 쓴다. 본문 문장 안에 `∴`를 끼워 넣으면 심사위원이 두 번 해석해야 한다.

**R4. Displayed equation은 둘러싼 문장의 일부다(points 10, 23).** 수식 앞에는 불필요한 colon을 두지 않는다. equation 끝의 마침표·쉼표도 문장 부호에 맞게 쓴다.

> displayed equation의 끝이 문장의 끝이면 수식 뒤에 마침표.
> displayed equation 다음에 산문이 이어지면 수식 뒤에 쉼표 또는 무부호.

**R5. 인용 형식(point 19).** "Equation (5)", "Theorem 2", "Lemma 3.1". 번호가 붙으면 첫 글자 대문자.

**R6. 정의는 서로 다른 두 방식으로 쓴다(point 11).** 수식과 산문을 함께 쓴다. "Let $\mathbf{T} \in SE(3)$ denote the rigid-body transform from sensor frame to world frame."에서는 수식과 산문이 같은 정의를 서로 다른 방식으로 제시한다.

**R7. 중요한 수식을 displayed로 두고, 멀리서 참조할 중요한 수식에는 번호를 붙인다(point 16).** 모든 수식에 번호를 붙이면 중요도의 위계가 흐려진다. 번호가 필요한 수식을 원고 전체에서 일관되게 고른다.

**R8. 같은 기호를 두 의미로 쓰지 않는다(point 14).** 로보틱스에서 흔한 충돌이다. $R$이 회전행렬·residual·reward로 동시에 쓰이는 문서가 있다. 한 문서 안에서는 한 의미로만 쓴다. [ch31](./chapter_31_notation_hygiene.md)의 매크로 위생과 직결된다.

**R9. "that"을 빼지 마라(point 8).**

> ❌ We show $X$ converges.
>
> ✓ We show that $X$ converges.

영어 논문에서 "that"을 생략하면 해석이 어려워질 때가 있다.

**R10. "we"를 쓰고 "I"는 피한다(point 6).** 여기서 `we`는 저자와 독자가 함께 논의를 따라간다는 뜻일 때 쓴다. 저자의 인격이 논점과 무관한 기술 글에서는 `I`를 피하라는 권고다. 한국 영어 교육에서 강조해 온 수동태 우선 관행과 충돌하지만, ch01에서 다룬 지도교수의 스타일을 따른다는 원칙과 같은 결정축에 있다.

---

## 30.2 Theorem·Lemma·Proof — 자기완결과 signposting

**Theorem statement는 자기완결적이다.** Knuth point 5의 핵심이다. 정리 안의 모든 기호가 정리문 안에서 정의되거나 명시 참조되어야 한다. 앞 단락을 다시 읽어야 statement가 이해되면 self-contained가 아니다.

> ❌ **Theorem 1.** Under the conditions above, the estimator converges.
>
> ✓ **Theorem 1.** Let $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$, where $\mathbf{x}_0\in\mathbb{R}^n$, $\mathbf{A}\in\mathbb{R}^{n\times n}$, and $\lVert\mathbf{A}\rVert_2<1$. Then $\lVert\mathbf{x}_k\rVert_2\leq\lVert\mathbf{A}\rVert_2^k\lVert\mathbf{x}_0\rVert_2$, and hence $\mathbf{x}_k\to\mathbf{0}$ as $k\to\infty$.

**Motivate before stating.** 정리 진술 직전에 왜 이 정리가 필요한지 짧게 짚는다. 구체적인 문장 수보다 독자가 이 결과의 역할을 알 수 있게 하는 것이 중요하다.

**Lemma·Theorem·Corollary는 위계가 다르다.** Lemma는 디딤돌이고, Theorem은 본 주장이며, Corollary는 직접 귀결이다. 한국 학생이 디딤돌도 Theorem으로 표시하는 일이 흔하다. 그러면 위계가 무너져 심사위원이 실제 main result를 찾기 어렵다.

**증명 안의 signpost.** "We divide the proof into two parts." "The lemma is half proved." 증명이 길거나 논리 단계가 여러 개면 signpost를 둔다. 반 페이지는 편집 휴리스틱일 뿐 필수 기준이 아니다.

**Direct proof가 가능하면 contradiction부터 쓰지 않는다.** Knuth의 권고다. proof by contradiction은 독자에게 부정 명제를 작업 기억에 들고 있을 부담을 지운다. direct proof가 가능한 곳에서는 direct를 우선한다.

**증명 마침 표시(∎).** venue·class·template가 쓰는 규약을 따른다. LaTeX의 proof 환경이 자동으로 표시하는 경우 따로 중복하지 않는다.

---

## 30.3 로보틱스·CV 특화 패턴

**SE(3)·Lie group 표기.** $\mathbf{T} \in SE(3)$, $\boldsymbol{\xi} \in \mathfrak{se}(3)$. 한 논문 안에서 case·bold·hat을 통일한다. 회전행렬을 한 곳에서 $\mathbf{R}$, 다른 곳에서 $R$로 쓰면 심사위원이 다른 양인지 추측해야 한다. [ch31](./chapter_31_notation_hygiene.md)에서 매크로로 통일한다.

**Optimization 수식 패턴.**

$$\mathbf{x}^\star = \arg\min_{\mathbf{x}} f(\mathbf{x}) \quad \text{s.t.} \quad g(\mathbf{x}) = 0$$

`\text{s.t.}`인지 `\text{subject to}`인지 한 문서 안에서 통일한다. 처음 등장할 때 산문으로 한 번 풀어 쓴다.

**Probabilistic 수식.** $p(\mathbf{x} \mid \mathbf{z})$의 `\mid`와 `|`를 섞지 않는다. Bayes filter 단계마다 prior, likelihood, posterior가 무엇을 가리키는지 산문에서 명시한다. R6의 이중 표현이 적용된다.

**잔차·loss 정의.** $\mathbf{r}_i = \mathbf{z}_i - h(\mathbf{x})$ 같은 잔차 정의에서는 인덱스 $i$가 무엇을 순회하는지 산문에서 항상 밝힌다. "for each measurement $i \in \{1, \ldots, N\}$." 인덱스 변수만 두면 독자가 어떤 집합 위에서의 합인지 추측해야 한다.

**수식 줄바꿈에서 등호의 위치.** Inline에서는 등호 뒤에서 끊고, displayed에서는 등호 앞에서 끊는다. Knuth가 §1에 박은 typographic convention이다.

---

## 30.4 진단 — 자기 derivation의 'blah' 통과

자기 글의 derivation 한 페이지를 골라 모든 수식을 'blah'로 바꾸어 본다. 그 페이지가 산문으로서 흘러야 한다. 흐름이 끊기는 곳이 between-equation prose가 비어 있는 자리다.

Knuth는 §2-§3에서 같은 정리의 atrocious proof와 polished proof를 나란히 놓고 줄별로 비교한다. 발췌와 분석은 [`knuth_proof_rewrite.md`](./excerpts/excerpt_04_knuth_proof_rewrite.md)에 있다.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) — Mathematical Writing §1의 27 points에서 추린 10개(points 1, 2, 3, 5, 6, 8, 10, 11, 13, 14, 16, 19, 23을 주제별로 묶음). atrocious-vs-polished proof는 §2-§3. Halmos box와 Nilsson 강연도 같은 문서에 실려 있다. 로보틱스·CV의 네 패턴(SE(3), optimization, probabilistic, 잔차·loss)은 이 장에서 정리했다.

다음: [Ch.16 — 표기 위생](./chapter_31_notation_hygiene.md)
