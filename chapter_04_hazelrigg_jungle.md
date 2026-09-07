# Ch.4 — 연구와 작업을 구분하는 법

[Ch.3 (주도권의 이동)](./chapter_03_ownership_shift.md)에서 화법·작업 단위가 학생 쪽으로 기울고 나면 책상 위의 작업을 내 작업이라 부를 수 있는 단계가 온다. 이 단계에 이르면 마주하는 난관의 성격도 달라진다. 매일 코드를 짜고, system을 tuning하고, 새로운 dataset을 돌려도, 그 작업이 연구인지 task인지의 감각이 흐릿하게 남는 단계다. 손에 들어온 작업이 의미를 가지려면 그 작업이 새 지식을 만드는지 아닌지를 진단할 도구가 필요하다.

진단 도구는 두 가지다. 정글 탐험가 비유가 직관적 표현이고, 네 가지 연구 유형이 추상 분류다. [Ch.2 (문제 정의)](./chapter_02_feynman_problem.md)에서 좁힌 problem statement를 두 도구에 가져다 댄다.

---

## 4.1 작업 vs 연구: task / objective / goal

[권창현 교수](https://gradschoolstory.chkwon.net/changhyun/%ec%a7%80%ea%b8%88-%ed%95%98%ea%b3%a0-%ec%9e%88%eb%8a%94-%ea%b2%8c-%ec%97%b0%ea%b5%ac%ec%9d%b8%ea%b0%80-%ec%95%84%eb%8b%8c%ea%b0%80/)는 「지금 하고 있는 게 연구인가, 아닌가?」에서 학생의 시간 단위를 세 층으로 나눴다. **task**는 오늘 한 일이다. 코드 한 줄, 실험 한 회, 그림 한 컷이 task다. **objective**는 지금 쓰는 한 논문에서 보일 결과다. "이 논문에서 BEV feature가 night-time loop closure에 효과적임을 보인다"가 objective다. **goal**은 분야 전체가 풀려는 큰 질문이다. "long-term autonomy를 어떻게 달성할 것인가"가 goal이다.

학생이 시간을 쓰는 곳은 task다. 학생은 이번 연구에서 달성할 objective를 명확히 세우고, 학계 전체가 지향하는 거대한 goal과 이를 정렬해야 한다. 세 층은 위계를 이룬다. task만 쌓이고 objective가 비어 있으면 1년치 작업이 한 편의 논문으로 묶이지 않는다. objective는 있으나 goal과 연결이 흐릿하면 그 논문이 분야에 왜 필요한지에 대한 답이 안 나온다.

"개발", "설계", "최적화", "제어" 같은 동사는 task로는 가능하지만 자동으로 objective·goal로 올라가지 않는다. SLAM system을 개발하는 일과 SLAM의 어떤 명제를 검증하는 일은 다르다. 전자는 engineering achievement이고 후자는 research contribution이다. 둘은 venue도, 심사위원이 묻는 질문도, 졸업 심사에서 받는 평가도 다르다.

> **task ≠ objective ≠ goal.** 세 층의 구분이 흐릿한 채로 작업을 쌓으면 그 작업이 연구인지 task인지 진단되지 않는다.

---

## 4.2 정글 탐험가 비유

§1의 세 층 구분은 추상적이다. 같은 명제를 직관적인 한 줄로 압축한 비유가 있다. [최윤섭 박사](https://gradschoolstory.chkwon.net/yoonsup/what-phd-means/)가 「박사 학위의 의미」에서 적은 정글 탐험가 비유다.

> 교과서는 이미 탐사된 영역의 지도, 박사는 그 끝을 넘어 자기 손으로 지도를 새로 그리는 과정.

비유에서 중요한 장면은 지도의 끝이다. 지도의 안쪽이 기존 학계가 이미 규명해 놓은 기성의 영토라면, 그 바깥은 연구자 자신이 직접 발을 딛으며 밝혀내야 할 미개척지다. 박사 학위는 지도를 전부 외웠다는 인증이 아니라, 지도의 경계 밖에서 계속 그릴 준비가 되었다는 인증에 가깝다.

끝 안쪽은 누군가 이미 그렸고, 누구나 들여다볼 수 있다. 그 영역에서 작업을 잘하는 일은 가치 있는 task다. 다만 지도를 새로 그리는 일은 아니다. 새 지식은 끝 바깥에서만 만들어진다. 한 발짝의 크기는 작아도 된다. 지도에 안 적힌 곳이라는 조건만 만족하면 된다.

연구라 부를 수 있는 작업은 모두 이 한 발짝의 변형이다. 다만 한 발짝을 어떤 방향으로 디디는지가 분류된다. Hazelrigg의 4-type이 그 방향의 분류이고, §1의 시간 층위(task/objective/goal)와 직교하는 내용 층위다.

---

## 4.3 새 지식의 네 가지 형태

§1의 task/objective/goal이 시간 층위의 분류 — 오늘 / 이번 논문 / 분야 전체 — 였다면, Hazelrigg 4-type은 내용 층위의 분류다. objective 슬롯에 들어간 한 contribution이 어떤 종류의 새 지식을 만드는가를 묻는다. 두 분류는 직교 축이다.

NSF의 George Hazelrigg가 Honing Your Proposal Writing Skills에서 제시하고 권창현 교수가 소개한 연구 목표의 네 문형은 한 한국어 단락으로 옮길 수 있다. 연구란 새로운 지식을 축적하는 활동이다. 이때 생산되는 지식은 성격에 따라 크게 네 가지 유형으로 구분된다. 그 네 가지는 명제가 옳은지 그른지를 데이터로 결정하는 가설 검정, 현상의 정량적 성질을 데이터로 결정하는 측정, 명제가 옳다는 것을 논리로 결정하는 추측 증명, 다른 분야의 도구·관점을 본 분야 문제에 적용하는 학제간 융합이다. 새 지식을 만들지 않는 작업은 이 네 칸 어디에도 들어가지 않는다.

- **가설 검정 (hypothesis testing).** 명제가 옳은지 그른지를 데이터로 결정하는 작업이다. 명제가 미리 적혀 있고, 그 명제가 참이라면 어떤 데이터가 보일지가 미리 그려져 있고, 실험은 그 그림과 실제 데이터를 비교한다. "BEV feature가 night-time loop closure에 효과적이다"가 가설의 한 예다.
- **측정 (measurement).** 현상의 정량적 성질을 데이터로 결정하는 작업이다. 가설은 어느 쪽이 옳은가를 묻지만 측정은 얼마인가를 묻는다. "KITTI-360에서 6개 SLAM system의 RTE (relative translation error) 분포는 어떻게 생겼는가"가 측정의 한 예다.
- **추측 증명 (proof of conjecture).** 명제가 옳다는 것을 논리로 결정하는 작업이다. 데이터가 아니라 증명이 결정의 도구다. 예컨대 "관측 오염률 $r$이 명시된 상한 $r_{\max}$보다 작으면 제안한 최적화 절차가 전역 최적해로 수렴한다"는 명제를 세우고 증명하는 작업이 여기에 해당한다.
- **학제간 융합 (interdisciplinary transfer).** 다른 분야의 도구·관점을 본 분야 문제에 적용하는 작업이다. 도구의 출처와 적용 대상이 분야 경계를 넘는다. "communication theory의 codebook 학습을 visual descriptor 설계에 적용한다"가 한 예다.

자기 작업을 네 칸에 가져다 대 본다. 어디에도 안 들어가면 그 작업은 task일 가능성이 높다. 한 칸에 들어가면 그게 곧 contribution claim의 type이다. 한 기여가 두 칸에 동시에 들어갈 수도 있다. 예를 들어 다른 분야의 방법을 적용하고 그 효과를 가설 검정으로 확인할 수 있다.

---

## 4.4 single contribution과의 연결

Hazelrigg 4-type이 연구 목표를 어떤 형식으로 설명할지 묻는다면, [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) Rule 1은 한 논문의 중심 기여에 초점을 맞추라고 권한다.

> Focus your paper on a central contribution, which you communicate in the title.

한 논문은 하나의 중심 contribution을 명료하게 전달해야 한다. 여러 기여에 동시에 초점을 맞추면 각 기여의 설득력이 약해질 수 있다. 다만 Mensh-Kording은 하나의 중심 메시지를 위해 여러 혁신을 설명할 수 있고, 중심 기여 자체도 여러 측면을 가질 수 있다고 적었다.

이 두 framework를 함께 쓰면 paper-level scoping을 두 질문으로 점검할 수 있다. 어떤 종류의 새 지식을 만드는가. 그 지식을 하나의 중심 기여로 설명할 수 있는가. 여러 type이 함께 나타나더라도 하나의 주장을 뒷받침한다면 Rule 1과 충돌하지 않는다. 논문 분리는 type의 개수보다 각 결과가 독립된 중심 메시지를 갖는지를 보고 판단한다.

> **한 논문은 하나의 중심 contribution에 초점을 맞춘다.** 여러 type의 작업이 그 기여를 함께 뒷받침할 수 있다.

---

## 4.5 로보틱스/CV에서의 4-type

진단 도구는 추상 분류만으로는 손에 잘 잡히지 않는다. 자기 분야의 사례에 한 번 가져다 대 보면 분류의 칸이 비로소 구체화된다. 로보틱스/CV의 흔한 작업을 네 칸에 한 사례씩 박는다.

가설 검정. "BEV feature pyramid는 night-time loop closure recall을 raw image보다 높인다"는 한 줄짜리 명제가 있다. 명제가 참이라면 night benchmark에서 BEV-feature 기반 retrieval의 recall@1이 image-feature baseline보다 통계적으로 유의하게 높을 것이라는 그림을 미리 그린다. 실험은 그 그림과 실제 측정을 비교한다. ICRA·IROS의 방법 논문 다수가 여기 들어간다.

측정. "KITTI-360, MulRan, Boreas 세 dataset에서 LIO-SAM·KISS-ICP·SuMa 세 system의 RTE 분포는 어떻게 다른가"라는 물음은 참과 거짓을 가리는 명제가 아닌 정량적 측정 질문이다. 여기서 도출해야 할 결론은 옳고 그름의 이분법을 넘어 구체적인 수치와 오차 분포의 특성에 있다. T-RO·IJRR의 benchmark·survey 논문, 그리고 일부 dataset 논문이 여기 들어간다.

추측 증명. "관측 오염률 $r<r_{\max}$이고 필요한 정규성 조건이 성립할 때 제안한 최적화 절차가 전역 최적해로 수렴한다"는 식의 명제는 데이터만으로 결정할 작업이 아니다. $r_{\max}$와 정규성 조건을 정리 안에 명시하고 논리로 증명해야 한다. T-RO, IJRR의 일부 이론 논문과 control·optimization 논문에서 이런 형식을 볼 수 있다.

학제간 융합. "communication theory의 vector quantization codebook 학습 절차를 visual place recognition descriptor에 적용한다"는 작업은 도구의 출처가 다른 분야이고 적용 대상이 본 분야다. 융합은 단순 적용으로 끝나지 않고 적용 과정에서 새로운 문제 정의를 동반하는 경우가 많다. CVPR의 cross-domain 논문, ICRA의 learning-based perception 논문 일부가 여기 들어간다.

연구실이나 venue별 type 분포는 corpus를 정해 실제 논문을 분류하기 전에는 단정할 수 없다. 대신 본인 연구실의 최근 논문을 네 type으로 표시해 보면 어떤 질문과 방법에 작업이 몰려 있는지 확인할 수 있다. ICRA·IROS·CVPR, T-RO·IJRR처럼 형식이 다른 venue를 비교할 때도 같은 표본 기간과 분류 기준을 써야 한다.

> type 분포는 연구실의 질문 포트폴리오를 보는 진단표다. 다양화가 필요한지는 연구 문제와 검증 역량, 목표 venue를 함께 보고 결정한다.

---

## 4.6 superlative 회피와 claim 정량화

[Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 point 12가 4-type 진단의 마지막 점검 도구다.

> When describing your own work, be humble and don't use superlatives of praise, even if you are enthusiastic.

자기 작업을 설명할 때 "best", "novel", "state-of-the-art" 같은 최상급은 claim의 비교 기준이 비었는지 점검하라는 신호가 된다. 비교가 무엇 대비 무엇인지, 어떤 metric에서 얼마나 다른지를 함께 밝힌다. "novel SLAM system"보다 "frame-to-frame matching에서 RANSAC inlier ratio를 X% → Y%로 올린 SLAM system"이 검증 가능하다. X와 Y는 문장 형식을 보이는 placeholder며 실제 초록에는 측정값과 protocol을 적는다.

같은 점검을 4-type 목록으로 다시 한 번 한다. "robotic system을 개선했다"는 claim은 4-type 어디에도 안 들어갈 가능성이 있다. 어떤 가설이 검정됐는가, 무엇이 측정됐는가, 무엇이 증명됐는가, 어떤 분야의 도구가 옮겨졌는가. 네 질문 어디에도 답하기 어렵다면 작업을 했다는 보고에서 더 나아가 무엇을 새로 알게 됐는지 살핀다. 4-type 목록이 superlative 점검과 같은 방향에서 작동한다. 둘 다 claim이 가리키는 구체적인 작업과 근거를 묻는 도구다.

> "best", "novel", "state-of-the-art"가 자기 초록에 보이면 그 표현을 4-type 목록으로 다시 검사한다. 어떤 새 지식을 주장하는지 짚은 뒤, 성능의 우열을 말한다면 superlative 자리에 비교 조건과 수치를 넣는다.

같은 목록이 [Ch.23 (Introduction)](./chapter_23_introduction.md)에서 contribution claim 작성 단계의 자기 점검 도구로 다시 등장한다. 진단의 도구가 작성의 도구로 그대로 이어진다.

---

4-type 어디에 들어가는지 매번 즉답할 수 있는 학생은 거의 없다. 같은 곳에서 권창현 교수가 인용한 아인슈타인의 한 줄이 위안이 된다.

> 우리도 우리가 뭐하는지 잘 모르잖아요. 알면 연구 아니잖아요.

자기 작업이 어느 type인지 흐릿한 채로 한 학기가 지나가는 일은 정상이다. 흐릿한 채로 한 발짝씩 디디면서 type이 점차 또렷해지는 게 정상의 모양이다. 다만 흐림과 막힘은 다르다. type을 전혀 묻지 않은 채로 1년이 지나가면 그 1년의 작업이 task의 더미로 끝날 위험이 있다. 한 달에 한 번이라도 자기 작업을 4-type 목록과 정글 비유에 가져다 대는 습관이 그 위험을 막는다.

같은 정글 비유가 「대학원노트」 Ch.1 「박사를 결정한다는 일」에서 진학 여부를 가늠하는 나침반으로 쓰였다면, 여기서는 책상 위의 일상적 작업을 점검하는 진단 도구로 활용된다. 같은 비유가 두 층위에 적용된다.

작업이 4-type 중 한 칸에 들어간다는 진단이 끝나도 그 작업이 언제 어떻게 진행되는가는 별개의 질문이다.

---

**출처.** [권창현 교수 「지금 연구인가」](https://gradschoolstory.chkwon.net/changhyun/%ec%a7%80%ea%b8%88-%ed%95%98%ea%b3%a0-%ec%9e%88%eb%8a%94-%ea%b2%8c-%ec%97%b0%ea%b5%ac%ec%9d%b8%ea%b0%80-%ec%95%84%eb%8b%8c%ea%b0%80/), [최윤섭 박사 「박사 학위 의미」](https://gradschoolstory.chkwon.net/yoonsup/what-phd-means/), [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619), [Knuth et al. 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html). 로보틱스/CV의 4-type 예시는 이 장에서 만든 진단용 사례다. venue별 분포는 corpus와 분류 기준 없이 단정하지 않는다.

다음: [Ch.5 — 생각의 시간: 책상에 오래 있었다고 연구가 된 것은 아니다](./chapter_05_thinking_time.md)
