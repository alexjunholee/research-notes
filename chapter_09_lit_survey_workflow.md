# Ch.9 — Literature Survey Workflow: 논문 입력 시스템

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) 3-pass는 한 편이 손에 들어왔을 때 무엇을 하는가의 규약이다. 그런데 본인이 한 주에 다섯 편을 정독한다고 해도, 그 다섯 편이 어디서 흘러 들어오는가는 별개의 작업으로 남는다. ch01에서 다룬 안 읽을 25편 표시가 triage라면, 이 장은 그 25편이 어떤 입력 시스템에서 올라오는가를 본다.

여기서 자주 어긋나는 결정이 있다. 입력원을 늘리는 일과 판단 시간을 정하는 일을 분리하는 결정이다. alert, paper graph, lab page, OpenReview, 학회 program, SNS를 모두 켜 놓으면 입력은 늘어나지만 판단은 흐려진다. 2026년의 문제는 후보 과잉이다. 입력 시스템의 목적은 이번 주에 직접 읽을 3-5편을 남기고 나머지를 내려놓는 일이다.

---

## 9.1 입력 4종 — 무엇을 켜고 무엇을 닫는가

분야 senior가 실제로 운영하는 입력은 네 묶음 안에 들어간다. 각 입력이 들어오는 것과 비용이 다른 만큼, 네 묶음을 모두 같은 강도로 보는 결정은 잘못된 결정이다.

**입력 1 — paper graph와 alert.** Google Scholar·Semantic Scholar·OpenAlex·arXiv·Connected Papers류 도구가 담당하는 층위다. 이 입력은 후보를 넓게 잡는 데 강하지만 노이즈도 크다. 매일 열지 말고 weekly brief의 재료로 둔다.

**입력 2 — 신뢰 그룹·저자·랩 페이지.** ch01에서 정한 신뢰 prior가 있는 그룹·저자의 신작을 받는다. cold start 그룹을 많이 follow하면 alert가 다시 잡음으로 바뀐다. 신뢰는 alert가 만들어 주지 않는다. 신뢰가 쌓인 뒤에 alert를 거는 편이 맞다.

**입력 3 — venue와 심사 surface.** 학회 proceedings, OpenReview thread, accepted 논문 list, 워크숍 page, tutorial page가 여기에 들어간다. 여기서는 어떤 논문이 어느 자리에서 논쟁됐는가가 보인다. 답변서와 심사위원 토의가 공개된 venue에서는 초록보다 심사 thread가 더 빠른 triage 신호가 되기도 한다.

**입력 4 — 해설과 큐레이션.** 분야 senior blog, 연구실 note, tutorial slide, newsletter, 긴 form의 해설 글이다. 들어오는 것은 왜 이 논문이 중요한가의 해석이다. 논문이 못 잡은 디테일이 senior의 blog에 풀려 있는 사례가 많은 만큼, 본 형식의 정독+구현 사이클은 [Ch.14](./chapter_14_reading_with_code.md)에서 자세히 다룬다.

SNS는 별도 입력 시스템으로 세지 않는다. 좋은 신호가 들어오기도 하지만 휘발성이 강하고, 클릭하는 순간 다른 것까지 같이 끌고 온다. 학회 주간에만 켜거나, 이미 신뢰하는 사람의 thread를 나중에 확인하는 정도면 충분하다.

본인 시간 예산이 주 1.5시간이라면 입력 1·2만 켠다. 시간이 늘어나면 입력 3·4가 따라붙는다. 입력 수가 본인 시간을 역으로 결정하지 않도록 두는 것이 핵심이다.

---

## 9.2 AI weekly brief — 자동화의 기본 단위

입력원을 골랐으면 한 weekly brief로 묶는다. 직접 수집 파이프라인을 짜는 일은 이제 기본값이 아니다. 이미 있는 alert와 paper graph export를 가져오고, 필요한 경우에만 작은 스크립트나 agent를 붙인다. 핵심은 질문 양식이다.

weekly brief가 답해야 할 질문은 정해져 있다.

| 질문 | 출력 |
|---|---|
| 이번 주 내 thesis와 가장 가까운 후보는 무엇인가 | 후보 5-10편 |
| 왜 가까운가 | thesis keyword와 연결되는 한 줄 |
| 어디를 확인해야 하는가 | abstract·figure·table·OpenReview 위치 |
| 무엇을 안 읽을 것인가 | 제외 후보와 제외 이유 |

AI에는 metadata와 초록에 더해 source URL, project page, 코드 link, OpenReview link가 있으면 같이 넣는다. 그러고 나서 "후보를 고르되 각 후보마다 근거 위치를 붙이고, 근거가 없으면 없음이라고 표시하라"고 묻는다. 한 시간짜리 weekly 블록은 AI가 올린 후보와 제외 사유를 검증하는 시간으로 바뀐다.

AI 선별 결과를 읽었다고 착각하지 않는다. 0차 후보 선별과 근거 위치 후보까지가 AI의 몫이고, 1st pass는 본인이 들어간다. AI가 만든 5 Cs를 그대로 노트에 박아두면, 6개월 후 본인의 노트가 본인이 통과한 자료가 아닌 AI가 통과한 자료의 누적이 된다. 노트에 남길 것은 본인이 확인한 근거 위치와 다음 결정이다.

---

## 9.3 core paper set이 먼저 — 신간은 그 위에 놓인다

입력 시스템은 신간만 다루지 않는다. 분야의 고전 5-10편을 본인 안에 박아두지 않으면, 신간이 어떤 흐름 위에 놓이는지 안 잡힌다. 그래서 신입 1년차의 권장 작업은 core paper 1편을 정독하는 것 쪽으로 기운다.

분야 쪽 논의의 정전 리스트는 robotics-practice ch20 § 20.4 필독 논문 리스트에 정리되어 있다. SLAM 쪽이라면 ORB-SLAM, LOAM, VINS-Mono, FAST-LIO2가 리스트의 머리에 놓인다. CV 쪽이라면 ResNet, Transformer, ViT가 같이 묶인다. 신간이 들어왔을 때 첫 작업은 이 논문이 우리 분야의 어느 고전 위에 놓이는가를 한 줄로 적어 보는 것이고, 그 한 줄이 적히지 않으면 core paper set이 아직 본인 안에 안 박혔다는 신호다.

신입의 우선순위는 core paper 1편 정독이다. 입력 시스템은 core paper가 박힌 후에 본격 가동된다. core paper가 비어 있는 상태에서 신간 30편을 읽으면 30편이 각각 따로 남는 한편, core paper가 박힌 후의 신간 5편은 한 흐름 위에 묶여 들어간다.

---

## 9.4 weekly digest 운영 — 정해진 시간에만 본다

입력원을 골랐고 weekly brief도 만들었고 core paper도 박혔으면, 남은 결정은 언제 보는가다. 매일 보는 결정은 잘못된 결정이다. 매일 보면 집중력이 거기서 닳고, 본인이 정독에 쓸 두 시간이 알림으로 흩어진다. 권장 운영은 주 1회 1-2시간 블록 쪽으로 잡힌다.

이 블록의 출력은 정해져 있다.

| 항목 | 내용 |
|---|---|
| 후보 5편 | 그 주의 1st pass 후보 |
| 각 5 Cs 한 줄 | category·context·correctness·contribution·clarity (ch03 양식) |
| 근거 위치 | abstract·figure·table·review thread 중 확인한 자리 |
| 결정 게이트 | 중단 / 보류 / 진행 (ch01 §2의 네 신호 적용) |
| 보류 큐 | 다시 돌아올 시점 함께 |

이 출력이 본인의 노트 시스템(ch10에서 자세히)에 그대로 흘러 들어간다. weekly 블록 끝에 5편의 한 줄짜리 5 Cs와 근거 위치가 노트에 박히면, 한 달이 지난 시점에서 20편의 검증된 노트가 본인 안에 누적된다.

분야 쪽 논의에서 같은 관점이 한 번 더 짚인다.

> 코드 작성 도구가 널리 쓰이는 지금도, 만 줄짜리 문서를 읽고 맥락을 파악하는 일은 사람에게 남아 있다. 잘 읽는 사람이 도구도 잘 다룬다.
>
> — robotics-practice ch22 § 22.5

자동화가 논문을 대신 읽어 주지는 않는다. 입력 시스템이 매일 흘러도, weekly 블록에서 어느 논문을 직접 읽을지 고르는 결정은 여전히 본인 몫이다. 그 결정이 본인의 thesis가 놓일 곳을 정한다.

---

**출처.** [김기섭 교수 「arXiv 최신논문 트래킹 자동화」](https://gsk1m.github.io/productivity/2023/03/18/arxiv-searcher-automation.html) (2023.03), [김기섭 교수 「Robotics 최신 학계 소식 받아보기」](https://gsk1m.github.io/productivity/2023/02/28/robotics-worldwide.html) (2023.02), [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §1, robotics-practice ch20 § 20.4 (필독 논문 리스트, 분야 쪽 논의)·ch22 § 22.5 (AI 시대 참조). paper graph 기반 입력, weekly brief 운영, AI를 이용한 0차 선별과 근거 위치 검증은 이 장에서 정리했다.

다음: [Ch.5 — Reviewer로 읽기](./chapter_10_reading_for_review.md)
