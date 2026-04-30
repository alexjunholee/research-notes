# Ch.30 — 수식·정리·증명 쓰기

수식이 들어간 문단을 reviewer가 어떻게 읽는지에 대한 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html)의 관찰 — 이 장의 출발점이다. 첫 독서에서 독자는 수식을 *건너뛴다*. 두 번째 독서에서야 수식을 들여다본다. 그래서 수식이 빠져도 산문이 흘러야 한다는 'blah' 테스트가 §1 rule 16에 박혀 있다. 모든 수식을 단어 'blah'로 치환해도 문장이 이어져야 한다는 입장이다.

학생들이 가장 자주 어기는 곳이 여기다. displayed equation 다섯 줄을 줄줄 던지고 between-equation prose가 0줄인 derivation이 흔하다. 그러면 reviewer가 첫 독서에서 그 페이지를 통과하지 못한다. Nilsson이 §34에 적은 "쉽게 쓴 글일수록 읽기 어렵다"가 같은 문제를 가리킨다. 결국 수식 prose는 가장 어렵게 다듬어야 가장 쉬워진다.

---

## 30.1 수식이 문장에 박히는 법 — Knuth 10원칙

**R1. 인접한 수식 사이에는 단어를 넣는다 (rule 1).** 두 수식이 쉼표만으로 이어지면 어디서 한 수식이 끝나고 다음이 시작하는지 즉시 안 잡힌다.

> ❌ Consider $S_q$, $q < p$.
>
> ✓ Consider $S_q$, where $q < p$.

**R2. 문장은 수식으로 시작하지 않는다 (rule 2).**

> ❌ $X$ denotes the rotation matrix.
>
> ✓ Let $X$ denote the rotation matrix.

문장 첫 자리는 산문 단어가 받는다. ch14의 topic position 원칙과 같다.

**R3. 산문 안에 ∴ ⇒ ∀ ∃ 금지 (rule 3).** 논리 기호는 수식 *안*에서만 산다. 그래서 본문 문장 안에 `∴`를 끼워 넣으면 reviewer가 두 번 parsing해야 한다.

**R4. Displayed equation은 둘러싼 문장의 일부 (rule 6).** displayed 다음에 stray colon 금지. equation 끝의 마침표·쉼표는 *문장 부호*로서 정확하게.

> displayed equation의 끝이 문장의 끝이면 수식 뒤에 마침표.
> displayed equation 다음에 산문이 이어지면 수식 뒤에 쉼표 또는 무부호.

**R5. 인용 형식.** "Equation (5)", "Theorem 2", "Lemma 3.1". 번호가 붙으면 첫 글자 대문자.

**R6. 정의는 두 번 다른 방식으로 (rule 5).** 수식 + 산문. "Let $\mathbf{T} \in SE(3)$ denote the rigid-body transform from sensor 관점 to world 관점."에서 수식과 산문이 같은 정의를 두 번 다른 방식으로 던진다.

**R7. 중요한 수식만 displayed, 참조되는 것만 number (rule 6).** 모든 수식에 번호를 붙이면 모든 수식이 중요해지고, 결국 아무것도 안 중요해진다. 본문에서 다시 인용하지 않는 수식은 번호 빼기.

**R8. 같은 기호를 두 의미로 쓰지 마라 (rule 9).** 로보틱스에서 흔한 충돌이다. $R$이 회전행렬·residual·reward로 동시에 쓰이는 문서가 있다. 한 문서 안에서 한 의미. ch16의 매크로 위생과 직결된다.

**R9. "that"을 빼지 마라 (rule 8).**

> ❌ We show $X$ converges.
>
> ✓ We show that $X$ converges.

영어 논문에서 "that" 생략은 종종 parsing을 어렵게 만든다.

**R10. "we"를 쓰고 "I"는 피한다 (rule 7).** Knuth, Whitesides, Mensh-Kording이 모두 같은 권고를 한다. 한국 영어 교육에서 강조해 온 passive 우선 관행과 충돌하는 한편, ch01에서 다룬 *지도교수 스타일을 따른다*는 입장과 같은 결정 축이다.

---

## 30.2 Theorem·Lemma·Proof — 자기완결과 signposting

**Theorem statement는 자기완결적이다.** Knuth rule 4의 핵심이다. 정리 안의 모든 기호가 정리문 안에서 정의되거나 명시 참조되어야 한다. 앞 단락을 다시 읽어야 statement가 이해되면 self-contained가 아니다.

> ❌ **Theorem 1.** *Under the conditions above, the estimator converges.*
>
> ✓ **Theorem 1.** *Let $\hat{\mathbf{x}}_k$ denote the EKF posterior mean at step $k$, and assume the observation noise satisfies $\mathbb{E}[\mathbf{v}_k] = \mathbf{0}$ and $\mathrm{Cov}(\mathbf{v}_k) = \mathbf{R}$. Then $\hat{\mathbf{x}}_k \to \mathbf{x}_k^\star$ as $k \to \infty$ in mean square.*

**Motivate before stating.** 정리 진술 직전 1-2 문장으로 *왜 이 정리가 필요한가*를 짚는다. 그 한 문장이 없으면 reviewer가 정리를 받고 "그래서?"부터 묻게 된다.

**Lemma·Theorem·Corollary는 위계가 다르다.** Lemma는 디딤돌, Theorem은 본 주장, Corollary는 직접 귀결이다. 한국 학생이 디딤돌도 Theorem으로 박는 일이 흔하다. 그러면 위계가 무너지면서 reviewer가 *진짜 main result*를 못 잡는다.

**증명 안의 signpost.** "We divide the proof into two parts." "The lemma is half proved." 증명이 반 페이지를 넘기면 signpost가 필수다. 그래야 독자가 어디쯤 와 있는지 잡을 단서가 된다.

**Direct proof가 가능한데 contradiction부터 가지 마라.** Knuth의 권고다. proof by contradiction은 독자에게 *부정 명제를 working memory에 들고 있을 부담*을 지운다. 그래서 direct proof가 닿는 곳에서는 direct가 우선이다.

**Halmos box (∎).** 증명 끝에 명시한다. 한국 학생들이 종종 빠뜨린다.

---

## 30.3 로보틱스·CV 특화 패턴

**SE(3)·Lie group 표기.** $\mathbf{T} \in SE(3)$, $\boldsymbol{\xi} \in \mathfrak{se}(3)$. 한 논문 안에서 case·bold·hat을 통일한다. 회전행렬을 한 곳에서 $\mathbf{R}$, 다른 곳에서 $R$로 쓰면 reviewer가 *다른 양인지* 추측해야 한다. ch16에서 매크로로 강제한다.

**Optimization 수식 패턴.**

$$\mathbf{x}^\star = \arg\min_{\mathbf{x}} f(\mathbf{x}) \quad \text{s.t.} \quad g(\mathbf{x}) = 0$$

`\text{s.t.}` 인지 `\text{subject to}`인지 한 문서 안에서 통일한다. 첫 등장 시 prose에서 한 번 풀어 둔다.

**Probabilistic 수식.** $p(\mathbf{x} \mid \mathbf{z})$의 `\mid`와 `|`를 섞지 않는다. Bayes filter 단계마다 prior, likelihood, posterior가 무엇을 가리키는지 prose에서 명시한다 — R6 이중 표현이 적용된다.

**잔차·loss 정의.** $\mathbf{r}_i = \mathbf{z}_i - h(\mathbf{x})$ 같은 잔차 정의에서, 인덱스 $i$가 무엇 위에서 도는지 prose에서 항상 밝힌다. "for each measurement $i \in \{1, \ldots, N\}$." 인덱스 변수만 던져두면 독자가 *어떤 집합 위에서의 합인지* 추측해야 한다.

**수식 줄바꿈에서 등호의 위치.** Inline에서는 등호 *뒤*에서 끊고, displayed에서는 등호 *앞*에서 끊는다. Knuth가 §1에 박은 typographic convention이다.

---

## 30.4 진단 — 자기 derivation의 'blah' 통과

자기 글의 derivation 한 페이지를 골라 모든 수식을 'blah'로 치환해 본다. 그 페이지가 산문으로서 흘러야 한다. 흐름이 끊기는 곳이 곧 between-equation prose가 비어 있는 자리다.

Knuth가 §2-§3에 박은 atrocious-vs-polished proof — 같은 정리의 두 버전을 나란히 놓고 줄별로 비교하는 자료가 이 장의 정전 사례다. 발췌와 분석은 Part 3 [`knuth_proof_rewrite.md`](./excerpts/excerpt_04_knuth_proof_rewrite.md)에.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) — *Mathematical Writing* §1의 27 rules에서 추린 10개 (rules 1, 2, 3, 4, 5, 6, 7, 8, 9, 16). atrocious-vs-polished proof는 §2-§3. Halmos box, Nilsson "쉽게 쓴 글" 인용도 같은 문서. 로보틱스·CV 4 패턴(SE(3), optimization, probabilistic, 잔차·loss)은 이 장에서 정리했다.

다음: [Ch.16 — 표기 위생](./chapter_31_notation_hygiene.md)
