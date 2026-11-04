# Ch.1 — 리뷰 논문에서 시작하라

"이 분야 논문 좀 읽어 와." 분야에 막 들어온 학생이 첫 지시로 이런 말을 듣기도 한다. 지도교수는 분야의 이름까지만 일러준다. 그 안에서 무엇이 끝났고 무엇이 남았는지는 학생이 직접 찾아내야 한다. 그러려면 먼저 분야 전체를 한눈에 보여 줄 지도가 있어야 한다.

이 장의 독자는 아직 주제가 정해지기 전 단계에 있다. 주제도 흐릿하고, 어떤 venue가 중요한지 모르고, 아는 좋은 저자도 한둘뿐이다. 한 달 안에 분야 지도를 그리는 데에는 리뷰 논문 한 편, 인용 그래프, 한 줄짜리 hypothesis placeholder를 쓴다. 개별 논문을 깊이 읽는 방법은 Ch.7의 Keshav 3-pass에서 다룬다.

---

## 1.1 분야 지도가 없을 때

분야 지도 없이 논문 한 편에서 출발하면, 어디가 끝이고 어디가 시작인지 모르는 채 한 학기가 흘러간다. 지도교수가 건넨 한 편을 정독하고, 그 인용을 따라 같은 저자의 다음 논문을 찾고, 거기서 다시 인용을 따라간다. 일종의 random walk다. 이렇게 읽으면 언제 멈출지 정할 기준이 생기기 어렵다.

리뷰 논문은 분야가 흘러온 순서, 갈라진 subfield, 해결된 문제와 열린 문제를 한 편에 담는다. 분야의 history와 taxonomy를 한 저자나 한 그룹이 정리해 두었으니, 학생이 처음부터 세울 필요가 없다. 좋은 리뷰 한 편을 읽고 거기서부터 따라간 논문들의 인용 관계를 그리면 분야의 좌표를 잡을 수 있다. 좌표가 잡혀야 논문 한 편이 분야의 어디에 놓이는지 보인다.

> **분야에 들어갈 때는 리뷰 논문(또는 분야 전체를 정리한 자료)에서 시작한다.** 논문 한 편에서 시작하면 좌표 없이 읽게 된다. 리뷰가 아직 없는 신생 subfield에서 쓸 자료(best paper, tutorial, thesis)는 §1.5에 있다.

---

## 1.2 연구의 맥락을 파악했는지 묻는 질문

[최윤섭 박사](https://gradschoolstory.chkwon.net/yoonsup/first-research-subject/)는 「첫 연구 주제를 어떻게 정하고 접근할 것인가」에서 선배에게 이렇게 물어보라고 권한다. 이 주제를 왜 시작했는가, 이전에는 어떤 연구가 있었고 이 주제는 그 연구와 어떻게 이어지는가, 이 주제는 기존 연구가 풀지 못한 어떤 문제를 풀려고 하는가. 그리고 논문을 읽는 내내 "이러한 기존 연구의 흐름 속에서 내가 풀어야 할 질문은 무엇일까", "나는 어떠한 가설을 가지고 있는가"를 붙들고 있어야 한다고 한다. 이 물음들을 네 질문으로 줄여 적는다.

> 1. 왜 이 주제인가
> 2. 기존 연구는 어디까지 와 있는가
> 3. 남은 미해결 문제는 무엇인가
> 4. 나의 가설은 무엇인가

최윤섭 박사는 앞의 물음들을 두고 "그 질문에 제대로 답할 수 없으면 그 연구의 의미를 제대로 파악하고 있다고 할 수 없다"고 적었다.

분야에 막 들어온 학생이라면 4번이 비어 있는 게 자연스럽다. 비어 있다는 사실을 알고 그대로 두면 된다. 1·2·3번은 리뷰 한 편으로 거의 채워지고, 4번은 시간을 두고 천천히 채워진다. 논문 한 편마다 네 질문의 답을 카드 한 장에 적어 두면, 분야는 그 카드들의 묶음이 된다.

> **네 질문으로 이해한 범위를 확인한다.** 진입 단계에서는 4번을 빈칸으로 남겨도 된다. 끝까지 읽은 뒤에도 네 질문에 답하지 못하면 해당 부분을 다시 읽는다.

---

## 1.3 citation overlap survey

리뷰 한 편은 쓰인 시점의 분야만 보여 준다. 그 뒤에 나온 연구와 리뷰가 빠뜨린 subfield는 리뷰에 없다. 이 빈자리를 채울 때 [Keshav 2007 §3](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)의 literature survey 절차를 쓴다.

Keshav가 §3에 적은 절차는 단순하다. 2026년에는 쓰는 도구만 달라진다.

(1) Google Scholar, Semantic Scholar, OpenAlex, Connected Papers 같은 paper graph 도구에 분야 keyword를 넣어 최근 논문 3–5편을 seed로 찾고, 각각 1st pass로 읽는다. seed의 related work가 좋은 서베이를 인용하고 있으면 거기서 끝이다.

(2) seed들의 참고문헌에서 여러 번 인용된 논문과 자주 나오는 저자를 뽑는다. 여러 seed가 함께 인용한 논문이 분야의 핵심 논문이고, 자주 나오는 저자가 핵심 연구자다. 그 연구자들이 최근 논문을 낸 venue를 보면 그 분야의 top conference를 가늠하는 데 도움이 된다. 뛰어난 연구자는 대개 top conference에 논문을 내기 때문이다.

(3) top venue의 최근 proceedings, OpenReview, project page를 훑어 최근에 나온 좋은 논문을 더한다.

(4) 새로 더한 논문들이 모두 인용하는데 아직 못 본 핵심 논문이 있으면 그것도 구해 읽고 같은 일을 되풀이한다. 새 핵심 논문이 더 나오지 않으면 멈춘다.

최윤섭 박사의 글에도 같은 절차가 있다. 리뷰 논문을 읽고, 인용된 논문을 "꼬리에 꼬리를 물고" 읽고, 그 논문을 인용한 후속 연구를 찾는다. 길을 잃었을 때는 단계가 정해진 Keshav의 절차로 돌아가는 편이 빨리 좌표를 되찾는다.

> citation overlap survey는 backward 인용과 forward 인용을 함께 본다. Keshav의 2단계처럼 참고문헌 목록만 따라가는 backward 추적으로는 최근 연구가 빠진다. Google Scholar, Semantic Scholar, OpenAlex의 citation graph에서 seed를 인용한 후속 논문(forward citation)도 함께 따라간다.

---

## 1.4 분야에 들어설 때부터 hypothesis placeholder를 둔다

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)는 1절 "What is a Scientific Paper?"에서 "A paper is not just an archival device for storing a completed research program; it is also a structure for planning your research in progress"라고 적었다(논문은 끝난 연구를 보관하는 수단이면서 진행 중인 연구를 계획하는 틀이기도 하다). [Ch.17 — 아웃라인부터 시작하기](./chapter_17_outline_first.md)의 `[HYPOTHESIS]` placeholder도 이 생각에서 나왔다.

분야에 들어설 때도 같은 placeholder를 쓴다. 리뷰를 읽으면서 풀고 싶은 질문을 한 줄로 적어 둔다. 진짜 가설이 아니어도 되고, 한 달 뒤에 통째로 갈아엎어도 된다. 한 줄이라도 적혀 있으면, 다음에 읽는 논문이 그 질문에서 얼마나 떨어져 있는지 잴 수 있다.

> 진입 단계의 hypothesis placeholder는 한 줄짜리 stub이면 충분하다. "X subfield에서 Y가 아직 안 풀렸고, 나는 Z 방향을 보고 싶다" 정도로 적고 점차 채운다.

이 한 줄은 [Ch.2 — 문제 정의는 답보다 먼저 좁혀진다](./chapter_02_feynman_problem.md)의 첫 단계, 파인만이 말한 "write down the problem"에 그대로 들어간다.

---

## 1.5 로보틱스와 CV에서 시작할 곳

분야에 처음 들어선 학생에게는 추상적인 절차보다 리뷰 자료를 어디서 찾는지, 어떤 도구를 쓰는지 알려 주는 편이 빠르다.

로보틱스 리뷰는 보통 [T-RO (IEEE Transactions on Robotics)](https://www.ieee-ras.org/publications/t-ro), [IJRR (International Journal of Robotics Research)](https://journals.sagepub.com/home/ijr), [RAS (Robotics and Autonomous Systems)](https://www.sciencedirect.com/journal/robotics-and-autonomous-systems)에 실린다. SLAM에서는 Cadena et al. 2016이, motion planning에서는 LaValle의 책 Planning Algorithms가 리뷰 역할을 한다. CV 리뷰는 [TPAMI (IEEE Transactions on Pattern Analysis and Machine Intelligence)](https://www.computer.org/csdl/journal/tp)에 많이 실리고, 신생 subfield는 CVPR·ICCV·ECCV의 tutorial이 리뷰 구실을 한다.

분야에 들어설 때 많이 쓰는 도구는 다음과 같다.

- [Google Scholar Profile](https://scholar.google.com): 분야 핵심 저자의 profile에서 publication list를 시간순과 인용순으로 본다. 인용 상위 10편을 보면 그 저자가 분야에서 무엇을 해 왔는지 알 수 있다.
- [arXiv cs.RO / cs.CV](https://arxiv.org/list/cs.RO/recent): 매일 쏟아지는 논문이 너무 많지만, keyword에 "survey", "review", "tutorial"을 붙여 검색하면 리뷰 후보가 추려진다.
- [Semantic Scholar](https://www.semanticscholar.org): seed 한 편이 인용한 논문(backward)과 그 논문을 인용한 논문(forward)을 한 화면에 보여 준다.
- [Connected Papers](https://www.connectedpapers.com): seed 한 편을 넣으면 가까운 논문들을 그래프로 그려 준다. citation overlap survey를 한 화면에서 해 볼 수 있다.

신생 subfield에는 리뷰 논문이 아예 없는 경우가 흔하다. NeRF가 처음 나왔을 때처럼 한두 해 동안은 연구가 리뷰보다 먼저 쌓인다. 이럴 때는 리뷰 대신 다음 자료를 쓴다. (1) 그 subfield의 best paper나 많이 인용된 workshop paper. (2) 그 subfield를 이끄는 PI가 학회에서 한 keynote나 tutorial 슬라이드. (3) 믿을 만한 thesis, 특히 박사 학위 논문의 related work 장.

> 리뷰 논문이 없는 신생 subfield에서는 best paper, workshop paper, tutorial, thesis의 related work를 대신 읽는다. 논문 한 편만 들고 시작하지 않는다.

---

**출처.** [최윤섭 박사 「첫 연구 주제를 어떻게 정하고 접근할 것인가」](https://gradschoolstory.chkwon.net/yoonsup/first-research-subject/), [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §3, [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767).

다음: [Ch.2 — 문제 정의는 답보다 먼저 좁혀진다](./chapter_02_feynman_problem.md)
