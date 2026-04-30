# Ch.10 — Reviewer로 읽기

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.3은 "리뷰어가 한 번 훑어보고도 요지를 잡지 못하면 그 논문은 십중팔구 반려된다"고 적었다. 그 한 번이 1st pass다. 다만 의견을 *작성*하는 단계는 3rd pass다. 두 패스를 섞으면 인상 비평이 되고, 인상 비평은 reviewer 자신을 reject 사유로 만든다.

---

## 10.1 3rd pass를 완주한다는 것

Keshav가 새내기 reviewer에게 권장한 시간은 4-5시간이다. 본인은 1시간 안쪽으로 끝낸다고 적었지만, 이 차이는 *경력*이지 *능력*이 아니라는 점을 동시에 강조했다. 그래서 의뢰를 수락한 시점에 캘린더에 5시간 블록을 박는 것이 첫 작업이다. 회피하기 좋은 사유가 두 가지 있다. "내 분야가 아니어서 잘 모르겠다"와 "deadline이 일주일 남았다". Keshav는 둘 다 답이 아니라고 적었다. 전자에는 §4의 *적격성 유보* 양식이 받고, 후자에는 거절 회신이 받는다.

3rd pass의 정의 자체가 *논문을 머릿속으로 재구현해 보는 것*이다 (Keshav §2.3). 재구현 없이 적은 코멘트는 reviewer 본인 위치에서 검증된 의견이 아니다. editor가 이런 review를 받으면 reviewer 풀에서 빼는 쪽이 합리적이라는 점을, reviewer 의뢰를 처음 받은 사람이 먼저 알아두는 편이 안전하다.

같은 자세가 *지적 성실성*의 한 면이다. [김기섭 교수](https://gsk1m.github.io/productivity/2024/05/25/entering-research.html)가 적은 한 줄이 그 자세를 짧게 정한다.

> *"실험 결과가 가설과 다르면, 결과를 의심하기 전에 가설을 의심하라."*

reviewer 자세에서 같은 권고를 적용하면, 본문이 자기 직관과 다르게 흘러갈 때 *논문이 틀린 게 아니라 자기 사전 가정이 틀렸을 가능성*을 먼저 본다는 절차가 된다. 자기 마음을 바꿀 수 있는 학생만이 reviewer 코멘트에서도 *자기 가설*을 의심하는 절차를 굴린다. *내가 모르는 것이 무엇인지 아는* 메타인지가 reviewer 적격성의 본체와 겹친다.

---

## 10.2 Virtual re-implementation 4단계

Keshav §2.3은 "challenge every assumption"을 reviewer 모드의 핵심 동작으로 든다. 이 동작을 학생이 실제로 수행할 수 있는 절차로 풀면 다음 4단계가 된다.

1. **Contribution 목록을 자기 언어로 다시 적는다.** 저자 표현을 그대로 베끼지 않는다. 베끼면 자기 머리를 통과하지 않은 채 다음 단계로 간다.
2. **각 contribution마다 "내가 이걸 만든다면 어떻게?"를 3-5분 즉흥 설계한다.** 노트 한 페이지면 충분하다. 깔끔할 필요는 없다.
3. **저자의 선택과 자기 즉흥을 비교한다.** 두 설계가 어긋나는 지점이 있다. 그 지점이 *implicit assumption*이다.
4. **차이가 *왜* 다른지 본문에서 근거를 찾는다.** 못 찾으면 그 가정은 unstated assumption이고, reviewer 코멘트의 일등 후보가 된다.

이 절차는 `왜 이 선택?`이 아니라 `내가 다르게 했을 텐데 저자는 왜 같지 않았나?`를 질문으로 만든다. 후자가 곧 evidence-based question이다. 전자는 의견에 그치는 한편, 후자는 reviewer가 작성할 자격이 있는 코멘트가 된다.

---

## 10.3 가정 유형별 진단

Keshav는 가정 유형을 따로 분류하지 않았다. 그래서 로보틱스/CV 분야에서 반복적으로 나타나는 유형 5가지를 자체로 정리하면 다음과 같다.

**데이터 가정.** 분포가 i.i.d.라고 명시되거나 묵시되는 경우다. 로보틱스에서는 거의 깨진다. 진단 질문은 "이 분포가 i.i.d.가 아니면 결과가 어디서 무너지나?"이다.

**벤치마크 가정.** [KITTI](https://www.cvlibs.net/datasets/kitti/)만 등장하고 [Newer College](https://ori-drs.github.io/newer-college-dataset/)나 [MulRan](https://sites.google.com/view/mulran-pr/home)이 비어 있는 결과 표가 흔하다. 저자가 generalization을 주장한다면, 그 지점에서 evidence가 부족해진다.

**Baseline 선택 가정.** 비교 대상이 2년 전 SOTA로 굳어 있고 최신 baseline이 빠져 있는 경우다. 진단 질문은 "이 baseline을 고른 *이유*가 본문에 있나?"이다.

**Ablation 누락 가정.** Contribution이 셋인데 ablation은 하나만 등장하는 표가 자주 보인다. 나머지 둘은 검증 없이 기여로 적혔다.

**수학적 가정.** 가정 1, 2, 3이 나열되었는데 그중 하나가 결과에 결정적이고 *그 한 가정만* 본문에 motivation 한 줄도 없는 경우다. Keshav가 든 "challenge every assumption"이 가장 강하게 적용되는 곳이다.

다섯 유형의 공통점은 challenge가 *공격*이 아니라는 점이다. 곧 evidence 요청이다. 톤은 본 가이드 [Part 2 ch17 (Revision·Rebuttal)](./chapter_32_revision_rebuttal.md)에서 받는 쪽 입장과 함께 다룬다.

---

## 10.4 코멘트 한 줄 = 본문 한 위치

Reviewer 양식에서 coordinator가 가장 자주 거절하는 코멘트는 *위치 없는 코멘트*다. "전반적으로 동기 부여가 약함"에는 위치가 없다. 그래서 editor가 이를 저자에게 전달하기 어렵고, 저자는 어디를 고쳐야 하는지 모른다. 결국 코멘트는 본문 위치(섹션·페이지·줄·figure 번호)와 1대1로 짝지어야 한다.

작업 양식은 단순하다. 시트 하나에 세 칸을 둔다.

```
[코멘트 본문] | [근거 위치] | [심각도: major / minor / clarification]
```

심각도 분류 규칙을 자체로 정해두면 일관성이 올라간다.

- **Major**: 핵심 contribution claim을 흔드는 evidence 부족. 예: "Section 3.2 (p.4, l.12) claims rotation-invariance, but the ablation in Table 2 omits rotation perturbation."
- **Minor**: 명확성·표기·실험 보강 요청. 예: "Figure 4의 y축 단위 누락."
- **Clarification**: "이게 X를 의미하는 게 맞나요?" 형태의 질문.

Major 수와 fix 가능성이 추천(accept/weak accept/reject) 결정의 본체가 된다. 저자의 이름·기관·표기 친숙도가 결정에 끼어들면, 그것이 *그 reviewer의 reject 사유*가 된다.

분야 적격성은 별도 칸이다. Reviewer 양식의 *confidence*는 1-5 척도가 흔하다. 이 칸은 모르는 부분을 모른다고 적기 위한 칸이지, 통과시켜 주기 위한 칸이 아니다. 평가 못 하는 부분을 아는 척 통과시키면 적격성 유보의 반대편으로 가게 된다. Keshav가 적은 표현으로는, "전체 그림을 보기도 전에 디테일에 빠져 익사하지" 않는 절차가 의견 작성에도 똑같이 적용된다.

---

같은 *referee-as-teacher* 회로가 후배 멘토링에서 다시 굴러간다. 「대학원노트」 [Part 5 ch01 「후배를 키운다」](../grad-notes/chapter_21_mentor_juniors.md)가 본 챕터의 frame을 *후배 멘토링* layer로 옮긴다. 동료의 글을 reviewer-as-teacher 자세로 읽는 일과 후배를 미래의 본인을 위한 리더십 위치에서 가르치는 일이, 결국 같은 frame의 두 적용이다.

**출처.** [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.3 (3rd pass + virtual re-implementation, "challenge every assumption", reviewer 시간 예산). 가정 유형 분류·심각도 규칙·위치 매칭 양식은 자체.

다음: [Ch.6 — CCC 렌즈로 논문 해부하기](./chapter_11_ccc_lens.md)
