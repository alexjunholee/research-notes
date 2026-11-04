# Ch.27 — 그림: 안티패턴과 좋은 패턴

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf)은 second pass에서 그래프의 축 라벨과 error bar를 확인하라고 하며, 이런 흔한 실수에서 서둘러 만든 엉성한 연구와 정말 뛰어난 연구가 갈린다고 했다([Ch.7 §7.2](./chapter_07_keshav_three_passes.md)). [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619)은 rule 9에서 제목, 초록, 그림을 보는 사람이 논문의 나머지를 읽는 사람보다 훨씬 많으니 그만큼 시간을 들이라고 권한다.

[Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)는 2.2절에서 어떻게 그려야 가장 분명하고 보기 좋은지 정하려고 그림 하나를 다섯 번에서 열 번까지 다르게 스케치하기도 한다고 적었다. 이 횟수는 Whitesides 자신의 작업 방식이다.

그림에서 흔히 보는 안티패턴(피해야 할 패턴)은 [cxli233 (GitHub)의 Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends)에 모여 있다.

---

## 27.1 차트 안티패턴

**평균 차이를 bar plot으로 그린다.** 평균을 막대로 그리면 분포가 가려진다. 두 막대의 차이가 표본 수 때문인지, 분산 때문인지, 실제 평균 차이 때문인지 가리기 어렵다. KITTI 시퀀스별 RTE의 평균을 방법 A와 B의 막대 두 개로 그리는 그림이 그런 예다. 시퀀스별 값을 점으로 찍는 strip plot을 깔고, 그 위에 평균 막대나 box plot을 얹는다.

**표본이 적은데 violin plot을 쓴다.** violin plot은 커널 밀도 추정(KDE)으로 분포 모양을 그리므로, 표본이 적으면 bandwidth를 어떻게 잡느냐에 따라 모양이 크게 달라진다. 모든 분포에 통하는 `n≥10` 같은 문턱은 없다. 점을 직접 보여 주고, violin plot을 쓴다면 표본 수와 bandwidth를 함께 확인한다. KITTI 시퀀스 몇 개처럼 관측을 모두 보일 수 있으면 strip plot이 데이터를 있는 그대로 보여 준다.

**한 방향 데이터에 양방향 colormap을 쓴다.** RdBu, coolwarm 같은 발산형 colormap은 0을 중심으로 양과 음에 뜻이 있을 때만 쓴다. 0~100% recall에 RdBu를 쓰면 50%가 중간값처럼 보이지만, recall 50%에는 그런 뜻이 없다. 0 이상의 값만 있는 데이터에는 viridis, magma처럼 값의 차이가 고르게 보이도록 설계한(perceptually uniform) 순차형 colormap을 쓴다.

**pie chart를 쓴다.** 비슷한 비율 여러 개를 각도로 비교하기는 어렵다. 순위와 차이를 정확히 보여 줘야 하면 정렬한 가로 막대가 낫다. 항목 수로 문턱을 정하지 말고, 라벨이 겹치는지와 차이를 읽을 수 있는지를 본다.

**rainbow colormap(jet)을 쓴다.** cxli233은 빨강·초록이나 무지개 색 척도가 적록 색각 이상이 있는 독자에게 문제가 되고, 흑백으로 인쇄하면 정보가 잘 남지 않는다고 지적한다. 밝기가 값에 따라 고르게 변하지 않아서 데이터에 없는 경계가 보이기도 한다. Matplotlib은 2.0 버전부터 기본 colormap을 viridis로 바꿨다. depth map이나 error map을 그릴 때는 데이터가 한 방향으로 커지는지, 기준값을 중심으로 양쪽으로 갈리는지 먼저 따지고, 그에 맞는 perceptually uniform colormap을 고른다.

---

## 27.2 라벨·축·통계 안티패턴

**축 라벨이나 단위가 없다.** 가로축이 시간인지 frame 번호인지, 단위가 초인지 밀리초인지 그림만 보고 알 수 있어야 결과를 해석할 수 있다. 세로축도 마찬가지다. drift가 m인지 %인지, RTE가 m/s인지 m/frame인지 밝힌다.

**error bar가 무엇인지 적지 않는다.** 막대 위에 ± 표시만 있으면 독자는 그것이 표준편차(std)인지, 표준오차(sem)인지, 95% 신뢰구간인지 알 수 없다. 캡션에 한 줄로 밝혀야 독자가 결과의 불확실성을 판단할 수 있다.

**유의성 표시가 무엇인지 적지 않는다.** `*`, `**`, `***`가 어떤 검정의 어떤 p값 기준인지 캡션에 적는다. 별표만 그리고 검정 이름을 빼면 독자는 유의성을 확인할 수 없다.

---

## 27.3 캡션은 self-explanatory해야 한다

캡션만 읽어도 그림을 이해할 수 있어야 한다. 심사위원이 그림만 훑어볼 때도 캡션에서 요점(takeaway)을 얻어야 한다.

캡션은 다음 순서로 쓴다.

1. **요점 한 줄.** "Method A는 KITTI 시퀀스 00-10 전반에서 method B보다 RTE가 14% 낮다" 같은 서술문으로 쓴다. 14%는 문형을 보여 주려고 지어낸 수치다.
2. **데이터·축·기호의 뜻.** 점, 색, error bar가 각각 무엇을 나타내는지 적는다.
3. **통계와 표본 수.** 표본 수, 검정 방법, p값 기준을 적는다.

---

## 27.4 그림 만드는 과정

**여러 판을 스케치해 비교한다.** 종이에 거칠게 그려서 무엇을 보여 줄지와 무엇을 비교할지 먼저 점검하고, 구조가 잡힌 뒤에 그림 코드를 짠다. 몇 번 스케치할지, 언제 코드로 옮길지는 그림이 얼마나 복잡한지에 맞춰 정한다.

**본문 초고를 쓰기 전에 그림의 메시지를 시험한다.** Results를 쓰기 전에 핵심 그림 후보를 스케치해 보면 필요한 비교와 빠진 실험이 드러난다. Whitesides도 개요 단계에서 그림을 스케치해 데이터를 정리하라고 했다(2.2절).

**panel마다 색, 기호, 선 모양을 똑같이 쓴다.** 한 논문 안에서 method A는 늘 같은 색과 기호로 표시한다. 그림 3에서 파란 동그라미였던 방법이 그림 7에서 빨간 세모가 되면 심사위원은 범례를 다시 읽어야 한다.

---

## 27.5 좋은 그림 체크리스트

초안을 마친 그림마다 다음 항목을 확인한다.

- 축 라벨과 단위를 적었는가
- 캡션에 error bar의 뜻을 적었는가
- 색각 이상이 있는 독자도 구분할 수 있는 팔레트(viridis 계열이나 ColorBrewer의 팔레트)를 썼는가
- 캡션 첫 줄이 요점을 말하는 서술문인가
- panel마다 색과 기호가 같은가
- 선과 도형이 중심인 그림은 되도록 vector 형식(PDF/SVG)으로 저장하고 글꼴을 포함했는가. 사진이나 heatmap은 학회·학술지가 요구하는 해상도와 색 공간을 지켰는가

그 그림에 해당하는 항목 가운데 하나라도 통과하지 못했다면 그림은 아직 초안이다.

---

**출처.** [cxli233 (GitHub), Friends Don't Let Friends Make Bad Graphs](https://github.com/cxli233/FriendsDontLetFriends) — 차트 안티패턴 목록. [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.2 — second pass에서 그림, 축 라벨, error bar 확인. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) 2.2절 — 그림을 다섯 번에서 열 번 스케치하기. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 9 — 그림에 시간 들이기. [Matplotlib 2.0 default style changes](https://matplotlib.org/stable/users/prev_whats_new/dflt_style_changes.html) — 기본 colormap을 viridis로 바꿈. 로보틱스·컴퓨터 비전 예와 체크리스트는 이 장에서 정리했다.

다음: [Ch.28 — 표: 수치를 비교하는 자리](./chapter_28_tables.md)
