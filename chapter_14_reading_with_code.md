# Ch.14 — 코드 동반 읽기

SLAM·CV 분야는 코드 공개가 기본값이다. arXiv 첫 페이지에 GitHub 링크가 박혀 있는 분야 표준인 만큼, *paper만 읽은 학생*과 *코드까지 본 학생*의 격차가 벌어진다. 같은 한 편이 두 학생에게 다른 깊이로 남는다.

ch08이 dense math를 어느 패스에 어디까지 펼치는가를 정했다면, 이 장은 그 옆에 한 층위를 더 둔다. paper가 못 잡은 디테일이 GitHub repo·issue tracker·PR comment에 자주 풀려 있는 만큼, 재구현 작정의 읽기는 paper만으로 끝낼 수 없다. paper는 *what*을 적고, GitHub은 *how*를 담는다.

---

## 14.1 paper와 repo의 거리

Keshav 3rd pass — virtual re-implementation — 은 paper만으로 끝낼 수 있는 작업이 아니다. paper §3 method가 *알고리즘의 골격*을 적는다면, 같은 알고리즘이 어떤 hyperparameter에서 안정적이고 어디서 무너지는가는 코드와 issue tracker 안에 놓여 있다.

학생이 자주 빠지는 함정은 paper만 읽고 *그게 전부*라고 결론을 내리는 결정이다. 한 편을 1st·2nd pass로 끝낸 후 GitHub repo를 한 번도 안 열고 다음 편으로 넘어가면, 그 한 편은 *abstract 수준*에서만 본인 안에 남는다. 6개월 후 자기 thesis에서 baseline으로 다시 그 한 편을 부르려는 시점에, 본인이 들고 있는 정보가 그 baseline을 돌리기에 부족하다.

분야 senior가 자기 블로그에 *해설형 자료*를 남기는 동기가 같은 결에 놓여 있다. 김기섭 교수의 SLAM 14편 블로그 — *FAST-LIO Fast 한 이유*·*Pose-graph SLAM Tutorial* 같은 형식 — 가 한 본보기다. paper만으로는 안 잡히는 *왜 이 코드가 이렇게 빠른가*를 issue·코드·본인 빌드 + paper 셋의 교차에서 풀어 적은 형식이다. 같은 결의 자료를 한 편에 두 시간 들여 합치는 작업이 senior의 층위로 굳었다.

---

## 14.2 코드 동반 사이클 — 4단계 일주일

한 편을 *재구현·실행* 단계까지 끌고 가는 사이클은 4단계다. 한 세션에 다 끝내려 들면 한 단계마다 막혀 다음 단계로 못 넘어간다. 한 편 = 일주일 분량의 작업이라는 관점이 깔려 있다.

**단계 1 — paper Keshav 1st·2nd pass (1-2시간).** GitHub은 아직 안 연다. 5 Cs 한 줄이 잡히고 abstract의 broad-narrow-broad가 통과하는지 확인한 후 다음 단계로 넘어간다. 이 단계에서 paper가 막히면 다음 단계는 미루는 편이 마찰이 적다.

**단계 2 — repo 둘러보기 (30분).** README·디렉토리 구조·entry script 위치를 한 번 훑는다. 이 단계의 출력은 *어디서 시작해서 어디로 가는가*의 한 줄 답이다. SLAM 코드라면 *"main에서 sequential하게 관점을 받아 odometry 모듈로 넘기고 mapping이 받아 keyframe을 뽑는다"* 같은 한 줄이 들어간다.

**단계 3 — 직접 빌드 + 한 번 돌려본다 (2-4시간).** docker 또는 native에서 빌드한다. 첫 build error에서 두 시간이 들어가는 일이 흔한데, 이는 *예상 작업이지 예외가 아니다*. CMake 버전·OpenCV 버전·CUDA 호환·ROS distribution이 어긋나는 지점이 build error의 본체이고, issue tracker에 *대부분의 함정*이 이미 올라와 있다.

**단계 4 — paper와 코드 1:1 대응 (2-4시간).** paper §3 method의 한 단락이 코드의 어느 함수에 있는가? 매핑 노트를 만든다. paper 안의 *수식 2*와 코드의 *line 47-83*이 짝지어지면 그 한 점이 본인 안에 박힌다. 다만 모든 단락·수식을 매핑하지 않는다. 단계 4의 매핑은 ch08 §2의 *결정적 한두 줄*이 코드에서 어디에 놓이는지 찾는 작업이고, 그 한두 점이 본인의 thesis가 돌아갈 좌표가 된다.

단계 1-4를 한 세션에 다 끝내려 들지 않는다. 한 편 = 일주일 분량의 작업이고, 분야 senior가 한 분야의 정전 repo *한 편*에 한 달을 쓰는 풍경이 흔한 이유가 같은 관점에 놓여 있다.

---

## 14.3 issue·PR을 *읽기 자료*로 본다

GitHub issue tracker는 *이 코드의 알려진 함정*의 저장소다. 본인이 build에서 막혔을 때 *대부분의 함정*은 issue에 이미 올라와 있다. 같은 자료가 *코드의 design 결정*까지 함께 담는다. *왜 이 모듈을 multi-thread로 안 했는가*가 issue 한 토론에서 한 단락으로 풀리는 일이 흔하다.

PR comment에는 paper에 없는 디테일이 들어간다. *왜 hyperparameter A를 0.05가 아니라 0.1로 바꿨는가*가 PR에서 한 줄로 풀려 있으면, paper §4 experiment의 한 줄 *"set α = 0.1"*보다 더 많은 정보를 던진다. paper가 실험 결과를 *적은* 글이라면, PR은 그 결과에 도달하기까지 들었던 시도 중 *살아남은 한 결정*을 적은 글이다.

issue·PR을 *읽기 자료*로 둔다. 막혔을 때 외에도 단계 4 매핑 작업의 한 축으로 둔다. 정독의 양식은 단순하다.

| 항목 | 출력 |
|---|---|
| 닫힌 issue 상위 5개 | 자주 막히는 함정 + 처방 |
| merge된 PR 상위 5개 | 결정적 design 변경 이유 |
| open issue 상위 3개 | 현재 알려진 한계 |

이 세 출력이 paper §6 limitation에 적힌 한 단락보다 더 정확한 *분야 쪽 논의의 한계*를 본인 안에 남긴다. paper의 limitation 섹션이 *저자가 인지한* 한계라면, issue tracker의 open issue는 *사용자가 부딪힌* 한계다.

---

## 14.4 분야 쪽 논의 — 정전 repo 1편이 우선

분야의 정전 repo가 robotics-practice ch20 § 20.6 *유용한 GitHub 저장소*에 정리되어 있다. SLAM 쪽이라면 ORB-SLAM3, FAST-LIO2, LIO-SAM, RTAB-Map이 머리에 놓이고, CV 쪽이라면 SAM, DINOv2, NeRF Studio, COLMAP가 같이 들어간다.

한 분야 신입의 권장 작업은 정전 repo *1-2편*을 4단계 사이클로 끝내고, 분야의 standard test dataset (KITTI·TUM·EuRoC)으로 trajectory를 비교하는 작업이다. robotics-practice ch20 § 20.7 *중급 마일스톤*과 같은 결이다. *"ORB-SLAM3를 직접 빌드하고 데이터셋으로 돌려서 trajectory를 ground truth와 비교할 수 있으면 중급 단계 졸업이다."*

신입이 자기 코드를 처음부터 짜기 전에, 정전 repo 1편을 끝까지 따라가는 작업이 우선이다. 분야 표준 셋업·디버깅 패턴·logging 양식이 그 한 편 안에 들어 있는 만큼, 이 한 편을 거친 후 자기 셋업을 만드는 학생과 거치지 않고 자기 셋업을 짠 학생의 5년 누적 격차가 벌어진다. 「대학원노트」 [Part 3 ch05 「도구 함정」](../grad-notes/chapter_11_tool_trap.md)의 *작게 시작하라* 관점과 같은 결이다. 처음부터 자기 코드를 모두 짜려 들지 않고, 한 편을 끝까지 따라간 후 *어디를 바꿀지*를 결정하는 순서다.

---

## 14.5 AI 보조 도구 — 코드 동반 읽기의 가속

paper와 코드의 1:1 매핑은 AI에 잘 위임된다. *"이 paper의 'we apply pre-integration on IMU measurements between keyframes' 줄이 코드의 어느 함수에 있는지 찾아줘"* 같은 질문을 던지면, AI가 후보 함수 2-3개를 짚어 준다. 본인이 그 후보를 검증하면, 본인이 코드를 처음부터 grep하던 한 시간이 줄어든다.

PR comment의 분야 표현 직역이 막혔을 때도 AI가 한 번에 풀어 준다. PR comment의 영어가 분야 jargon이 dense하고 informal한 톤이 섞여 있어, 본인이 한 단락을 다섯 번 읽고도 안 잡힐 때가 있다. AI에 *"이 PR comment의 핵심 결정 + 그 이유를 한 단락으로 풀어 줘"*를 던지면, 본인이 그 결정의 위치를 한 번에 잡는다.

AI가 만든 *paper-코드 매핑*을 본인이 한 번 더 검증한다. line 번호가 hallucinate되는 일이 흔하고, AI가 *비슷해 보이는* 함수를 짚지만 실제로는 다른 함수인 일도 흔하다. 검증 없이 매핑을 노트에 박아두면, 6개월 후 본인의 thesis에서 잘못된 line 번호로 자기 작업이 무너진다.

분야 쪽 논의에서 같은 관점이 참조로 한 번 더 들어간다.

> 코드 작성 도구가 널리 쓰이는 지금도, 만 줄짜리 문서를 읽고 맥락을 파악하는 일은 사람에게 남아 있다. 잘 읽는 사람이 도구도 잘 다룬다.
>
> — robotics-practice ch22 § 22.5

paper-코드 매핑이 *사람이 읽고 결정해야 하는 작업*인 본질이 같은 곳을 가리킨다. 코드는 AI가 짜고, 그 코드와 paper가 *어떻게 짝지어지는가*의 결정은 본인이 들어간다. 그 결정의 누적이 5년 후 본인의 분야 senior 위치를 만든다.

---

**출처.** [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.3 (3rd pass · virtual re-implementation), robotics-practice ch20 § 20.4 (필독 논문 리스트)·§ 20.6 (유용한 GitHub 저장소)·§ 20.7 (중급 마일스톤)·ch22 § 22.5 (AI 시대 참조). [김기섭 교수 SLAM 14편 블로그](https://gisbi-kim.github.io/) — 분야 정독+구현 사례. 「대학원노트」 [Part 3 ch05 (도구 함정)](../grad-notes/chapter_11_tool_trap.md) — *작게 시작하라* 관점 연결. 4단계 사이클, issue·PR 정독 자세, AI 보조 도구 정책은 이 장에서 정리했다.

다음: [Ch.10 — 노트와 인용 관리](./chapter_15_notes_and_citations.md)
