# Ch.32 — 개정과 답변서

처음 심사위원 의견을 받은 학생은 흔히 화부터 낸다. "리뷰어가 내 논문을 제대로 안 읽었다"는 인상이 먼저 든다. 그 인상이 맞을 때도 있다. 다만 그 인상이 작업 방향을 정하면 답변서는 변호문으로 바뀌고, 편집자는 그 패턴을 빠르게 알아챈다.

심사위원의 의견은 내 글이 누군가에게 어떻게 읽혔는지 보여 주는 외부 자료이기도 하다. 심사에 쓴 시간은 알 수 없으므로 1-2주라고 가정하지 않는다. 화내고 끝내면 그 자료를 버린다. [임형태 박사](https://github.com/LimHyungTae/paper-writing-checklist)는 "리뷰어가 틀렸어도 내 글이 그렇게 읽히게 쓴 책임은 나에게 있다"고 적었다. 이 한 줄이 답변서의 어조를 정한다.

---

## 32.1 심사위원 의견의 4유형

각 유형마다 답변의 어조와 변경 여부가 다르다. 유형부터 정확히 분류하지 않으면 모든 comment에 같은 어조로 답하게 된다.

**유형 1 — Factual error.** 수식·실험 설정·인용·수치의 명백한 오류. 답변 톤은 완전 인정 + 즉시 수정이다. 오히려 변호 시도 그 자체가 심사위원을 적대로 돌린다.

> "We thank the reviewer for catching this. Equation (7) was incorrect; the corrected derivation is now in §3.2 (page 5)."

**유형 2 — Presentation 요구.** 그림 추가·표 재구성·문장 재배치·정의 명시가 여기에 속한다. 타당한 요청은 수용하고 어디를 바꾸었는지 밝힌다. 본문 한도를 넘으면 venue policy가 허용하는 보충자료나 압축안을 검토한다. 수용하지 못할 때는 지면·scope·중복 같은 이유와 대신 한 조치를 적는다.

**유형 3 — Scope/contribution 의문.** "이게 왜 새로운가?" "X와 차별점이 뭔가?" 같은 질문이다. 핵심 contribution을 1-2문장으로 다시 밝히고 인용·실험으로 근거를 댄다. 본문의 서론과 Related Work도 보강한다. comment 자체에만 답하면 같은 의문이 다음 심사위원에게서 재발할 수 있다.

**유형 4 — 단순 오해.** 심사위원이 명백히 오독한 부분. 답변 톤은 내 글의 책임으로 인정 + 본문에서 어디를 어떻게 명확히 했는지다.

> "We realize that §4.1 was not sufficiently clear; we have rewritten the paragraph to emphasize that …"

"the reviewer misread X"처럼 사람의 잘못을 앞세우지 않는다. 심사위원 한 명이 오독했다면 본문 그곳이 다른 독자에게도 오독될 가능성을 먼저 점검한다. 다만 comment가 원고에 없는 내용을 전제한다면 인용 가능한 본문 위치와 함께 사실 관계를 차분히 바로잡는다.

---

## 32.2 무례한 단어를 바꿔 쓰기

몇몇 단어는 답변서의 어조를 한 번에 무너뜨린다. 학생들이 자기도 모르게 쓰는 단어다.

**금지어와 대안.**

- "outperform" — 그 자체로 무례한 금지어는 아니지만 비교 조건이 빠지기 쉽다. → metric·dataset·불확실성을 함께 명시
- "fail to" — 심사위원 동작에 쓰면 모욕. → "may have been unclear because"
- "obviously / clearly" — 독자에게 넌 멍청해 신호. → 그냥 삭제
- "the reviewer is mistaken" → "we have clarified that …"
- "as we already stated" — 짜증 신호. → "to make this clearer, we have added …"

ch14의 stress position 원칙이 여기서도 작동한다. 무례한 단어가 문장 끝에 오면 그 무례함이 강조된다. 단어만 바꾸기 어렵다면 문장 전체를 다시 쓴다.

인사말이 길면 변경 사항에 도달하기 늦어진다. "We thank the reviewers for their comments."처럼 짧게 열고 곧바로 주요 변경으로 간다. 긴 인사가 특정한 심리 상태의 신호라고 단정할 필요는 없다.

---

## 32.3 답변서 구조 — 3블록

**블록 1 — 감사 + 변경 요약.** 5-8줄로 쓴다. 첫 줄은 한 문장 감사로 열고, 그 뒤에 major change를 번호로 묶는다.

> "We thank the reviewers for their constructive feedback. The major changes are: (1) we added experiments on MulRan (§5.3), (2) we clarified the relation to Vizzo et al. 2023 (§2.2), (3) we corrected Equation (7) (§3.2)."

**블록 2 — 항목별 답변.** 심사위원별로 묶고, 그 안에서 comment별로 묶는다. 각 comment마다 세 부분.

1. **Comment 원문 인용.** italic 또는 quote 블록.
2. **Response.** 우리의 답.
3. **Change in manuscript.** 본문 어디에 어떻게 반영했는지 — 페이지, 섹션, 수식 번호 명시.

세 번째 부분이 가장 자주 빠진다. 답변에 "we agree …"만 있고 본문이 어디서 바뀌었는지 밝히지 않으면 심사위원이 변경 사항을 직접 찾아야 한다. 그 일을 심사위원에게 떠넘기면 다음 round에서 같은 comment가 다시 도착한다.

**블록 3 — 마무리.** 1-2문장으로 쓰고 인사를 반복하지 않는다.

> "We hope these revisions address the reviewers' concerns."

**변경된 본문 표시는 venue·editor 지침을 따른다.** 변경 추적 PDF, 색상 표시, clean manuscript 가운데 무엇을 요구하는지 확인한다. 별도 지침이 없으면 변경 위치를 답변서에 page·section·line으로 명시해 심사위원이 직접 찾게 하지 않는다.

**길이 점검.** comment당 100-200단어는 이 장의 편집용 출발 범위일 뿐 보편 한계가 아니다. venue의 전체 word·character limit를 먼저 따른다. 답변이 길어지면 결론·근거·본문 변경이 반복되는지 점검한다.

---

## 32.4 마무리 섹션에서 피할 네 가지

원고를 개정할 때 마무리 섹션(Conclusion · Future work)에서 거절 사유가 되풀이되기도 한다. [엄태웅 대표 G2 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/)은 이를 네 항목으로 정리했다.

> **Conclusion = Abstract 반복.** 두 곳에 같은 문장이 들어가면 Conclusion의 자리값이 빈다.
>
> **Conclusion에 새 내용.** Discussion에 들어갈 새 결과를 Conclusion에 박으면 심사위원이 evidence를 못 찾는다.
>
> **과도한 Future work.** "limitations로 가장한 contribution 묻기" 패턴. 한 단락이면 충분하다.
>
> **원어민 교정에만 의존.** 영어 표면을 다듬는 작업과 논문 구조의 reject 사유 줄이기는 다른 작업이다. 후자가 먼저다.

네 항목은 Whitesides의 마무리 섹션 권고와도 맞닿는다. 답변서를 쓰다가 심사위원의 지적이 결론에 들어갔어야 할 내용을 가리킨다면 본문의 그 부분부터 다시 본다.

[최윤섭 박사 G4 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/)의 일화도 같은 어조다. 약 6개월의 개정 기간에 추가 실험을 하며 심사위원의 지적에 데이터로 대응했다. 변호하는 답변서를 쓰는 일과 본문에 근거를 더하는 일은 다르다. 후자를 택해야 심사위원의 의문이 다음 심사에서 되풀이되지 않는다.

심사위원이 추가 ablation을 요구했다면 AI로 실험 설계의 초안을 만들 수 있다. 내 모델이 baseline에 비해 무엇을 개선했는지 보이려면 어떤 ablation이 필요한지 묻는다. 결과 표가 나온 뒤 이 표에서 가능한 분석을 묻는 방법도 있다. AI는 놓친 관점을 짚어 주는 보조 도구로만 쓴다.

> AI의 ablation 제안을 그대로 본문에 박지 않는다. 자기 연구의 contribution과 정합하지 않는 ablation을 제안할 수 있다. 실험 설계의 최종 판단은 연구자의 몫이다.

AI가 만든 초안이 자기 기여 주장과 어긋나지 않는지 점검한다. 그 과정에서 이 ablation이 왜 기여를 받치는지 한 줄로 정리하고 답변서에 넣는다.

---

## 32.5 특수 상황

**Major revision.** 본문을 대폭 보강해야 하는 경우다. 8~12주는 이 장의 계획 예시일 뿐 실제 기한은 editor letter가 정한다. 감정이 가라앉을 시간을 둔 뒤 §1의 분류부터 시작하되 공식 deadline을 넘기지 않는다.

**Minor revision.** 주로 국소적인 사실·표현·설명 수정이지만, 공식 기한과 필요한 검증에 맞춰 일정을 잡는다.

**Reject (with encouragement to resubmit).** decision letter가 허용하는 경로와 새 submission 요건을 확인한다. 심사 의견을 claim·evidence·scope 차원에서 반영하고, 같은 venue에 다시 낼지 다른 venue로 옮길지는 논문의 변화와 policy를 보고 결정한다. 같은 심사위원에게 배정된다고 가정하지 않는다.

**Conference rebuttal.** page·word·character limit와 새 실험 허용 여부는 venue·연도마다 다르다. CVPR·NeurIPS·ICRA도 같은 규칙을 공유한다고 가정하지 말고 해당 연도의 author instructions를 확인한다. supplementary에 답변을 둘 수 있는지도 공식 policy를 따른다.

**24시간 룰.** 리뷰를 받은 직후 첫 24시간은 답변을 쓰지 않는다. 화·억울함이 가라앉은 뒤 §1 분류부터 들어간다. conference rebuttal처럼 마감이 촉박할 때는 무리지만, journal revision에서는 권한다. 임형태 박사도 같은 권고를 적어 두었다.

---

## 32.6 마지막 점검 — 자기 답변서를 심사위원 시점에서 읽기

답변서를 다 쓴 뒤 가능하면 시간을 두고 심사위원의 시점에서 다시 읽는다. 24시간은 일정 예시이지 제출 규칙이 아니다. 두 가지를 본다.

첫째, 변호로 읽히는 부분이 있는가. "we already stated", "the reviewer fails to", "this is obvious" 류의 톤이 살아남았는가.

둘째, comment마다 Change in manuscript 항목이 채워져 있는가. 빈 항목이 있으면 그 comment는 답변이 안 된 것이다.

이 두 가지가 통과하면 답변서를 보낸다.

---

**출처.** [임형태 박사, paper-writing-checklist](https://github.com/LimHyungTae/paper-writing-checklist) — rebuttal 마음가짐, 내 글이 그렇게 읽힌 책임 인용, 24시간 룰 권고. [최윤섭 박사 G4 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/) — 6개월 리비전 일화·데이터 기반 대응. [엄태웅 대표 G2 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/) — 마무리 섹션 4 회피 항목. robotics-practice ch19 § 19.7.3 — 실험 설계 보조 도구에 관한 보조 사례 (분야 쪽 논의). ch01·ch14와 교차. 4유형 분류, 표현 swap 사전, 3블록 letter 구조, conference vs journal 구분은 이 장에서 정리했다.

[Part 4 — 발표와 학회](./chapter_33_conference_roi.md)
