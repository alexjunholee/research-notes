# 32장 개정과 답변서

원고를 다듬어 투고하고 몇 달 뒤 심사위원 의견을 처음 받아 들면, 억울함과 화부터 치밀어 오르기 쉽다. "리뷰어가 내 논문을 제대로 읽지도 않았다"는 생각이 제일 먼저 머리를 스치고, 실제로 그 생각이 맞을 때도 적지 않다. 하지만 그 감정 그대로 펜을 들면 답변서가 아니라 날 선 변호문이 되고 만다.

심사위원의 의견은 내 논문이 저자의 의도를 떠나 다른 전문가의 눈에 어떻게 읽혔는지 보여 주는 가장 솔직한 거울이다. 화만 내고 덮어 버리면 그 귀한 진단 자료를 고스란히 버리는 셈이 된다. [임형태 박사](https://github.com/LimHyungTae/paper-writing-checklist)는 논문에서 "이 세상에 없던 지식을 타인이 읽고도 오해 없이 명확하게 이해할 수 있도록 하는 것이 무엇보다 중요"하다고 적었다. 심사위원이 오해했다면, 결국 내 글이 아직 그 명료함에 이르지 못했다는 뜻이다. 모든 답변서는 바로 이 전제에서 출발해야 한다.

---

## 32.1 심사위원 의견의 네 유형

감정을 가라앉혔다면 무작정 첫 줄부터 답을 쓰기 전에 심사평을 네 가지 유형으로 먼저 분류해 본다. 어느 유형에 속하느냐에 따라 답변의 어조와 본문을 고칠 범위가 완전히 달라지기 때문이다.

**유형 1 — Factual error.** 수식, 실험 설정, 인용, 수치가 명백히 틀린 경우다. 변명하려 들수록 심사위원의 반감만 키우므로 오류를 깨끗이 인정하고 곧바로 바로잡는다.

> "We thank the reviewer for catching this. Equation (7) was incorrect; the corrected derivation is now in §3.2 (page 5)."

**유형 2 — Presentation 요구.** 그림을 추가하거나 표를 다시 짜고, 문장 순서를 바꾸거나 개념 정의를 더 밝혀 달라는 요청이다. 타당한 지적이라면 기꺼이 수용해 고친 위치를 정확히 알려 주고, 지면 한도를 넘긴다면 venue 정책이 허용하는 보충자료로 옮기거나 다른 문단을 줄일 방법을 찾는다. 만약 받아들이기 어려운 요청이라면 단순히 거절하지 말고 지면 한계나 논문 범위(scope) 같은 구체적인 이유를 대면서 대신 해 줄 수 있는 보완을 제시한다.

**유형 3 — Scope/contribution 의문.** "이게 왜 새로운가?", "X와 무엇이 다른가?" 같은 근본적인 질문이다. 이때는 답변서에서만 핵심 contribution을 한두 문장으로 되풀이하지 말고, 관련 인용과 실험을 근거로 삼아 본문의 서론과 Related Work도 함께 보강해야 한다. comment에만 답하고 본문을 그대로 두면, 다음 심사위원이나 앞으로 논문을 읽을 독자도 똑같은 질문을 던진다.

**유형 4 — 단순 오해.** 심사위원이 본문을 명백히 잘못 읽은 경우다. 이럴 때도 심사위원의 실수("the reviewer misread X")를 짚기보다, 내 글이 충분히 분명하지 못했음을 인정하고 본문 어디를 어떻게 고쳤는지 알린다.

> "We realize that §4.1 was not sufficiently clear; we have rewritten the paragraph to emphasize that …"

심사위원 한 사람이 잘못 읽은 대목이라면 다른 독자도 똑같이 걸려 넘어질 가능성이 높으니 그 문단부터 다시 손보는 편이 맞다. 다만 comment가 원고에 전혀 없는 내용을 전제한다면, 해당 본문 위치를 들어 사실관계를 차분하게 바로잡아 준다.

---

## 32.2 무례하게 들리는 단어 바꾸기

의견을 분류해 답변 방향을 잡았다면, 이제 문장마다 뾰족한 표현이 남아 있지 않은지 걸러 내야 한다. 몇몇 단어는 저자의 의도와 상관없이 답변서 전체의 어조를 단번에 망친다.

**주의할 표현과 대안.**

- "outperform" — 임형태 박사는 이 단어를 논문에서 "절대로" 쓰지 말자고 했다. baseline 저자가 바로 그 심사위원일 가능성이 높아서다. → "showed lower error"처럼 완곡하게 쓰고 metric·dataset·조건을 함께 적는다
- "fail to" — 심사위원의 행동에 쓰면 모욕으로 들린다. → "may have been unclear because"
- "obviously / clearly" — 독자를 무시하는 말로 들린다. → 지운다
- "the reviewer is mistaken" → "we have clarified that …"
- "as we already stated" — 짜증이 묻어난다. → "to make this clearer, we have added …"

앞서 [12장 §12.2](./chapter_12_reader_expectations_diagnosis.md)에서 짚은 stress position 원칙은 답변서에서도 그대로 작동한다. 무례하거나 방어적인 단어가 문장 맨 끝에 자리 잡으면 그 날 선 어감이 훨씬 두드러지게 들리므로, 단어만 바꿔서 어색하다면 문장 전체를 통째로 다시 쓰는 편이 낫다.

---

## 32.3 답변서의 세 부분

어조를 잡았다면 답변서의 뼈대를 세 부분으로 나누어 채운다.

**첫 부분 — 감사와 변경 요약.** 전체 길이는 5~8줄 안팎으로 짧게 쓴다. 인사말이 장황하면 독자가 변경 사항을 늦게 보게 되므로, 첫 줄에 한 문장으로 감사한 뒤 곧바로 주요 변경 사항(major change)에 번호를 붙여 요약한다.

> "We thank the reviewers for their constructive feedback. The major changes are: (1) we added experiments on MulRan (§5.3), (2) we clarified the relation to Vizzo et al. 2023 (§2.2), (3) we corrected Equation (7) (§3.2)."

**둘째 부분 — 항목별 답변.** 심사위원별로 구역을 나누고, 그 안에서 개별 comment마다 다음 세 단계를 빠짐없이 갖춘다.

1. **Comment 원문.** italic이나 quote 블록으로 그대로 옮긴다.
2. **Response.** 우리 답변을 적는다.
3. **Change in manuscript.** 본문 어디를 어떻게 고쳤는지 페이지, 섹션, 수식 번호로 정확히 밝힌다.

여기서 가장 흔히 빠지는 것이 세 번째 항목이다. 답변에 "we agree …"라고만 적어 두고 정작 본문이 바뀐 곳을 안 알려 주면 심사위원이 변경 사항을 직접 찾아야 하므로, 다음 심사에서도 같은 comment가 다시 오기 쉽다.

**셋째 부분 — 마무리.** 마지막 인사는 한두 문장으로 깔끔하게 끝맺고, 감사는 한 번만 전한다.

> "We hope these revisions address the reviewers' concerns."

고친 본문을 어떻게 표시할지는 venue와 editor의 지침을 그대로 따른다. 변경 추적 PDF를 요구하는지, 색상 표시를 원하는지, 아니면 clean manuscript만 내면 되는지 먼저 확인하고, 따로 지침이 없다면 답변서에 변경 위치를 page·section·line으로 정확히 적는다.

분량은 대개 comment당 100~200단어 안팎에서 출발하되 정해진 정답은 없으며, venue가 정한 전체 word·character 제한을 먼저 따른다. 답변이 길어졌다면 혹시 결론과 근거, 본문 변경 내용을 같은 말로 되풀이하고 있지 않은지 살펴보고 겹치는 부분을 덜어 낸다.

---

## 32.4 원고를 고칠 때 결론에서 피할 것

답변서와 함께 본문을 손보다 보면, 심사평에서 지적한 거절 사유가 유독 Conclusion과 Future work 대목에서 되풀이되는 경우를 자주 만난다. [엄태웅 대표의 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/)에서는 Conclusion을 쓸 때 저지르는 실수와 영어 교정 문제를 다음 네 가지로 짚는다.

- **Conclusion을 Abstract처럼 쓰는 실수.** Abstract는 논문을 읽지 않은 사람이 처음 읽는 글이고, Conclusion은 논문을 다 읽은 사람에게 전체를 정리해 주는 글이다. 그래서 Abstract는 문제 제기와 연구의 중요성·기여에, Conclusion은 실험으로 얻은 지식과 그 의의에 무게를 조금 더 두어야 한다.
- **Conclusion에서 새 이야기를 꺼내는 실수.** 본문에서 주장한 것보다 한 걸음 더 나아가는 것도 마찬가지로 부적절하다.
- **Future work에 너무 많은 것을 늘어놓는 실수.** 이 분야 사람들은 Future work가 "OOO은 안 했음"이라는 뜻임을 안다. 그래서 하지 못한 것을 Future work로 방어하는 방법은 좋지 않다. 연구의 한계는 결과 논의 끝에 솔직히 밝힌다.
- **원어민 영어 교정에 기대는 실수.** 교정자는 내용을 이해하지 못한 채 문법을 고치므로, 저자와 대화가 없으면 교정이 오히려 오해를 만들어 내기 일쑤다. 저자 스스로 좋은 영어를 쓰도록 노력해야 한다.

Whitesides 역시 Conclusions가 단순 요약이 아니라 한 단계 높은 분석이어야 한다고 강조했다([20장 §20.4](./chapter_20_subheadings_and_conclusions.md)). 심사위원의 지적이 본래 결론에 들어갔어야 할 내용을 가리킨다면, 답변서로 무마하려 들지 말고 본문의 그 부분부터 먼저 고쳐야 한다.

결론을 다듬는 수준을 넘어 실험을 더 해 달라는 의견도 자주 온다. [최윤섭 박사의 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/)에 실린 세 번의 리비전과 6개월간의 추가 실험 일화는 이미 [16장](./chapter_16_mindset.md)에서 살펴보았다. 최윤섭 박사가 강조하듯, 심사위원의 지적에 어떤 논리와 실험으로 대응할지 전체 전략을 세우는 일이 무엇보다 중요하다.

심사위원이 ablation 실험을 더 요구했는데 어떤 조합을 더 확인해야 할지 막막하다면 AI에게 실험 설계 초안을 물어볼 수 있다. 내 모델이 baseline보다 무엇을 개선했는지 보이려면 어떤 ablation이 필요한지 묻거나, 새 결과 표가 나온 뒤에 그 표로 어떤 분석을 끌어낼 수 있을지 묻는 식이다. 다만 AI는 어디까지나 내가 놓친 관점을 짚어 주는 보조 도구로만 쓴다.

> AI가 제안한 ablation을 그대로 본문에 넣지 않는다. AI는 내 연구의 contribution과 맞지 않는 ablation을 제안하기도 한다. 실험 설계는 연구자가 최종 판단한다.

따라서 최종 실험 설계는 연구자가 직접 결정하고, 받아들인 ablation이 논문의 contribution을 어떻게 뒷받침하는지 각각 한 줄로 정리해 답변서에 넣는다.

---

## 32.5 까다로운 심사 의견 대응 사례

투고처와 판정 결과에 따라 개정과 답변을 준비하는 조건도 달라지므로, 각 상황에 맞춰 일정을 잡아야 한다.

**Major revision.** 본문 논리와 실험을 크게 보강해야 하는 경우다. 흔히 8~12주를 예로 들 수 있지만 실제 기한은 editor letter에 적혀 있으니, 공식 마감 안에 모든 작업을 끝낸다.

**Minor revision.** 대개 사실관계나 표현, 국소적인 설명을 고치는 수준이다. 그래도 공식 기한과 필요한 검증 절차를 거꾸로 따져 일정을 잡는다.

**Reject (with encouragement to resubmit).** 불합격이지만 재투고를 권유받았다면 decision letter가 허용하는 경로와 새 투고 요건을 먼저 확인한다. 심사 의견을 단순히 문구만 고치는 수준이 아니라 claim, evidence, scope 수준에서 깊이 반영한 뒤, 논문이 얼마나 바뀌었는지와 각 venue의 정책을 보고 같은 곳에 다시 낼지 다른 venue로 옮길지 정한다. 같은 곳에 다시 내더라도 새 심사위원이 배정될 수 있음을 염두에 둔다.

**Conference rebuttal.** 학회 rebuttal은 page·word·character 제한과 새 실험 허용 여부가 venue와 연도마다 다르다. CVPR, NeurIPS, ICRA가 모두 같은 규칙을 쓸 것이라 가정하지 말고 반드시 그해의 author instructions를 확인한다. 답변을 supplementary에 둘 수 있는지도 공식 정책을 살펴 따른다.

**24시간 미루기.** 리뷰를 받은 뒤 첫 24시간은 답변서를 한 줄도 쓰지 않고 묵혀 둔다. 화와 억울함이 가라앉은 뒤에야 §32.1의 분류부터 냉정하게 시작할 수 있다. conference rebuttal처럼 마감이 촉박하면 어렵더라도, 시간에 여유가 있는 journal revision에서는 꼭 권하고 싶은 습관이다.

---

## 32.6 마지막 점검 — 심사위원이 되어 답변서 읽기

답변서 초안을 다 썼다면 되도록 시간을 조금 두었다가, 이번에는 내 편이 아니라 심사위원의 눈으로 처음부터 다시 읽는다. (24시간은 일정의 예일 뿐 정해진 제출 규칙이 아니다.) 이때 다음 두 가지만은 끝까지 확인한다.

먼저, 억울해서 변명하는 글처럼 읽히는 곳이 남아 있지 않은지 본다. "we already stated", "the reviewer fails to", "this is obvious" 같은 말투가 한 줄이라도 보이면 바로 걷어 낸다.

다음으로, comment마다 `Change in manuscript` 항목이 빠짐없이 채워져 있는지 확인한다. 이 항목이 비어 있다면 그 comment에는 사실상 아직 답하지 않은 것이나 다름없다.

이 두 관문을 모두 통과했다면 비로소 답변서를 제출해도 좋다.

여기까지가 논문을 쓰고 다듬어 심사위원을 설득해 내는 과정이다. 하지만 어렵게 통과한 논문도 학술지에 조용히 묻어 두면 연구의 절반밖에 끝내지 못한 셈이다. 이제 4부에서는 완성된 논문을 들고 학회 현장으로 나가 세상과 직접 대화하는 법을 살펴본다.

---

**출처.** [임형태 박사, paper-writing-checklist](https://github.com/LimHyungTae/paper-writing-checklist) — 오해 없이 이해되는 글이 가장 중요하다는 원칙, 'outperform'을 쓰지 말라는 권고. [최윤섭 박사 「첫 번째 논문을 최대한 빨리 써라」](https://gradschoolstory.chkwon.net/yoonsup/first-paper/) — 세 번의 리비전과 6개월 일화, 리뷰어 대응 전략. [엄태웅 대표 「영어 못해도 논문 잘 쓰는 법」](https://gradschoolstory.chkwon.net/terry/englishpaperwriting/) — Conclusion·Future work·영어 교정 조언. Whitesides(2004) "Whitesides' Group: Writing a Paper" — Conclusions 절. 16장·29장과 함께 읽는다.

다음: [33장 학회에 가는 이유와 비용](./chapter_33_conference_roi.md)
