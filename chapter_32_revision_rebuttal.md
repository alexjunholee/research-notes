# Ch.32 — Revision · Rebuttal

처음 reviewer 의견을 받은 학생의 첫 반응이 *화*인 경우가 흔하다. "리뷰어가 내 논문을 제대로 안 읽었다"는 인상부터 들어온다. 그 인상이 맞는 경우도 있다. 다만 그 인상이 작업 방향을 정하면 답변 letter가 *변호*로 변하고, editor는 변호 패턴을 가장 빠르게 잡아낸다.

다르게 보면 reviewer의 의견은 *내 글이 누군가에게 어떻게 읽혔는지에 대한 1차 외부 데이터*다. 한 외부인이 1-2주 동안 본 인상이 익명으로 도착한 자료다. 화내고 끝내면 그 데이터를 버리게 된다. [임형태 박사](https://github.com/LimHyungTae/paper-writing-checklist)가 이 점을 적은 표현이 "리뷰어가 틀렸어도 내 글이 그렇게 읽히게 쓴 책임은 나에게 있다"이다. 이 한 줄이 rebuttal 작업의 톤을 정해 둔다.

---

## 32.1 Reviewer 의견의 4유형

각 유형마다 *답변 톤*과 *변경 여부*가 다르다. 유형 분류부터 정확히 하지 않으면 letter가 모든 comment에 같은 톤으로 답하게 된다.

**유형 1 — Factual error.** 수식·실험 설정·인용·수치의 명백한 오류. 답변 톤은 *완전 인정 + 즉시 수정*이다. 오히려 변호 시도 그 자체가 reviewer를 적대로 돌린다.

> *"We thank the reviewer for catching this. Equation (7) was incorrect; the corrected derivation is now in §3.2 (page 5)."*

**유형 2 — Presentation 요구.** 그림 추가·표 재구성·문장 재배치·정의 명시. 답변 톤은 *수용 + 어디로 옮겼는지 명시*다. 본문 한도를 넘으면 supplementary로 보낸다. 거의 모든 case에서 수용을 권한다. reviewer가 못 읽었다는 신호이고 editor가 같은 신호를 받을 가능성이 높다.

**유형 3 — Scope/contribution 의문.** "이게 왜 새로운가?" "X와 차별점이 뭔가?" 가장 많이 도착하는 유형이다. 답변 톤은 *핵심 contribution을 1-2문장으로 재진술 + 인용·실험으로 evidence*다. 그리고 본문 Introduction과 Related Work를 보강한다. comment 자체에만 답하면 같은 의문이 다음 reviewer에게서 재발한다.

**유형 4 — 단순 오해.** reviewer가 명백히 오독한 부분. 답변 톤은 *내 글의 책임으로 인정 + 본문에서 어디를 어떻게 명확히 했는지*다.

> *"We realize that §4.1 was not sufficiently clear; we have rewritten the paragraph to emphasize that …"*

"the reviewer misread X" 같은 표현은 절대 금지다. 오히려 reviewer 한 명이 오독했다는 사실이 본문 그곳이 *다른 reviewer에게도 오독될 가능성*을 가리킨다.

---

## 32.2 무례한 단어 회피 — 표현 swap

특정 단어 몇 개가 rebuttal letter의 톤을 한 번에 무너뜨린다. 학생들이 자기도 모르게 쓰는 단어다.

**금지어와 대안.**

- "outperform" — 상대를 깎아내리는 인상. → "achieves higher accuracy than"
- "fail to" — reviewer 동작에 쓰면 모욕. → "may have been unclear because"
- "obviously / clearly" — 독자에게 *넌 멍청해* 신호. → 그냥 삭제
- "the reviewer is mistaken" → "we have clarified that …"
- "as we already stated" — 짜증 신호. → "to make this clearer, we have added …"

ch14의 stress position 원칙이 여기서도 작동한다. 무례한 단어가 *문장 끝*에 오면 그 무례함이 강조된다. swap이 안 되는 단어는 그 단어가 들어간 문장 그 자체를 다시 쓴다.

한국어→영어로 옮길 때 인사말이 길어지는 학생이 흔하다. "The authors would like to express their sincere gratitude for the constructive and insightful feedback …" 같은 두 줄짜리 인사는 영어 letter에서 *desperation 신호*로 읽힌다. "We thank the reviewers for their comments." 한 줄이면 충분하다.

---

## 32.3 Rebuttal letter 구조 — 3블록

**블록 1 — 감사 + 변경 요약.** 5-8줄. 첫 줄은 한 문장 감사로 연다. 그 뒤로 major change를 *번호로* 묶는다.

> *"We thank the reviewers for their constructive feedback. The major changes are: (1) we added experiments on MulRan (§5.3), (2) we clarified the relation to Vizzo et al. 2023 (§2.2), (3) we corrected Equation (7) (§3.2)."*

**블록 2 — 항목별 답변.** reviewer별로 묶고, 그 안에서 comment별로 묶는다. 각 comment마다 세 부분.

1. **Comment 원문 인용.** italic 또는 quote 블록.
2. **Response.** 우리의 답.
3. **Change in manuscript.** 본문 어디에 어떻게 반영했는지 — 페이지, 섹션, 수식 번호 명시.

세 번째 부분이 가장 자주 빠진다. 답변에 "we agree …"만 있고 *어디서 본문이 바뀌었는지*가 없으면 reviewer가 변경 사항을 직접 찾아야 한다. 그 일을 reviewer에게 떠넘기면 다음 round에서 같은 comment가 다시 도착한다.

**블록 3 — 마무리.** 1-2 문장. 반복 인사는 금지한다.

> *"We hope these revisions address the reviewers' concerns."*

**변경된 본문은 colored diff 또는 별도 PDF로 첨부.** 본문에 파란 글씨로 변경 자리를 표시한 PDF가 표준이다. reviewer가 변경을 *찾게* 하지 않는다.

**길이 한계.** comment 1개당 답변 100-200 단어. 그 이상으로 길어지면 *변호 모드*에 들어갔다는 신호다. 자기 letter를 읽으면서 200단어를 넘어가는 답변이 있으면 그 부분부터 점검한다.

---

## 32.4 마무리 섹션 회피 항목 — 엄태웅 대표 4종

revision 작업 중 manuscript의 마무리 섹션(Conclusion · Future work)에서 reject 사유가 *재발*하는 자리가 있다. [엄태웅 대표 G2 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/)가 같은 위치를 4 항목으로 정리했다.

> **Conclusion = Abstract 반복.** 두 곳에 같은 문장이 들어가면 Conclusion의 자리값이 빈다.
>
> **Conclusion에 새 내용.** Discussion에 들어갈 새 결과를 Conclusion에 박으면 reviewer가 evidence를 못 찾는다.
>
> **과도한 Future work.** "limitations로 가장한 contribution 묻기" 패턴. 한 단락이면 충분하다.
>
> **원어민 교정에만 의존.** 영어 표면을 다듬는 작업과 *논문 구조의 reject 사유 줄이기*는 다른 작업이다. 후자가 먼저다.

네 항목 모두 Whitesides §4.6의 closing-section 권고와 정합한다. 그래서 revision letter를 쓰면서 reviewer 지적이 *Conclusion 자리에 박혀야 했을 내용*을 가리킬 때, 본문 그곳부터 다시 본다.

[최윤섭 박사 G4 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/)가 적은 본인 일화도 같은 톤이다. 약 6개월 리비전 동안 추가 실험을 돌리며 reviewer 지적에 *데이터 기반*으로 대응했다. 한편 변호 letter로 답하는 길과 본문에 evidence를 더 박는 길은 다르다. 후자가 reviewer 의문을 다음 round에서 재발시키지 않는 유일한 길이다.

reviewer가 추가 ablation을 요구한 자리에서 층위가 한 단 얹힌다. *내 모델이 baseline 대비 무엇을 개선했는지 보이려면 어떤 ablation이 필요한가*를 AI에게 던지면 실험 설계 초안이 잡힌다. 결과 표가 다 나온 뒤 *이 표에서 어떤 분석이 가능한가*를 던지는 것도 같은 층위다 — AI는 놓친 관점을 한 번 짚어 주는 보조 도구로 작동한다.

> AI의 ablation 제안을 그대로 본문에 박지 않는다. 자기 연구의 contribution과 정합하지 않는 ablation을 제안할 수 있다. 실험 설계의 최종 판단은 연구자의 몫이다.

AI가 짠 초안과 자기 contribution claim 사이의 마찰을 점검하는 작업이 그 자리에서 발생한다. 그 마찰이 곧 *왜 이 ablation이 contribution을 받치는가*의 한 줄짜리 정당화로 letter에 들어간다. (이전에 robotics-practice ch19 § 19.7.3에 정리된 내용으로, 분야 보조 사례로 가져옴.)

---

## 32.5 특수 상황

**Major revision.** 4 유형이 모두 도착하고 본문 substantive 보강이 필요한 경우. 통상 8-12주 작업. 24시간 룰을 지키고, 24시간 뒤 §1 분류부터 시작한다.

**Minor revision.** 주로 유형 1·2. 1-2주.

**Reject (with encouragement to resubmit).** 새 논문처럼 다시 쓴다. reviewer 지적 사항을 *모두* 보강한 뒤 같은 venue에 재투고할 때만 의미가 있다. 부분 보강만 한 채 같은 venue에 다시 던지면 같은 reviewer가 같은 reject 사유를 다시 적는다.

**Conference rebuttal.** 분량 제한이 보통 1 page다. 톤·구조는 §3 동일하지만 블록 1을 한 줄로 압축한다. CVPR·NeurIPS·ICRA 패턴이다. 한편 문자 수가 부족해서 항목별 답변이 짧아지는 곳이 자주 생기는데, *답변 못 한 comment를 supplementary로 미루는 결정*은 권하지 않는다. main rebuttal에 다 적는다.

**24시간 룰.** 리뷰를 받은 직후 첫 24시간은 답변을 쓰지 않는다. 화·억울함이 가라앉은 뒤 §1 분류부터 들어간다. conference rebuttal처럼 마감이 촉박할 때는 무리지만, journal revision에서는 권한다. 임형태 박사도 같은 권고를 적어 두었다.

---

## 32.6 마지막 점검 — 자기 letter를 reviewer 시점에서 읽기

letter를 다 쓴 뒤 24시간 거리를 두고 reviewer 시점에서 다시 읽는다. 두 가지를 본다.

첫째, *변호*로 읽히는 부분이 있는가. "we already stated", "the reviewer fails to", "this is obvious" 류의 톤이 살아남았는가.

둘째, comment마다 *Change in manuscript* 항목이 채워져 있는가. 빈 항목이 있으면 그 comment는 답변이 안 된 것이다.

이 두 가지가 통과되면 letter를 보낸다.

---

**출처.** [임형태 박사, paper-writing-checklist](https://github.com/LimHyungTae/paper-writing-checklist) — rebuttal 마음가짐, *내 글이 그렇게 읽힌 책임* 인용, 24시간 룰 권고. [최윤섭 박사 G4 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/) — 6개월 리비전 일화·데이터 기반 대응. [엄태웅 대표 G2 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/) — 마무리 섹션 4 회피 항목. robotics-practice ch19 § 19.7.3 — 실험 설계 보조 도구에 관한 보조 사례 (분야 쪽 논의). ch01·ch14와 교차. 4유형 분류, 표현 swap 사전, 3블록 letter 구조, conference vs journal 구분은 이 장에서 정리했다.

작성 단계의 작업은 여기서 끝난다. Part 3의 발췌 사례들은 본문 뒤에 부록처럼 붙는다.
