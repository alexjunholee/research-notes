# Ch.20 — 정보가 담긴 소제목과 결론 ≠ 요약

논문 본문을 끝까지 읽지 않고 소제목을 훑은 뒤 그림으로 내려가는 독자도 있다. 이런 독자에게 논문의 핵심 메시지를 전하려면 소제목에 주장이 담겨 있어야 한다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)는 2.3절에서 소제목을 되도록 구체적이고 정보가 많게 쓰라고 권했다.

---

## 20.1 소제목에 주장이 필요한 이유

훑어 읽는 독자는 본문보다 소제목과 그림 캡션을 먼저 본다. 이 독자에게 "Loop Closure Experiments"라는 소제목은 실험 주제만 알려 준다. 같은 자리에 "Loop closure recall improves 14% with multi-scale BEV"를 쓰면 한 줄로 핵심 결과가 전해진다. 이 예와 아래 표의 수치는 소제목의 문장 구조를 보여 주려고 만든 가상의 값이다.

Whitesides는 Results & Discussion을 주요 주제별로 나누고 굵은 소제목을 달라고 했다. 그래야 구성이 분명해지고, 독자가 원고를 훑으며 관심 있는 부분을 찾을 수 있다. 그가 든 예에서 "The Rate of Self-Exchange Decreases with the Polarity of the Solvent"는 "Measurement of Rates"보다 길지만 독자에게 훨씬 쓸모 있다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)의 rule 7도 결과가 주장을 받치는 논리를 서술문의 연속으로 바꿔 Results의 소제목으로 쓰라고 권한다. 이렇게 쓴 소제목을 모으면 소제목만 읽어도 논문의 논리를 따라갈 수 있다.

"Network Architecture", "Ablation Study" 같은 주제형 소제목은 분야에서 관행으로 굳어 있어 낯설지 않다. Whitesides가 든 예에도 "Synthesis of Alkane Thiols"처럼 주제만 밝힌 소제목이 섞여 있다. 결과를 다루는 소제목이라면 주장을 담을 수 있는지 먼저 따져 본다.

---

## 20.2 Before / After 5쌍

로보틱스 논문에서 볼 법한 소제목 다섯 쌍을 비교한다.

| Before (topic) | After (claim) |
|---|---|
| Loop Closure Experiments | **Loop closure recall improves 14% with multi-scale BEV** |
| Ablation Study | **Removing geometric prior degrades RTE by 38% on KITTI-08** |
| Comparison with Baselines | **Our method matches LIO-SAM accuracy at 1/3 the runtime** |
| Network Architecture | **A two-branch encoder separates appearance from geometry** |
| Dataset and Metrics | **We evaluate on KITTI-360 and VIVID with rotation/translation error** |

After 쪽 소제목에는 모두 동사와 대상이 있다. "improves 14%", "degrades RTE by 38%", "matches LIO-SAM accuracy at 1/3 the runtime", "separates appearance from geometry"가 각각 한 줄에 들어 있다. 동사 없이 명사구만 남으면 소제목은 주제만 알려 준다.

---

## 20.3 작성 절차 3단계

주장을 담은 소제목 한 줄은 다음 순서로 만든다.

1. 해당 섹션 본문의 핵심 결론을 한 문장으로 적는다.
2. 주어-동사-목적어 구조로 다듬고, 명사구 안의 수식 관계도 확인한다. Whitesides는 3절 "Some Points of Style"에서 명사를 형용사처럼 쓰지 말라고 했다. "ATP formation" 대신 "formation of ATP"로 쓰라는 예를 들었다.
3. 학회 템플릿의 지면 폭 안에서 한 줄로 읽히게 줄인다. 60-80자를 초안의 출발 범위로 잡아 볼 수 있지만 정해진 규칙은 없다. 길이보다 주장이 완결됐는지, 같은 층위의 소제목들과 형식이 맞는지를 먼저 본다.

이 작업은 [Ch.17](./chapter_17_outline_first.md)에서 나눈 outline 반복의 4-5회차에 한다. 1-3회차에는 소제목을 임시로 두어도 된다. 본문의 결론이 정해져야 소제목에 담을 주장도 정해진다.

---

## 20.4 Conclusions ≠ Summary

Conclusions 섹션에서 흔한 결함 하나는 Results의 숫자를 다시 늘어놓는 것이다. "In summary, we showed A, B, and C."로 시작하는 Conclusions는 초록과 Results에 이미 있는 정보를 되풀이할 뿐이어서 독자가 새로 얻는 것이 없다.

Whitesides는 2.3절에서 Conclusions를 이렇게 정의했다. outline 단계에서는 결론을 짧은 구나 문장의 목록으로 정리한다. Results에 있는 내용은 특별히 강조할 때가 아니면 되풀이하지 않는다. Conclusions에는 말 그대로 결론을 쓰고, 한 단계 높은 분석을 더하고 연구의 의의를 분명히 밝혀야 한다. 그 앞의 2.2절에서는 outline에 적은 생각을 Introduction, Results and Discussion, Conclusions로 나누면서 Conclusions에 들어갈 질문으로 "What does it all mean? What hypotheses were proved or disproved? What did I learn? Why does it make a difference?"를 꼽았다.

Discussion 섹션이 따로 있는 논문이라면 Conclusions는 짧아도 된다. 짧은 요점 3-5개에서 시작해 볼 수 있고, 학회 형식과 기여의 수에 따라 조정한다. Discussion이 없는 형식이라면 Conclusions가 해석과 한계까지 맡아 길어진다. 어느 경우든 Results의 숫자를 되풀이하는 데서 멈추지 않는다.

---

## 20.5 흔한 실수

Conclusions와 소제목에서 되풀이되는 실수는 다음과 같다.

- Conclusions에 future work 한 줄만 적는다. 한 단계 높은 분석이 빠져 있다. future work는 분석 뒤에 덧붙인다.
- 소제목 길이가 들쭉날쭉하다. 한 섹션 안에 10자짜리와 90자짜리 소제목이 섞이면 형식이 맞지 않아 훑어 읽기 어렵다. 같은 층위의 소제목은 길이를 비슷하게 맞춘다.

---

## 20.6 점검 절차

주장을 담은 소제목은 본문 섹션에서 결론 문장을 먼저 뽑은 뒤에 만든다. 그 문장을 주어-동사-목적어 구조로 다듬고, 길이 제약에 맞춰 줄이고, 같은 섹션 안 다른 소제목과 길이와 문장 구조를 맞춘다. outline 반복의 후반부에 사람이 직접 되풀이해야 하는 작업이다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 2.2절(Conclusions에 들어갈 질문), 2.3절(정보가 담긴 소제목, 요약이 아닌 결론), 3절(명사를 형용사로 쓰지 않기). [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7 (서술문 소제목). 로보틱스 소제목 다섯 쌍과 그 수치는 이 책에서 만든 예시다.

다음: [Ch.21 — 문단 흐름](./chapter_21_paragraph_flow.md)
