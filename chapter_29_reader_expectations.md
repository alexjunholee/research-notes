# Ch.29 — 문장 구조와 독자 기대

영어 논문이 잘 읽히지 않는다고 느끼면 어휘부터 바꾸고 싶어진다. [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)은 다른 곳을 본다. 대부분의 사람은 과학 글이 어려운 까닭을 개념과 데이터, 분석이 워낙 복잡해서 어쩔 수 없는 일로 여기지만, 두 저자는 정보를 문장의 어느 자리에 두었는지가 더 큰 원인이라고 본다. 독자가 기대하는 자리에 정보를 놓으면 내용을 단순하게 줄이지 않고도 글이 분명해진다.

글의 질을 높이면 생각의 질도 실제로 높아진다는 두 저자의 말은 [Ch.12 §12.1](./chapter_12_reader_expectations_diagnosis.md)에서 보았다. Gopen과 Swan은 글 끝에서, URF 단락을 뺀 나머지 예문을 고치다 보니 원문 구조에 가려 있던 개념의 빈틈이 드러났다고 썼다. 문장 구조를 점검하면 생각도 함께 점검하게 된다.

두 저자는 독자 기대에서 끌어낸 원칙들을 규칙으로 여기지 말라고 덧붙였다. 어떤 기대든 효과를 노리고 어길 수 있다. 다만 글을 잘 쓰는 사람은 대부분의 문장에서 기대를 지키기 때문에, 어긴 곳이 일부러 어긴 곳으로 읽힌다.

---

## 29.1 문장 안의 위치

Gopen과 Swan은 글 끝에 원칙 일곱 개를 정리했다. 그중 stress position, topic position, 주어와 동사의 거리, 이미 나온 정보와 새 정보의 순서는 [Ch.12 §12.2](./chapter_12_reader_expectations_diagnosis.md)에서 진단 1–4로 보았다.

> ❌ The proposed method achieves 14% improvement in this paper.
>
> ✓ In this paper, the proposed method improves accuracy by 14%.

"in this paper"는 앞 내용과 이어 주는 말이라 문장 앞(topic position)에 둔다. 문장 끝에는 14%를 둔다. 14%는 어순을 보여 주려고 지어낸 수치다.

**행위는 동사로 쓴다.** 문장이 말하는 행위를 동사 자리에 둔다. 행위를 명사로 바꾸면 동사 자리가 비어 버린다.

> ❌ We performed an evaluation of the algorithm on KITTI.
>
> ✓ We evaluated the algorithm on KITTI.

첫 문장에서는 별 뜻 없는 performed가 동사 자리를 차지하고, 실제 행위인 evaluation은 명사구 안에 묻혔다.

---

## 29.2 한 단위에 한 가지

Gopen과 Swan은 크기와 상관없이 글의 단위 하나는 한 가지 일을 하거나 한 가지 요점을 말해야 한다고 했다. 문장도 마찬가지다. 이 책에서는 이렇게 점검한다. stress position에 놓일 만큼 무게 있는 정보가 한 문장에 둘 이상이면 두 문장으로 나눈다.

문장을 길게 써야 할 때는 쌍점이나 쌍반점으로 두 번째 stress position을 만든다. 두 저자는 URF 예문을 고치면서 쌍반점으로 두 번째 강조 자리를 만들었다. 이때 쌍반점 앞부분은 혼자서도 완전한 문장이어야 하고, 그 끝에도 강조할 정보가 와야 한다.

---

## 29.3 한국어로 생각하고 영어로 쓸 때 생기는 함정

Gopen과 Swan은 미국 전문 글쓰기를 두고 이 글을 썼다. 한국어 모어 화자에게는 모국어 구조에서 오는 함정이 더 있다.

**동사를 끝으로 미룬다.** 한국어는 동사가 문장 끝에 온다. 이 습관대로 영어를 쓰면 주어와 동사 사이가 길어진다.

> ❌ The proposed method, which combines geometric ICP with a learned residual network trained on \(N\) sequences from benchmark \(B\), reduces ATE on the benchmark.
>
> ✓ The proposed method reduces ATE on benchmark \(B\). It combines geometric ICP with a learned residual network trained on \(N\) sequences.

주어 바로 뒤에 동사를 두고, 덧붙이는 설명은 다음 문장으로 뺀다.

**"은/는"과 영어 topic position은 다르다.** 한국어 "은/는"은 주제를 내세우기도 하고 대조를 나타내기도 한다. 영어 topic position은 앞 문장과 이어 주는 자리다. 대조할 내용이 없는데도 단락 첫머리에 "On the other hand"를 습관처럼 붙이는 실수도 있다. 이럴 때는 앞 내용을 이어 받는 말을 두어야 흐름이 매끄럽다.

**행위를 명사로 바꾼다.** "~의 수행", "~의 분석" 같은 한국어 학술체를 영어로 옮기면 `the performance of`, `the analysis of`가 되기 쉽다. 행위가 중요한 문장이라면 동사가 명사 안에 묻히지 않았는지 본다. 개념 자체를 가리키는 명사는 그대로 두고, 핵심 행위를 감추는 명사만 동사로 바꾼다.

**there 구문을 남발한다.** "there are several methods that …"로 시작하면 문장 첫머리가 아무것도 가리키지 않는다. 앞 내용과 이어 줄 자리가 비고, several methods는 문장 안에서 갈 곳을 잃는다. "Prior work explores several methods …"로 쓰면 prior work가 앞 내용을 이어 받는다.

한국어 문장의 어순을 그대로 옮기지 말고, 다 쓴 영어 문장을 보며 확인한다. 무엇이 앞과 이어지는 정보이고 무엇이 새 정보인지, 독자가 무엇을 강조해 읽을지를 topic position과 stress position에서 본다.

---

## 29.4 자기 문장 점검하기

단락 하나를 다 쓰면 다음을 본다.

**문장 첫머리를 이어 본다.** 문장마다 첫 명사구만 뽑아 한 줄로 늘어놓는다. 이 줄이 서로 이어져야 한다. 문장마다 첫 명사구가 새것이라면 앞 문장과의 고리가 끊긴 것이다.

**문장 끝을 본다.** 문장마다 마지막 명사구만 뽑는다. "this paper", "the proposed method", "our approach" 같은 상투구가 문장 끝에 와 있으면 자리를 옮긴다.

**소리 내어 읽는다.** 주어와 동사가 멀면 읽다가 숨이 끊긴다. Knuth도 Mathematical Writing에서 문장에는 리듬이 있으니 쓴 글을 읽어 보고 매끄럽지 않으면 고치라고 했고, 학생 답안을 평하면서 "소리 내어 읽어 보라(Read your words aloud to yourself)"고 했다.

URF/ATPase 단락을 Gopen과 Swan이 어떻게 고쳤는지는 [`gopen_swan_urf_rewrite.md`](./excerpts/excerpt_03_gopen_swan_urf_rewrite.md)에 발췌하고 줄마다 분석해 두었다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) — stress position, topic position, 주어와 동사의 거리, 이미 나온 정보와 새 정보의 순서, 행위를 동사로 쓰기, 한 단위에 한 가지, 원칙을 규칙으로 여기지 말라는 단서. 한국어 모어 화자의 함정 네 가지와 점검 방법은 이 장에서 정리했다. 소리 내어 읽기는 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 point 7과 §5.

다음: [Ch.30 — 수식·정리·증명 쓰기](./chapter_30_math_and_proofs.md)
