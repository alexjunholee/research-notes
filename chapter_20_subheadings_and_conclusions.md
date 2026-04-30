# Ch.20 — 정보가 담긴 소제목과 결론 ≠ 요약

논문 본문을 끝까지 읽는 독자는 소수다. 다수는 소제목만 훑고 figure로 내려간다. 그래서 그 다수에게 논문의 main message가 전달되려면 소제목 자체에 주장이 박혀 있어야 한다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §III가 이 점을 정면으로 짚는다.

---

## 20.1 헤딩이 claim을 가져야 하는 이유

skim 패턴의 독자는 본문을 읽지 않고 소제목과 figure caption만 본다. 이 독자에게 "Loop Closure Experiments"라는 헤딩은 정보가 0이다. 같은 곳에 "Loop closure recall improves 14% with multi-scale BEV"가 들어가면, 그제서야 그 한 줄로 main message가 전달된다.

heading은 자동 생성되는 TOC다. 그리고 그 TOC가 곧 논문의 골격이다. Whitesides가 §III에 적은 권고를 다른 표현으로 옮기면 *heading만 읽어도 논문의 main message가 재구성되어야 한다*가 된다. 이 조건이 깨진 논문은 skim 단계에서 reject 사유를 만든다.

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

After 쪽 다섯 헤딩의 공통점은 동사·숫자·대상이 명시되어 있다는 점이다. "improves 14%", "degrades RTE by 38%", "matches at 1/3 runtime", "separates appearance from geometry"가 한 줄에 박혔다. 동사가 빠진 명사구만 남으면 헤딩은 정보를 잃는다.

---

## 20.3 작성 절차 3단계

claim-style 헤딩 한 줄을 만드는 절차는 다음과 같다.

1. 본문 핵심 결론을 한 문장으로 적는다.
2. 명사구가 아니라 SVO로 다듬는다. Whitesides §III의 *no nouns as adjectives* 규칙이 여기에 작동한다. "ATP formation"이 아니라 "formation of ATP"가 권장 형태다.
3. 길이를 60-80자 사이로 자른다. 90자가 넘으면 헤딩이 단락처럼 읽히고, 30자 아래로 내려가면 정보량이 부족하다.

이 절차는 outline iteration 4-5회차에 들어가는 작업이다. 1-3회차에서는 헤딩이 placeholder로 남아 있어도 된다. claim-style로 다듬는 작업은 본문 결론이 안정된 뒤에야 비로소 의미가 있다.

---

## 20.4 Conclusions ≠ Summary

Conclusions 섹션에 Results의 숫자를 다시 나열하는 패턴이 가장 흔한 결함이다. "In summary, we showed A, B, and C."로 시작하는 Conclusions는 abstract와 Results에 이미 있는 정보를 한 번 더 반복한다. 독자에게 새 정보가 0이다.

Whitesides가 §III에 적은 정의는 명확하다. Conclusions는 *higher-level analysis*다. 결과들이 합쳐 무엇을 말하는지, 분야에 어떻게 기여하는지, 어떤 가설이 살아남고 어떤 가설이 죽었는지가 들어간다. 형태는 "목록 of short phrases"고, 각 phrase는 새로운 통찰이어야 한다.

Discussion 섹션이 별도로 있는 논문이라면 Conclusions는 더 짧아진다 — 3-5 phrase 정도가 적정선이다. Discussion이 없는 venue 형식이라면 Conclusions가 그 역할을 흡수해 길어진다. 어느 쪽이든 Results의 요약이 들어가서는 안 된다는 점은 같다.

---

## 20.5 흔한 실수

Conclusions·heading 양쪽에서 반복되는 실수는 다음과 같다.

- "In summary, we showed A, B, and C." — A·B·C는 이미 abstract와 Results에 있다. 한 단계 위로 올라가지 않았다.
- Conclusions에 future work 한 줄만 달랑 쓰는 경우 — higher-level analysis가 비어 있다. future work는 Conclusions의 *마지막 phrase*지 *전부*가 아니다.
- 헤딩 길이가 들쭉날쭉한 경우 — 한 섹션 안에 10자 헤딩과 90자 헤딩이 섞이면 평행성이 깨진다. 같은 스케일의 헤딩은 길이가 비슷해야 skim에서 리듬이 살아난다.
- claim-style 헤딩에서 동사가 빠지는 경우 — "BEV-based Loop Closure"는 명사구다. claim이 되려면 동사가 들어가야 한다.

---

## 20.6 점검 절차

claim-style 헤딩은 본문 한 섹션에서 결론 문장을 먼저 추출한 뒤 만든다. 그 문장을 SVO로 다듬고, 길이 제약 안에서 잘라 내며, 같은 섹션 안의 헤딩 길이와 문장 구조를 맞춘다. outline iteration 후반부에서 사람이 손으로 반복해야 하는 절차다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §III (information-rich subheadings, conclusions as higher-level analysis). [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7 (declarative statements, 보조). 로보틱스 5쌍은 이 장에서 정리했다.

다음: [Part 2 그룹 C — 섹션별 작성법](./chapter_22_title_abstract.md)
