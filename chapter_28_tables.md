# Ch.28 — Tables: 비교의 자리

ch12의 figure가 분포·궤적·qualitative를 보여 준다면, table은 수치 비교를 받는다. 두 영역의 결정 기준이 다른 만큼, figure를 표로 옮기거나 표를 figure로 옮기는 작업이 항상 한쪽을 약화시킨다. 분포가 중요한 곳에 표를 박으면 분포가 사라지고, 정확한 수치 비교가 중요한 곳에 figure를 박으면 reviewer가 bar 길이에서 수치를 추출해야 한다.

[cxli233 (GitHub)의 Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends)가 figure 안티패턴을 카탈로그한 것처럼, table 안티패턴도 분야에서 정형화된 형태로 반복된다. 이 장은 ch12와 같은 방식으로 table의 안티패턴과 좋은 패턴을 정리한다.

---

## 28.1 안티패턴 5종

**강조 표시 일관성 부재.** 본인 방법은 bold, baseline은 plain. 그런데 ablation 표에서는 best component가 underline. 한 논문 안에서 강조의 의미가 표마다 바뀌면 reviewer가 매번 caption을 backtrack해야 한다. 한 논문 한 규약 — bold = best, underline = second best가 분야에서 가장 안전한 기본.

**너무 많은 column.** KITTI 11 시퀀스를 모두 column으로 박으면 표가 한 페이지를 넘는다. 시퀀스를 row로, metric을 column으로 (또는 그 반대) 일관되게. 표 하나에 5-15 row × 3-7 column이 가독성 한계.

**Vertical line 남발.** LaTeX 기본 `|`가 모든 column 사이에 들어가는 패턴. booktabs(`\toprule`, `\midrule`, `\bottomrule`만)가 분야 표준이고, vertical line 0개가 권고.

**Default 폰트 크기.** 표가 본문 폰트와 같은 크기면 cell 여백이 부족해 답답하게 읽힌다. `\small` 또는 `\footnotesize`로 한 단계 줄이면 cell 호흡이 살아난다.

**숫자 정렬 부재.** 0.143과 0.07이 한 column에 섞여 있는데 소수점 위치가 안 맞으면 시각적 비교가 깨진다. `siunitx` package 또는 `\phantom{0}`으로 자릿수 맞추기. 한 column 안에서 모든 숫자의 소수점이 같은 위치에 와야 한다.

---

## 28.2 좋은 패턴

**Booktabs.** `\toprule` (표 상단), `\midrule` (header와 body 사이), `\bottomrule` (표 하단). vertical line 0개. column 그룹이 필요하면 `\cmidrule{2-4}`로 부분 horizontal line. 분야 reviewer 입장에서 가장 빠르게 완성도를 받는 패턴이다.

**강조 규약 명시.** caption 첫 줄 또는 표 하단 footnote에 명시. Bold marks the best, underline the second best in each column. 한 논문의 모든 표가 같은 규약을 공유한다.

**Caption 구조 3단.**

1. **한 줄 takeaway.** "Method A consistently outperforms baselines on KITTI sequences 00-10."
2. **표 읽는 법.** bold/underline 의미·dataset split·평균 횟수.
3. **통계.** std 또는 95% CI·n·seed.

**본인 방법 row 강조.** 음영(`\rowcolor{gray!15}`) 또는 별표. 표 아래 footnote에 Our method 라벨. reviewer skim 단계에서 어느 row가 본인 방법인가가 한 눈에 잡혀야 한다 — ch11 §5와 같은 권고.

---

## 28.3 세 종류 — 비교 표·ablation 표·hyperparameter 표

**비교 표.** row = method, column = dataset/sequence × metric. 본인 방법 한 줄, baseline 5-10줄. 분야 standard SOTA가 빠지면 desk reject — ch11 §3 항목. column이 많아지면 dataset별로 표를 나눈다.

| Method | KITTI 00 ATE ↓ | KITTI 09 ATE ↓ | TUM fr1 ATE ↓ | Runtime ↓ |
|---|---|---|---|---|
| ORB-SLAM3 | 0.51 | 1.34 | 0.018 | 22 ms |
| LIO-SAM | 0.42 | 0.91 | — | 28 ms |
| **Ours** | **0.38** | <u>0.73</u> | **0.012** | **18 ms** |

**Ablation 표.** row = removed component, column = metric. 첫 행 또는 마지막 행이 full method (baseline). 한 component씩 제거. ch11 §2의 표 예시가 같은 형태.

**Hyperparameter 표.** row = parameter, column = value · meaning · sensitivity. 마지막 column이 ablation 섹션과 직결 — 변경 시 RTE 0.84 → 0.61처럼 sensitivity가 박혀 있으면 reviewer가 ablation에서 검증된 항목을 한 눈에 받는다.

---

## 28.4 흔한 실수 4종

**강조 일관성 부재.** bold/underline의 의미가 표마다 다름. 한 논문 한 규약을 어김.

**Column 폭주.** row와 column 축이 잘못 잡힘. 시퀀스가 column에 가서 표가 가로로 넘침.

**숫자 정렬 부재.** 소수점이 어긋남. 시각적 비교가 깨짐.

**Caption 한 줄 takeaway 부재.** 표만 보고 결론을 못 잡음. ch12 §3의 figure caption 권고와 같은 권고.

---

## 28.5 ch12와의 결정 기준

figure와 table 중 어느 쪽에 정보를 박을지 결정하는 기준은 다음과 같다.

- **분포가 중요하면** figure (strip plot · violin · box). row 5개 column 3개 표는 분포를 못 보여 준다.
- **정확한 수치 비교가 중요하면** table. figure의 bar 길이에서 reviewer가 수치를 추출해야 하면 비교 정확도가 떨어진다.
- **Trajectory·spatial 정보면** figure (궤적 시각화·heatmap·error map). 표가 spatial 정보를 못 받는다.
- **Method 간 다차원 비교면** table. 5-7 dimension의 비교는 figure로 표현하기 어렵다.

두 매체가 같은 결과를 중복해서 보여 주면 한쪽을 빼는 것이 권고. 같은 KITTI 결과를 figure 하나와 표 하나로 동시에 박으면 한쪽이 잉여로 남는다. figure는 qualitative trajectory, 표는 quantitative metric 비교로 분담.

LaTeX 도구(booktabs·algorithm2e)의 자세한 사용법은 [robotics-practice ch20 § 20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#2085-도구)에 링크로 둔다.

---

**출처.** [cxli233 (GitHub), Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends) — 안티패턴 문체 기준 (chart 카탈로그를 table로 적용). [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) — figure/table 일반 원칙 (간접). [robotics-practice ch20 § 20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#2085-도구) — booktabs·algorithm2e LaTeX (link). 안티패턴 5종, 좋은 패턴, 세 종류 분류, 흔한 실수 4종은 이 장에서 정리했다.

다음: [Ch.14 — 문장 구조와 독자 기대](./chapter_29_reader_expectations.md)
