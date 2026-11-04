# Ch.32 — 개정과 답변서

심사위원 의견을 처음 받으면 화부터 나기도 한다. "리뷰어가 내 논문을 제대로 안 읽었다"는 생각이 먼저 든다. 그 생각이 맞을 때도 있다. 다만 그 생각대로 답변서를 쓰면 답변서가 변호문이 된다.

심사위원의 의견은 내 글이 다른 사람에게 어떻게 읽혔는지 알려 주는 자료이기도 하다. 화만 내고 끝내면 그 자료를 버리는 셈이다. [임형태 박사](https://github.com/LimHyungTae/paper-writing-checklist)는 논문에서 "이 세상에 없던 지식을 타인이 읽고도 오해 없이 명확하게 이해할 수 있도록 하는 것이 무엇보다 중요"하다고 적었다. 심사위원이 오해했다면 그 목표에 아직 못 미친 것이다. 답변서는 이 전제에서 출발한다.

---

## 32.1 심사위원 의견의 네 유형

유형마다 답변의 어조와 본문을 고칠지가 달라진다. 의견을 먼저 유형별로 나눠야 comment마다 맞는 어조로 답할 수 있다.

**유형 1 — Factual error.** 수식, 실험 설정, 인용, 수치가 분명히 틀린 경우다. 오류를 그대로 인정하고 바로 고친다. 변호하려 들면 심사위원을 적으로 돌린다.

> "We thank the reviewer for catching this. Equation (7) was incorrect; the corrected derivation is now in §3.2 (page 5)."

**유형 2 — Presentation 요구.** 그림을 더하거나, 표를 다시 짜거나, 문장 순서를 바꾸거나, 정의를 밝혀 달라는 요청이다. 타당한 요청은 받아들이고 고친 위치를 정확히 알린다. 지면 한도를 넘으면 venue 정책이 허용하는 보충자료로 옮기거나 다른 부분을 줄일 방법을 찾는다. 받아들일 수 없는 요청이라면 지면 한계나 논문 범위(scope) 같은 구체적인 이유를 대고, 대신 할 수 있는 보완을 제시한다.

**유형 3 — Scope/contribution 의문.** "이게 왜 새로운가?", "X와 무엇이 다른가?" 같은 질문이다. 핵심 contribution을 한두 문장으로 다시 밝히고 인용과 실험으로 근거를 댄다. 본문의 서론과 Related Work도 보강한다. comment에만 답하고 본문을 그대로 두면 다음 심사위원도 같은 질문을 한다.

**유형 4 — 단순 오해.** 심사위원이 본문을 분명히 잘못 읽은 경우다. 내 글이 불분명했다고 인정하고, 본문 어디를 어떻게 고쳤는지 알린다.

> "We realize that §4.1 was not sufficiently clear; we have rewritten the paragraph to emphasize that …"

답변에서는 심사위원의 잘못("the reviewer misread X")을 짚기보다 본문을 고친 이야기를 한다. 심사위원 한 명이 잘못 읽은 곳은 다른 독자도 잘못 읽을 수 있으니 그 부분부터 다시 본다. 다만 comment가 원고에 없는 내용을 전제한다면, 해당 본문 위치를 들어 사실관계를 차분히 바로잡는다.

---

## 32.2 무례하게 들리는 단어 바꾸기

몇몇 단어는 답변서의 어조를 단번에 망친다.

**주의할 표현과 대안.**

- "outperform" — 임형태 박사는 이 단어를 논문에서 "절대로" 쓰지 말자고 했다. baseline 저자가 심사위원일 가능성이 높아서다. → "showed lower error"처럼 완곡하게 쓰고 metric·dataset·조건을 함께 적는다
- "fail to" — 심사위원의 행동에 쓰면 모욕으로 들린다. → "may have been unclear because"
- "obviously / clearly" — 독자를 무시하는 말로 들린다. → 지운다
- "the reviewer is mistaken" → "we have clarified that …"
- "as we already stated" — 짜증이 묻어난다. → "to make this clearer, we have added …"

[Ch.12 §12.2](./chapter_12_reader_expectations_diagnosis.md)에서 본 stress position 원칙이 여기에도 적용된다. 무례한 단어가 문장 끝에 오면 무례함이 더 두드러진다. 단어만 바꿔서 안 되면 문장을 통째로 다시 쓴다.

인사말이 길면 독자가 변경 사항에 늦게 닿는다. "We thank the reviewers for their comments."처럼 짧게 시작하고 곧바로 주요 변경 사항으로 넘어간다.

---

## 32.3 답변서의 세 부분

**첫 부분 — 감사와 변경 요약.** 5~8줄로 쓴다. 첫 줄에 한 문장으로 감사하고, 이어서 주요 변경(major change)에 번호를 붙여 적는다.

> "We thank the reviewers for their constructive feedback. The major changes are: (1) we added experiments on MulRan (§5.3), (2) we clarified the relation to Vizzo et al. 2023 (§2.2), (3) we corrected Equation (7) (§3.2)."

**둘째 부분 — 항목별 답변.** 심사위원별로 묶고, 그 안에서 comment별로 나눈다. comment마다 다음을 쓴다.

1. **Comment 원문.** italic이나 quote 블록으로 옮긴다.
2. **Response.** 우리의 답이다.
3. **Change in manuscript.** 본문 어디를 어떻게 고쳤는지 페이지, 섹션, 수식 번호로 적는다.

세 번째 항목은 빠지기 쉽다. 답변에 "we agree …"만 있고 본문에서 바뀐 곳이 없으면 심사위원이 변경 사항을 직접 찾아야 한다. 그러면 다음 round에 같은 comment가 다시 오기 쉽다.

**셋째 부분 — 마무리.** 한두 문장으로 쓰고, 인사는 한 번만 한다.

> "We hope these revisions address the reviewers' concerns."

**고친 본문 표시는 venue와 editor의 지침을 따른다.** 변경 추적 PDF, 색상 표시, clean manuscript 가운데 무엇을 요구하는지 확인한다. 따로 지침이 없으면 답변서에 변경 위치를 page·section·line으로 적는다.

**길이.** comment당 100~200단어는 이 장이 제안하는 출발점일 뿐 정해진 한계가 아니다. venue가 정한 전체 word·character 제한을 먼저 따른다. 답변이 길어지면 결론, 근거, 본문 변경 내용을 되풀이하지 않았는지 살핀다.

---

## 32.4 원고를 고칠 때 결론에서 피할 것

원고를 고칠 때 Conclusion과 Future work에서 거절 사유가 되풀이되기도 한다. [엄태웅 대표의 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/)은 Conclusion을 쓸 때 저지르는 실수와 영어 교정에 관해 다음과 같이 적었다.

- **Conclusion을 Abstract처럼 쓰는 실수.** Abstract는 논문을 읽지 않은 사람이 처음 읽는 글이고, Conclusion은 논문을 다 읽은 사람에게 전체를 정리해 주는 글이다. 그래서 Abstract는 문제 제기와 연구의 중요성·기여에, Conclusion은 실험으로 얻은 지식과 그 의의에 무게를 조금 더 두어야 한다.
- **Conclusion에서 새 이야기를 꺼내는 실수.** 본문에서 주장한 것보다 한 걸음 더 나아가는 것도 마찬가지로 부적절하다.
- **Future work에 너무 많은 것을 늘어놓는 실수.** 이 분야 사람들은 Future work가 "OOO은 안 했음"이라는 뜻임을 안다. 그래서 하지 못한 것을 방어하는 방법으로 좋지 않다. 연구의 한계는 결과 논의 끝에 솔직히 밝힌다.
- **원어민 영어 교정에 기대는 실수.** 교정자는 내용을 이해하지 못한 채 문법을 고치므로, 저자와 대화가 없으면 교정이 오히려 오해를 만들어 내기 일쑤다. 저자 스스로 좋은 영어를 쓰도록 노력해야 한다.

Whitesides도 Conclusions 절은 요약이 아니어야 하며, 한 단계 높은 분석을 더하고 연구의 의의를 밝혀야 한다고 했다. 심사위원의 지적이 결론에 들어갔어야 할 내용을 가리킨다면 답변서보다 본문의 그 부분을 먼저 고친다.

[최윤섭 박사의 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/)에도 리비전 이야기가 나온다. 그가 주도한 논문은 출판한 저널에서 리비전을 세 번 거쳤고, 추가 실험과 논문 수정에만 6개월이 걸렸다. 그는 리뷰어의 지적에 어떤 논리와 실험으로 대응할지 정하는 전략이 중요하다고 했다.

심사위원이 ablation 실험을 더 요구했다면 AI에게 실험 설계 초안을 부탁할 수 있다. 내 모델이 baseline보다 무엇을 개선했는지 보이려면 어떤 ablation이 필요한지 묻는다. 결과 표가 나온 뒤에 그 표로 어떤 분석을 할 수 있는지 물어도 된다. AI는 내가 놓친 관점을 짚어 주는 보조 도구로만 쓴다.

> AI가 제안한 ablation을 그대로 본문에 넣지 않는다. AI는 내 연구의 contribution과 맞지 않는 ablation을 제안하기도 한다. 실험 설계는 연구자가 최종 판단한다.

AI가 만든 초안이 내 contribution 주장과 어긋나지 않는지 확인한다. 확인하면서 이 ablation이 contribution을 어떻게 뒷받침하는지 한 줄로 적어 답변서에 넣는다.

---

## 32.5 특수한 경우

**Major revision.** 본문을 크게 보강해야 하는 경우다. 이 장에서는 8~12주를 예로 들지만, 실제 기한은 editor letter에 적혀 있다. 감정이 가라앉을 시간을 둔 뒤 §32.1의 분류부터 시작하고, 공식 마감 안에 끝낸다.

**Minor revision.** 대개 사실, 표현, 설명을 국소적으로 고친다. 그래도 공식 기한과 필요한 검증에 맞춰 일정을 잡는다.

**Reject (with encouragement to resubmit).** decision letter가 허용하는 경로와 새 투고 요건을 확인한다. 심사 의견을 claim, evidence, scope 수준에서 반영한다. 같은 venue에 다시 낼지 다른 venue로 옮길지는 논문이 얼마나 바뀌었는지와 각 venue의 정책을 보고 정한다. 다시 내면 새 심사위원이 배정될 수도 있다.

**Conference rebuttal.** page·word·character 제한과 새 실험을 허용하는지는 venue와 연도마다 다르다. CVPR, NeurIPS, ICRA가 같은 규칙을 쓴다고 가정하지 말고 그해 author instructions를 확인한다. 답변을 supplementary에 둘 수 있는지도 공식 정책을 따른다.

**24시간 미루기.** 리뷰를 받은 뒤 첫 24시간은 답변을 쓰지 않는다. 화와 억울함이 가라앉은 뒤 §32.1의 분류부터 시작한다. conference rebuttal처럼 마감이 촉박하면 어렵지만, journal revision에서는 권한다.

---

## 32.6 마지막 점검 — 심사위원이 되어 답변서 읽기

답변서를 다 쓰면 되도록 시간을 두었다가 심사위원의 눈으로 다시 읽는다. 24시간은 일정의 예일 뿐 제출 규칙이 아니다. 다음을 확인한다.

먼저, 변호처럼 읽히는 곳이 있는지 본다. "we already stated", "the reviewer fails to", "this is obvious" 같은 말투가 남아 있지 않은지 확인한다.

다음으로, comment마다 Change in manuscript 항목이 채워져 있는지 본다. 이 항목이 빈 comment에는 아직 답하지 않은 것이다.

둘 다 문제없으면 답변서를 보낸다.

---

**출처.** [임형태 박사, paper-writing-checklist](https://github.com/LimHyungTae/paper-writing-checklist) — 오해 없이 이해되는 글이 가장 중요하다는 원칙, 'outperform'을 쓰지 말라는 권고. [최윤섭 박사 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/) — 세 번의 리비전과 6개월 일화, 리뷰어 대응 전략. [엄태웅 대표 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/) — Conclusion·Future work·영어 교정에 관한 조언. Whitesides(2004) "Whitesides' Group: Writing a Paper" — Conclusions 절. Ch.16·Ch.29와 함께 읽는다. 네 유형 분류, 표현 대체 목록, 답변서의 세 부분 구조, 학회와 저널별 대응은 이 장에서 따로 정리했다.

[Part 4 — 발표와 학회](./chapter_33_conference_roi.md)
