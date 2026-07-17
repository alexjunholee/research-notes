# Ch.26 — 결과와 논의

Results와 Discussion의 분리 여부는 venue와 논문 형식에 따라 다르다. 두 섹션을 합치더라도 결과의 명시와 해석을 문단 안에서 구분해야 어느 줄이 관측이고 어느 줄이 해석인지 추적할 수 있다. ch04 §5에서 다룬 content와 conclusion 층위의 혼합이 여기서 다시 나타난다.

[Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7은 Results의 논리 구조를, rule 8은 Discussion의 해석·한계·의의를 다룬다. Results에는 주장을 뒷받침하는 그림·표·관측이 들어가고, Discussion에는 그 결과의 해석과 한계가 들어간다. 새 결과를 어디에 둘지는 venue 형식에 따르되, 해석의 근거가 되는 관측을 독자가 찾을 수 있어야 한다.

---

## 26.1 Results의 골격 — Method를 거꾸로

**Results의 각 서브섹션은 Method의 서브섹션을 거꾸로 받는다.** ch10 §1에서 본 짝짓기의 결과다. Method의 절차가 Results의 그림·표를 만들고, 그 그림·표가 다시 Results의 서브섹션 골격을 정한다.

**이 장의 출발 골격은 4단이다.** 모든 논문에 네 항목이 필요한 것은 아니며 중심 claim에 맞춰 고른다.

1. **Main result 비교** — 핵심 비교 표. 본인 방법이 가장 가까운 기존 방법과 공개된 최신 비교군 대비 어디에 있는가.
2. **정성적 그림 1-2개** — 정량적 비교가 못 보여 주는 부분(궤적 시각화·실패 사례 비교 등).
3. **Ablation** — component별 효과 검증.
4. **Failure case** — 본인 방법이 깨지는 지점. limitation 섹션과 짝짓기.

**소제목은 주장형으로 쓴다.** ch05의 권고가 가장 강하게 작동하는 곳이 Results다. "Loop closure recall improves 14% with multi-scale BEV"는 형식을 보이기 위한 가상 수치다. 실제 소제목에는 검증된 결과만 넣는다.

---

## 26.2 Ablation — 변인 통제

**Component별 기여를 주장한다면 ablation이 필요하다.** 어떤 component가 어떤 효과를 만드는지 주장하면서 이를 분리해 검증하지 않으면 실제로 어느 부분이 작동하는지 추적할 수 없다. ablation이 모든 논문에 의무인 것은 아니지만, component-level claim에는 그에 맞는 검증이 따라야 한다.

**Ablation 표 구성.** 행에는 제거한 component(또는 변경한 변인)를, 열에는 결과 metric을 둔다. Full method는 첫 행이나 마지막 행에 둔다. 아래 수치는 형식을 보이기 위한 가상 값이다.

| Variant | KITTI ATE (m) ↓ | KITTI RTE (%) ↓ | Runtime (ms) ↓ |
|---|---|---|---|
| **Ours (full)** | **0.42** | **0.61** | **18** |
| w/o geometric prior | 0.58 | 0.84 | 15 |
| w/o multi-scale fusion | 0.51 | 0.73 | 14 |
| w/o loop closure | 0.71 | 1.12 | 12 |

**Component는 한 번에 하나씩 제거한다.** 두 component를 동시에 제거하면 심사위원은 어느 쪽의 효과인지 추적할 수 없다. 두 component의 상호작용을 보고 싶으면 별도 행(w/o A + B)을 추가한다.

---

## 26.3 통계 유의성과 공정 비교

**반복 가능한 확률적 실험에는 변동성을 함께 보고한다.** 표본과 estimand에 맞춰 std, standard error, confidence interval, 분포 그림 가운데 적절한 것을 고른다. 실행 횟수는 계산 비용·분산·분야 protocol로 정하며, 모든 분야에 통하는 3-5회 규칙은 없다. seed와 집계 방법도 명시한다.

**Hyperparameter 비교 기회를 공정하게 둔다.** 본인 방법만 넓게 탐색하고 baseline은 검증 없이 기본값으로 두면 비교가 본인 방법에 유리해진다. 방법마다 탐색 공간이 다를 수 있으므로 기계적으로 같은 trial 수만 강제하지 말고, 공식 설정·검증 protocol·탐색 공간·계산 budget을 모두 보고한다.

**Dataset split·evaluation protocol을 일치시킨다.** 공식 benchmark나 직접 비교 논문이 지정한 split과 metric을 확인한다. 다른 split을 쓴다면 이유를 설명하고, baseline도 같은 protocol에서 다시 평가했는지 밝힌다. KITTI처럼 task마다 공개 ground truth와 test server 구성이 다른 dataset은 해당 task의 공식 지침을 따른다.

**Best 열의 개수로 논문을 평가하지 않는다.** 사전에 정한 주 metric과 claim에 필요한 trade-off를 본다. 정확도·runtime·memory·robustness 가운데 무엇을 개선했고 무엇을 양보했는지 Discussion에서 설명한다.

---

## 26.4 Discussion — 결과의 해석

**Discussion 골격 4단.** Mensh-Kording rule 8에 근거한다.

1. **핵심 발견의 원인.** 결과가 왜 그런 형태로 나왔는가.
2. **분야 합의와의 관계.** Related Work의 분류 axis 위에서 본인 결과가 어디에 위치하는가.
3. **한계.** 방법의 가정·실험 범위·계산 복잡도.
4. **다음 단계.** 짧게.

**한계를 명시한다.** 별도 Limitation 섹션의 필요 여부는 venue policy를 따르지만, 방법의 가정·실험 범위·계산 비용은 Discussion이나 지정된 섹션에서 밝혀야 한다. "한계가 없다"는 선언 대신 현재 검증이 닿는 범위를 적는다.

**한계 기본 세 항목.** 방법의 가정(예: static environment 가정), 실험 범위(예: 실내 dataset만 검증), 계산 복잡도(예: $O(N^2)$ memory). 분야별로 추가.

**Discussion에 새 결과 등장 금지.** 새 숫자, 새 그림, 새 ablation은 Results의 몫이다. Discussion이 해석이 아니라 추가 결과가 되면 두 섹션의 분담이 무너진다.

---

## 26.5 분야별 벤치마크 후보

분야별로 널리 쓰이는 benchmark와 metric이 있지만 task·sensor·연도에 따라 달라진다. 아래 표는 후보를 찾는 출발점이지 공식 표준 목록이 아니다. 실제 제출에서는 benchmark의 공식 evaluation page와 직접 비교 논문의 protocol을 확인한다.

| 분야 | Default dataset | Default metric |
|---|---|---|
| Visual SLAM | KITTI · TUM RGB-D · EuRoC | ATE · RTE |
| LiDAR SLAM | KITTI · MulRan · Newer College | ATE · RTE · Loop closure recall |
| 3D 재구성 | ScanNet · Tanks and Temples · Replica | F-score · 정확도 · 완전성 |
| Object detection | COCO · LVIS · Open Images | mAP · AP@[0.5:0.95] |

**표 직전 단락에서 표를 읽는 법을 한 줄로 설명한다.** "Bold marks the best in each column. Underline the second best." 한 줄이 빠지면 심사위원이 매번 캡션을 backtrack한다. ch13 §3에서 더 자세히.

**본인 방법 row 강조.** 음영 또는 별표. 표 아래 footnote에 Our method 라벨. 심사위원의 skim 단계에서 어느 row가 본인 방법인가가 한눈에 잡혀야 한다.

분야별 사례는 [robotics-practice ch20 § 20.8.2](https://alexjunholee.github.io/robotics-practice/guide.html#2082-실험-설계와-ablation)에 링크로 둔다. ablation·변인 통제·통계 유의성·공정 비교의 분야별 사례가 거기에 있다.

---

## 26.6 흔한 실수 5종

**Ablation 부재.** component별 기여를 주장하지만 효과를 분리해 검증하지 않음.

**단일 run.** std/CI 부재. 우연성 미통제.

**불공정 비교.** hyperparameter budget·dataset split 비대칭.

**Discussion에 새 결과.** content와 conclusion 스케일 혼합.

**Limitation 누락.** 공격 빌미 자가 노출.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rules 7·8 — Results의 논리와 Discussion의 역할. [robotics-practice ch20 §20.8.2](https://alexjunholee.github.io/robotics-practice/guide.html#2082-실험-설계와-ablation) — ablation·통계·공정 비교의 적용 사례. benchmark 표와 통계 보고 방식은 task의 공식 protocol과 연구 설계에 맞춰 다시 확인한다.

다음: [Ch.12 — Figures: 안티패턴과 좋은 패턴](./chapter_27_figures.md)
