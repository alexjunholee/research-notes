# Ch.4 — 연구와 작업을 구분하는 법

[Ch.3 (주도권의 이동)](./chapter_03_ownership_shift.md)에서 화법·작업 단위가 학생 쪽으로 기울고 나면 책상 위의 작업을 내 작업이라 부를 수 있는 단계가 온다. 그 다음 막힘은 모양이 또 다르다. 매일 코드를 짜고, system을 tuning하고, 새로운 dataset을 돌려도, 그 작업이 연구인지 task인지의 감각이 흐릿하게 남는 단계다. 손에 들어온 작업이 의미를 가지려면 그 작업이 새 지식을 만드는지 아닌지를 진단할 도구가 필요하다.

이 장은 그 진단의 두 도구를 겹쳐 쓴다. 정글 탐험가 비유가 직관 표현이고, 네 가지 연구 유형이 추상 분류다. 두 표현을 같이 두고 자기 작업을 가져다 댄다. [Ch.2 (문제 정의)](./chapter_02_feynman_problem.md)에서 좁힌 problem statement가 그 두 도구를 통과하는 시점이 이 장의 입력이다.

---

## 4.1 작업 vs 연구: task / objective / goal

[권창현 교수](https://gradschoolstory.chkwon.net/changhyun/%ec%a7%80%ea%b8%88-%ed%95%98%ea%b3%a0-%ec%9e%88%eb%8a%94-%ea%b2%8c-%ec%97%b0%ea%b5%ac%ec%9d%b8%ea%b0%80-%ec%95%84%eb%8b%8c%ea%b0%80/)는 「지금 하고 있는 게 연구인가, 아닌가?」에서 학생의 시간 단위를 세 층으로 잘랐다. **task**는 오늘 한 일이다. 코드 한 줄, 실험 한 회, figure 한 컷이 task다. **objective**는 지금 쓰고 있는 한 논문에서 보일 것이다. "이 논문에서 BEV feature가 night-time loop closure에 효과적임을 보인다"가 objective다. **goal**은 분야 전체가 풀려는 큰 질문이다. "long-term autonomy를 어떻게 달성할 것인가"가 goal이다.

학생이 시간을 쓰는 곳은 task다. 학생이 정해야 하는 곳은 objective이고, 학생이 바라보는 곳은 goal이다. 세 층은 위계를 이룬다. task만 쌓이고 objective가 비어 있으면 1년치 작업이 한 편의 논문으로 묶이지 않는다. objective는 있으나 goal과 연결이 흐릿하면 그 논문이 분야에 왜 필요한지가 답이 안 된다.

"개발", "설계", "최적화", "제어" 같은 동사는 task로는 가능하지만 자동으로 objective·goal로 올라가지 않는다. SLAM system을 개발하는 일과 SLAM의 어떤 명제를 검증하는 일은 다르다. 전자는 engineering achievement이고 후자는 research contribution이다. 둘은 venue도, reviewer가 묻는 질문도, 졸업 심사에서 받는 평가도 다르다.

> **task ≠ objective ≠ goal.** 세 층의 구분이 흐릿한 채로 작업을 쌓으면 그 작업이 연구인지 task인지 진단되지 않는다.

---

## 4.2 정글 탐험가 비유

§1의 세 층 구분은 추상적이다. 같은 명제를 직관 한 줄로 압축한 비유가 있다. [최윤섭 박사](https://gradschoolstory.chkwon.net/yoonsup/what-phd-means/)가 「박사 학위의 의미」에서 적은 정글 탐험가 비유다.

> 교과서는 이미 탐사된 영역의 지도, 박사는 그 끝을 넘어 자기 손으로 지도를 새로 그리는 과정.

비유에서 중요한 장면은 지도의 끝이다. 지도의 안쪽은 이미 누군가가 그려 둔 영역이고, 그 바깥은 본인이 한 걸음씩 확인해야 하는 영역이다. 박사 학위는 지도를 전부 외웠다는 인증이 아니라, 지도의 경계 밖에서 계속 그릴 준비가 되었다는 인증에 가깝다.

비유의 핵심은 지도의 끝에 있다. 끝 안쪽은 누군가 이미 그렸고, 누구나 들여다볼 수 있다. 그 영역에서 작업을 잘 하는 일은 가치 있는 task다. 다만 지도를 새로 그리는 일은 아니다. 새 지식은 끝 바깥에서만 만들어진다. 한 발짝의 크기는 작아도 된다. 지도에 안 적힌 곳이라는 조건만 만족하면 된다.

연구라 부를 수 있는 작업은 모두 이 한 발짝의 변형이다. 다만 한 발짝을 어떤 방향으로 디디는지가 분류된다. Hazelrigg의 4-type이 그 방향의 분류이고, §1의 시간 층위(task/objective/goal)와 직교하는 내용 층위다. 두 층위를 같이 든 채 다음 섹션에서 진단을 진행한다.

---

## 4.3 새 지식의 네 가지 형태

§1의 task/objective/goal이 시간 층위의 분류 — 오늘 / 이번 논문 / 분야 전체 — 였다면, Hazelrigg 4-type은 내용 층위의 분류다. objective 슬롯에 들어간 한 contribution이 어떤 종류의 새 지식을 만드는가를 묻는다. 두 분류는 직교 축이고, 이 장은 두 축을 같이 든 채로 진단을 진행한다.

NSF의 George Hazelrigg가 On the Role and Use of Mathematical Models in Engineering Design에서 제시한 4-type은 한 한국어 paragraph로 옮길 수 있다. 연구는 새로운 지식을 만들어내는 활동이고, 그 활동이 만드는 지식의 종류는 네 가지다. 명제가 옳은지 그른지를 데이터로 결정하는 가설 검정, 현상의 정량적 성질을 데이터로 결정하는 측정, 명제가 옳다는 것을 논리로 결정하는 추측 증명, 다른 분야의 도구·관점을 본 분야 문제에 적용하는 학제간 융합. 새 지식을 만들지 않는 작업은 이 네 칸 어디에도 들어가지 않는다.

네 칸을 분리해서 본다.

- **가설 검정 (hypothesis testing).** 명제가 옳은지 그른지를 데이터로 결정하는 작업이다. 명제가 미리 적혀 있고, 그 명제가 참이라면 어떤 데이터가 보일지가 미리 그려져 있고, 실험은 그 그림과 실제 데이터를 비교한다. "BEV feature가 night-time loop closure에 효과적이다"가 가설의 한 예다.
- **측정 (measurement).** 현상의 정량적 성질을 데이터로 결정하는 작업이다. 가설은 어느 쪽이 옳은가를 묻지만 측정은 얼마인가를 묻는다. "KITTI-360에서 6개 SLAM system의 RTE (relative translation error) 분포는 어떻게 생겼는가"가 측정의 한 예다.
- **추측 증명 (proof of conjecture).** 명제가 옳다는 것을 논리로 결정하는 작업이다. 데이터가 아니라 증명이 결정의 도구다. "SLAM의 핵심 최적화 절차인 Bundle Adjustment의 수렴이 outlier ratio < 30%에서 보장된다"가 증명의 한 예다.
- **학제간 융합 (interdisciplinary transfer).** 다른 분야의 도구·관점을 본 분야 문제에 적용하는 작업이다. 도구의 출처와 적용 대상이 분야 경계를 넘는다. "communication theory의 codebook 학습을 visual descriptor 설계에 적용한다"가 한 예다.

자기 작업을 네 칸에 가져다 대 본다. 어디에도 안 들어가면 그 작업은 task일 가능성이 높다. 한 칸에 들어가면 그게 곧 contribution claim의 type이다. 다만 두 칸에 동시에 들어가면 다음 섹션에서 볼 봉합 문제가 발생한다.

---

## 4.4 single contribution과의 봉합

Hazelrigg 4-type이 작업의 종류를 묻는다면, [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) Rule 1은 한 논문에 몇 개의 작업이 들어가는가를 답한다.

> Focus your paper on a central contribution, which you communicate in the title.

한 논문 = 한 contribution이다. 두 contribution을 한 논문에 욱여넣으면 둘 모두에 대한 설득력이 떨어지고, 독자는 1년 뒤 그 논문을 한 줄로 요약하지 못한다. Mensh-Kording의 표현을 빌리면 greedy paper다.

이 두 framework를 봉합하면 paper-level scoping의 첫 질문이 한 줄로 정리된다. 이 한 논문의 한 contribution은 4-type 중 어디에 해당하는가. 이 질문에 한 칸으로 답이 안 나오면 보통 둘 중 하나다. (1) 작업이 4-type 어디에도 안 들어간다. engineering achievement일 가능성이 높고 venue 선택이 다르다. (2) 두 type이 동시에 들어 있다. Rule 1을 깬 것이고, 한 논문을 두 편으로 분리하거나 한 type을 다음 논문으로 미뤄야 한다.

> **한 논문 = 한 contribution = 한 type.** 4-type 중 어디에 해당하는지 한 칸으로 답이 안 나오면 paper-level scoping이 안 된 상태다.

---

## 4.5 로보틱스/CV에서의 4-type

진단 도구는 추상 분류만으로는 손에 잘 잡히지 않는다. 자기 분야의 사례에 한 번 가져다 대 보면 분류의 칸이 비로소 구체화된다. 로보틱스/CV의 흔한 작업을 네 칸에 한 사례씩 박는다.

가설 검정. "BEV feature pyramid는 night-time loop closure recall을 raw image보다 높인다"는 한 줄짜리 명제가 있다. 명제가 참이라면 night benchmark에서 BEV-feature 기반 retrieval의 recall@1이 image-feature baseline보다 통계적으로 유의하게 높을 것이라는 그림을 미리 그린다. 실험은 그 그림과 실제 측정을 비교한다. ICRA·IROS의 method paper 다수가 여기 들어간다.

측정. "KITTI-360, MulRan, Boreas 세 dataset에서 LIO-SAM·KISS-ICP·SuMa 세 system의 RTE 분포는 어떻게 다른가"는 명제가 아니라 정량 질문이다. 결정해야 하는 답은 옳은가/그른가가 아니라 얼마인가, 어떤 분포인가다. T-RO·IJRR의 benchmark·survey paper, 그리고 일부 dataset paper가 여기 들어간다.

추측 증명. "outlier ratio가 30% 미만일 때 graduated non-convexity가 global optimum으로 수렴한다"는 명제는 데이터로 결정할 작업이 아니다. 가정과 정리의 형태로 적히고, 증명이 결정의 도구가 된다. T-RO, IJRR의 일부 theoretical paper, 그리고 control·optimization 쪽 논문이 여기 들어간다. 다만 한국 lab에서는 빈도가 낮다.

학제간 융합. "communication theory의 vector quantization codebook 학습 절차를 visual place recognition descriptor에 적용한다"는 작업은 도구의 출처가 다른 분야이고 적용 대상이 본 분야다. 융합은 단순 적용으로 끝나지 않고 적용 과정에서 새로운 문제 정의를 동반하는 경우가 많다. CVPR의 cross-domain paper, ICRA의 learning-based perception paper 일부가 여기 들어간다.

분야 단면을 한 줄로 적는다. 한국 robotics lab은 가설 검정과 학제간 융합 빈도가 높고 측정과 증명 빈도가 낮다. venue로 옮기면 ICRA·IROS·CVPR은 type 1·4 우세, T-RO·IJRR은 type 2·3 비중이 높다. 한 lab이 type 1·4에만 몰리면 venue 선택의 자유도가 좁아진다.

> type 다양화는 venue 선택의 자유도를 늘린다. type 2·3 작업을 한 번씩이라도 시도해 두면 졸업까지의 publication 분포가 균형을 잡는다.

---

## 4.6 superlative 회피와 claim 정량화

[Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 rule 12가 4-type 진단의 마지막 점검 도구다.

> When describing your own work, be humble and don't use superlatives of praise, even if you are enthusiastic.

자기 작업을 설명할 때 "best", "novel", "state-of-the-art" 같은 최상급은 거의 항상 claim의 정량화 부족 신호다. 비교가 무엇 대비 무엇인지가 빠져 있고, 어떤 metric에서 얼마만큼 좋은지가 빠져 있다. 같은 작업을 정량화된 형태로 다시 적으면 superlative가 자연스럽게 사라진다. "novel SLAM system"보다 "frame-to-frame matching에서 RANSAC inlier ratio를 X% → Y%로 올린 SLAM system"이 정직하고 검증 가능하다.

같은 점검을 4-type 목록으로 다시 한 번 한다. "robotic system을 개선했다"는 claim은 4-type 어디에도 안 들어갈 가능성이 있다. 어떤 가설이 검정됐는가, 무엇이 측정됐는가, 무엇이 증명됐는가, 어떤 분야의 도구가 옮겨졌는가. 네 질문 중 하나에 답이 안 나오면 그 claim은 task의 보고이지 contribution claim이 아니다. 4-type 목록이 superlative 점검과 같은 방향에서 작동한다. 둘 다 claim을 정량화 가능한 형태로 끌어내리는 도구다.

> "best", "novel", "state-of-the-art"가 자기 abstract에 보이면 그 표현을 4-type 목록으로 다시 검사한다. 어느 칸에 들어가는지 정확히 짚이면 superlative 자리에 정량화된 비교가 들어온다.

같은 목록이 [Part 3 ch02 (Introduction)](./chapter_23_introduction.md)에서 contribution claim 작성 단계의 자기 점검 도구로 다시 등장한다. 진단의 도구가 작성의 도구로 그대로 이어진다.

---

진단의 끝에 마음의 짐이 하나 남는다. 4-type 어디에 들어가는지 매번 즉답할 수 있는 학생은 거의 없다는 사실이다. 같은 곳에서 권창현 교수가 인용한 아인슈타인의 한 줄이 위안이 된다.

> 우리도 우리가 뭐하는지 잘 모르잖아요. 알면 연구 아니잖아요.

자기 작업이 어느 type인지 흐릿한 채로 한 학기가 지나가는 일은 정상이다. 흐릿한 채로 한 발짝씩 디디면서 type이 점차 또렷해지는 게 정상의 모양이다. 다만 흐림과 막힘은 다르다. type을 전혀 묻지 않은 채로 1년이 지나가면 그 1년의 작업이 task의 더미로 끝날 위험이 있다. 한 달에 한 번이라도 자기 작업을 4-type 목록과 정글 비유에 가져다 대는 습관이 그 위험을 막는다.

같은 정글 비유가 「대학원노트」 Part 1 ch01 「박사를 결정한다는 일」에서는 진학을 결정하는 단서로 쓰인다. 이 장은 같은 비유를 현재 작업을 진단하는 단서로 가져왔다. 같은 비유가 두 층위에 적용된다.

작업이 4-type 중 한 칸에 들어간다는 진단이 끝나도 그 작업이 언제 어떻게 진행되는가는 별개의 질문이다. 다음 챕터는 type이 분류된 작업이 생각의 시간에 들어가 있는지, 책상 점유 시간에만 머물고 있는지를 가른다.

---

**출처.** [권창현 교수 G8 「지금 연구인가」](https://gradschoolstory.chkwon.net/changhyun/%ec%a7%80%ea%b8%88-%ed%95%98%ea%b3%a0-%ec%9e%88%eb%8a%94-%ea%b2%8c-%ec%97%b0%ea%b5%ac%ec%9d%b8%ea%b0%80-%ec%95%84%eb%8b%8c%ea%b0%80/), [최윤섭 박사 「박사 학위 의미」](https://gradschoolstory.chkwon.net/yoonsup/what-phd-means/), [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619), [Knuth et al. 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html). 로보틱스/CV의 4-type 사례와 venue별 type 분포 관찰은 이 장에서 정리했다.

다음: [Ch.5 — 생각의 시간: 책상에 오래 있었다고 연구가 된 것은 아니다](./chapter_05_thinking_time.md)
