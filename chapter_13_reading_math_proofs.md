# Ch.13 — 수식·증명 읽기

[Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 rule 16에 박힌 *blah 테스트*는 글쓴이의 self-check다. 모든 수식을 단어 'blah'로 치환해도 산문이 흘러야 한다. 이 self-check는 독자에게 한 가지 사실을 던진다. *첫 독서에서 수식을 건너뛰는 것이 정상이다*. 글쓴이가 그렇게 쓰도록 권고를 받는다면, 독자도 그렇게 읽으면 된다.

학생 입장에서 자주 깨지는 대목이 여기다. 모든 패스에서 모든 수식을 손으로 따라가려 들면, 한 페이지에 두 시간이 들어가고 그날의 다른 9편이 죽는다. ch07이 문장 단위 진단이고 ch15가 수식 *쓰기*라면, 이 장은 그 사이에서 *읽는 쪽이 어느 패스에 어디까지 들어가는가*를 정해 둔다.

---

## 13.1 패스에 따라 수식의 처리가 다르다

수식을 *건너뛰는가* *손으로 따라가는가*는 패스에 따라 다르다. Keshav 1st pass에서는 수식을 건너뛴다. 2nd pass에서는 prose를 따라가되 displayed equation은 한 번 훑고 넘어간다. 3rd pass(재구현·reviewer)에서만 손으로 따라간다.

이 분리가 안 잡히면 두 함정 중 하나에 빠진다. 모든 패스에서 *모든 수식을 손으로 따라가려는* 학생은 한 편이 두 시간을 먹고 다음 편을 못 본다. 반대로 *모든 패스에서 모든 수식을 건너뛰는* 학생은 1년 후에도 분야 dense math가 외부에 머문다. Keshav가 권장하는 길은 그 사이에 분리된 운영이다. 어느 패스에서 어떤 수식을 어느 정도 들여다보는가의 결정.

분야 쪽 논의에서 자주 어긋나는 풍경이 있다. SLAM 신입이 ORB-SLAM 한 편을 1st pass에 4시간을 쓰고 자코비안 derivation에서 막혀 있는 그림이다. 1st pass의 출력은 *5 Cs 한 페이지* 쪽이다. 자코비안에 들어가는 시점은 3rd pass이고, 그 시점에는 본인이 *이 한 편을 재구현할 작정*인지의 결정이 먼저 와 있어야 한다.

---

## 13.2 derivation 한 페이지를 읽는 4 단계

dense한 derivation 한 페이지가 손에 들어왔을 때, 다음 네 단계를 *순서대로* 적용한다. 순서를 섞으면 한 페이지에 두 시간이 들어가게 된다.

**단계 1 — 입력·출력 명시.** 그 페이지가 *어떤 양에서 어떤 양으로 가는가*를 한 줄로 적는다. EKF 예측 단계라면 *"이전 step posterior $(\mu_{k-1}, \Sigma_{k-1})$에서 현 step prior $(\bar{\mu}_k, \bar{\Sigma}_k)$로 간다"* 같은 한 줄. 이 한 줄이 적히지 않으면 그 페이지의 목적이 잡히지 않은 것이고, 다음 단계로 넘어가지 않는 편이 마찰이 적다.

**단계 2 — 가정 추출.** 본문에 적힌 가정 + 묵시 가정 두 묶음으로 분리한다. EKF의 경우 본문에 적힌 가정은 *프로세스 노이즈가 가우시안이고 평균이 0*이고, 묵시 가정은 *선형화 점이 진짜 평균에 충분히 가깝다*다. 묵시 가정이 곧 ch05 reviewer 모드의 unstated assumption 후보다. derivation을 읽는 작업과 reviewer 모드가 같은 자료를 두 층위로 본다.

**단계 3 — prose만 따라간다.** 수식을 일단 건너뛰고 *between-equation prose*만 읽어 한 페이지의 흐름이 잡히는지 본다. 잡히면 그 페이지는 글쓴이가 prose를 잘 깐 글이고, 더 이상 손 derivation 없이 한 페이지가 본인 안에 들어온다. 잡히지 않으면 그 페이지는 글쓴이가 *between-equation prose를 비워둔* 글이다. 이 진단이 곧 ch15 R1의 거울이다. 글쓴이가 인접한 수식 사이에 단어를 넣지 않은 결손이, 독자에게 *blah 테스트*가 깨진 결과로 돌아온다.

**단계 4 — 결정적 한두 줄에 깊이 들어간다.** 모든 수식을 손으로 따라가지 않는다. *결과의 운명을 가르는 한두 줄*만 골라 손 derivation을 한다. 보통 가정이 결과로 변환되는 줄, 근사가 들어간 줄, 잔차가 정의되는 줄 쪽이다. EKF라면 *Kalman gain의 정의 한 줄*과 *update 후 covariance가 작아지는 한 줄*이 그 후보다.

4 단계는 순서대로다. 입출력 → 가정 → prose → 결정적 한두 줄. 단계 1을 건너뛰고 단계 4부터 들어가면, *어느 한두 줄이 결정적인가*를 잡지 못한 채 모든 줄을 따라가게 된다.

---

## 13.3 proof block — 통째로 건너뛰는가, 펼치는가

Theorem statement 그 자체가 자기완결적인지 먼저 본다. ch15 R6에서 글쓴이에게 권고되는 항목의 거울이다. statement 안의 모든 기호가 statement에서 정의되거나 명시 참조되어야 하고, 앞 단락을 다시 읽어야 statement가 이해되면 self-contained가 아니다. 본문 위로 거슬러 올라가야 하는 *횟수*가 곧 글쓴이가 statement를 다듬지 않았다는 신호다.

proof block을 통째로 건너뛰는 결정의 시점이 정해져 있다.

| Pass | proof block 정책 |
|------|------------------|
| 1 | 항상 건너뛴다 |
| 2 | 그 정리가 본인 작업에 *직접* 쓰일 때만 펼친다 |
| 3 | 펼친다 |

펼친 proof는 signpost를 따라 읽는다. *"We divide the proof into two parts"* 같은 줄이 들어가 있으면 두 part로 따라가고, 없으면 본인이 만들면서 읽어야 한다. signpost가 비어 있는 proof block에서 막히는 책임은 글쓴이에게 있다. 그러니 본인의 working memory 부족으로 진단을 돌리기 전에 글쓴이가 signpost를 깐 글인지부터 본다.

direct proof가 가능한 곳에 contradiction이 들어가 있는 경우도 같은 결이다. Knuth가 §1에서 환기한 권고는 direct proof가 닿는 자리에서는 direct가 우선이라는 것이다. proof by contradiction은 독자에게 *부정 명제를 working memory에 들고 있을 부담*을 지운다. 본인이 그 부담 앞에서 막힌다면, 그 부담을 *본인의 부족*으로 해석하지 않는다. ch07 §1과 같은 관점이다. 안 읽힘의 1차 책임은 글쓴이에게 있다.

proof block에서 막혔을 때의 진단 질문은 *"글쓴이가 signpost를 깐 글인가, 안 깐 글인가"*다. 안 깐 글이면 reviewer 코멘트 evidence가 거기에 잡힌다 (ch05 양식과 같은 결).

---

## 13.4 SLAM 분야 쪽 논의 — 자코비안·EKF·MAP

분야의 dense math 영역이 셋 정도로 정해져 있다.

**자코비안 derivation.** SE(3)·SO(3) 위의 perturbation 자코비안이 첫 영역이다. *prose만 따라가기*에서 흔히 막히는 지점은 chain rule의 어느 항이 spatial 관점이고 어느 항이 body 관점인지가 글쓴이마다 다른 데서 갈라진다. 진단 질문은 *"첫 등장에서 관점 convention이 명시되었는가"*이고, 명시 안 되어 있으면 한 자료를 끝까지 따라가기보다 관점 convention이 정해진 다른 자료(예: $\mathfrak{se}(3)$ 표기를 통일한 교과서)를 정전으로 두고 시작하는 편이 마찰이 적다.

**EKF predict/update.** 한 페이지에 수식이 8-10줄 들어가는 본보기다. 단계 1(입출력)이 잘 잡히면 한 페이지가 흐른다. 다만 ResearchGate·교과서·논문마다 표기가 다른 만큼, 한 표기로 통일된 자료를 본인 안의 정전으로 두고 *그 표기 안에서만* 비교하는 편이 흔들림을 줄인다. 다른 자료에서 표기가 다르게 나오면 *번역* 단계를 먼저 거친다.

**MAP estimation 유도.** Bayes rule → log → 최적화 → Newton step의 사이클이다. 가정(가우시안 prior·likelihood)이 *어디에서* 들어가는지 추적하는 작업이 본 작업의 본체다. 같은 derivation이 maximum likelihood로 굴러갈 때와 maximum a posteriori로 굴러갈 때의 차이가 *prior 항 한 줄*에서 갈린다. 그 한 줄이 본인의 단계 4(결정적 한두 줄) 후보다.

분야 dense math는 한 번에 잡히지 않는다. 같은 자료를 *반복해서* 읽되, 매번 *어디서 막혔는지*를 적어둔다. 막힘 좌표가 본인의 학습 곡선의 본체다. 분야 senior가 자기 블로그에 *해설형 자료*를 남기는 동기도 같은 데 있고, paper의 between-equation prose가 비어 있을 때 senior의 해설이 그 prose 층위를 보강한다 (ch09에서 코드 동반 읽기로 자세히).

---

## 13.5 막힘 좌표 노트 — 학습 곡선의 기록

한 페이지 막힘은 진단 분류가 가능하다. 본인의 *어휘 부족*인가, *분야 prior 부족*인가, *글쓴이의 prose 부족*인가의 세 갈래로 갈라진다. 진단이 잡히면 다음 액션이 달라진다. 어휘 부족이면 그 어휘를 노트에 박고, 분야 prior 부족이면 core paper 한 편 더, 글쓴이 prose 부족이면 그 부분을 *건너뛰거나* reviewer 코멘트 evidence로 둔다.

막힘 좌표 노트의 양식은 단순하다.

```
[자료 + page · line] | [막힌 줄 원문 인용] | [진단 분류] | [다음 액션]
```

같은 진단 분류가 5회 이상 누적되면, 그 항목이 본인의 학습 곡선에 한 마디로 들어간다. 분야 senior에게 *한 질문을 묶어서* 던지는 시점이 그때 따라붙는다. 「대학원노트」 [Part 3 ch04 「하나의 질문 메일」](../grad-notes/chapter_10_one_question_email.md)이 그 출구다.

막힘 좌표 노트는 *학습 곡선*인 동시에 *후배 멘토링 자료*가 된다. 본인이 막혔던 곳은 다음 후배도 막힐 곳이고, 노트에 박힌 좌표가 그대로 후배의 학습 좌표가 된다. 5년 후 본인이 같은 분야의 신입에게 무엇을 던질지의 자료가, 5년 동안 누적된 막힘 좌표에서 만들어진다.

---

**출처.** [Knuth, Larrabee, Roberts 1989](https://www-cs-faculty.stanford.edu/~knuth/klr.html) §1 rule 16 (blah test, between-equation prose) · §1 rule 4 (self-contained statement) · §1 (direct proof 우선). Part 3 [ch09 (수식·정리·증명 쓰기)](./chapter_30_math_and_proofs.md) — 이 장의 거울. 「대학원노트」 [Part 3 ch04 (하나의 질문 메일)](../grad-notes/chapter_10_one_question_email.md) — 막힘 좌표 노트의 출구. 4단계 derivation 절차, proof block 패스 결정, 막힘 좌표 노트 양식, SLAM 3 영역(자코비안·EKF·MAP) 진단은 이 장에서 정리했다.

다음: [Ch.9 — 코드 동반 읽기](./chapter_14_reading_with_code.md)
