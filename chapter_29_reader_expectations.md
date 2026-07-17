# Ch.29 — 문장 구조와 독자 기대

영어 논문이 안 읽힌다는 직감을 가진 학생이 어휘를 더 어렵게 바꾸려 든다. [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing)의 진단은 정반대 방향을 가리킨다. 글의 어려움은 어휘가 아니라 구조에서 온다. 단어를 바꾸는 작업은 헛수고에 가깝고, 고쳐야 하는 곳은 문장 안에서 정보가 놓이는 위치다.

Gopen-Swan은 같은 논문에서 "글의 질을 개선하면 사고의 질이 개선된다"고 적었다. 구조를 다듬다 보면 개념의 빈틈이 드러난다는 관찰이다. 문장 구조 점검은 사고를 점검하는 도구로도 작동한다.

다만 이들은 규칙이 아니라 원칙이라는 단서가 같이 붙는다. 잘 쓰는 사람은 잘 어긴다. 어기는 위치가 일관되고, 어겨도 되는 이유를 안다.

---

## 29.1 문장 안의 위치 — 5대 원칙

**Stress position — 문장 끝에는 새 정보를 둔다.** 문장 끝이나 `;` `:` 직전이 강조 위치다. 독자는 거기에 도달할 때 닫힘(closure)을 느끼고 가장 강하게 기억한다. 보일러플레이트가 거기에 오면 강조가 사라진다.

> ❌ The proposed method achieves 14% improvement in this paper.
>
> ✓ In this paper, the proposed method improves accuracy by 14%.

"in this paper"는 backward link 역할을 하므로 topic position에 둔다. stress position에는 14%를 둔다. 14%는 어순을 보이기 위한 가상 수치다.

**Topic position — 문장 머리에는 이미 등장한 것.** 문장 첫 단어는 관점을 정하고 backward link를 건다. 새 명사를 첫머리에 던지면 독자가 앞 단락과 연결할 단서를 잃는다.

**Subject-Verb proximity — 주어와 동사 사이는 짧게 둔다.** 주어와 동사 사이가 15단어를 넘으면 위험 신호다. 한국 학생이 관계절·전치사구를 끼워 넣다가 가장 자주 어기는 원칙이다. 독자는 동사를 만나기 전까지 주어를 작업 기억에 들고 있어야 한다.

**Old-before-New.** topic = old, stress = new. Gopen-Swan이 "미국 전문 글쓰기 1번 문제"라고 박은 원칙. 정보 흐름이 거꾸로 가면 독자가 매 문장에서 왜 이 정보가 지금 들어오는지를 추론하느라 인지자원을 쓴다.

**Action-in-verb.** action은 verb 자리에 둔다. 명사화하면 verb 자리가 헐거워진다.

> ❌ We performed an evaluation of the algorithm on KITTI.
>
> ✓ We evaluated the algorithm on KITTI.

명사화는 공식적 톤을 만들지만 stress position을 약화한다. evaluation이 stress position에 갇히고, 정작 새 정보인 KITTI가 끝에서 밀린다.

---

## 29.2 단위 하나, 메시지 하나

한 문장 = 한 메시지가 Gopen-Swan의 다섯 번째 원칙이다. 진단법은 단순하다. stress position 자격 후보가 둘 이상이면 그 문장이 너무 길다.

> "딸기 쇼트케이크로 시작해 브로콜리로 끝내는 식사는 없다."

stress position에 들어갈 만큼 무게 있는 명사구가 한 문장 안에 둘 이상 등장하면 식사 메뉴가 어긋난다. 끊어서 두 문장으로 만든다.

길게 갈 수밖에 없는 곳에서는 `:`나 `;`가 secondary stress를 만든다. punctuation이 만드는 medial closure다. 그 자리에도 무게 있는 명사구가 오도록 배치한다.

---

## 29.3 한국어 → 영어 — 모국어가 만드는 함정 4가지

Gopen-Swan은 영어 모국어 독자만 다룬다. 한편 한국 학생에게는 모국어 구조가 만드는 추가 함정이 있다.

**SOV → SVO 전환 실패.** 한국어는 동사가 끝에 온다. 머릿속에서 동사를 마지막까지 미루는 습관이 영어 작문에서도 살아남고, 그 결과가 주어와 동사 사이를 늘리는 문장이다.

> ❌ The proposed method, which combines geometric ICP with a learned residual network trained on \(N\) sequences from benchmark \(B\), reduces ATE on the benchmark.
>
> ✓ The proposed method reduces ATE on benchmark \(B\). It combines geometric ICP with a learned residual network trained on \(N\) sequences.

주어 다음에 바로 동사를 두고, 부연은 다음 문장으로 분리한다.

**"은/는" topic 표지 ≠ 영어 topic position.** 한국어의 "은/는"은 주제와 대조를 동시에 표시한다. 한편 영어 topic position은 backward link만 한다. "On the other hand"를 매 단락 첫 자리에 두는 학생이 흔한데, 보통 거기에는 대조가 아니라 연속이 들어가야 한다. 그러지 않으면 backward link가 끊어진다.

**Nominalization 함정.** "~의 수행", "~의 분석" 같은 한국어 학술체가 영어로 옮길 때 `the performance of`, `the analysis of`로 굳어질 수 있다. 행위를 강조해야 하는 문장에서는 동사가 명사화에 묻히지 않았는지 확인한다. 개념을 가리키는 명사화는 유지하고, 행위를 숨기는 명사형은 동사로 풀어 본다.

**There-구문 남발.** "there are several methods that …"가 topic position을 유령으로 채운다. backward link를 거는 자리가 비고, several methods가 sentence body에서 떠다닌다. 그 대신 "Prior work explores several methods …"로 시작해 prior work가 backward link를 받게 한다.

old/new 정보의 순서도 한국어와 같지 않다. 한국어는 종결어미와 어순이 강조를 만들고, 영어는 위치가 강조를 만든다. 그래서 한국식 "이 결과는 중요한데 …"의 강조를 그대로 옮기면 stress position이 사라진다.

---

## 29.4 자기 진단 — 자기 문장 reverse-read

한 단락을 다 쓴 뒤 다음 두 가지를 점검한다.

**Topic-flow 추적.** 각 문장의 첫 명사구만 추출해 한 줄로 나열한다. 그 체인이 끊기지 않고 이어져야 한다. 첫 명사구가 매 문장마다 새로운 것이라면 backward link가 무너졌다.

**Stress 점검.** 각 문장의 마지막 명사구만 추출한다. "this paper", "the proposed method", "our approach" 같은 보일러플레이트가 stress position을 차지하고 있으면 모두 재배치해 둔다.

**소리 내어 읽기.** 주어-동사 거리가 멀면 호흡이 끊긴다. Knuth가 Mathematical Writing에서도 같은 처방을 권한 만큼, 자기 글을 큰 소리로 읽는 작업이 두 사람의 권고에서 같은 위치를 차지한다.

URF/ATPase 단락의 before/after rewrite와 Gopen-Swan이 같은 논문 §III에 제시한 사례의 발췌·줄별 분석은 [`gopen_swan_urf_rewrite.md`](./excerpts/excerpt_03_gopen_swan_urf_rewrite.md)에 있다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) — stress/topic position, subject-verb proximity, old-before-new, action-in-verb, "1번 문제" 인용, 쇼트케이크 비유. 한국어→영어 4함정(SOV/은-는/nominalization/There-구문)은 이 장에서 정리했다. Knuth와 공통되는 큰 소리로 읽기 처방은 [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html)와 교차.

다음: [Ch.15 — 수식·정리·증명 쓰기](./chapter_30_math_and_proofs.md)
