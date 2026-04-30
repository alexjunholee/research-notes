# Ch.27 — Figures: 안티패턴과 좋은 패턴

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)의 1st pass에서 reviewer가 본문은 건너뛰어도 figure는 본다. 본문보다 figure에 시간을 쓰라는 [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9의 권고가 이 비대칭에서 나왔다. figure가 한 컷에서 message를 못 전달하면, 본문이 그 빈 곳을 못 채운다.

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V는 figure 한 컷을 5-10회 다시 그리는 것을 작업 표준으로 잡았다. 처음 그린 figure는 거의 항상 약하므로, 가장 약한 버전을 버리고 가장 강한 한 컷을 남기는 절차를 따로 둔다는 입장이다.

학생들이 첫 figure를 matplotlib 기본 설정 그대로 PDF에 박는 패턴이 흔하다. 안티패턴 카탈로그는 [cxli233 (GitHub)의 *Friends Don't Let Friends Make Bad Graphs*](https://github.com/cxli233/FriendsDontLetFriends)에 정리되어 있다. 이 장은 그 카탈로그를 로보틱스·CV 사례로 재작성하고 Whitesides의 process 규칙과 합쳐 둔다.

---

## 27.1 차트 안티패턴

**Mean separation에 bar plot.** 평균 차이를 막대로 그리면 분포가 안 보인다. 두 막대의 차이가 sample size 때문인지, variance 때문인지, 진짜 평균 차이 때문인지 구별이 안 된다. KITTI 시퀀스별 RTE 평균을 method A·B로 두 막대로 그리는 figure가 흔한 사례다. 처방은 시퀀스별 점을 strip plot으로 깔고, 위에 평균 막대 또는 box plot을 얹는 것.

**Small n에 violin plot.** Violin은 KDE 위에 깔린다. KDE는 n≥10에서 의미 있는 매끈함을 만들고, n=3-5에서는 *거짓 매끈함*을 만든다. KITTI 4-5 시퀀스만으로 violin을 그리면 분포처럼 보이지만 분포가 아니다. 4-5 시퀀스 비교는 strip plot + 평균 막대로 충분하다.

**Unidirectional 데이터에 bidirectional color.** RdBu, coolwarm 같은 발산형 colormap은 *0을 중심으로 의미 있는 양/음*에만 쓴다. 0-100% recall에 RdBu를 쓰면 50%가 "중립"으로 보이는데, recall 50%는 중립이 아니다. 단방향 양수 데이터에는 viridis, magma 같은 perceptually uniform sequential colormap을 쓴다.

**Pie chart.** 인간이 가장 정확도가 떨어지는 비교 작업이 *각도 비교*다. 실패 모드 분류를 pie로 그리지 말고 가로 막대로. 항목이 5개를 넘으면 막대도 정렬이 필요하다.

**Rainbow scale (jet).** 비단조 luminance, 색맹에 hostile, 경계에서 인지적 불연속이 생긴다. matplotlib 2.0 이후 기본이 viridis로 바뀐 것이 이 합의의 결과다. depth map, error map 모두 viridis 계열을 기본으로.

---

## 27.2 라벨·축·통계 안티패턴

**Axis label 누락 또는 단위 누락.** 가로축이 시간인지 관점 index인지, 단위가 second인지 millisecond인지 figure만 보고 답이 안 나오면 desk reject 사유가 될 수 있다. 세로축도 동일. drift가 m인지 %인지, RTE가 m/s인지 m/관점인지.

**Error bar 정의 누락.** 막대 위에 ± 표시만 있고 그게 std인지 sem인지 95% CI인지 caption에서 안 밝히면 figure가 통계적으로 무의미해진다. caption 한 줄이 빠져서 figure 전체가 반박 불가가 되는 경우다.

**Significance 표기 정의 누락.** `*`, `**`, `***`이 어떤 test의 어떤 p-threshold인지 caption에 명시. 학생들이 별표만 그리고 test 이름을 빼는 일이 흔하다.

---

## 27.3 Caption은 self-explanatory해야 한다

Whitesides §V의 강한 규칙 하나는 caption이 본문을 다시 펼치지 않고도 figure를 이해시켜야 한다는 것이다. reviewer가 본문을 안 읽고 figure만 훑을 때 caption이 *takeaway*를 전달해야 한다. 그래서 본문에 기댄 caption은 1st pass에서 무용지물로 돌아간다.

caption의 권장 구조는 세 부분으로 나뉜다.

1. **한 줄 takeaway.** "Method A는 KITTI 시퀀스 00-10 전반에서 method B 대비 RTE 14% 낮다." 같은 declarative.
2. **데이터·축·기호 정의.** 점이 무엇이고, 색이 무엇이며, error bar가 무엇인지.
3. **통계·n.** sample size, test, p-threshold.

ORB-SLAM (Mur-Artal et al., 2015) 논문의 figure 1이 system overview + caption 한 줄 takeaway를 결합한 사례다. 발췌와 분석은 Part 3 [`orb_slam_contribution.md`](./excerpts/excerpt_02_orb_slam_contribution.md)에.

---

## 27.4 Figure 제작 process

**5-10회 스케치, 가장 약한 버전을 버린다.** Whitesides의 규칙. 한 번에 final이 나오는 figure는 거의 없다. 종이에 거칠게 그린 sketch부터 시작하고, matplotlib 코드는 가장 마지막 두 회차에 들어간다.

**Figure 먼저, 본문 나중.** figure가 message를 못 정하면 본문도 못 정한다. Results 절을 쓰기 전에 figure 후보 3-4개를 종이에 먼저 그려본다.

**Panel 간 색·기호·선 종류 일관.** 한 논문 안에서 method A는 늘 같은 색과 기호로 등장. figure 3에서 파란 동그라미였다가 figure 7에서 빨간 세모이면 reviewer가 두 번 읽어야 한다.

---

## 27.5 좋은 figure 체크리스트

draft가 끝난 figure 한 컷에 다음 여섯 항목을 적용해 둔다.

- Axis label과 단위 명시
- Error bar 정의 caption에
- Colorblind-safe palette (viridis 계열, 또는 ColorBrewer 종류)
- Caption 첫 줄이 declarative takeaway
- Panel 간 색·기호 일관
- Vector format (PDF/SVG), embedded font

여섯 항목 모두 통과하지 못하면 figure는 아직 draft다.

---

**출처.** [cxli233 (GitHub), *Friends Don't Let Friends Make Bad Graphs*](https://github.com/cxli233/FriendsDontLetFriends) — 차트 안티패턴 카탈로그. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V — 5-10회 스케치, self-explanatory caption. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9 — figure에 시간 배분. 로보틱스·CV 사례 재작성과 체크리스트는 이 장에서 정리했다.

다음: [Ch.13 — Tables: 비교의 자리](./chapter_28_tables.md)
