# Ch.4 — 연구와 작업을 구분하는 법

[Ch.3 (주도권의 이동)](./chapter_03_ownership_shift.md)에서 보고 방식과 주고받는 단위가 학생 쪽으로 옮겨 오면, 책상 위의 일을 내 일이라 부를 수 있게 된다. 이때부터는 다른 데서 막힌다. 매일 코드를 짜고, system을 tuning하고, 새 dataset을 돌려도, 그 일이 연구인지 그냥 작업인지 감이 오지 않는다. 손에 쥔 일이 의미가 있으려면 그 일이 새 지식을 만드는지 따져 볼 방법이 있어야 한다.

[Ch.2 (문제 정의)](./chapter_02_feynman_problem.md)에서 좁힌 problem statement를 여기에 대 본다.

---

## 4.1 작업, 목표, 목적: task / objective / goal

[권창현 교수](https://gradschoolstory.chkwon.net/changhyun/%ec%a7%80%ea%b8%88-%ed%95%98%ea%b3%a0-%ec%9e%88%eb%8a%94-%ea%b2%8c-%ec%97%b0%ea%b5%ac%ec%9d%b8%ea%b0%80-%ec%95%84%eb%8b%8c%ea%b0%80/)는 「지금 하고 있는 게 연구인가, 아닌가?」에서 *A Manual for Writers of Research Papers, Theses, and Dissertations*의 "연구 주제에 대해 삼단계로 말해보기"를 소개한다. "저는 X라는 주제에 대해 공부하고 있습니다." "왜냐하면, 저는 왜 Y인지 알고 싶거든요." "그러면, 제가 다른 사람들이 왜 Z인지 이해할 수 있게 도와줄 수 있거든요." 권창현 교수는 이 세 단계를 각각 작업(task), 목표(objective), 목적(goal)이라고 부른다.

- **task**는 연구에 필요한 활동이다. 개발, 설계, 최적화 같은 일이다. 코드 한 줄, 실험 한 번, 그림 한 장이 여기 들어간다.
- **objective**는 연구 결과로 얻는 새 지식이다. 예를 들어 "BEV feature가 야간 loop closure에 효과가 있는지 밝힌다"가 objective다.
- **goal**은 objective를 이루어 다가가려는 궁극적인 방향이다. 예를 들어 "로봇이 오랜 기간 스스로 움직이게 하는 것(long-term autonomy)"이 goal이 될 수 있다.

권창현 교수는 대학원생이 주로 첫 단계에 모든 시간을 쓰고 그것만으로도 벅차다고 쓴다. 그러면서 objective와 goal을 종종 생각하며 연구하면 크게 도움이 될 것 같다고 덧붙인다. 1년 동안 한 작업을 논문 한 편으로 묶으려면 task 위에 objective가 있어야 한다. 그 논문이 분야에 왜 필요한지 답하려면 objective가 goal로 이어져야 한다.

권창현 교수는 NSF의 George Hazelrigg가 쓴 "Honing Your Proposal Writing Skills"도 인용한다. Hazelrigg는 심사위원에게 "not research"로 읽히는 낱말로 "develop", "design", "optimize", "control", "manage" 등을 꼽았다. 이런 동사는 task를 가리킨다. objective가 되려면 무엇을 새로 알아낼지가 붙어야 한다. SLAM system을 개발하는 일은 공학적 성과다. 연구 기여가 되려면 그 system으로 SLAM에 대한 어떤 명제를 검증해야 한다.

---

## 4.2 정글 탐험가 비유

task, objective, goal의 구분은 추상적이다. [최윤섭 박사](https://gradschoolstory.chkwon.net/yoonsup/what-phd-means/)는 「박사 학위라는 것의 의미」에서 같은 이야기를 한 장면으로 보여 준다. 박사 말년 차에 궁금한 것이 생겨 논문을 아무리 뒤져도 답이 없었는데, 생각해 보니 그 답은 지구상의 누구도 가지고 있지 않았다고 한다.

> 마치 탐험가가 지도를 보고 열심히 정글을 헤쳐왔는데, 지도의 가장자리에 나오는 끝까지 왔음에도 여전히 내 앞에는 끝없는 정글이 펼쳐져 있는 형국이었다. … 지금부터는 다름 아닌 내가 한 걸음씩 조심스럽게 내딛으면서 앞에 절벽이 있는지, 강이 있는지 스스로 지도를 그려가야 한다.

이 비유에서 눈여겨볼 곳은 지도의 가장자리다. 지도 안쪽은 이미 누군가 밝혀 놓은 영역이고, 바깥은 연구자가 직접 걸어 들어가며 밝혀야 할 곳이다. 최윤섭 박사는 박사 학위가 특정 주제를 많이 알거나 최고의 전문가가 됐다는 뜻이 아니라고 본다. 그에게 박사 학위는 "인류가 가진 지식의 경계를 앞으로도 평생 스스로 넓혀갈 수 있을 만한 준비가 되었다는 것"이었다.

지도 안쪽에서 일을 잘하는 것도 가치 있는 task다. 가장자리 바깥으로 나가는 한 걸음은 작아도 된다. 지도에 아직 없는 곳이기만 하면 된다.

그 한 걸음으로 무엇을 알아낼지 적을 때 Hazelrigg의 네 문형을 참고할 수 있다.

---

## 4.3 연구 목표를 적는 네 가지 문형

Hazelrigg는 공학 연구 목표를 적는 방법을 자기가 아는 한 네 가지뿐이라고 했다. 권창현 교수가 옮긴 그 네 문장은 이렇다.

1. "The research objective of this proposal is to test the hypothesis H." (가설 검정)
2. "The research objective of this proposal is to measure parameter P with accuracy A." (측정)
3. "The research objective of this proposal is to prove the conjecture C." (추측 증명)
4. "The research objective of this proposal is to apply method M from disciplinary area D to solve problem P in disciplinary area E." (학제간 융합)

권창현 교수는 사회과학과 공학이 겹치는 자기 분야에서는 꼭 맞지 않는다고 느낄 때도 있지만, 이 네 범주 밖의 일반적인 기술 방법은 알지 못한다고 덧붙인다.

- **가설 검정.** 명제를 데이터로 검토한다. 명제를 먼저 적고, 그 명제가 참이면 어떤 데이터가 나올지 미리 그린 다음, 실험으로 그 그림과 실제 데이터를 비교한다. "BEV feature가 야간 loop closure에 효과가 있다"가 가설의 예다.
- **측정.** 현상의 정량적 성질을 데이터로 정한다. 가설 검정은 어느 쪽이 옳은지 묻고, 측정은 얼마인지 묻는다. "KITTI-360 등 세 dataset에서 SLAM system 세 개의 RTE(relative translation error) 분포는 어떤 모양인가"가 측정의 예다.
- **추측 증명.** 명제가 옳다는 것을 논리로 보인다. 결론을 내는 도구가 데이터에서 증명으로 바뀐다. 예를 들어 "관측 오염률 $r$이 정해진 상한 $r_{\max}$보다 작으면 제안한 최적화 절차가 전역 최적해로 수렴한다"는 명제를 세우고 증명한다.
- **학제간 융합.** 다른 분야의 도구나 관점을 이 분야의 문제에 쓴다. 도구가 나온 분야와 쓰이는 분야가 다르다. "communication theory의 codebook 학습을 visual descriptor 설계에 쓴다"가 예다.

자기 일을 네 문형으로 적어 본다. 어느 문형으로도 적기 어렵다면 무엇을 새로 알아내려는지, 어떻게 알아낼지가 충분히 구체적인지 살핀다. 기여가 있는지는 문형에 들어맞는지와 따로 판단한다. 기여 하나가 두 문형에 걸칠 수도 있다. 다른 분야의 방법을 가져와 쓰고 그 효과를 가설 검정으로 확인하는 경우가 그렇다.

---

## 4.4 중심 기여 하나

Hazelrigg의 네 문형은 연구 목표를 어떤 꼴로 적을지 다룬다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)은 Rule 1에서 논문 한 편이 중심 기여 하나에 초점을 두라고 권한다.

> Focus your paper on a central contribution, which you communicate in the title.

여러 기여에 한꺼번에 초점을 두면 기여마다 설득력이 약해질 수 있다. 다만 Mensh와 Kording은 중심 메시지 하나를 위해 여러 혁신을 설명해도 되고, 중심 기여 자체에 여러 측면이 있을 수 있다고 적었다.

두 기준을 함께 쓰면 논문 범위를 이렇게 점검할 수 있다. 어떤 종류의 새 지식을 만드는가. 그 지식을 중심 기여 하나로 설명할 수 있는가. 여러 문형이 함께 나와도 주장 하나를 뒷받침하면 Rule 1에 어긋나지 않는다. 논문을 나눌지는 문형의 개수보다 각 결과에 따로 설 중심 메시지가 있는지를 보고 정한다.

---

## 4.5 로보틱스/CV의 네 문형 예

네 문형을 자기 분야의 사례에 적용하면 연구 목표를 어떻게 적을지 구체적으로 생각할 수 있다. 다음은 로보틱스/CV의 작업을 각 문형으로 표현한 예다.

가설 검정. "BEV feature pyramid는 night-time loop closure recall을 raw image보다 높인다"는 한 줄짜리 명제가 있다. 명제가 참이라면 night benchmark에서 BEV-feature 기반 retrieval의 recall@1이 image-feature baseline보다 통계적으로 유의하게 높을 것이라는 그림을 미리 그린다. 실험은 그 그림과 실제 측정을 비교한다. 이런 형식으로 ICRA·IROS의 방법 논문이 검정하려는 가설을 적어 볼 수 있다.

측정. "KITTI-360, MulRan, Boreas 세 dataset에서 LIO-SAM·KISS-ICP·SuMa 세 system의 RTE 분포는 어떻게 다른가"라는 물음은 참과 거짓을 가리지 않고 양을 묻는다. 결론은 구체적인 수치와 오차 분포의 모양으로 나온다. T-RO·IJRR의 benchmark 논문과 일부 dataset 논문에서 이런 형식을 볼 수 있다.

추측 증명. "관측 오염률 $r<r_{\max}$이고 필요한 정규성 조건이 성립할 때 제안한 최적화 절차가 전역 최적해로 수렴한다"는 식의 명제는 데이터만으로는 결정되지 않는다. $r_{\max}$와 정규성 조건을 정리 안에 명시하고 논리로 증명해야 한다. T-RO, IJRR의 일부 이론 논문과 control·optimization 논문에서 이런 형식을 볼 수 있다.

학제간 융합. "communication theory의 vector quantization codebook 학습 절차를 visual place recognition descriptor에 적용한다"는 작업은 도구의 출처가 다른 분야이고 적용 대상이 본 분야다. 옮겨 쓰는 과정에서 문제를 새로 정의해야 할 때가 많다. CVPR의 cross-domain 논문이나 ICRA의 learning-based perception 논문 일부에서 이런 형식을 볼 수 있다.

연구실이나 venue별로 어느 문형이 많은지 알려면 corpus를 정해 실제 논문을 분류해야 한다. 우선 본인 연구실의 최근 논문을 네 문형으로 표시해 보면 어떤 질문과 방법에 작업이 몰려 있는지 확인할 수 있다. ICRA·IROS·CVPR, T-RO·IJRR처럼 형식이 다른 venue를 비교할 때도 같은 표본 기간과 분류 기준을 써야 한다.

> 다른 문형으로 넓힐지는 연구 문제와 검증 역량, 목표 venue를 함께 보고 결정한다.

---

## 4.6 최상급을 피하고 claim을 수치로 적기

[Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1의 12번 항목은 끝부분에서 최상급(superlative)을 경계한다.

> When describing your own work, be humble and don't use superlatives of praise, either explicitly or implicitly, even if you are enthusiastic.

자기 작업을 설명할 때 "best", "novel", "state-of-the-art" 같은 최상급이 보이면 claim에 비교 기준이 빠지지 않았는지 살핀다. 비교가 무엇 대비 무엇인지, 어떤 metric에서 얼마나 다른지를 함께 밝힌다. "novel SLAM system"보다 "frame-to-frame matching에서 RANSAC inlier ratio를 X% → Y%로 올린 SLAM system"이 검증 가능하다. X와 Y는 문장 형식을 보이는 자리표시이며 실제 초록에는 측정값과 protocol을 적는다.

네 문형으로도 같은 점검을 한다. "robotic system을 개선했다"는 claim은 네 문형 어디에도 들어가지 않을 수 있다. 어떤 가설이 검정됐는가, 무엇이 측정됐는가, 무엇이 증명됐는가, 어떤 분야의 도구가 옮겨졌는가. 네 질문 어디에도 답하기 어렵다면 작업을 했다는 보고에서 더 나아가 무엇을 새로 알게 됐는지 살핀다.

서론에서 contribution claim을 요약하는 방법은 [Ch.23 (Introduction)](./chapter_23_introduction.md)에서 다룬다.

---

자기 일이 어느 문형에 들어가는지 매번 바로 답하기는 어렵다. 권창현 교수는 같은 글 첫머리에 아인슈타인이 했다는 다음 말을 옮겨 둔다. 아인슈타인의 원 출처는 확인하지 못했다.

> If we know what it was we were doing, it would not be called research, would it?

자기 작업으로 무엇을 새로 알아내려는지 처음부터 또렷하게 적기는 어렵다. 일을 진행하며 목표를 다시 쓰고, 목표에 비추어 다음 일을 고를 수 있다. 한 학기나 1년 동안 작업만 쌓이지 않도록, 한 달에 한 번이라도 무엇을 새로 알게 됐는지 돌아본다.

---

**출처.** [권창현 교수 「지금 하고 있는 게 연구인가, 아닌가?」](https://gradschoolstory.chkwon.net/changhyun/%ec%a7%80%ea%b8%88-%ed%95%98%ea%b3%a0-%ec%9e%88%eb%8a%94-%ea%b2%8c-%ec%97%b0%ea%b5%ac%ec%9d%b8%ea%b0%80-%ec%95%84%eb%8b%8c%ea%b0%80/), [최윤섭 박사 「박사 학위라는 것의 의미」](https://gradschoolstory.chkwon.net/yoonsup/what-phd-means/), [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619), [Knuth et al. 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html). 로보틱스/CV의 문형 예시, BEV·long-term autonomy 예는 이 장에서 만든 사례다. venue별 분포는 corpus와 분류 기준을 정한 뒤에 판단한다.

다음: [Ch.5 — 생각의 시간: 진척을 재는 기준](./chapter_05_thinking_time.md)
