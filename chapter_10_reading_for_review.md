# Ch.10 — 심사위원으로 읽기

[Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.3은 심사위원이 한 번 훑어보고도 요지를 잡지 못하면 그 논문이 반려될 가능성이 크다고 설명한다. 그 한 번이 1st pass다. 다만 의견을 작성하는 단계는 3rd pass다. 두 패스를 섞으면 근거가 부족한 인상 비평이 된다.

---

## 10.1 3rd pass를 완주한다는 것

Keshav는 3rd pass가 초보 독자에게 약 4-5시간, 숙련된 독자에게 약 한 시간이 걸릴 수 있다고 적었다. 심사에 필요한 실제 시간은 논문 길이와 분야 친숙도에 따라 달라지므로, 의뢰를 수락할 때 충분한 작업 블록을 먼저 잡는다. Keshav 원문은 전문성 부족이나 촉박한 deadline에 대한 수락 기준을 다루지 않는다. 그 결정은 venue의 reviewer policy에 따라 이해 충돌·전문성·가용 시간을 확인하고, 감당할 수 없으면 즉시 거절하거나 area chair에게 알린다.

3rd pass의 핵심은 저자와 같은 가정을 놓고 논문을 머릿속으로 재구현해 보는 것이다(Keshav §2.3). 모든 코드를 실제로 다시 만들라는 뜻은 아니다. 주장·가정·실험 절차를 따라가며 무엇이 생략됐는지 확인한 뒤 코멘트를 쓴다.

같은 자세가 지적 성실성의 한 면이다. [김기섭 교수](https://gsk1m.github.io/productivity/2024/05/25/entering-research.html)가 적은 한 줄이 그 자세를 짧게 정한다.

> "실험 결과가 가설과 다르면, 결과를 의심하기 전에 가설을 의심하라."

심사위원도 본문이 자기 직관과 다르게 흘러갈 때는 자기 사전 가정이 틀렸을 가능성부터 봐야 한다. 자기 마음을 바꿀 수 있는 학생만이 심사위원 코멘트에서도 자기 가설을 의심한다. 무엇을 모르는지 아는 메타인지가 심사위원 적격성의 핵심과 겹친다.

---

## 10.2 Virtual re-implementation 4단계

Keshav §2.3은 "challenge every assumption"을 심사위원 모드의 핵심 동작으로 든다. 아래 네 단계는 그 권고를 학생이 수행할 수 있게 이 장에서 만든 절차다.

1. **기여 목록을 자기 언어로 다시 적는다.** 저자 표현을 그대로 베끼지 않는다. 베끼면 자기 머리를 통과하지 않은 채 다음 단계로 간다.
2. **각 contribution마다 "내가 이걸 만든다면 어떻게?"를 즉흥 설계한다.** 노트 한 페이지에 3-5분을 써 보는 것은 시작 예시일 뿐이다. 논문의 복잡도에 맞게 늘리되 초안을 깔끔하게 만드는 데 시간을 쓰지 않는다.
3. **저자의 선택과 자기 즉흥을 비교한다.** 두 설계가 어긋나는 지점을 표시한다. 설계 대안이 다른지, 가정이나 자신의 이해가 다른지 살펴볼 출발점이다.
4. **차이가 왜 생겼는지 본문에서 근거를 찾는다.** 결론에 필요한 가정인데도 본문에 설명이 없다면 unstated assumption의 후보로 기록한다. 아직 이유를 모르는 설계 차이는 먼저 확인할 질문으로 남긴다.

이 절차는 `내가 했다면 다르게 했을 텐데, 저자는 왜 이렇게 했나?`라는 질문을 만든다. 그것이 곧 evidence-based question이다. 그런 질문이라야 심사위원 코멘트로 쓸 자격이 생긴다.

---

## 10.3 가정 유형별 진단

Keshav는 가정 유형을 따로 분류하지 않았다. 로보틱스/CV 분야에서 반복적으로 나타나는 유형 5가지는 다음과 같다.

**데이터 가정.** 분포가 i.i.d.라고 명시되거나 묵시되는 경우다. 시간·장소·sensor가 이어지는 로보틱스 데이터에서는 독립·동일분포 가정이 성립하는지 따로 확인해야 한다. 진단 질문은 "이 분포가 i.i.d.가 아니면 결과가 어디서 무너지나?"이다.

**벤치마크 가정.** [KITTI](https://www.cvlibs.net/datasets/kitti/)만으로 넓은 generalization을 주장한다면 다른 환경·sensor 조건의 근거가 필요한지 묻는다. [Newer College](https://ori-drs.github.io/newer-college-dataset/)나 [MulRan](https://sites.google.com/view/mulran-pr/home)은 가능한 후보일 뿐 모든 논문에 필수인 dataset은 아니다.

**Baseline 선택 가정.** claim과 가장 가까운 강한 비교군이 빠져 있는 경우다. 제출 시점의 관련 연구와 동일 protocol에서 비교 가능한 방법을 확인하고, "이 baseline을 고른 이유가 본문에 있나?"라고 묻는다.

**Ablation 누락 가정.** 기여가 셋인데 ablation은 하나만 등장하는 표를 만났다면, 나머지 둘을 어떤 근거로 뒷받침하는지 확인한다. 다른 실험이나 증명이 있을 수 있으므로 ablation의 수만으로 검증이 없다고 판단하지 않는다.

**수학적 가정.** 가정 1, 2, 3이 나열되었는데 그중 하나가 결과에 결정적이고 그 한 가정만 본문에 motivation 한 줄도 없는 경우다. Keshav가 든 "challenge every assumption"이 적용되는 곳이다.

다섯 유형의 공통점은 challenge가 곧 evidence 요청이라는 점이다. 톤은 [Ch.32 (개정과 답변서)](./chapter_32_revision_rebuttal.md)에서 받는 쪽 입장과 함께 다룬다.

---

## 10.4 코멘트 한 줄 = 본문 한 위치

"전반적으로 동기 부여가 약함"처럼 위치 없는 코멘트는 저자가 어디를 고쳐야 하는지 알기 어렵다. 가능한 경우 코멘트를 본문 위치(섹션·페이지·줄·그림 번호)와 짝짓고, 원고 전체 문제라면 반복되는 대표 위치를 든다.

작업 양식은 단순하다. 시트 하나에 세 칸을 둔다.

```
[코멘트 본문] | [근거 위치] | [심각도: major / minor / clarification]
```

심각도 분류 규칙을 정해 두면 일관성이 올라간다.

- **Major**: 핵심 contribution claim을 흔드는 evidence 부족. 예: "Section 3.2 (p.4, l.12) claims rotation-invariance, but the ablation in Table 2 omits rotation perturbation."
- **Minor**: 명확성·표기·실험 보강 요청. 예: "Figure 4의 y축 단위 누락."
- **Clarification**: "이게 X를 의미하는 게 맞나요?" 형태의 질문.

Major issue의 심각도와 수정 가능성은 추천을 판단하는 근거 가운데 하나다. accept/weak accept/reject 척도와 판단 기준은 venue rubric을 따른다. 저자의 이름·기관·익숙한 표기처럼 논문 내용과 무관한 요소가 결정에 끼어들면 공정한 심사가 아니다.

분야 적격성은 별도 판단이다. reviewer form에 confidence 척도가 있다면 venue가 정한 의미에 맞춰 모르는 부분을 낮게 표시하고, 평가할 수 없는 핵심 영역은 area chair에게 알린다. 1-5가 모든 venue의 공통 척도는 아니다. Keshav가 말한 것처럼 전체 그림을 보기 전에 디테일에 빠지지 않는 절차도 의견 작성에 적용된다.

---

같은 referee-as-teacher 회로가 후배 멘토링에서 다시 굴러간다. 「대학원노트」 [Ch.21 「후배를 키운다」](../grad-notes/chapter_21_mentor_juniors.md)가 이 장의 관점을 후배 멘토링 층위로 옮긴다. 동료의 글을 reviewer-as-teacher 자세로 읽는 일과 미래의 독립 연구 책임자로서 설명과 피드백을 연습하며 후배를 가르치는 일이, 결국 같은 관점의 두 적용이다.

**출처.** [Keshav 2007](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) §2.3(3rd pass, virtual re-implementation, "challenge every assumption", 독서 시간의 대략적 예). reviewer 수락·confidence·recommendation 기준은 각 venue의 공식 policy를 우선한다. 가정 유형 분류와 심각도 판별 기준, 위치 매칭 양식은 심사 실무에 맞추어 본문에서 체계화한 것이다.

다음: [Ch.11 — CCC 렌즈로 논문 해부하기](./chapter_11_ccc_lens.md)
