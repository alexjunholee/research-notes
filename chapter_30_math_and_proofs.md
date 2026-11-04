# Ch.30 — 수식·정리·증명 쓰기

[Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 point 13은 "처음 읽을 때 수식을 훑고 넘어가는 독자가 많다"고 적고, 그러니 간단한 수식만 남기고 나머지를 모두 "blah" 같은 소리로 바꾸어도 문장이 매끄럽게 읽혀야 한다고 했다. 이 장에서는 이것을 'blah' 테스트라고 부른다.

수식 다섯 줄을 연달아 늘어놓고 그 사이에 설명을 한 줄도 쓰지 않은 유도 과정은 이 원칙을 어긴다. 처음 읽는 심사위원은 그 페이지에서 막히기 쉽다. Knuth는 point 10에서 숙제 답안처럼 수식만 나열하지 말고 설명으로 개념을 이어 가라고 했다.

---

## 30.1 수식을 문장에 넣는 법

**R1. 이웃한 수식 사이에는 단어를 넣는다(point 1).** 두 수식을 쉼표로만 이으면 한 수식이 어디서 끝나고 다음 수식이 어디서 시작하는지 바로 알아보기 어렵다.

> ❌ Consider $S_q$, $q < p$.
>
> ✓ Consider $S_q$, where $q < p$.

**R2. 문장을 기호로 시작하지 않는다(point 2).**

> ❌ $X$ denotes the rotation matrix.
>
> ✓ Let $X$ denote the rotation matrix.

문장 첫머리에는 단어를 둔다. Ch.29의 topic position 원칙과도 맞는다.

**R3. 본문 문장에 ∴, ⇒, ∀, ∃를 쓰지 않는다(point 3).** Knuth는 이런 기호를 해당하는 단어로 바꾸라고 했다. 논리학 글은 예외다. 본문 문장에 `∴`가 끼어 있으면 심사위원은 기호를 다시 말로 풀어 읽어야 한다.

**R4. displayed equation은 앞뒤 문장의 일부다(points 4, 23).** 정리 바로 앞 문장은 완결된 문장이거나 쌍점으로 끝나야 한다(point 4). 문장 중간에 수식을 따로 세울 때는 그 앞에 쌍점을 습관처럼 찍지 않는다. Knuth는 point 23에서 그런 쌍점을 틀렸다고 했다. 수식 뒤의 문장부호도 문장에 맞춘다.

> displayed equation에서 문장이 끝나면 수식 뒤에 마침표를 찍는다.
> displayed equation 뒤로 문장이 이어지면 쉼표를 찍거나 아무것도 찍지 않는다.

**R5. 번호 붙은 이름은 대문자로 시작한다(point 19).** "Equation (5)", "Theorem 2", "Lemma 3.1"처럼 쓴다.

**R6. 정의는 서로 보완하는 두 방식으로 쓴다(point 11).** Knuth는 특히 정의를 내릴 때 같은 것을 두 번, 서로 다른 방식으로 말해 보라고 했다. 변수는 처음 나올 때 최소한 비공식적으로라도 정의해야 한다. "Let $\mathbf{T} \in SE(3)$ denote the rigid-body transform from sensor frame to world frame."에서는 수식과 말이 같은 정의를 두 방식으로 전한다.

**R7. 중요한 수식은 따로 한 줄에 세우고 번호를 붙인다(point 16).** Knuth는 중요한 수식을 따로 세우고, 멀리서 참조할 수식이 있다면 가장 중요한 수식 모두에 번호를 붙이라고 했다. 실제로 참조하지 않는 수식이라도 그렇다. 다른 대목에서는 모든 displayed equation에 번호를 붙이는 것은 대개 좋지 않다고도 했다.

**R8. 한 기호를 두 가지 뜻으로 쓰지 않는다(point 14).** $R$을 회전행렬로도, residual로도, reward로도 쓰는 원고가 있다. 한 문서에서는 한 기호를 한 뜻으로만 쓴다. 매크로로 표기를 관리하는 법은 [Ch.31](./chapter_31_notation_hygiene.md)에서 다룬다.

**R9. "that"을 빼지 않는다(point 8).**

> ❌ We show $X$ converges.
>
> ✓ We show that $X$ converges.

Knuth는 독자가 문장 구조를 파악하는 데 도움이 될 때 "that"을 빼지 말라고 했다.

**R10. "we"를 쓰고 "I"는 피한다(point 6).** Knuth는 수동태를 피하는 데 "we"가 쓸모 있을 때가 많다고 했다. 다만 이 "we"는 "당신과 나 함께"라는 뜻일 때 쓰고, "I"를 격식 있게 바꾼 말로 쓰지는 말라고 하며, 저자와 독자의 대화로 생각하라고 했다. 대부분의 기술 글에서는 저자 개인이 논점과 관련 있는 경우가 아니면 "I"를 피해야 한다고 했다.

---

## 30.2 정리와 증명

**정리는 그 자체로 읽혀야 한다.** Knuth는 point 5에서 정리문은 대개 앞 본문의 가정에 기대지 않고 그 자체로 완결되어야 한다고 했다. 정리에 쓰인 기호는 정리문 안에서 정의하거나 어디서 정의했는지 밝힌다. 앞 단락을 다시 읽어야 정리문을 이해할 수 있다면 완결된 정리문이 아니다.

> ❌ **Theorem 1.** Under the conditions above, the estimator converges.
>
> ✓ **Theorem 1.** Let $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$, where $\mathbf{x}_0\in\mathbb{R}^n$, $\mathbf{A}\in\mathbb{R}^{n\times n}$, and $\lVert\mathbf{A}\rVert_2<1$. Then $\lVert\mathbf{x}_k\rVert_2\leq\lVert\mathbf{A}\rVert_2^k\lVert\mathbf{x}_0\rVert_2$, and hence $\mathbf{x}_k\to\mathbf{0}$ as $k\to\infty$.

**정리를 내놓기 전에 왜 필요한지 밝힌다.** Knuth는 point 4와 12에서 정리 앞 문장을 앞의 논의와 이어 주는 동기 설명으로 쓰고, 독자가 뒤에 올 내용을 기다리게 하라고 했다. 몇 문장을 쓰느냐보다 독자가 이 결과가 어떤 역할을 하는지 알게 하는 것이 중요하다.

**Lemma, Theorem, Corollary는 급이 다르다.** Lemma는 주장을 세우는 데 쓰는 중간 결과다. Theorem은 논문의 핵심 결과다. Corollary는 Theorem에서 바로 따라 나오는 결과다. 중간 결과까지 모두 Theorem으로 표시하면 급이 뒤섞여 심사위원이 진짜 주요 결과를 찾기 어렵다.

**증명 안에 길잡이 문장을 둔다.** Knuth는 학생 답안 가운데 읽기 쉬웠던 증명이 "The lemma is half proved.", "We divide the proof into two parts, first proving ⟨blah⟩ and then proving ⟨grunt⟩." 같은 문장을 담고 있었다고 소개했다. 증명이 길거나 논리 단계가 여럿이면 이런 길잡이 문장을 둔다. 반 페이지 정도를 기준으로 삼을 수 있지만 어림값일 뿐이다.

**직접 증명할 수 있으면 직접 증명한다.** Knuth는 §3에서 연습 문제의 증명이 쓸데없이 귀류법을 썼다고 지적하고 직접 증명으로 다시 썼다. 귀류법을 쓰면 독자는 증명이 끝날 때까지 부정한 명제를 머릿속에 들고 있어야 한다.

**증명 끝 표시(∎)는 학회와 문서 클래스, 템플릿의 규약을 따른다.** LaTeX의 proof 환경이 표시를 자동으로 넣는다면 그 표시만 쓴다.

---

## 30.3 로보틱스·CV에서 자주 쓰는 수식

**SE(3)와 Lie group 표기.** $\mathbf{T} \in SE(3)$, $\boldsymbol{\xi} \in \mathfrak{se}(3)$처럼 쓴다. 한 논문 안에서 대소문자, 굵은 글씨, hat 표기를 통일한다. 회전행렬을 한 곳에서는 $\mathbf{R}$로, 다른 곳에서는 $R$로 쓰면 심사위원은 둘이 다른 양인지 따져 봐야 한다. [Ch.31](./chapter_31_notation_hygiene.md)에서 매크로로 통일하는 법을 다룬다.

**최적화 문제.**

$$\mathbf{x}^\star = \arg\min_{\mathbf{x}} f(\mathbf{x}) \quad \text{s.t.} \quad g(\mathbf{x}) = 0$$

`\text{s.t.}`와 `\text{subject to}` 가운데 하나를 골라 문서 전체에 쓴다. 처음 나올 때는 수식이 무엇을 뜻하는지 말로 한 번 풀어 쓴다.

**확률 수식.** $p(\mathbf{x} \mid \mathbf{z})$에서 `\mid`와 `|` 가운데 하나로 통일한다. Bayes filter의 단계마다 prior, likelihood, posterior가 무엇인지 말로 밝힌다. R6에서 말한 두 방식 정의가 여기에도 들어맞는다.

**잔차와 loss 정의.** $\mathbf{r}_i = \mathbf{z}_i - h(\mathbf{x})$ 같은 잔차를 정의할 때는 인덱스 $i$가 무엇을 도는지 말로 밝힌다. 예를 들어 "for each measurement $i \in \{1, \ldots, N\}$"처럼 쓴다. 인덱스만 적어 두면 독자는 무엇을 더하는지 짐작해야 한다.

**수식을 줄바꿈할 때 등호의 위치.** 문장 안의 수식은 등호 뒤에서 줄을 바꾸고, 따로 세운 수식은 등호 앞에서 줄을 바꾼다. Knuth가 §8에서 소개한 조판 관례다.

---

## 30.4 자기 유도 과정에 'blah' 테스트 해 보기

자기 원고에서 유도 과정이 담긴 페이지 하나를 골라, 간단한 수식만 남기고 나머지를 'blah'로 바꾸어 본다. 그래도 문장이 이어져야 한다. 흐름이 끊기는 곳이 수식 사이에 설명이 빠진 자리다.

Knuth는 §2에서 문체가 엉망인(atrocious) 학생 증명을 내놓고, §3에서 이를 다듬은 답안을 보여 준다. 발췌와 분석은 [`knuth_proof_rewrite.md`](./excerpts/excerpt_04_knuth_proof_rewrite.md)에 있다.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) — §1의 27개 항목 가운데 points 1, 2, 3, 4, 5, 6, 8, 10, 11, 12, 13, 14, 16, 19, 23을 주제별로 묶었다. 학생 증명과 다듬은 답안은 §2–§3, 증명의 길잡이 문장은 §5, 등호와 줄바꿈은 §8. 로보틱스·CV 수식 패턴은 이 장에서 정리했다.

다음: [Ch.31 — 표기 위생](./chapter_31_notation_hygiene.md)
