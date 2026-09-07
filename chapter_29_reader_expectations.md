# Ch.29 — 문장 구조와 독자 기대

영어 논문이 안 읽힌다고 느끼는 학생은 어휘를 더 어렵게 바꾸려 든다. [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing)의 진단은 정반대 방향을 가리킨다. 글의 어려움은 주로 정보가 배치되는 문장 구조에서 발생한다. 단어만 교체하는 접근으로는 실질적 효과를 거두기 힘들다. 독자가 기대하는 자리에 정보를 정렬하는 배치가 글의 명료성을 결정한다.

Gopen-Swan은 같은 논문에서 "글의 질을 개선하면 사고의 질이 개선된다"고 적었다. 구조를 다듬다 보면 개념의 빈틈이 드러난다는 뜻이다. 문장 구조 점검은 사고를 점검하는 도구이기도 하다.

다만 이 지침들은 기계적 규칙이라기보다 유연한 원칙에 가깝다는 단서가 붙는다. 글을 능숙하게 쓰는 사람은 필요할 때 원칙을 의도적으로 넘나든다. 어기는 위치가 일관되고, 그 선택의 분명한 이유를 이해하고 있기 때문이다.

---

## 29.1 문장 안의 위치 — 5대 원칙

**Stress position — 문장 끝에는 새 정보를 둔다.** 문장 끝이나 `;` `:` 직전이 강조 위치다. 독자는 거기에 도달할 때 닫힘(closure)을 느끼고 가장 강하게 기억한다. 보일러플레이트가 거기에 오면 강조가 사라진다.

> ❌ The proposed method achieves 14% improvement in this paper.
>
> ✓ In this paper, the proposed method improves accuracy by 14%.

"in this paper"는 backward link 역할을 하므로 topic position에 둔다. stress position에는 14%를 둔다. 여기서 14%는 문맥상의 어순 배치를 예시하기 위해 든 수치다.

**Topic position — 문장 머리에는 이미 등장한 것.** 문장 첫 단어는 관점을 정하고 backward link를 건다. 새 명사를 첫머리에 던지면 독자가 앞 단락과 연결할 단서를 잃는다.

**Subject-Verb proximity — 주어와 동사 사이는 짧게 둔다.** 주어와 동사 사이가 15단어를 넘으면 위험 신호다. 한국어 모어 화자인 학생이 관계절·전치사구를 끼워 넣다가 가장 자주 어기는 원칙이다. 독자는 동사를 만나기 전까지 주어를 작업 기억에 들고 있어야 한다.

**Old-before-New.** topic = old, stress = new. Gopen-Swan이 "미국 전문 글쓰기 1번 문제"라고 박은 원칙. 정보의 흐름 순서가 뒤틀리면 독자가 매 문장에서 왜 이 정보가 지금 들어오는지 추론하느라 인지자원을 소모하게 된다.

**Action-in-verb.** action은 verb 자리에 둔다. 명사화하면 verb 자리가 헐거워진다.

> ❌ We performed an evaluation of the algorithm on KITTI.
>
> ✓ We evaluated the algorithm on KITTI.

명사화는 행위를 약화한다. 동사 자리를 일반 동사 performed가 차지해 정작 행위인 evaluation이 명사구 안에 묻힌다.

---

## 29.2 단위 하나, 메시지 하나

한 문장 = 한 메시지도 Gopen-Swan의 원칙이다. 진단법은 단순하다. stress position에 놓일 후보가 둘 이상이면 그 문장이 너무 길다.

> "딸기 쇼트케이크로 시작해 브로콜리로 끝내는 식사는 없다."

stress position에 들어갈 만큼 무게 있는 명사구가 한 문장 안에 둘 이상 등장하면 식사 메뉴가 어긋난다. 끊어서 두 문장으로 만든다.

길게 갈 수밖에 없는 곳에서는 `:`나 `;`가 secondary stress를 만든다. punctuation이 만드는 medial closure다. 그 자리에도 무게 있는 명사구가 오도록 배치한다.

---

## 29.3 한국어 → 영어 — 모국어가 만드는 함정 4가지

Gopen-Swan은 영어 모국어 독자만 다룬다. 한편 한국어 모어 화자인 학생에게는 모국어 구조가 만드는 추가 함정이 있다.

**SOV → SVO 전환 실패.** 한국어는 동사가 끝에 온다. 머릿속에서 동사를 문장 끝까지 미루는 언어 습관이 영어 작문으로 이어지면서 주어와 동사 사이의 간격이 비대해진다.

> ❌ The proposed method, which combines geometric ICP with a learned residual network trained on \(N\) sequences from benchmark \(B\), reduces ATE on the benchmark.
>
> ✓ The proposed method reduces ATE on benchmark \(B\). It combines geometric ICP with a learned residual network trained on \(N\) sequences.

주어 다음에 바로 동사를 두고, 부연은 다음 문장으로 분리한다.

**"은/는" topic 표지 ≠ 영어 topic position.** 한국어의 "은/는"은 주제 제시와 대조의 기능을 동시에 수행한다. 영어의 topic position은 앞 문맥과의 연결(backward link)에 집중하는 자리다. 단락 첫머리에 습관적으로 "On the other hand"를 두는 실수가 잦지만, 대다수 맥락에서는 대조보다 논리적 연속성을 확보해야 backward link가 매끄럽게 유지된다.

**Nominalization 함정.** "~의 수행", "~의 분석" 같은 한국어 학술체가 영어로 옮길 때 `the performance of`, `the analysis of`로 굳어질 수 있다. 행위를 강조해야 하는 문장에서는 동사가 명사화에 묻히지 않았는지 확인한다. 개념 자체를 지칭하는 명사화는 살리되, 핵심 동작을 은폐하는 명사 표현은 동사 형태로 전환하는 편이 바람직하다.

**There-구문 남발.** "there are several methods that …"가 topic position을 유령으로 채운다. backward link를 거는 자리가 비고, several methods가 sentence body에서 떠다닌다. 그 대신 "Prior work explores several methods …"로 시작해 prior work가 backward link를 받게 한다.

한국어에서 의도한 old/new 정보의 관계와 강조가 영어 문장에서도 이어지는지 점검한다. "이 결과는 중요한데 …"처럼 미완성인 구절의 어순을 따라 옮기기보다, 완성된 영어 문장에서 독자가 무엇을 강조점으로 읽을지 topic position과 stress position을 확인한다.

---

## 29.4 자기 진단 — 자기 문장 reverse-read

한 단락을 다 쓴 뒤 다음 세 가지를 점검한다.

**Topic-flow 추적.** 각 문장의 첫 명사구만 추출해 한 줄로 나열한다. 그 체인이 끊기지 않고 이어져야 한다. 첫 명사구가 매 문장마다 새로운 것이라면 backward link가 무너졌다.

**Stress 점검.** 각 문장의 마지막 명사구만 추출한다. "this paper", "the proposed method", "our approach" 같은 보일러플레이트가 stress position을 차지하고 있으면 모두 재배치해 둔다.

**소리 내어 읽기.** 주어-동사 거리가 멀면 호흡이 끊긴다. Knuth가 Mathematical Writing에서도 같은 처방을 권한 만큼, 자기 글을 큰 소리로 읽는 작업이 두 자료의 권고에서 같은 위치를 차지한다.

URF/ATPase 단락의 before/after rewrite와 Gopen-Swan이 같은 논문 §III에 제시한 사례의 발췌·줄별 분석은 [`gopen_swan_urf_rewrite.md`](./excerpts/excerpt_03_gopen_swan_urf_rewrite.md)에 있다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) — stress/topic position, subject-verb proximity, old-before-new, action-in-verb, "1번 문제" 인용, 쇼트케이크 비유. 한국어 모어 화자가 직면하는 네 가지 구조적 함정은 본문에서 독자적으로 분석해 체계화했다. Knuth와 공통되는 큰 소리로 읽기 처방은 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html)와 교차.

다음: [Ch.30 — 수식·정리·증명 쓰기](./chapter_30_math_and_proofs.md)
