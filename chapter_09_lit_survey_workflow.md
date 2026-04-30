# Ch.9 — Literature Survey Workflow: 논문 input pipeline

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) 3-pass는 *한 편이 손에 들어왔을 때* 무엇을 하는가의 규약이다. 그런데 본인이 한 주에 다섯 편을 정독한다고 해도, 그 다섯 편이 *어디서 흘러 들어오는가*는 별개의 작업으로 남는다. ch01에서 다룬 *안 읽을 25편 표시*가 triage라면, 본 챕터는 그 25편이 *어느 채널로 들어오는가*를 본다.

여기서 자주 어긋나는 결정이 있다. 본인이 input 채널을 *늘리는* 작업과 *볼 시간을 정하는* 작업을 한 쌍으로 묶지 않는 결정이다. 채널만 늘리고 시간을 정하지 않으면, 매일 RSS와 X를 들여다보다 그날의 집중력이 한 시간 안에 닳는다. [김기섭 교수](https://gsk1m.github.io/)가 「arXiv 최신논문 트래킹 자동화」(2023.03)에서 적은 한 줄이 같은 곳을 짚는다.

> *"매일 내가 직접 `python3 arxiv_saver_to_db.py` 하고 다시 commit 하고 … 이 과정을 수행하는 것은 피곤하다."*

manual 채널 점검의 비용을 인정한 한 줄이다. 자동화도 자동화지만, 자동화 위에 *볼 시간을 정한 운영*이 함께 얹혀야 input pipeline이 닳지 않는다.

---

## 9.1 5 채널 — 무엇을 켜고 무엇을 닫는가

분야 senior가 실제로 운영하는 input 채널은 다섯 묶음 안에 들어간다. 각 채널이 들어오는 *것*과 *비용*이 다른 만큼, 다섯을 모두 켜는 결정은 잘못된 결정이다.

**채널 1 — arXiv RSS feed.** cs.RO, cs.CV, eess.SP 카테고리에서 매일 100-300편의 metadata가 흘러 들어온다. 폭주의 본체이자 가장 노이즈가 큰 채널이다. 매일 보면 거기서 집중력이 닳는 만큼, 주 1회 1-2시간 블록으로 묶어 본다. 김기섭 교수가 자기 통계를 적은 줄에 따르면, 이 블록의 실제 트래픽은 *50-100 title 훑고, ~10 abstract 보고, 1-2편 정독*에 가깝다.

**채널 2 — Mailing list.** robotics-worldwide·dbworld·ml-news 같은 분야 큐레이션 메일링이다. 들어오는 것은 논문 자체가 아니라 *학계 환경 정보* — CFP, workshop 공지, 잡 공고, 세미나, tutorial 녹화, 학회지 신간 쪽이다. 김기섭 교수가 「Robotics 최신 학계 소식 받아보기」(2023.02)에서 적은 한 줄이 이 채널의 역할을 정한다.

> *"최신 학계소식 + 논문들에 대한 팔로업follow-up 하는 것은 중요하다."*

논문 input과 *학계 환경 input*이 한 채널 안에 같이 흐른다. 별도 메일 폴더로 분리해 weekly 30분 블록에 처리하는 운영이 자주 권장된다.

**채널 3 — 신뢰 그룹·저자 alert.** Google Scholar alerts와 Semantic Scholar Research Feed가 같은 일을 한다. ch01에서 정한 *신뢰 prior*가 있는 그룹·저자의 신작을 받아 1st pass 우선권을 둔다. cold start 그룹은 alert을 걸지 않는 편이 마찰이 적다. alert은 후보를 늘리는 도구지, 신뢰를 만들어 주는 도구는 아니다.

**채널 4 — Blog·RSS.** 분야 senior 블로그를 Feedly·Inoreader 같은 reader에 묶는다. 들어오는 것은 한 편의 *해설*과 *분야 흐름 정리* 쪽이다. 김기섭 교수의 SLAM 14편 블로그 — *FAST-LIO Fast 한 이유*·*Pose-graph SLAM Tutorial* 같은 형식 — 가 분야 layer의 본보기에 가깝다. paper가 못 잡은 디테일이 senior의 blog에 풀려 있는 사례가 많은 만큼, 본 형식의 정독+구현 사이클은 ch09에서 자세히 다룬다.

**채널 5 — Twitter/X + 학회 hashtag.** arXiv 직후 분야 senior가 한 줄 반응을 적는 통로다. 논문 자체보다 빠른 평가 신호가 들어오는 한편, 가장 끊기 어려운 채널이기도 하다. 본인 의지로 통제가 안 되면 그 자리에서 닫는 편이 마찰이 적다. 켜둔다면 학회 주간 한정 + 신뢰 follow 30명 이내가 안전한 운영이다.

🟡 5 채널을 *고르는* 작업이 input pipeline의 본체다. 본인 시간 예산이 주 1.5시간이라면, 채널 1·3을 켜고 나머지는 닫는다. 시간이 늘어나면 채널 2·4가 따라붙고, 채널 5는 마지막이다. 채널 수가 본인 시간을 *역으로* 결정하지 않도록 두는 것이 핵심이다.

---

## 9.2 자동화 — RSS 파이프라인 + AI 보조 layer

채널을 골랐으면 자동화한다. 김기섭 교수가 같은 자동화 글에서 푼 사례 — RSS → SQLite → GitHub Actions cron → FastAPI → Streamlit — 가 한 본보기다. RSS reader가 *시간순*으로만 보여 주는 자료를 keyword·저자·연도로 cross-cut 검색 가능한 DB로 옮겨 둔 작업이다. 이 자동화의 진입 장벽이 한 줄로 풀리는 대목도 같은 글 안에 놓여 있다.

> *"대충 이렇게 저렇게 하고 싶어 라고 설명하니까 ChatGPT가 만들어주었다."*

이 한 줄이 자동화의 시점을 정한다. 분야 senior가 손으로 짜던 시기에서, 본인이 *대충 설명한* 결과를 ChatGPT가 받는 시기로 넘어왔다. 자동화 자체는 본인 코딩 능력보다 *원하는 워크플로우의 명확성*에 더 기대게 된다.

자동화 위에 한 layer가 더 얹힌다. 매일 들어오는 metadata에 abstract를 첨부해 AI에 던지고 *"내 키워드와 관련된 후보 5편을 골라줘"*를 묻는 패턴이다. 1st pass 전의 0차 triage가 거기서 만들어진다. 한 시간짜리 weekly 블록이 본인이 직접 5편을 *고르는 시간*에서 *고른 결과를 검증하는 시간*으로 옮겨간다.

🔴 AI 요약을 *읽었다*고 착각하지 않는다. 0차 triage 후보 선별까지가 AI의 몫이고, 1st pass는 본인이 들어간다. AI가 만든 5 Cs를 그대로 노트에 박아두면, 6개월 후 본인의 노트가 본인이 통과한 자료가 아닌 AI가 통과한 자료의 누적이 된다.

---

## 9.3 core paper set이 *먼저* — 신간은 그 위에 놓인다

input pipeline은 *신간*만 다루지 않는다. 분야의 *고전 5-10편*을 본인 안에 박아두지 않으면, 신간이 어떤 흐름 위에 놓이는지 안 잡힌다. 그래서 신입 1년차의 권장 작업은 *신간 채널 5개를 켜는 것*보다 *core paper 1편을 정독하는 것* 쪽으로 기운다.

분야 layer의 정전 리스트는 robotics-practice ch20 § 20.4 *필독 논문 리스트*에 정리되어 있다. SLAM 쪽이라면 ORB-SLAM, LOAM, VINS-Mono, FAST-LIO2가 리스트의 머리에 놓인다. CV 쪽이라면 ResNet, Transformer, ViT가 같이 묶인다. 신간이 들어왔을 때 첫 작업은 *이 논문이 우리 분야의 어느 고전 위에 놓이는가*를 한 줄로 적어 보는 것이고, 그 한 줄이 적히지 않으면 core paper set이 아직 본인 안에 안 박혔다는 신호다.

🟡 신입은 *신간 5채널*보다 *core paper 1편 정독*이 우선이다. input pipeline은 core paper가 박힌 *후*에 본격 가동된다. core paper가 비어 있는 상태에서 신간 30편을 읽으면 30편이 각각 따로 남는 한편, core paper가 박힌 후의 신간 5편은 한 흐름 위에 묶여 들어간다.

---

## 9.4 weekly digest 운영 — 정해진 시간에만 본다

채널을 골랐고 자동화도 했고 core paper도 박혔으면, 남은 결정은 *언제 보는가*다. 매일 보는 결정은 잘못된 결정이다. 매일 보면 집중력이 거기서 닳고, 본인이 정독에 쓸 두 시간이 RSS feed로 흩어진다. 권장 운영은 주 1회 1-2시간 블록 쪽으로 잡힌다.

이 블록의 출력은 정해져 있다.

| 항목 | 내용 |
|---|---|
| 후보 5편 | 그 주의 1st pass 후보 |
| 각 5 Cs 한 줄 | category·context·correctness·contribution·clarity (ch03 양식) |
| 결정 게이트 | stop / defer / proceed (ch01 §2의 네 신호 적용) |
| defer 큐 | 다시 돌아올 시점 함께 |

이 출력이 본인의 노트 시스템(ch10에서 자세히)에 그대로 흘러 들어간다. weekly 블록 끝에 5편의 한 줄짜리 5 Cs가 노트에 박히면, 한 달이 지난 시점에서 20편의 한 줄짜리 노트가 본인 안에 누적된다.

분야 layer에서 같은 frame이 한 번 더 짚인다.

> "에이전트가 코드를 짜 주는 시대지만, 만 줄짜리 문서를 읽고 맥락을 파악하는 건 아직 사람의 일이다. 잘 읽는 사람이 AI도 잘 부린다."
>
> — robotics-practice ch22 § 22.5

읽기의 비용이 줄었다기보다, 오히려 *읽기의 가치*가 더 정확히 드러난다. input pipeline이 매일 자동으로 흘러도, 본인이 weekly 블록에서 *고르는 결정*은 위임되지 않는다. 그 결정이 본인의 thesis가 놓일 곳을 정한다.

---

**출처.** [김기섭 교수 「arXiv 최신논문 트래킹 자동화」](https://gsk1m.github.io/productivity/2023/03/18/arxiv-searcher-automation.html) (2023.03), [김기섭 교수 「Robotics 최신 학계 소식 받아보기」](https://gsk1m.github.io/productivity/2023/02/28/robotics-worldwide.html) (2023.02), [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §1, robotics-practice ch20 § 20.4 (필독 논문 리스트, 분야 layer)·ch22 § 22.5 (AI 시대 cameo). 5 채널 분류, weekly digest 운영, AI 0차 triage layer는 자체.

다음: [Ch.5 — Reviewer로 읽기](./chapter_10_reading_for_review.md)
