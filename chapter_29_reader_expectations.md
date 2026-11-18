# 29장 문장 구조와 독자 기대

그림과 표를 아무리 잘 만들어도 그 사이를 잇는 영어 문장이 엉키면 독자는 논리 흐름을 놓친다. 영어 논문이 잘 읽히지 않는다고 느끼면 대개 어휘부터 어려운 단어로 바꾸려 들지만, [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)은 문제의 뿌리를 다른 곳에서 찾는다. 사람들은 흔히 과학 글이 어려운 까닭을 개념과 데이터, 분석 자체가 복잡해서 어쩔 수 없는 일로 여기지만, 두 저자는 정보를 문장의 어느 자리에 배치했는지가 훨씬 큰 원인이라고 본다. 독자가 정보를 기다리는 위치에 그 정보를 놓기만 하면, 내용을 억지로 단순화하지 않고도 글이 한결 또렷해진다.

앞서 [12장 §12.1](./chapter_12_reader_expectations_diagnosis.md)에서 보았듯, 두 저자는 글의 질을 높이면 생각의 질까지 함께 높아진다고 강조했다. 실제로 Gopen과 Swan은 글 말미에서 URF 단락을 제외한 나머지 예문들을 손보는 과정에서, 처음에는 원문 구조에 가려져 보이지 않던 개념의 빈틈이 고스란히 드러났다고 적었다. 문장 구조를 다듬는 작업이 곧 자신의 논리를 점검하는 과정이 되는 셈이다.

물론 두 저자는 독자 기대에서 이끌어 낸 원칙을 절대적인 규칙으로 삼지는 말라고 단서를 달았다. 어떤 기대든 특별한 효과를 노리고 일부러 어길 수 있기 때문이다. 다만 글을 잘 쓰는 사람은 대부분의 문장에서 이 기대를 충실히 따르기 때문에, 정작 원칙을 깬 대목에 이르렀을 때 독자가 그것이 실수가 아니라 저자의 의도적인 강조임을 알아차린다.

---

## 29.1 문장 안의 위치

Gopen과 Swan은 논문 끝에 일곱 가지 원칙을 정리했고, 그중 stress position, topic position, 주어와 동사의 거리, 이미 나온 정보와 새 정보의 순서는 [12장 §12.2](./chapter_12_reader_expectations_diagnosis.md)에서 진단 1–4로 살펴보았다. 여기서는 실전에서 가장 자주 어긋나는 topic position과 stress position부터 예문으로 다시 짚어 보자.

> ❌ The proposed method achieves 14% improvement in this paper.
>
> ✓ In this paper, the proposed method improves accuracy by 14%.

앞 문장과 이어 주는 구실인 "in this paper"는 문장 맨 앞(topic position)으로 보내고, 독자가 기억해야 할 핵심 수치인 14%는 문장 맨 끝(stress position)에 세운 것이다. (14%는 어순 차이를 보여 주려고 지어낸 수치다.)

**행위는 동사로 쓴다.** 문장이 전하려는 핵심 행위를 그대로 동사 자리에 두어야 문장에 힘이 실린다. 행위를 명사로 눌러 담아 버리면 정작 동사 자리가 공허해진다.

> ❌ We performed an evaluation of the algorithm on KITTI.
>
> ✓ We evaluated the algorithm on KITTI.

첫 문장에서는 별다른 뜻이 없는 `performed`가 동사 자리를 꿰찬 탓에, 진짜 행위인 `evaluation`이 명사구 안에 묻혀 버렸다.

---

## 29.2 한 단위에 한 가지

문장 안의 자리를 잡았다면, 다음은 한 문장이 감당하는 정보의 무게를 가늠할 차례다. Gopen과 Swan은 크기와 상관없이 글의 단위 하나가 오직 한 가지 일을 하거나 한 가지 요점만 전해야 한다고 말한다. 문장도 예외가 아니다.

구체적으로는 stress position에 놓일 만큼 무게감 있는 정보가 한 문장에 둘 이상 들어찼다면 두 문장으로 나누는 편이 안전하다. 물론 문장을 길게 이어 써야 할 때도 있는데, 이때는 쌍점(`:`)이나 쌍반점(`;`)으로 두 번째 stress position을 열어 줄 수 있다. 두 저자 역시 URF 예문을 고치면서 쌍반점을 활용해 두 번째 강조 자리를 만들었다. 다만 쌍반점을 쓸 때는 앞 절이 그 자체로 완전한 문장이어야 하며, 쌍반점 바로 앞자리에도 강조할 만한 핵심 정보가 놓여야 제 역할을 한다.

---

## 29.3 한국어로 생각하고 영어로 쓸 때 생기는 함정

Gopen과 Swan은 미국 전문 글쓰기를 염두에 두고 이 글을 썼다. 여기에 한국어 모어 화자가 한국어 문장 구조대로 생각하고 영어로 옮길 때 빠지기 쉬운 함정 네 가지가 더 얹힌다.

**동사를 문장 끝으로 미루는 습관.** 한국어는 서술어가 문장 맨 뒤에 오기 때문에, 그 습관 그대로 영어 문장을 지으면 주어와 동사 사이가 한없이 벌어지기 쉽다.

> ❌ The proposed method, which combines geometric ICP with a learned residual network trained on \(N\) sequences from benchmark \(B\), reduces ATE on the benchmark.
>
> ✓ The proposed method reduces ATE on benchmark \(B\). It combines geometric ICP with a learned residual network trained on \(N\) sequences.

주어 바로 뒤에 동사를 붙여 문장의 뼈대를 먼저 세우고, 수식어나 부연 설명은 다음 문장으로 넘기는 편이 훨씬 숨이 편하다.

**"은/는"을 영어 topic position과 혼동하는 습관.** 한국어의 조사 "은/는"은 주제를 내세울 때도 쓰지만 대조를 나타낼 때도 쓴다. 반면 영어의 topic position은 어디까지나 앞 문장과 맥락을 이어 주는 자리다. 뚜렷이 대조할 대상이 없는데도 단락 첫머리에 습관처럼 "On the other hand"를 붙이는 실수가 잦은데, 이 자리에는 앞 내용을 이어받는 말을 두어야 흐름이 끊기지 않는다.

**행위를 명사로 바꾸는 습관.** "~의 수행", "~의 분석" 같은 한국어 학술 표현을 직역하면 영어로 `the performance of`, `the analysis of` 같은 명사구가 되기 일쑤다. 문장의 핵심 행위가 중요한 대목이라면 동사가 명사 뒤에 숨지 않았는지 살펴야 한다. 개념 자체를 가리키는 명사는 그대로 두되, 핵심 동작을 가리는 명사만 동사로 되살린다.

**there 구문을 남발하는 습관.** 문장을 "there are several methods that …"로 열면 정작 문장 첫머리에 아무런 지시 대상이 서지 않는다. 앞 내용과 이어 줄 topic position이 텅 비고, `several methods`는 문장 한가운데서 갈 곳을 잃는다. 대신 "Prior work explores several methods …"로 시작하면 `prior work`가 자연스럽게 앞 맥락을 이어받는다.

한국어 어순을 머릿속에서 그대로 직역하지 말고, 다 쓴 영어 문장을 앞에 두고 다시 확인해 보자. 무엇이 앞 내용과 이어지는 정보이고 무엇이 새 정보인지, 또 독자가 어느 단어를 강조해 읽을지를 topic position과 stress position에 비춰 점검하면 문장이 눈에 띄게 정돈된다.

---

## 29.4 자기 문장 점검하기

단락 하나를 다 쓰고 나면 다음 두 가지 방법으로 문장을 점검해 본다.

**문장 첫머리와 끝을 뽑아 보기.** [21장 §21.5](./chapter_21_paragraph_flow.md)에서 다룬 '두 줄 뽑기'를 직접 적용해 본다. 문장 첫머리만 모아 놓은 줄에 앞 문장과 무관한 새 명사구만 잇달아 나온다면 흐름의 고리가 끊겼다는 신호다. 반대로 끝 줄에 "this paper", "the proposed method", "our approach" 같은 상투구가 몰려 있다면 강조할 핵심 정보를 문장 뒤로 옮겨야 한다.

**소리 내어 읽기.** 주어와 동사가 멀어지거나 구조가 꼬인 문장은 눈으로 훑을 때는 넘어가도 입으로 읽어 보면 금세 숨이 막힌다. Knuth 역시 *Mathematical Writing*에서 문장에는 리듬이 있으니 쓴 글을 직접 읽어 보고 매끄럽지 않으면 고치라고 권하며, 학생 답안을 평하면서 "소리 내어 읽어 보라(Read your words aloud to yourself)"고 당부했다.

Gopen과 Swan이 실제로 URF/ATPase 단락을 어떻게 고쳤는지 그 전후 과정이 궁금하다면, [`gopen_swan_urf_rewrite.md`](./excerpts/excerpt_03_gopen_swan_urf_rewrite.md)에 발췌해 둔 원문과 줄별 분석을 참고하면 감이 훨씬 빨리 잡힌다.

일반 산문에서 독자가 기대하는 자리가 있듯, 수식과 정리가 들어가는 문장에도 지켜야 할 문법과 리듬이 있다. 다음 장에서는 수식을 문장 속에 매끄럽게 녹여 내는 법을 살펴본다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) — stress position, topic position, 주어와 동사의 거리, 이미 나온 정보와 새 정보의 순서, 행위를 동사로 쓰기, 한 단위에 한 가지, 원칙을 규칙으로 여기지 말라는 단서. 소리 내어 읽기는 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 point 7과 §5.

다음: [30장 수식·정리·증명 쓰기](./chapter_30_math_and_proofs.md)
