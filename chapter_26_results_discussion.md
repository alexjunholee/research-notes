# Ch.26 — 결과와 논의

Results와 Discussion을 나눌지 합칠지는 학회·학술지와 논문 형식에 따라 다르다. 두 섹션을 합치더라도 문단 안에서 결과를 밝히는 문장과 해석하는 문장을 구분해야 독자가 어느 문장이 관측이고 어느 문장이 해석인지 가려낼 수 있다. [Ch.19 §19.5](./chapter_19_ccc.md)에서 다룬, content와 conclusion이 한 문단에 뒤섞이는 결함이 여기서도 나타난다.

[Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)은 rule 7에서 Results의 논리 구조를, rule 8에서 Discussion이 다룰 내용(빈틈을 어떻게 메웠는지, 해석의 한계, 분야에 주는 의미)을 다룬다. Results에는 주장을 뒷받침하는 그림, 표, 관측을 싣고, 결과의 해석과 한계는 Discussion에서 다룬다. 새 결과를 어디에 둘지는 학회·학술지 형식을 따르되, 해석의 근거가 되는 관측을 독자가 찾을 수 있어야 한다.

---

## 26.1 Results의 골격 — Method와 맞추기

**Results의 서브섹션은 Method의 서브섹션과 하나씩 대응한다.** [Ch.25 §25.1](./chapter_25_method.md)에서 Method의 순서를 Results에 맞춘 결과다. Method의 절차로 Results의 그림과 표를 만들고, 그 그림과 표가 Results의 서브섹션을 이룬다.

**처음 골격은 아래 항목으로 잡아 본다.** 모든 논문에 모든 항목이 필요하지는 않다. 중심 주장에 맞춰 고른다.

1. **주요 결과 비교** — 핵심 비교 표. 자기 방법을 가장 가까운 기존 방법, 공개된 최신 방법과 비교한다.
2. **정성 비교 그림 한두 개** — 궤적 시각화나 실패 사례 비교처럼 수치 비교로 드러나지 않는 부분을 보여 준다.
3. **Ablation** — 구성 요소(component)를 하나씩 빼 보며 각각의 효과를 검증한다.
4. **실패 사례(failure case)** — 자기 방법이 실패하는 조건을 보여 주고, 한계를 다루는 부분과 연결한다.

**소제목은 주장을 담은 문장으로 쓴다.** [Ch.20](./chapter_20_subheadings_and_conclusions.md)의 권고는 Results에 가장 잘 맞는다. Mensh와 Kording도 rule 7에서 결과가 주장을 뒷받침하는 논리를 서술문으로 바꿔 Results의 서브섹션 제목으로 쓰라고 했다. "Loop closure recall improves 14% with multi-scale BEV"는 형식을 보여 주려고 지어낸 예다. 실제 소제목에는 검증한 결과만 넣는다.

---

## 26.2 Ablation — 구성 요소를 하나씩 빼 보기

**구성 요소마다 기여를 주장한다면 ablation이 필요하다.** 어느 구성 요소가 어떤 효과를 내는지 보이려면 구성 요소를 하나씩 떼어 내고 결과를 비교해야 한다.

**Ablation 표 구성.** 행에는 뺀 구성 요소(또는 바꾼 설정)를, 열에는 결과 metric을 둔다. 전체 방법(full method)은 첫 행이나 마지막 행에 둔다. 아래 수치는 표의 배치를 보여 주려고 지어낸 것이다.

| Variant | KITTI ATE (m) ↓ | KITTI RTE (%) ↓ | Runtime (ms) ↓ |
|---|---|---|---|
| **Ours (full)** | **0.42** | **0.61** | **18** |
| w/o geometric prior | 0.58 | 0.84 | 15 |
| w/o multi-scale fusion | 0.51 | 0.73 | 14 |
| w/o loop closure | 0.71 | 1.12 | 12 |

**구성 요소는 한 번에 하나씩 뺀다.** 두 개를 함께 빼면 어느 쪽의 효과인지 가릴 수 없다. 두 구성 요소의 상호작용을 보고 싶으면 둘을 함께 뺀 행(w/o A + B)을 따로 넣는다.

---

## 26.3 통계 유의성과 공정한 비교

**무작위성이 있는 실험을 반복할 수 있다면 결과의 변동도 함께 보고한다.** 표본과 추정 대상(estimand)에 맞춰 표준편차(std), 표준오차, 신뢰구간, 분포 그림 가운데 맞는 것을 고른다. 실행 횟수는 계산 비용, 결과의 분산, 분야의 표준 평가 절차를 함께 따져 정한다. seed와 결과를 모은 방법도 적는다.

**hyperparameter를 조정할 기회를 공정하게 준다.** 자기 방법만 넓게 탐색하고 baseline은 검증 없이 기본값으로 두면 비교가 자기 방법에 유리해진다. 방법마다 탐색 공간이 다를 수 있으니 시도 횟수만 똑같이 맞추지 말고, 공식 설정, 검증 절차, 탐색 공간, 계산 예산을 모두 보고한다.

**dataset split과 평가 절차(evaluation protocol)를 맞춘다.** 공식 benchmark나 직접 비교하는 논문이 정한 split과 metric을 확인한다. 다른 split을 쓴다면 이유를 설명하고, baseline도 같은 절차로 다시 평가했는지 밝힌다. KITTI처럼 task마다 공개 ground truth와 test server 구성이 다른 dataset은 해당 task의 공식 지침을 따른다.

**미리 정한 주 metric으로 평가한다.** 주 metric과 함께, 주장에 필요한 trade-off도 본다. 정확도, runtime, 메모리, 강건성 가운데 무엇을 개선했고 무엇을 내주었는지 Discussion에서 설명한다.

---

## 26.4 Discussion — 결과의 해석

**Mensh와 Kording이 rule 8에서 든 Discussion의 순서는 다음과 같다.**

1. **첫 문단은 Results의 중요한 발견을 요약한다.** 결과를 꼼꼼히 읽지 않은 독자도 이 문단에서 요지를 얻는다. 두 사람이 든 예에서 이 요약은 결과의 의미에 초점을 맞춘다.
2. **이어지는 문단은 논문의 약점이나 강점을 하나씩 다룬다.** 각 문단은 약점이나 강점을 관련 문헌과 이어서 평가하고, 앞으로의 실험으로 약점을 어떻게 다룰 수 있는지 말하기도 한다.
3. **마지막 문단은 이 논문이 분야를 어떻게 앞으로 나아가게 하는지 말한다.**

**한계를 밝힌다.** Limitation 섹션을 따로 둘지는 학회·학술지 규정을 따르되, 방법의 가정, 실험 범위, 계산 비용은 Discussion이나 규정이 정한 섹션에서 밝힌다. "한계가 없다"고 쓰지 말고 지금의 검증이 어디까지 닿는지 적는다.

**한계로 먼저 살펴볼 것.** 방법의 가정(예: 정적인 환경을 가정함), 실험 범위(예: 실내 dataset에서만 검증함), 계산 복잡도(예: 메모리가 $O(N^2)$로 늘어남)를 먼저 본다. 분야에 따라 항목을 더한다.

**Results와 Discussion을 나누는 형식이면 새 결과는 Results에 둔다.** 새 수치, 새 그림, 새 ablation은 Results에 싣는다. Discussion에 추가 실험 결과가 끼어들면 독자는 어디까지가 결과이고 어디부터가 해석인지 가리기 어렵다.

---

## 26.5 분야별 벤치마크 후보

분야마다 널리 쓰는 benchmark와 metric이 있지만, task와 센서, 연도에 따라 달라진다. 아래 표는 후보를 찾는 출발점이고 공식 표준 목록은 아니다. 실제로 제출할 때는 benchmark의 공식 평가 페이지와 직접 비교하는 논문의 평가 절차를 확인한다.

| 분야 | 데이터셋 후보 | 지표 후보 |
|---|---|---|
| Visual SLAM | KITTI · TUM RGB-D · EuRoC | ATE · RTE |
| LiDAR SLAM | KITTI · MulRan · Newer College | ATE · RTE · Loop closure recall |
| 3D 재구성 | ScanNet · Tanks and Temples · Replica | F-score · 정확도 · 완전성 |
| Object detection | COCO · LVIS · Open Images | mAP · AP@[0.5:0.95] |

**방법별 결과를 비교하는 표에는 강조 규약을 한 줄로 적는다.** 예를 들면 "Bold marks the best in each column. Underline marks the second best." 같은 문장을 캡션이나 표 아래 각주에 둔다. 이 한 줄이 없으면 심사위원은 굵은 글씨와 밑줄이 무엇을 뜻하는지 짐작해야 한다. 자세한 내용은 [Ch.28 §28.2](./chapter_28_tables.md)에 있다.

**자기 방법의 행을 눈에 띄게 한다.** 음영이나 별표로 표시하고, 표 아래 각주에 "Ours" 같은 표시가 무엇인지 적는다. 심사위원이 표를 훑어볼 때 어느 행이 자기 방법인지 바로 알아볼 수 있어야 한다.

ablation, 변인 통제, 반복 실험, 공정한 비교의 요점은 [robotics-practice ch20 §20.8.2](https://alexjunholee.github.io/robotics-practice/guide.html#208-연구-실전)에 있다.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 7(Results의 논리, 서술문 소제목), rule 8(Discussion의 순서와 한계). [robotics-practice ch20 §20.8.2](https://alexjunholee.github.io/robotics-practice/guide.html#208-연구-실전) — ablation, 변인 통제, 반복 실험, 공정한 비교의 요점. benchmark 표와 통계 보고 방식은 task의 공식 평가 절차와 연구 설계에 맞춰 다시 확인한다.

다음: [Ch.27 — 그림: 안티패턴과 좋은 패턴](./chapter_27_figures.md)
