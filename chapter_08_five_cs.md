# Ch.8 — 5 Cs 체크리스트

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.1은 1st pass의 끝에 다섯 가지를 답하라고 적는다. Category, Context, Correctness, Contributions, Clarity. 영문 머릿글자를 따 5 Cs라 부른다.

원문에서는 한 단락 안에 흩어져 있는 다섯 항목이지만, 매 논문 같은 폼에 채우는 *시트*로 떼어내면 비교가 가능해진다. 후일의 lit survey, peer-review 의견 작성에 그대로 재활용되는 자산으로 쌓인다. 그래서 1st pass의 *output 형식*을 5 Cs로 고정해 둔다. 5 Cs를 안 채운 1st pass는 끝난 게 아니라 흘려본 것에 가깝다.

---

## 8.1 Category — 어떤 종류의 논문인가

새 측정을 다룬 논문인지, 시스템을 만든 논문인지, 새 아이디어를 제안한 논문인지, 기존 작업을 분석한 논문인지를 한 줄로 적는다.

자료원은 title 한 줄과 abstract 첫 문장이다. "딥러닝 논문" 같은 답은 Category로 쓰지 않는다. 그 답은 어느 칸으로도 쓸 수 없을 만큼 넓다. "RGB-D 입력에서 dense map을 만드는 시스템 논문" 정도가 채워진 칸의 해상도다.

---

## 8.2 Context — 누구의 작업과 연결되는가

intro 첫 단락과 reference 목록 표지를 보고, 이 논문이 어느 갈래의 어느 선행 작업과 연결되는지를 적는다.

ref 갯수만 세는 것이 흔한 실수다. 오히려 ref 갯수보다 *어느 그룹의 어느 논문이 빠졌는지*가 정보를 더 많이 담는다. Keshav §2.1은 이 칸을 채우는 능력 자체를 분야 배경의 진단으로 쓸 수 있다고 적는다. Context가 안 채워지면 그 분야에서의 1st pass는 보류하고 survey 한 편을 먼저 거치는 편이 마찰이 적다.

---

## 8.3 Correctness — 가정이 타당해 보이는가

abstract claim과 intro의 contribution 목록을 보고, 가정이 첫인상에서 타당해 보이는지를 적는다.

이 칸의 가장 흔한 오해는 1st pass에서 *증명*하려 드는 것이다. Keshav §2.1은 분명히 1st pass에서는 *냄새 점검*만 한다고 적었고, 증명은 3rd pass의 일이다. 그래서 1st pass에서 잡는 것은 "이 가정이 곧 무너질 것 같다"는 1차 직감이고, 그 직감의 근거 한 줄을 적어 두는 정도면 충분하다.

---

## 8.4 Contributions — 핵심 기여가 무엇인가

intro 마지막 단락의 bullet contribution이나 conclusion에서 직접 채운다.

흔한 실수 하나가 figure 1을 contribution으로 착각하는 것이다. figure 1은 *논증*을 한 컷으로 담는다 (Ch.1 figure 1 test 참조). contribution 목록 그 자체는 아니다. Contribution은 글쓴이가 명시적으로 적은 문장에서 채운다. 명시되어 있지 않다면, 그 자체가 Clarity 칸의 신호다.

---

## 8.5 Clarity — 잘 쓰였는가

abstract와 heading의 broad-narrow-broad 구조가 무너지지 않았는지를 보고 적는다.

Clarity와 영어 native 여부를 혼동하지 않는 권고가 자주 붙는다. Clarity는 영어 문장의 매끄러움이 아니라 *구조*의 문제다. [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)이 다룬 reader expectations의 함의가 여기에 닿는다. 같은 논리는 한국어로 옮겨도 그대로 적용된다 (Ch.7에서 자세히). 1st pass의 Clarity 칸에는 "abstract가 모래시계인가 / heading이 information-rich한가"의 두 줄짜리 점검이면 충분하다.

---

## 8.6 Verdict와 시트 템플릿

5 Cs 다섯 칸을 채운 직후 stop / defer / proceed 셋 중 하나를 결정한다.

다섯 칸 모두 명확하고 관심 영역에 걸리면 → **proceed**, 2nd pass로 넘어간다. 한편 Category와 Contributions만 잡히고 Context·Correctness·Clarity가 모호하면 → **defer**, 배경 보강 후 복귀 큐로 보낸다. Clarity 자체가 무너졌으면 → **stop**, 글쓴이 책임으로 두고 다음 후보로 넘어간다.

Keshav가 자주 환기하는 점은 5 Cs 시트가 *비교의 단위*가 된다는 점이다. 한 분야의 논문 50편을 같은 폼에 채워 두면, 그 분야의 지형이 그대로 잡힌다.

시트 자체는 한 줄당 한 C로 적는 단순한 폼이다. 영문 keyword와 한국어 메모를 섞어 적는다. Verdict 칸은 stop / defer / proceed의 체크박스로 두고, 별도 tag 칸에 lit survey 큐로 보낼 키워드를 적어 둔다.

```
Title:
Authors / Year / Venue:

Category    :
Context     :
Correctness :
Contributions:
Clarity     :

Verdict: [ ] stop  [ ] defer  [ ] proceed
Tag: (lit survey 큐 키워드)
```

defer 칸으로 보낸 시트는 빈칸을 그대로 둔다. 후일 같은 키워드로 새 논문이 잡히면 빈칸이 함께 채워진다. 이 누적 패턴이 5 Cs를 단발 도구가 아니라 분야 지형 자산으로 만든다.

---

**출처.** [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.1, [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rules 5·6, [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) (함의).

다음: [Ch.4 — Literature Survey Workflow](./chapter_09_lit_survey_workflow.md)
