# 21장 문단 흐름

문장 하나하나는 공들여 다듬었는데 단락으로 이어 읽으면 어딘가 흐름이 끊긴다고 호소하는 학생이 많다. 다섯 문장을 떼어 놓고 보면 흠잡을 데 없는데, 한데 붙여 놓으면 문장 사이가 삐걱거린다. 이 어색함은 개별 문장의 문법이 틀려서가 아니라, 문장의 첫머리(topic position)와 끝자리(stress position)가 단락 안에서 서로 맞물리지 않을 때 생긴다(→ [12장 §12.2](./chapter_12_reader_expectations_diagnosis.md)).

이 맞물림의 원리는 [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)이 잘 설명해 준다. 두 저자는 문장 첫머리에 이미 앞에서 나온 정보(old information)를 두고, 끝자리에 강조할 새 정보(new information)를 놓으라고 권한다. 이 배치는 문장 한 줄의 가독성을 넘어 단락 전체의 흐름까지 좌우한다. 첫머리마다 앞 내용과 이어 주지 못하는 낯선 말이 잇달아 나오면, 독자는 새 문장이 앞 문장과 어떤 고리로 이어지는지, 이 단락 안에서 무슨 구실을 하는지 매번 혼자 추측해야 하기 때문이다. 19장에서는 C-C-C로 단락의 어느 자리에 무엇이 들어갈지 큰 뼈대를 잡았고, 이번 장에서는 그 뼈대 안에서 문장과 문장을 틈 없이 잇는 방법을 다룬다.

---

## 21.1 문장 층위와 단락 층위

단락을 읽는 독자의 시선은 문장 층위와 단락 층위라는 두 흐름을 동시에 따라간다. 문장 안에서는 첫 자리(topic position)가 앞 문장을 받아 주는 연결 고리를 맡고, 끝자리(stress position)가 강조할 새 정보를 품는다. 한 단계 위인 단락 차원에서는 첫 문장이 들어가는 입구가 되고, 마지막 문장이 독자가 가져갈 요점(takeaway)을 건넨다.

잘 읽히는 단락에서는 이 두 층위가 모두 앞에서 나온 정보에서 새 정보 쪽으로 같은 방향을 바라보고 흐른다. 어느 한쪽이 엇나가면 독자는 문장이 바뀔 때마다 이 정보가 왜 지금 등장했는지 가늠하느라 에너지를 쓰고, 그런 작은 멈춤이 쌓이다 보면 단락 끝에 다다랐을 때 핵심 요점마저 흐려진다. 학생 원고에서 흔히 보이는 문제는 [29장](./chapter_29_reader_expectations.md)의 원칙을 떠올려 개별 문장은 어느 정도 손보면서도, 문장과 문장이 맞물리는 연결 상태까지 따로 점검해야 할 작업으로는 여기지 않는 데 있다.

---

## 21.2 Topic chain — 앞 문장과 잇는 첫머리

문장이 매끄럽게 넘어가려면 **각 문장의 첫 명사구가 앞 문장의 어딘가와 이어져 있어야 한다.** 가장 자연스러운 모양은 앞 문장의 끝자리에 놓였던 명사구를 다음 문장의 첫머리가 그대로 이어받는 형태다. 아래 두 예문을 나란히 놓고 첫 명사구가 어떻게 달라졌는지 살펴보자.

> 원문: The proposed method achieves 14% improvement on KITTI. Many KITTI sequences are challenging due to dynamic objects. Loop closure is critical.
>
> 연결을 일부 고친 문장: The proposed method achieves 14% improvement on KITTI. This benchmark contains many sequences that are challenging due to dynamic objects. Loop closure is critical.

예문의 14%는 문장 연결을 보여 주려고 넣은 가상 수치이며, 두 문안에 담긴 사실 정보는 똑같다. 원문에서는 첫 문장 끝의 KITTI와 둘째 문장 첫머리의 Many KITTI sequences가 느슨하게 겹치기만 하지만, 고친 문안에서는 둘째 문장이 This benchmark로 시작해 앞 문장의 KITTI를 곧바로 받는다. 덕분에 독자는 어느 데이터셋의 시퀀스를 가리키는지 한눈에 알아차린다.

반면 셋째 문장은 고친 뒤에도 여전히 앞 문장과 동떨어져 있다. Loop closure가 왜 중요한지, 앞서 말한 14% 향상이나 동적 물체와 어떤 관계가 있는지가 주어진 문장 어디에도 없기 때문이다. 이 빈틈을 메우려면 글재주로 문장을 이어 붙이기 전에 방법과 실험에서 근거부터 확인해야 한다. 연결을 살리겠다며 검증하지도 않은 "동적 물체가 있는 sequence에서도 14% 향상이 유지된다" 같은 말을 끼워 넣거나, critical을 most critical로 높여 부르면 원고에 없던 결과와 최상급 주장을 지어내는 셈이 된다.

앞 문장과 문장을 자연스럽게 잇는 **첫머리에는 바로 앞에 나온 명사나 대명사, 혹은 앞 문장 전체를 묶어 부르는 명사구**가 잘 어울린다. "this result", "such configurations" 같은 묶음 명사구가 좋은 연결 도구다. 이때 주의할 점을 [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)도 분명히 짚어 둔다. "this" 혼자 세우지 말고 반드시 뒤에 명사를 붙여 무엇을 가리키는지 밝히라는 것인데, 가령 "This is a fast reaction; This leads us to conclude" 대신 "This reaction is fast; This observation leads us to conclude"처럼 쓰면 앞 문장의 어느 대목을 받아 넘기는지 모호함이 사라진다.

---

## 21.3 Stress chain — 쌓여 가는 새 정보

Topic chain이 앞 문장과의 고리를 붙잡아 준다면, Stress chain은 단락의 논리를 앞으로 밀고 나간다. **한 문장의 끝자리에서 강조된 새 정보가 다음 문장의 첫머리로 넘어가면서, 단락 안에 새로운 정보가 층층이 쌓여 가는 구조다.**

> ✓ Textureless walls provide weak image gradients. Weak image gradients make photometric motion estimation less informative. This loss of photometric information motivates adding geometric constraints in a hybrid method.

이 세 문장을 따라가 보면 고리가 빈틈없이 맞물린다. 둘째 문장은 첫 문장 끝에 놓인 weak image gradients를 첫머리에서 그대로 받아 넘긴다. 이어 셋째 문장의 This loss of photometric information은 둘째 문장이 도달한 정보 손실을 한 묶음으로 받아, 기하 제약을 함께 쓰려는 이유로 연결한다. 그 결과 단락의 마지막 문장 끝자리에는 방법 선택의 이유라는 핵심 요점이 자연스럽게 올라선다.

다만 이 예문은 문장 흐름이 맞물리는 구조를 보여 줄 뿐, 그 방법이 실제로 통한다는 기술적 근거까지 대신해 주지는 않는다. 질감이 부족한 벽면에서는 밝기 변화에 기대는 추정이 약해지는 편이고, 기하 제약은 질감 유무와 무관하게 쓸 수 있다. 하지만 장면의 기하 구조 자체가 단조롭다면 기하 제약 역시 정보가 부족할 수 있으므로, 이 예문만으로 hybrid method의 성공이 보장되지는 않는다.

반대로 **문장 끝자리를 상투어가 차지하면 stress chain은 맥없이 끊긴다.** "in this paper", "of our approach" 같은 말이 매 문장의 끝을 막고 서면 정작 독자가 힘을 주어 읽어야 할 새 정보가 어디 있는지 흐려지고 만다. 이는 [12장 §12.2](./chapter_12_reader_expectations_diagnosis.md)에서 짚은 진단 1(stress position)과 똑같은 결함이다.

---

## 21.4 흔한 결함

Topic chain과 stress chain이 어긋날 때 학생 원고에서 되풀이되는 결함은 크게 네 가지로 요약된다.

**Topic 끊김.** 문장 첫머리에 앞 문장과 아무런 연결 고리가 없는 새 명사가 잇달아 등장해, 독자가 문장마다 앞뒤 관계를 스스로 이어 맞추어야 한다.

**Stress 흩뿌리기.** §21.3에서 본 것처럼 문장 끝자리마다 상투어가 자리 잡아, 강조되어야 할 새 정보가 문장 안쪽으로 밀려나 흐릿해진다.

**한 단락에 요점 둘.** 단락이 끝났을 때 독자가 들고 갈 요점 후보가 두 개 이상 남는다. [11장 §11.2](./chapter_11_ccc_lens.md)의 Q2(이 단락의 content는 한 가지인가)에서 바로 걸리는 결함이므로 단락을 나누어 각 요점에 독립된 자리를 주어야 한다.

**접속사 남발.** "However", "Moreover", "Therefore" 같은 접속사를 습관처럼 문장 첫머리에 둔다. 앞 문장의 내용을 이어 받는 명사구 대신 접속사만 세워 두면 topic chain이 텅 비어 버린다. 접속사는 앞뒤 정보 사이의 논리적 전환이나 인과 관계를 꼭 짚어야 할 때만 남긴다.

이 네 가지 결함은 읽을 때는 어렴풋이 "어색하다"는 느낌으로만 남지만, 문장의 앞뒤 조각을 따로 떼어 내면 눈으로 금방 가려낼 수 있다.

---

## 21.5 두 줄 뽑기로 스스로 진단하기

원고가 어딘가 뻑뻑하게 읽힌다면, 내 원고에서 단락 하나를 골라 아래 순서대로 두 줄을 뽑아 본다.

1. 문장마다 첫 명사구만 떼어 내 한 줄로 늘어놓는다. 이 줄이 **topic chain**이다.
2. 문장마다 마지막 명사구만 떼어 내 한 줄로 늘어놓는다. 이 줄이 **stress chain**이다.

뽑아낸 두 줄을 나란히 놓고 보면 단락의 건강 상태가 그대로 드러난다. Topic chain이 앞의 개념을 받아 자연스럽게 이어지는지, stress chain의 끝부분을 따라가며 새 정보가 차곡차곡 쌓이는지 살핀다. 두 줄 가운데 어느 한 곳이라도 뚝 끊기거나 헛도는 자리가 곧 흐름이 막힌 지점이다.

---

## 21.6 CCC 점검과 함께 쓰기

큰 뼈대와 세밀한 연결은 서로를 대신할 수 없지만, 두 점검이 모두 필요하다. C-C-C 골격을 잘 갖춘 단락이라도 둘째 문장 첫머리가 첫 문장 끝을 받아 주지 못하면 여전히 문장 사이가 삐걱거린다. 거꾸로 C-C-C가 무너진 단락은 두 줄 뽑기를 해 보면 stress chain의 마지막 낱말이 애초에 결론에 닿지 못한 채 겉도는 모습으로 나타난다.

따라서 점검 순서는 **C-C-C를 먼저, 두 줄 뽑기를 나중**으로 잡는 편이 낫다. 각 자리에 맥락과 내용, 결론이 빠짐없이 들어갔는지 확인한 뒤에야 문장과 문장을 매끄럽게 잇는 작업이 의미를 갖는다. 들어갈 내용 자체가 비어 있는데 문장 연결부터 다듬어 놓으면 빈자리는 결국 빈자리로 남기 때문이다.

이로써 아웃라인 설계([17장](./chapter_17_outline_first.md))와 시간 배분([18장](./chapter_18_time_budget.md))에서 출발해 C-C-C 구조([19장](./chapter_19_ccc.md)), 주장을 담은 소제목과 결론([20장](./chapter_20_subheadings_and_conclusions.md)), 그리고 문단 흐름까지 쓰기의 기본 도구를 모두 갖추었다. 다음 장부터는 이 도구를 실제 논문의 각 섹션에 차례로 적용해 보며, 독자가 가장 먼저 마주하는 제목과 초록부터 차근차근 짚어 나간다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) — topic position의 old information이 앞 문장과 어떻게 이어지는지, 단락 전체가 어떻게 전개되는지를 독자에게 알려 준다는 설명. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 3(단락 규모의 C-C-C). [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) — "this" 뒤에 명사를 붙이라는 권고.

다음: [22장 제목과 초록](./chapter_22_title_abstract.md)