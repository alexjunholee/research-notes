# Ch.27 — 그림: 안티패턴과 좋은 패턴

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)은 2nd pass에서 그림·도표를 주의 깊게 보고 축과 error bar를 확인하라고 한다. 1st pass의 항목에 그림이 명시된 것은 아니다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9도 그림이 본문보다 더 많은 독자에게 노출된다는 이유로 시간을 더 배분하라고 권한다.

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V는 그림 하나를 5-10회 스케치하는 자신들의 작업 방식을 예로 든다. 핵심은 첫 스케치를 최종본으로 곧바로 받아들이지 말고, 보여 줄 논리가 또렷해질 때까지 버전을 비교하라는 데 있다. 5-10회는 보편적 표준이 아니라 해당 그룹의 사례다.

학생들이 첫 그림을 matplotlib 기본 설정 그대로 PDF에 넣는 경우가 흔하다. 안티패턴 카탈로그는 [cxli233 (GitHub)의 Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends)에 정리되어 있다. 여기서는 그 카탈로그를 로보틱스·CV 사례에 적용하고 Whitesides의 작업 과정과 함께 살펴본다.

---

## 27.1 차트 안티패턴

**Mean separation에 bar plot.** 평균 차이를 막대로 그리면 분포가 보이지 않는다. 두 막대의 차이가 sample size 때문인지, variance 때문인지, 실제 평균 차이 때문인지 구별할 수 없다. KITTI 시퀀스별 RTE 평균을 method A·B의 막대 두 개로 그리는 그림이 흔한 사례다. 시퀀스별 점을 strip plot으로 깔고, 그 위에 평균 막대나 box plot을 얹는다.

**Small n에 violin plot.** Violin은 KDE에 의존하므로 표본이 적을 때 bandwidth 선택이 모양을 크게 바꿀 수 있다. 모든 분포에 통하는 `n≥10` 문턱은 없다. 점을 직접 보여 주고, violin을 쓴다면 표본 수와 bandwidth를 함께 검토한다. KITTI 몇 개 시퀀스처럼 각 관측을 모두 보일 수 있을 때는 strip plot이 더 정직할 수 있다.

**Unidirectional 데이터에 bidirectional color.** RdBu, coolwarm 같은 발산형 colormap은 0을 중심으로 의미 있는 양/음에만 쓴다. 0-100% recall에 RdBu를 쓰면 50%가 "중립"으로 보이는데, recall 50%는 중립이 아니다. 단방향 양수 데이터에는 viridis, magma 같은 perceptually uniform sequential colormap을 쓴다.

**Pie chart.** 비슷한 비율 여러 개를 각도로 비교하기는 어렵다. 정확한 순위와 차이가 중요하면 정렬한 가로 막대가 낫다. 항목 수에 고정 문턱을 두기보다 라벨이 겹치고 차이를 읽기 어려운지 확인한다.

**Rainbow scale (jet).** luminance가 단조롭지 않고 색각 이상이 있는 독자에게 불리하며, 경계처럼 보이는 인지적 불연속을 만들 수 있다. Matplotlib은 2.0부터 기본 colormap을 viridis로 바꿨다. depth·error map에는 데이터가 순차형인지 발산형인지 먼저 판단하고, 그 구조에 맞는 perceptually uniform palette를 고른다.

---

## 27.2 라벨·축·통계 안티패턴

**Axis label 누락 또는 단위 누락.** 가로축이 시간인지 frame index인지, 단위가 second인지 millisecond인지 그림만 보고 답이 안 나오면 결과를 해석할 수 없다. 세로축도 동일하다. drift가 m인지 %인지, RTE가 m/s인지 m/frame인지 밝힌다.

**Error bar 정의 누락.** 막대 위에 ± 표시만 있고 그게 std인지 sem인지 95% CI인지 캡션에서 안 밝히면 그림을 통계적으로 해석할 수 없다. 캡션 한 줄이 빠져서 결과의 불확실성을 판단하지 못하는 경우다.

**Significance 표기 정의 누락.** `*`, `**`, `***`이 어떤 test의 어떤 p-threshold인지 캡션에 명시한다. 학생들이 별표만 그리고 test 이름을 빼는 일이 흔하다.

---

## 27.3 캡션은 self-explanatory해야 한다

Whitesides §V는 본문을 다시 펼치지 않고도 캡션만으로 그림을 이해할 수 있어야 한다고 적었다. 심사위원이 본문을 읽지 않고 그림만 훑을 때도 캡션이 takeaway를 전달해야 한다. 본문에 기대는 캡션은 1st pass에서 제 역할을 하지 못한다.

캡션의 권장 구조는 세 부분으로 나뉜다.

1. **한 줄 takeaway.** "Method A는 KITTI 시퀀스 00-10 전반에서 method B 대비 RTE가 14% 낮다" 같은 서술문으로 쓴다. 14%는 형식을 보이기 위한 가상 값이다.
2. **데이터·축·기호 정의.** 점이 무엇이고, 색이 무엇이며, error bar가 무엇인지.
3. **통계·n.** sample size, test, p-threshold.

ORB-SLAM (Mur-Artal et al., 2015) 논문의 그림 1은 system overview와 캡션의 한 줄 takeaway를 결합한 사례다. 발췌와 분석은 [`orb_slam_contribution.md`](./excerpts/excerpt_02_orb_slam_contribution.md)에 있다.

---

## 27.4 그림 제작 과정

**여러 버전을 스케치하고 비교한다.** Whitesides 그룹의 5-10회는 반복의 효용을 보이는 사례다. 종이의 거친 스케치로 메시지와 비교군을 먼저 점검하고, 그림 코드는 구조가 잡힌 뒤에 작성한다. 스케치 횟수와 코드로 옮기는 시점은 그림의 복잡도에 맞게 정한다.

**그림의 메시지를 본문 초고 전에 시험한다.** Results 절을 쓰기 전에 핵심 그림 후보를 종이에 여러 번 그려 보면 필요한 비교와 빠진 실험이 드러난다. 후보 수와 작업 순서는 연구 형태에 맞춰 조정한다.

**Panel 간 색·기호·선 종류 일관.** 한 논문 안에서 method A는 늘 같은 색과 기호로 등장. 그림 3에서 파란 동그라미였다가 그림 7에서 빨간 세모이면 심사위원이 두 번 읽어야 한다.

---

## 27.5 좋은 그림 체크리스트

초안이 끝난 그림 한 컷에 다음 여섯 항목을 적용한다.

- Axis label과 단위 명시
- Error bar 정의 캡션에
- Colorblind-safe palette (viridis 계열, 또는 ColorBrewer 종류)
- 캡션 첫 줄이 declarative takeaway
- Panel 간 색·기호 일관
- 선·도형 중심 그림은 가능한 경우 vector(PDF/SVG)와 embedded font, 사진·heatmap은 venue가 요구하는 해상도와 색 공간

여섯 항목을 모두 통과하지 못했다면 그림은 아직 초안이다.

---

**출처.** [cxli233 (GitHub), Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends) — 차트 안티패턴 카탈로그. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V — 5-10회 스케치, self-explanatory 캡션. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9 — 그림에 시간 배분. [Matplotlib 2.0 default style changes](https://matplotlib.org/stable/users/prev_whats_new/dflt_style_changes.html) — viridis 기본 colormap 변경. 로보틱스·CV 사례 재작성과 체크리스트는 이 장에서 정리했다.

다음: [Ch.13 — Tables: 비교의 자리](./chapter_28_tables.md)
