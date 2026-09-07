# Ch.20 — 정보가 담긴 소제목과 결론 ≠ 요약

논문 본문을 끝까지 읽는 독자는 소수다. 다수는 소제목만 훑고 그림으로 내려간다. 그들에게 논문의 핵심 메시지를 전달하려면 소제목 자체가 주장을 담아야 한다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §III가 이 점을 정면으로 짚는다.

---

## 20.1 소제목에 주장이 필요한 이유

훑어 읽는 독자는 본문보다 소제목과 그림 캡션을 먼저 볼 수 있다. 이 독자에게 "Loop Closure Experiments"라는 소제목은 실험 주제만 알려 준다. 같은 곳에 "Loop closure recall improves 14% with multi-scale BEV"가 들어가면 그 한 줄로 핵심 메시지가 전달된다. 여기와 아래 표에 제시된 수치는 주장이 담긴 소제목의 문장 구조를 설명하기 위한 예시 데이터다.

소제목이 모이면 논문의 목차이자 골격이 된다. Whitesides가 §III에 적은 권고를 다른 표현으로 옮기면 "소제목만 읽어도 논문의 핵심 메시지를 재구성할 수 있어야 한다"가 된다. 이 조건이 깨진 논문은 훑어 읽는 단계에서 reject 사유를 만든다.

topic-style heading("Network Architecture", "Ablation Study")은 분야의 관행으로 굳어 있어 거부감이 적다. 다만 그 관행이 정보 전달의 기회를 놓치고 있다는 진단이 Whitesides의 입장이다.

---

## 20.2 Before / After 5쌍

로보틱스 분야 헤딩 5쌍을 비교하면 패턴이 보인다.

| Before (topic) | After (claim) |
|---|---|
| Loop Closure Experiments | **Loop closure recall improves 14% with multi-scale BEV** |
| Ablation Study | **Removing geometric prior degrades RTE by 38% on KITTI-08** |
| Comparison with Baselines | **Our method matches LIO-SAM accuracy at 1/3 the runtime** |
| Network Architecture | **A two-branch encoder separates appearance from geometry** |
| Dataset and Metrics | **We evaluate on KITTI-360 and VIVID with rotation/translation error** |

After 쪽 다섯 헤딩의 공통점은 동사와 대상이 명시되어 있다는 점이다. "improves 14%", "degrades RTE by 38%", "matches at 1/3 runtime", "separates appearance from geometry"가 한 줄에 박혔다. 동사가 빠진 명사구만 남으면 헤딩은 정보를 잃는다.

---

## 20.3 작성 절차 3단계

claim-style 헤딩 한 줄을 만드는 절차는 다음과 같다.

1. 본문 핵심 결론을 한 문장으로 적는다.
2. SVO로 다듬고, 명사구 안의 수식 관계도 확인한다. Whitesides §III의 '명사의 형용사적 용법 지양' 규칙에 따라, 가령 "ATP formation" 대신 전치사구를 활용한 "formation of ATP" 형태를 권장한다.
3. venue template와 지면 폭 안에서 한 줄로 읽히도록 줄인다. 60-80자를 초안의 출발 범위로 둘 수 있지만 보편적인 길이 규칙은 아니다. 숫자보다 claim의 완결성과 같은 층위 헤딩의 평행성을 먼저 본다.

이 절차는 outline iteration 4-5회차에 들어가는 작업이다. 1-3회차에서는 헤딩이 placeholder로 남아 있어도 된다. claim-style로 다듬는 작업은 본문 결론이 안정된 뒤에야 비로소 의미가 있다.

---

## 20.4 Conclusions ≠ Summary

Conclusions 섹션에 Results의 숫자를 다시 나열하는 패턴이 가장 흔한 결함이다. "In summary, we showed A, B, and C."로 시작하는 Conclusions는 abstract와 Results에 이미 있는 정보를 한 번 더 반복한다. 독자에게 새 정보가 0이다.

Whitesides가 §III에 적은 정의는 명확하다. Conclusions는 higher-level analysis다. 결과들이 합쳐 무엇을 말하는지, 분야에 어떻게 기여하는지, 어떤 가설이 살아남고 어떤 가설이 죽었는지가 들어간다. 각 항목은 간결한 구의 형태로 작성하되, 단순한 사실 나열을 넘어 새로운 학술적 통찰을 온전히 담아내야 한다.

Discussion 섹션이 별도로 있는 논문이라면 Conclusions는 더 짧아질 수 있다. 3-5개의 짧은 요점을 초안 출발값으로 삼을 수 있지만 venue 형식과 기여 수에 따라 달라진다. Discussion이 없는 형식이라면 Conclusions가 해석과 한계까지 흡수해 길어진다. 어느 쪽이든 Results의 숫자만 되풀이하는 요약에 머물러서는 안 된다.

---

## 20.5 흔한 실수

Conclusions·heading 양쪽에서 반복되는 실수는 다음과 같다.

- "In summary, we showed A, B, and C." — A·B·C는 이미 abstract와 Results에 있다. 한 단계 위로 올라가지 않았다.
- Conclusions에 future work 한 줄만 달랑 쓰는 경우 — higher-level analysis가 비어 있다. future work는 Conclusions의 마지막 구에만 들어간다.
- 헤딩 길이가 들쭉날쭉한 경우 — 한 섹션 안에 10자 헤딩과 90자 헤딩이 섞이면 평행성이 깨진다. 같은 스케일의 헤딩은 길이가 비슷해야 skim에서 리듬이 살아난다.
- claim-style 헤딩에서 동사가 빠지는 경우 — "BEV-based Loop Closure"는 명사구다. claim이 되려면 동사가 들어가야 한다.

---

## 20.6 점검 절차

claim-style 헤딩은 본문 한 섹션에서 결론 문장을 먼저 추출한 뒤 만든다. 그 문장을 SVO로 다듬고, 길이 제약 안에서 잘라 내며, 같은 섹션 안의 헤딩 길이와 문장 구조를 맞춘다. outline iteration 후반부에서 사람이 손으로 반복해야 하는 절차다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §III (information-rich subheadings, conclusions as higher-level analysis). [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7 (declarative statements, 보조). 로보틱스 분야를 위한 5쌍의 소제목 대비 예시는 본문에서 독자적으로 재구성한 자료다.

다음: [Ch.21 — 문단 흐름](./chapter_21_paragraph_flow.md)
