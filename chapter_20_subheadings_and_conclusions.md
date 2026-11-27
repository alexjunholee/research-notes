# 20장 주장을 담은 소제목과 요약이 아닌 결론

19장에서 살핀 C-C-C 구조가 단락과 섹션 본문의 뼈대를 잡아 준다면, 바쁜 독자가 가장 먼저 훑는 소제목과 원고의 문을 닫는 결론은 그 뼈대의 핵심 주장을 밖으로 꺼내 보여 주는 자리다. 실제로 논문 본문을 처음부터 끝까지 정독하지 않고 소제목만 훑은 뒤 그림으로 내려가는 독자가 적지 않다. 이런 독자에게도 논문의 중심 메시지가 닿으려면 소제목 자체에 주장이 실려 있어야 한다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 역시 2.3절에서 되도록 구체적이고 정보가 풍부한 소제목을 달라고 권한다.

---

## 20.1 소제목에 주장이 필요한 이유

원고를 훑어 읽는 독자의 시선은 본문 문단보다 소제목과 그림 캡션에 먼저 닿는다. 이 독자에게 "Loop Closure Experiments"라는 소제목은 그저 실험의 주제만 알려 줄 뿐 아무런 판단도 전하지 않는다. 같은 자리에 "Loop closure recall improves 14% with multi-scale BEV"라고 적어 두면 단 한 줄만으로 핵심 결과를 전할 수 있다(여기서 든 14%와 아래 표의 수치는 모두 소제목 문형을 보여 주려고 만든 가상의 값이다).

Whitesides는 Results & Discussion을 주요 주제별로 나누어 굵은 소제목을 달아야 구성이 분명해지고 독자도 관심 있는 대목을 금방 찾아 읽을 수 있다고 보았다. 그가 든 예에서 "The Rate of Self-Exchange Decreases with the Polarity of the Solvent"는 "Measurement of Rates"보다 길지만 독자에게 훨씬 실속 있는 정보를 건넨다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)의 rule 7도 같은 방향이다. 결과가 주장을 받치는 논리 흐름을 이어지는 서술문으로 바꿔 Results의 소제목으로 쓰라는 지침인데, 이렇게 짠 소제목만 위에서 아래로 훑어 내려가도 논문 전체의 논지를 자연스럽게 따라갈 수 있다.

물론 "Network Architecture"나 "Ablation Study" 같은 주제형 소제목이 분야에서 관행처럼 쓰여 낯설지 않은 것도 사실이다. Whitesides의 예시에도 "Synthesis of Alkane Thiols"처럼 주제만 밝힌 소제목이 섞여 있다. 다만 결과를 보고하는 섹션의 소제목이라면 주제어로 남겨 두기 전에 그 절의 주장을 문장으로 담을 수 있는지 먼저 따져 볼 만하다.

---

## 20.2 주장 없는 소제목 고쳐 쓰기 5가지 사례

주제만 적힌 소제목을 주장이 실린 문장으로 바꿀 때 문장의 골격이 어떻게 달라지는지, 로보틱스 논문에서 흔히 마주치는 다섯 쌍을 나란히 놓고 비교해 보자.

| Before (topic) | After (claim) |
|---|---|
| Loop Closure Experiments | **Loop closure recall improves 14% with multi-scale BEV** |
| Ablation Study | **Removing geometric prior degrades RTE by 38% on KITTI-08** |
| Comparison with Baselines | **Our method matches LIO-SAM accuracy at 1/3 the runtime** |
| Network Architecture | **A two-branch encoder separates appearance from geometry** |
| Dataset and Metrics | **We evaluate on KITTI-360 and VIVID with rotation/translation error** |

오른쪽 After 열을 보면 다섯 줄 모두에 동작을 나타내는 동사와 그 대상이 또렷이 살아 있다. "improves 14%", "degrades RTE by 38%", "matches LIO-SAM accuracy at 1/3 the runtime", "separates appearance from geometry"처럼 핵심 효과나 작동 원리가 한 줄 안에 담긴다. 반면 동사 없이 명사구만 남으면 소제목은 어떤 결론도 전하지 못한 채 주제 이름표에 그치고 만다.

---

## 20.3 주장형 소제목과 결론 작성 3단계

주장을 담은 소제목은 머릿속에서 단번에 뽑아내려 하기보다 본문 결론을 압축하는 절차를 거쳐 만드는 편이 깔끔하다.

1. 해당 섹션 본문에서 내리는 핵심 결론을 평서문 한 문장으로 적는다.
2. 주어-동사-목적어가 분명히 드러나도록 문장을 다듬고, 명사구 안쪽의 수식 관계도 손본다. Whitesides는 3절 "Some Points of Style"에서 명사를 형용사처럼 앞세워 붙이지 말라고 권하며 "ATP formation" 대신 "formation of ATP"로 쓰는 예를 들었다.
3. 학회 템플릿의 단 폭 안에서 가급적 한 줄에 들어오도록 군더더기를 덜어 낸다. 초안은 60–80자 안팎으로 시작해 볼 수 있지만 절대적인 길이 규칙이 있는 것은 아니므로, 글자 수에 매이기보다 주장이 온전히 맺히는지, 같은 층위의 소제목끼리 형식이 나란히 맞는지부터 살핀다.

이 다듬기 작업은 [17장](./chapter_17_outline_first.md)에서 나눈 아웃라인 반복 가운데 4–5회차에서 하는 편이 좋다. 1–3회차에서는 소제목을 임시 표지로 남겨 두었다가, 본문의 결론이 단단히 선 뒤에 그 결론을 끌어올려 소제목으로 확정하면 수정이 덜 꼬인다.

---

## 20.4 결론은 요약이 아니다

소제목이 각 절의 주장을 앞으로 끌어낸다면, 논문 말미의 Conclusions는 전체 연구에서 얻은 의미를 한 단계 끌어올려 글을 끝맺는 자리다. 그런데 Conclusions 섹션에서 가장 자주 보이는 결함은 Results의 수치를 그대로 다시 늘어놓는 일이다. "In summary, we showed A, B, and C."로 문을 여는 Conclusions는 독자가 초록과 Results에서 이미 읽은 정보를 되풀이할 뿐이어서 아무런 새 통찰도 주지 못한다.

Whitesides는 2.3절에서 Conclusions가 말 그대로 결론의 자리여야 하며, 한 단계 높은 분석을 보태고 연구의 의의를 분명히 밝혀야 한다고 강조한다. Results에 실린 내용은 특별히 힘주어 짚어야 할 대목이 아니라면 되풀이하지 않고, 아웃라인 단계에서는 결론을 짧은 구나 문장의 목록으로 먼저 추려 둔다. 그 앞의 2.2절에서도 아웃라인의 생각을 Introduction, Results and Discussion, Conclusions로 나누면서, Conclusions가 답해야 할 질문으로 "What does it all mean? What hypotheses were proved or disproved? What did I learn? Why does it make a difference?"를 꼽았다.

실제 분량은 논문의 구조에 따라 달라진다. Discussion 섹션이 별도로 마련된 논문이라면 해석과 한계는 앞선 섹션에서 이미 다루었으므로 Conclusions는 짧아도 좋다. 짧은 요점 3–5개 정도로 시작해 학회 형식과 기여의 수에 맞춰 조정하면 된다. 반면 Discussion 없이 곧장 Conclusions로 이어지는 형식이라면, 이 섹션에 결과의 해석과 한계까지 함께 담아야 하므로 자연히 호흡이 길어진다.

---

## 20.5 흔한 실수

소제목과 Conclusions를 다듬고 난 뒤에도 아래 두 가지 실수가 남아 있지는 않은지 마지막으로 한 번 더 훑어본다.

- **Conclusions에 future work 한 줄만 얹기** — 연구에서 무엇을 배웠고 왜 중요한지 한 단계 높여 분석하는 대목이 빠져 있다. 향후 과제는 그 분석과 의의를 짚은 뒤에 덧붙이는 편이 자연스럽다.
- **같은 층위의 소제목 길이가 들쭉날쭉하기** — 한 섹션 안에 10자짜리 소제목과 90자짜리 소제목이 뒤섞이면 훑어 읽는 리듬이 끊어진다. 같은 층위에 놓인 소제목은 문형과 길이를 비슷하게 맞춰 둔다.

주장을 담은 소제목으로 섹션의 문을 열고 요약이 아닌 분석으로 논문의 문을 닫으면 글 전체의 골격이 선명해진다. 이제 이 굵은 뼈대 안쪽으로 들어가, 한 단락 안에서 문장과 문장이 어떻게 맞물려 흘러가는지 다음 장에서 살펴본다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 2.2절(Conclusions에 들어갈 질문), 2.3절(정보가 담긴 소제목, 요약이 아닌 결론), 3절(명사를 형용사로 쓰지 않기). [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7(서술문 소제목). 로보틱스 소제목 다섯 쌍과 그 수치는 설명용으로 지어낸 예시다.

다음: [21장 문단 흐름](./chapter_21_paragraph_flow.md)