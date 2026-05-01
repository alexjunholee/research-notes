# Ch.1 — 리뷰 논문에서 시작하라

"이 분야 논문 좀 읽어 와." 분야에 막 들어온 학생이 가장 자주 듣는 첫 지시다. 어드바이저는 분야의 이름까지만 일러준다. 그 안에서 무엇이 끝났고 무엇이 남았는지는 학생이 직접 추출한다. 그 작업에 먼저 필요한 것은 한 장의 지도다.

이 장이 받는 학생은 "이미 주제가 있는 학생"보다 한 단계 앞에 서 있다. 주제도 흐릿하고, 어떤 venue가 중요한지도 모르고, 좋은 저자의 이름은 한둘뿐인 단계다. 한 달 안에 분야 지도를 그리는 도구로 리뷰 논문 한 편, 인용 그래프, hypothesis placeholder 셋을 잡는다. Part 1 ch02의 Keshav 3-pass는 논문 한 편 단위의 읽기 전략이고, 이 장은 분야 단위의 진입 전략이다. 적용 층위가 다른 두 단계다.

---

## 1.1 분야 지도가 없다는 상태

분야 지도 없이 단일 논문에서 출발하면, 어디가 끝이고 어디가 시작인지 모르는 채 한 학기가 흘러간다. 어드바이저가 던져 준 한 편을 정독하고, 그 인용을 따라가다 동일 저자의 다음 논문을 찾고, 거기서 다시 인용을 따라간다. 일종의 random walk다. random walk 그 자체가 나쁘지는 않다. 다만 이렇게 해서는 언제 멈출지의 기준이 안 생긴다. 좌표가 없으면 거리감도 없다.

리뷰 논문은 시간 순서·subfield 분기·해결된 문제·열린 문제를 한 편에 압축한다. 한 저자(또는 한 그룹)의 시선으로 분야의 history와 taxonomy가 정리되어 있다. 본인이 처음부터 세우지 않아도 된다. 좋은 리뷰 한 편과 그 리뷰가 인용한 그래프, 이것만으로 한 달 분량의 분야 좌표가 잡힌다. 좌표가 잡힌 뒤에야 비로소 단일 논문이 어디에 놓여 있는지 보인다.

> **분야 진입의 시작점은 리뷰 논문(또는 그에 준하는 분야-단위 자료)이다.** 단일 논문만으로 시작하면 좌표 없이 읽는다. 리뷰가 없는 신생 subfield의 대체 자료(best paper·tutorial·thesis)는 §5에서 다룬다.

---

## 1.2 논문을 읽었다고 말하기 위한 네 질문

[최윤섭 박사](https://gradschoolstory.chkwon.net/yoonsup/first-research-subject/)가 「첫 연구 주제를 어떻게 정하고 접근할 것인가」에서 정리한 질문 네 개가 좋은 entry다. 한 논문을 다 읽었다고 말하기 위해 답해야 하는 질문 목록이고, 본인이 한 논문의 의미를 파악했는지 자가 진단하는 도구이기도 하다.

> 1. 왜 이 주제인가
> 2. 기존 연구는 어디까지 와 있는가
> 3. 남은 미해결 문제는 무엇인가
> 4. 나의 가설은 무엇인가
>
> 이 질문에 답할 수 없으면 그 연구의 의미를 파악하고 있다 할 수 없다.

분야 진입 단계에서 4번 질문이 비어 있는 것은 오히려 정상이다. 지금의 목표는 비어 있다는 사실을 인지한 채 보관하는 것이다. 1·2·3번은 리뷰 한 편으로 거의 채워지지만, 4번은 시간을 두고 천천히 차오른다. 한 논문은 핵심 질문 4개짜리 카드, 한 분야는 그 카드들의 묶음으로 보면 된다.

> **최윤섭 박사의 4개 질문에 답할 수 없는 논문은 읽지 않은 논문이다.** 페이지를 넘긴 것 ≠ 의미 파악 완료.

---

## 1.3 citation overlap survey

리뷰 한 편을 잡았다고 해서 분야 지도가 완성되지는 않는다. 리뷰는 한 시점의 단면이다. 그 시점 이후의 연구와 그 리뷰가 빠뜨린 subfield는 보이지 않는다. 단면을 입체로 키우려면 [Keshav 2007 §3](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)의 literature survey workflow가 필요하다.

Keshav가 §3에 적은 절차는 단순하다. 2026년에 같은 절차를 실행하면 도구만 바뀐다. (1) Google Scholar·Semantic Scholar·OpenAlex·Connected Papers 같은 paper graph에서 분야 keyword로 최근 논문 3–5편을 seed로 찾고, 각각 1st pass로 본다. seed의 related-work에 좋은 서베이가 인용돼 있으면 거기서 끝이다. (2) seed들의 reference 목록과 forward citation을 같이 보며 공유 인용과 반복되는 저자를 추출한다. 여러 seed가 동시에 인용한 논문이 분야의 핵심 논문이고, 반복되는 저자가 분야의 핵심 연구자다. 그 연구자의 publication list에서 반복되는 venue가 곧 그 분야의 top conference다. (3) top venue의 최근 proceedings·OpenReview·project page를 훑어 최근 고품질 논문을 추가로 흡수한다. (4) 새로 흡수한 논문이 또 다른 "모두가 인용하는" 핵심 논문을 가리키면 그 논문도 가져와 반복한다. 새로운 핵심이 더 안 나오면 종료다.

최윤섭 박사가 한국어로 적은 "꼬리에 꼬리·인용 추적 3단계"는 같은 절차의 다른 표현이다. 한국어 표현이 더 직관적이지만, 길을 잃은 순간에는 정형화된 영어 procedure로 돌아가야 좌표가 빠르게 회복된다.

> citation-overlap survey는 backward 인용과 forward 인용을 같이 본다. Keshav가 §3에 적은 backward citation (reference 목록 추적)만으로는 최근 동향이 빠진다. Google Scholar·Semantic Scholar·OpenAlex의 citation graph로 forward citation — seed를 인용한 후속 논문 — 을 같이 추적한다.

---

## 1.4 hypothesis placeholder를 입구에서

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)는 §1에 "A paper is not just an archival device for storing a completed research program; it is also a structure for planning your research in progress"라고 적었다. 논문은 진행 중인 연구를 기획하는 구조라는 선언이다. 같은 개념은 [Ch.17 — 아웃라인 우선](./chapter_17_outline_first.md)의 `[HYPOTHESIS]` placeholder와 이어진다.

이 장은 그 placeholder를 분야 진입 단계에서도 적용한다. 리뷰를 읽으며, 본인이 풀고 싶은 질문의 자리를 한 줄로 그려 둔다. 진짜 가설이 아니어도 괜찮고, 한 달 뒤에 통째로 갈아엎을 placeholder여도 괜찮다. 빈 줄만 잡혀 있으면, 다음에 읽는 논문이 그 자리에서 얼마나 떨어져 있는지가 측정된다.

> hypothesis placeholder는 진입 단계에서는 한 줄짜리 stub로 충분하다. "X subfield에서 Y가 아직 안 풀렸고, 나는 Z 방향을 보고 싶다" 정도면 된다. 점차 채운다.

이 placeholder가 다음 챕터([Ch.2 — 문제 정의: Feynman 3-step과 잘못된 질문](./chapter_02_feynman_problem.md))의 첫 줄, 파인만이 말한 "write down the problem"의 입력으로 이어진다. 분야 진입과 문제 정의가 한 흐름으로 묶인다.

---

## 1.5 로보틱스/CV에서의 entry

추상적인 절차는 진입 단계의 학생에게 마찰이 크다. 그래서 분야별로 review가 어디에 살고 entry tool이 무엇인지 구체적으로 박아 두는 편이 빠르다.

로보틱스 쪽 review는 보통 [T-RO (IEEE Transactions on Robotics)](https://www.ieee-ras.org/publications/t-ro), [IJRR (International Journal of Robotics Research)](https://journals.sagepub.com/home/ijr), [RAS (Robotics and Autonomous Systems)](https://www.sciencedirect.com/journal/robotics-and-autonomous-systems)에 실린다. SLAM이라면 Cadena et al. 2016, motion planning이라면 LaValle의 Planning Algorithms 같은 reference book이 reference 역할을 한다. CV 쪽 review는 [TPAMI (IEEE Transactions on Pattern Analysis and Machine Intelligence)](https://www.computer.org/csdl/journal/tp)에 실리는 경우가 많고, CVPR/ICCV/ECCV의 tutorial track에서 신생 subfield의 review 격 자료가 나온다.

entry tool로는 다음 4종이 잘 알려져 있다.

- [Google Scholar Profile](https://scholar.google.com): 분야 핵심 저자의 profile에 들어가 publication list를 시간순/인용순으로 본다. 인용수 top 10이 그 저자의 분야 입장을 압축한다.
- [arXiv cs.RO / cs.CV](https://arxiv.org/list/cs.RO/recent): firehose지만 keyword + "survey" / "review" / "tutorial" 조합으로 검색하면 review 후보가 줄어든다.
- [Semantic Scholar](https://www.semanticscholar.org): paper graph를 explicit하게 보여 주는 도구. seed 한 편의 backward와 forward 양쪽이 한 화면에 나온다.
- [Connected Papers](https://www.connectedpapers.com): seed 한 편을 입력하면 graph로 인근 논문을 시각화한다. citation-overlap survey를 한 화면에 압축해 주는 도구다.

신생 subfield에서는 review 논문이 아예 없는 경우가 흔하다. NeRF가 처음 나왔을 때처럼, 한두 해 동안은 review가 분야의 속도를 따라잡지 못한다. 이 경우는 review 대신 다음 셋으로 대체한다. (1) 해당 subfield의 best paper 또는 highly-cited workshop paper. (2) 해당 subfield의 PI가 학회에서 한 keynote / tutorial slide. (3) 신뢰 가능한 thesis (특히 박사 학위 논문의 ch.2 related work).

> review 논문이 없는 신생 subfield에서는 best paper · workshop paper · tutorial · thesis의 related work로 대체한다. 빈손으로 단일 논문에서 시작하지 않는다.

---

분야 진입의 한 달은 본인이 어디에 서 있는지를 좌표화하는 시간이다. 리뷰 한 편(또는 신생 subfield라면 §5의 best paper·tutorial·thesis 대체) → 최윤섭 박사 4개 질문 → citation overlap → hypothesis placeholder 순으로 한 바퀴를 돌고 나면, 다음 챕터의 입력 — "문제 정의" — 이 준비된다. 좌표가 잡힌 뒤에야 비로소 잘못된 질문과 맞는 질문이 갈라진다. 다음 챕터의 첫 줄 "write down the problem"은 그제야 빈칸이 아니다.

---

**출처.** [최윤섭 박사 G3 「첫 연구 주제를 어떻게 정하고 접근할 것인가」](https://gradschoolstory.chkwon.net/yoonsup/first-research-subject/), [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §3, [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §1.

다음: [Ch.2 — 문제 정의는 답보다 먼저 좁혀진다](./chapter_02_feynman_problem.md)
