# Ch.28 — 표: 수치를 비교하는 자리

Ch.27에서 다룬 그림은 분포와 궤적, 정성 결과(qualitative result)를 보여 준다. 표는 수치를 비교할 때 쓴다. 분포가 중요한 자리에 표를 두면 분포가 보이지 않는다. 정확한 수치를 비교해야 하는 자리에 그림을 두면 심사위원은 막대 길이를 눈으로 재어 수치를 읽어 내야 한다.

[cxli233의 Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends)는 그림에서 되풀이되는 나쁜 패턴(안티패턴)을 목록으로 모았다. 표에서도 비슷한 실수가 비슷한 모양으로 되풀이된다. 이 장에서는 Ch.27처럼 표의 안티패턴과 좋은 패턴을 차례로 본다.

---

## 28.1 안티패턴

**강조 표시가 표마다 다르다.** 비교 표에서는 자기 방법을 bold로, baseline을 보통 글씨로 표시해 놓고, ablation 표에서는 가장 좋은 구성 요소에 밑줄을 긋는 식이다. 강조의 뜻이 표마다 바뀌면 심사위원은 표를 볼 때마다 캡션을 다시 읽어야 한다. `bold = best`, `underline = second best`는 흔히 쓰는 규약이지만 하나뿐인 표준은 아니다. 학회 템플릿과 접근성 지침을 확인해 규약을 고르고, 그 뜻을 캡션에 적는다.

**column이 너무 많다.** KITTI 시퀀스 11개를 모두 column에 넣으면 표가 지면 폭을 넘기 쉽다. 시퀀스를 row에, metric을 column에 두거나 그 반대로 두되, 한 논문 안에서는 한 방식을 지킨다. row 5~15개, column 3~7개는 초안을 점검할 때 쓰는 어림값이다. 읽기 쉬운 한계가 어디인지는 실제 지면과 글자 크기로 확인한다.

**세로선을 모든 column 사이에 긋는다.** LaTeX에서 모든 column 사이에 `|`를 넣으면 구획선이 데이터보다 먼저 눈에 들어온다. `booktabs` 패키지의 `\toprule`, `\midrule`, `\bottomrule`을 많이 쓴다. 세로선을 쓸지는 학회 템플릿과 column 묶음이 얼마나 복잡한지를 보고 정한다.

**글자가 너무 작다.** 표를 지면에 맞추려고 `\small`이나 `\footnotesize`를 거듭 쓰면 인쇄본에서도 화면에서도 읽기 어렵다. column 수와 문구부터 줄이고, 글자 크기는 학회가 허용하는 최소 크기 안에서만 줄인다.

**숫자의 소수점이 어긋난다.** 0.143과 0.07이 한 column에 있는데 소수점 위치가 다르면 눈으로 크기를 비교하기 어렵다. `siunitx` 패키지나 `\phantom{0}`으로 자릿수를 맞춰, 한 column 안의 소수점이 모두 같은 위치에 오게 한다.

---

## 28.2 좋은 패턴

**booktabs를 쓴다.** 표 위에 `\toprule`, header와 본문 사이에 `\midrule`, 표 아래에 `\bottomrule`을 긋는다. column을 묶을 때는 `\cmidrule{2-4}`를 쓴다. 장식선보다 데이터의 묶음이 먼저 보이게 하는 방법 가운데 하나다.

**강조 규약을 적는다.** 캡션 첫 줄이나 표 아래 각주에 "Bold marks the best, underline the second best in each column"처럼 적는다. 한 논문의 모든 표는 같은 규약을 쓴다.

**캡션을 세 부분으로 쓴다.**

1. **요점 한 줄.** "Method A shows lower ATE than the baselines on KITTI sequences 00-10."
2. **표 읽는 법.** bold와 underline의 뜻, dataset split, 몇 번 돌려 평균을 냈는지.
3. **통계.** 표준편차나 95% 신뢰구간, 표본 수 n, seed.

캡션에 요점이 없으면 표만 보고는 결론을 읽어 내기 어렵다. Ch.27 §27.3에서 그림 캡션에 권한 것과 같다.

**자기 방법의 행을 눈에 띄게 한다.** [Ch.26 §26.5](./chapter_26_results_discussion.md)에서 말한 음영은 LaTeX에서 `\rowcolor{gray!15}`로 넣는다.

---

## 28.3 표의 종류: 비교 표, ablation 표, hyperparameter 표

**비교 표.** row에는 방법을, column에는 dataset이나 시퀀스별 metric을 둔다. baseline을 몇 개 넣어야 한다는 규칙은 없다. 중심 주장과 직접 관련된 강한 비교 대상, 같은 평가 protocol로 잴 수 있는 방법을 넣는다. column이 많아지면 dataset별로 표를 나눈다. 아래 수치는 표의 배치를 보여 주려고 지어낸 값이다.

| Method | KITTI 00 ATE ↓ | KITTI 09 ATE ↓ | TUM fr1 ATE ↓ | Runtime ↓ |
|---|---|---|---|---|
| ORB-SLAM3 | 0.51 | 1.34 | 0.018 | 22 ms |
| LIO-SAM | 0.42 | 0.91 | — | 28 ms |
| **Ours** | **0.38** | **0.73** | **0.012** | **18 ms** |

**ablation 표.** row에는 뺀 구성 요소를, column에는 metric을 둔다. 전체 방법(full method)을 첫 행이나 마지막 행에 두고, 구성 요소를 하나씩 뺀 결과를 나란히 놓는다. Ch.26 §26.2의 표가 이 형태다.

**hyperparameter 표.** row에는 parameter를, column에는 값, 뜻, 민감도를 둔다. 민감도 column은 ablation이나 민감도 분석(sensitivity analysis)의 결과와 연결할 수 있다. `RTE 0.84 → 0.61` 같은 수치는 실제 분석으로 확인했을 때만 적는다. 아직 확인하지 않았다면 분석이 실린 절을 가리킨다.

---

## 28.4 그림으로 할지 표로 할지

정보를 그림에 담을지 표에 담을지는 다음 기준으로 정한다.

- **분포가 중요하면** 그림으로 그린다(strip plot, violin plot, box plot). row 5개, column 3개짜리 표로는 분포를 보여 주기 어렵다.
- **정확한 수치를 비교해야 하면** 표로 만든다. 심사위원이 그림의 막대 길이에서 수치를 읽어 내야 하면 비교가 부정확해진다.
- **궤적이나 공간 정보라면** 그림으로 그린다(궤적 시각화, heatmap, error map). 표로는 공간 정보를 전하기 어렵다.
- **여러 방법을 여러 기준으로 비교하면** 표로 만든다. 기준이 많을수록 표가 유리한 경우가 많다. 다만 column 수보다 독자가 무엇을 비교해야 하는지를 먼저 본다.

그림과 표가 같은 정보를 되풀이하기만 한다면 하나를 뺀다. 같은 KITTI 결과라도 그림은 어디서 실패하는지를 공간에 보여 주고 표는 정확한 metric을 보여 준다면, 둘을 함께 둔다. 이때는 각각이 무엇을 보여 주는지 캡션에 따로 적는다.

booktabs와 algorithm2e를 포함한 LaTeX 도구 목록은 [robotics-practice ch20 §20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#208-연구-실전)에 있다.

---

**출처.** [cxli233 (GitHub), Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends) — 그림 안티패턴 목록을 표에 적용했다. [robotics-practice ch20 §20.8.5](https://alexjunholee.github.io/robotics-practice/guide.html#208-연구-실전) — booktabs·algorithm2e. 표의 안티패턴, 좋은 패턴, 표의 종류는 이 장에서 정리했다.

다음: [Ch.29 — 문장 구조와 독자 기대](./chapter_29_reader_expectations.md)
