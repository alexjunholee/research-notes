# Ch.28 — 표: 비교의 자리

ch12의 그림이 분포·궤적·qualitative를 보여 준다면, 표는 수치 비교를 맡는다. 두 영역의 결정 기준이 다르므로 그림을 표로 옮기거나 표를 그림으로 옮기면 한쪽의 장점이 약해진다. 분포가 중요한 곳에 표를 두면 분포가 사라지고, 정확한 수치 비교가 중요한 곳에 그림을 두면 심사위원이 bar 길이에서 수치를 추출해야 한다.

[cxli233 (GitHub)의 Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends)가 그림 안티패턴을 목록으로 정리한 것처럼, 표 안티패턴도 분야에서 정형화된 형태로 반복된다. ch12와 같은 방식으로 표의 안티패턴과 좋은 패턴을 살펴본다.

---

## 28.1 안티패턴 5종

**강조 표시 일관성 부재.** 본인 방법은 bold, baseline은 plain으로 표시하면서 ablation 표에서는 best component에 underline을 쓰는 식이다. 한 논문 안에서 강조의 의미가 표마다 바뀌면 심사위원이 매번 캡션을 되짚어야 한다. `bold = best`, `underline = second best`는 흔한 규약이지만 유일한 표준은 아니다. venue template와 접근성을 확인하고 선택한 의미를 캡션에서 밝힌다.

**너무 많은 column.** KITTI 11 시퀀스를 모두 column에 넣으면 표가 지면 폭을 넘을 수 있다. 시퀀스를 row로, metric을 column으로 두거나 그 반대로 두되 일관성을 지킨다. 5-15 row × 3-7 column은 초안 점검용 범위일 뿐 가독성의 보편 한계가 아니다. 실제 지면과 글자 크기로 확인한다.

**Vertical line 남발.** LaTeX 기본 `|`를 모든 column 사이에 넣으면 구획선이 데이터보다 두드러질 수 있다. `booktabs`의 `\toprule`, `\midrule`, `\bottomrule`은 널리 쓰이는 선택지다. vertical line을 쓸지는 venue template와 복잡한 column grouping의 필요를 보고 정한다.

**지나치게 작은 폰트.** 표를 맞추려고 `\small`·`\footnotesize`를 반복 적용하면 인쇄와 화면에서 읽기 어려워진다. 먼저 column 수와 문구를 줄이고, venue가 허용하는 최소 글자 크기 안에서만 조정한다.

**숫자 정렬 부재.** 0.143과 0.07이 한 column에 섞여 있는데 소수점 위치가 안 맞으면 시각적 비교가 깨진다. `siunitx` package 또는 `\phantom{0}`으로 자릿수 맞추기. 한 column 안에서 모든 숫자의 소수점이 같은 위치에 와야 한다.

---

## 28.2 좋은 패턴

**Booktabs.** `\toprule`(표 상단), `\midrule`(header와 body 사이), `\bottomrule`(표 하단)을 쓰고, column 그룹에는 `\cmidrule{2-4}`를 쓸 수 있다. 장식선보다 데이터 grouping이 먼저 보이게 만드는 한 가지 구현이다.

**강조 규약 명시.** 캡션 첫 줄이나 표 하단 footnote에 "Bold marks the best, underline the second best in each column"처럼 적는다. 한 논문의 모든 표가 같은 규약을 공유한다.

**캡션 구조 3단.**

1. **한 줄 takeaway.** "Method A consistently outperforms baselines on KITTI sequences 00-10."
2. **표 읽는 법.** bold/underline 의미·dataset split·평균 횟수.
3. **통계.** std 또는 95% CI·n·seed.

**본인 방법 row 강조.** 음영(`\rowcolor{gray!15}`)이나 별표를 쓰고, 표 아래 footnote에 Our method라고 표시한다. 심사위원이 훑어 읽는 단계에서 어느 row가 본인 방법인지 한눈에 알아야 한다. ch11 §5와 같은 권고다.

---

## 28.3 세 종류 — 비교 표·ablation 표·hyperparameter 표

**비교 표.** row = 방법, column = dataset/sequence × metric. baseline 수에 고정된 5-10줄 규칙은 없다. 중심 claim과 직접 관련된 강한 비교군, 동일 protocol에서 평가 가능한 방법을 포함한다. column이 많아지면 dataset별로 표를 나눈다. 아래 수치는 layout을 보이기 위한 가상 값이다.

| Method | KITTI 00 ATE ↓ | KITTI 09 ATE ↓ | TUM fr1 ATE ↓ | Runtime ↓ |
|---|---|---|---|---|
| ORB-SLAM3 | 0.51 | 1.34 | 0.018 | 22 ms |
| LIO-SAM | 0.42 | 0.91 | — | 28 ms |
| **Ours** | **0.38** | <u>0.73</u> | **0.012** | **18 ms** |

**Ablation 표.** row = removed component, column = metric. 첫 행 또는 마지막 행이 full method (baseline). 한 component씩 제거. ch11 §2의 표 예시가 같은 형태.

**Hyperparameter 표.** row = parameter, column = value · meaning · sensitivity. 마지막 column은 ablation이나 sensitivity analysis와 연결할 수 있다. `RTE 0.84 → 0.61` 같은 수치는 실제 분석에서 확인된 경우에만 쓰고, 그렇지 않으면 분석 위치를 참조한다.

---

## 28.4 흔한 실수 4종

**강조 일관성 부재.** bold/underline의 의미가 표마다 다르면 한 논문 한 규약을 어긴다.

**Column 폭주.** row와 column 축을 잘못 잡아 시퀀스가 column에 몰리면 표가 가로로 넘친다.

**숫자 정렬 부재.** 소수점이 어긋나면 시각적 비교가 깨진다.

**캡션 한 줄 takeaway 부재.** 표만 보고 결론을 알 수 없다. ch12 §3의 그림 캡션 권고와 같은 내용이다.

---

## 28.5 ch12와의 결정 기준

그림과 표 중 어느 쪽에 정보를 박을지 결정하는 기준은 다음과 같다.

- **분포가 중요하면** 그림 (strip plot · violin · box). row 5개 column 3개 표는 분포를 못 보여 준다.
- **정확한 수치 비교가 중요하면** 표. 그림의 bar 길이에서 심사위원이 수치를 추출해야 하면 비교 정확도가 떨어진다.
- **Trajectory·spatial 정보면** 그림 (궤적 시각화·heatmap·error map). 표로는 공간 정보를 전달하기 어렵다.
- **방법 간 다차원 비교면** 표. 차원이 많아질수록 표가 유리할 수 있지만, column 수보다 독자가 해야 할 비교가 무엇인지 먼저 본다.

두 매체가 같은 정보만 중복하면 한쪽을 빼는 편이 낫다. 같은 KITTI 결과라도 그림이 공간적 실패 패턴을, 표가 정확한 metric을 보여 준다면 서로 보완한다. 각 매체가 답하는 질문을 캡션에서 분리한다.

LaTeX 도구(booktabs·algorithm2e)의 자세한 사용법은 [robotics-practice ch20 § 20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#2085-도구)에 링크로 둔다.

---

**출처.** [cxli233 (GitHub), Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends) — 안티패턴 문체 기준 (chart 카탈로그를 표로 적용). [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) — 그림/표 일반 원칙 (간접). [robotics-practice ch20 § 20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#2085-도구) — booktabs·algorithm2e LaTeX (link). 안티패턴 5종, 좋은 패턴, 세 종류 분류, 흔한 실수 4종은 이 장에서 정리했다.

다음: [Ch.14 — 문장 구조와 독자 기대](./chapter_29_reader_expectations.md)
