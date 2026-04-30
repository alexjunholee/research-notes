# Ch.26 — 결과와 논의

Results와 Discussion이 별도 섹션이라는 사실이 신입생 입장에서 가장 자주 흐려지는 frame이다. *결과의 명시*와 *결과의 해석*이 한 섹션에 섞이면 reviewer 입장에서 어느 줄이 새 정보이고 어느 줄이 해석인지 추적이 안 된다. ch04 §5의 *content와 conclusion 스케일이 섞인다* 결함이 두 섹션 사이에서 가장 자주 발현한다.

[Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 5와 rule 8이 두 섹션의 분담을 정식화한다. Results는 figure·table·숫자가 박히는 곳, Discussion은 *왜 그런 결과가 나왔는가*와 *어디까지가 한계인가*를 받는 곳. 결국 새 결과는 Discussion에 들어가지 않는다는 한 줄이 두 섹션을 가르는 분기점이다.

---

## 26.1 Results의 골격 — Method를 거꾸로

🔴 **Results의 각 sub-section은 Method의 각 sub-section을 거꾸로 받는다.** ch10 §1에서 본 짝짓기의 출구. Method의 procedure가 Results의 figure·table을 만들고, 그 figure·table이 다시 Results의 sub-section 골격을 정한다.

🟡 **Default 골격 4단.**

1. **Main result vs SOTA 비교** — 핵심 비교 표. 본인 방법이 분야 SOTA 대비 어디에 있는가.
2. **Qualitative figure 1-2개** — 정량적 비교가 못 보여 주는 부분(궤적 시각화·실패 사례 비교 등).
3. **Ablation** — component별 효과 검증.
4. **Failure case** — 본인 방법이 깨지는 지점. limitation 섹션과 짝짓기.

🟡 **Sub-heading은 claim style.** ch05의 권고가 가장 강하게 작동하는 곳이 Results다. "Loop closure recall improves 14% with multi-scale BEV"가 sub-heading 한 줄에 박혀 있으면 skim 단계에서 main message가 그대로 전달된다.

---

## 26.2 Ablation — 변인 통제

🔴 **Ablation 부재는 단일 reject 사유.** 어떤 component가 어떤 효과를 만드는가가 검증되지 않은 채 결과만 던지면 reviewer 입장에서 *어떤 부분이 진짜 작동하는가*를 추적 못 한다. ch01 §1의 reject complement 항목에서 가장 자주 잡히는 결함 중 하나다.

🟡 **Ablation 표 구성.** row = 제거된 component (또는 변경된 변인), column = 결과 metric. Full method (baseline)가 첫 행 또는 마지막 행. 표 한 컷 예시.

| Variant | KITTI ATE (m) ↓ | KITTI RTE (%) ↓ | Runtime (ms) ↓ |
|---|---|---|---|
| **Ours (full)** | **0.42** | **0.61** | **18** |
| w/o geometric prior | 0.58 | 0.84 | 15 |
| w/o multi-scale fusion | 0.51 | 0.73 | 14 |
| w/o loop closure | 0.71 | 1.12 | 12 |

🔴 **Component 한 번에 하나씩.** 두 component를 동시에 제거하면 reviewer가 *어느 쪽 효과인가*를 추적 못 한다. component 둘의 *상호작용*을 보고 싶으면 별도 행 (w/o A + B)으로 추가.

---

## 26.3 통계 유의성과 공정 비교

🔴 **Main result 표에 std 또는 95% CI.** 단일 run은 reviewer 입장에서 *우연일 수 있다*. seed 3-5회 average + std가 분야 default. seed 값까지 명시.

🔴 **Hyperparameter 검색 budget 동일.** 본인 방법은 grid search 100회 돌리고 baseline은 default 1회만 돌린 비교는 desk reject 사유. 두 방법에 같은 budget을 할당했음을 명시.

🔴 **Dataset split·evaluation protocol 일치.** KITTI sequence 00-10 train, 11-21 test 같은 standard split을 *옮기면* reviewer가 의심한다. split을 옮길 이유가 있으면 *왜 옮겼는가*를 본문에 한 줄.

🟡 **본인 방법의 best column 갯수.** 분야 reviewer가 받아들이는 강도는 *본인 방법이 best 또는 second-best를 차지하는 column 비율*에 비례한다. 모든 column에서 best일 필요는 없다. 한두 column에서 second-best여도 *왜 second-best인가*가 Discussion에서 받아지면 강도가 살아남는다.

---

## 26.4 Discussion — 결과의 해석

🟡 **Discussion 골격 4단.** Mensh-Kording rule 8 근거.

1. **핵심 발견의 *왜***. 결과가 *왜* 그런 형태로 나왔는가.
2. **분야 합의와의 관계.** Related Work의 분류 axis 위에서 본인 결과가 어디에 위치하는가.
3. **한계.** 방법의 가정·실험 범위·계산 복잡도.
4. **다음 단계.** 짧게.

🔴 **Limitation 섹션 누락 또는 *한계 없음* 선언은 desk reject.** 모든 방법은 한계가 있다. 명시하지 않으면 reviewer가 *공격 빌미*로 잡는다. ch17 rebuttal에서도 limitation 언급이 미리 박혀 있으면 review의 비판이 *이미 답변된 항목*으로 흡수된다.

🟡 **한계 default 세 항목.** 방법의 *가정*(예: static environment 가정), 실험 *범위*(예: 실내 dataset만 검증), *계산 복잡도*(예: $O(N^2)$ memory). 분야별로 추가.

🔴 **Discussion에 새 결과 등장 금지.** 새 숫자, 새 figure, 새 ablation은 Results의 몫이다. Discussion이 *해석*이 아니라 *추가 결과*가 되면 두 섹션의 분담이 무너진다.

---

## 26.5 분야 standard — 벤치마크 표 작성

분야별로 default 벤치마크 dataset과 metric이 정해져 있다. 그 default를 따르지 않으면 reviewer가 *왜 standard에서 벗어나는가*를 본문 어디서도 받지 못한다.

| 분야 | Default dataset | Default metric |
|---|---|---|
| Visual SLAM | KITTI · TUM RGB-D · EuRoC | ATE · RTE |
| LiDAR SLAM | KITTI · MulRan · Newer College | ATE · RTE · Loop closure recall |
| 3D 재구성 | ScanNet · Tanks and Temples · Replica | F-score · 정확도 · 완전성 |
| Object detection | COCO · LVIS · Open Images | mAP · AP@[0.5:0.95] |

🟡 **표 직전 paragraph가 표를 읽는 법을 한 줄로.** "Bold marks the best in each column. Underline the second best." 한 줄이 빠지면 reviewer가 매번 caption을 backtrack한다. ch13 §3에서 더 자세히.

🟡 **본인 방법 row 강조.** 음영 또는 별표. 표 아래 footnote에 *Our method* 라벨. reviewer skim 단계에서 *어느 row가 본인 방법인가*가 한 눈에 잡혀야 한다.

분야 instantiation은 [robotics-practice ch20 § 20.8.2](https://github.com/jhlee9633/robotics-practice/blob/main/ch20.md)에 link로 위임. ablation·변인 통제·통계 유의성·공정 비교의 분야별 사례가 거기에 있다.

---

## 26.6 흔한 실수 5종

🔴 **Ablation 부재.** component별 효과 검증 안 됨. 단일 reject 사유.

🔴 **단일 run.** std/CI 부재. 우연성 미통제.

🔴 **불공정 비교.** hyperparameter budget·dataset split 비대칭.

🔴 **Discussion에 새 결과.** content와 conclusion 스케일 혼합.

🟡 **Limitation 누락.** 공격 빌미 자가 노출.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 5·8 — Results·Discussion 골격. 분야 standard — KITTI·TUM·ScanNet 벤치마크 표. [robotics-practice ch20 § 20.8.2](https://github.com/jhlee9633/robotics-practice/blob/main/ch20.md) — ablation·통계 유의성·공정 비교 분야 instantiation (link). 흔한 실수 5종과 ablation·통계 권고는 자체.

다음: [Ch.12 — Figures: 안티패턴과 좋은 패턴](./chapter_27_figures.md)