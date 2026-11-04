# Ch.21 — 문단 흐름

문장 하나하나는 다듬었는데 단락으로 이어 읽으면 흐름이 끊긴다는 학생이 있다. 다섯 문장을 따로 보면 멀쩡하지만 이어 붙이면 어딘가 어긋난다. 이런 어긋남은 [Ch.12 §12.2](./chapter_12_reader_expectations_diagnosis.md)에서 다룬 topic position과 stress position 원칙이 단락 안에서 지켜지지 않을 때 생긴다.

[Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing)은 문장 첫머리에 앞에서 나온 정보(old information)를, 끝에 강조할 새 정보(new information)를 두라고 한다. 두 사람은 이 배치가 문장 하나를 넘어 단락 전체의 흐름에도 영향을 준다고 적었다. 첫머리를 앞 내용과 이어 주지 못하는 말이 계속 차지하면 독자는 새 문장이 앞 문장과 어떻게 이어지는지, 단락 안에서 무슨 구실을 하는지 알기 어렵다고 했다. Ch.19의 CCC로는 단락의 어느 자리에 무엇이 들어가는지를 점검했다. 이 장에서는 문장에서 문장으로 정보가 어떻게 넘어가는지를 본다.

---

## 21.1 문장 층위와 단락 층위

단락을 읽는 독자는 두 층위를 함께 따라간다. 문장 안에서는 첫 자리(topic position)가 앞 문장과 이어 주는 말을 받고, 끝자리(stress position)가 새 정보를 받는다. 단락 안에서는 첫 문장이 들어가는 입구가 되고, 마지막 문장이 독자가 가져갈 요점(takeaway)을 받는다.

두 층위 모두 앞에서 나온 것에서 새것으로 나아간다. 흐름이 자연스러운 단락에서는 두 층위가 같은 방향으로 움직인다. 어느 한 층위가 어긋나면 독자는 문장마다 이 정보가 왜 지금 나오는지 짐작해야 하고, 그런 짐작이 쌓이면 단락 끝에서 요점이 흐려진다.

학생 원고에서는 단락 층위가 어긋나기도 한다. 문장은 [Ch.29](./chapter_29_reader_expectations.md)의 원칙으로 어느 정도 다듬지만, 문장과 문장을 잇는 일을 따로 점검해야 할 작업으로 여기지 않기도 한다.

---

## 21.2 Topic chain — 앞 문장과 잇는 첫머리

**문장의 첫 명사구는 앞 문장의 어딘가와 이어져야 한다.** 흔히 쓰는 모양은 앞 문장 끝자리에 나온 명사구를 다음 문장 첫머리가 받는 모양이다.

> 원문: The proposed method achieves 14% improvement on KITTI. Many KITTI sequences are challenging due to dynamic objects. Loop closure is critical.
>
> 연결을 일부 고친 문장: The proposed method achieves 14% improvement on KITTI. This benchmark contains many sequences that are challenging due to dynamic objects. Loop closure is critical.

예문의 14%는 문장 연결을 보여 주려고 넣은 가상 수치다. 두 문안에 담긴 정보는 같다. 고친 문안에서는 둘째 문장의 this benchmark가 앞 문장의 KITTI를 받으므로 어느 자료의 sequence인지 바로 알 수 있다.

셋째 문장은 여전히 앞과 이어지지 않는다. Loop closure가 왜 중요한지, 앞의 성능이나 동적 물체와 어떤 관계인지가 주어진 문장에는 없다. 이 빈틈을 메우려면 방법과 실험에서 근거를 더 확인해야 한다. 연결을 고친다며 "동적 물체가 있는 sequence에서도 14% 향상이 유지된다"를 덧붙이거나 critical을 most critical로 바꾸면 없던 결과와 최상급 주장을 새로 만들게 된다.

**첫 명사구로는 바로 앞에 나온 명사나 대명사, 앞 내용을 묶어 부르는 명사구를 쓴다.** "this result", "such configurations" 같은 묶음 명사구가 앞 문장과 이어 주는 도구다. [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767)도 "this" 뒤에는 반드시 명사를 붙여 무엇을 가리키는지 분명히 하라고 했다("This is a fast reaction; This leads us to conclude" 대신 "This reaction is fast; This observation leads us to conclude").

---

## 21.3 Stress chain — 쌓여 가는 새 정보

**문장 끝자리의 새 정보는 다음 문장 첫머리로 넘어간다.** 이렇게 받아 넘기면 단락 안에 정보가 차례로 쌓인다.

> ✓ Textureless walls provide weak image gradients. Weak image gradients make photometric motion estimation less informative. This loss of photometric information motivates adding geometric constraints in a hybrid method.

둘째 문장은 첫 문장 끝의 weak image gradients를 그대로 받는다. 셋째 문장의 this loss of photometric information은 둘째 문장이 말한 정보 부족을 받아, 기하 제약을 함께 쓰려는 이유로 잇는다. 질감이 부족하면 밝기 변화에 기대는 추정이 어려워진다. 기하 제약은 질감과 상관없이 쓸 수 있지만, 장면의 형상에 따라 기하 제약도 부족할 수 있다. 그러니 이 예가 hybrid method의 성공을 보장하지는 않는다. 이 단락의 요점은 마지막 문장에 담긴 방법 선택의 이유다.

**문장 끝마다 상투어가 오면 stress chain이 빈다.** "in this paper", "of our approach" 같은 말이 문장 끝자리를 차지하면 새 정보가 어디 있는지 흐려진다. [Ch.12 §12.2](./chapter_12_reader_expectations_diagnosis.md)의 진단 1(stress position)과 같은 문제다.

---

## 21.4 흔한 결함

**Topic 끊김.** 문장 첫머리에 새 명사가 잇달아 나와 앞 문장과 이어 주는 말이 없다. 단락에서 문장마다 첫 명사구만 뽑아 한 줄로 늘어놓고, 그 줄이 이어지는지 본다.

**Stress 흩뿌리기.** 문장 끝마다 상투어가 와서 새 정보가 어디 있는지 흐릿하다. 문장마다 마지막 명사구만 뽑아 한 줄로 늘어놓고, 새 정보가 쌓이는지 본다.

**한 단락에 요점 둘.** 독자가 가져갈 요점 후보가 둘이다. [Ch.11 §11.2](./chapter_11_ccc_lens.md)의 Q2(이 단락의 content는 한 가지인가)로 잡히는 결함이다. 단락을 나눈다.

**접속사 남발.** "However", "Moreover", "Therefore"를 문장마다 첫머리에 놓는다. 앞 문장과 이어 주는 말 대신 접속사를 놓으면 topic chain이 빈다. 접속사는 정보 사이의 관계를 밝혀야 할 때만 남긴다.

---

## 21.5 두 줄 뽑기로 스스로 진단하기

자기 원고에서 단락 하나를 골라 아래 순서로 해 본다.

1. 문장마다 첫 명사구만 뽑아 한 줄로 늘어놓는다. 이 줄이 topic chain이다.
2. 문장마다 마지막 명사구만 뽑아 한 줄로 늘어놓는다. 이 줄이 stress chain이다.

두 줄을 나란히 놓고 topic chain이 이어지는지, stress chain에 새 정보가 쌓이는지 본다. 어느 한 줄이라도 끊기는 곳이 흐름에 결함이 있는 자리다.

이 방법은 [Ch.29](./chapter_29_reader_expectations.md) §29.4에서 따로 보던 문장 첫머리와 문장 끝을 나란히 놓고 본다. 같은 방법을 남의 논문 읽기에 쓴 예는 [Ch.12](./chapter_12_reader_expectations_diagnosis.md)에 있다.

---

## 21.6 CCC 점검과 함께 쓰기

Ch.19의 CCC는 단락의 각 자리에 무엇이 들어가는지 점검하고, 두 줄 뽑기는 문장 사이로 정보가 어떻게 넘어가는지 점검한다.

CCC 골격을 갖춘 단락에서도 topic chain과 stress chain은 끊길 수 있다. 첫 문장에 맥락이 잘 들어가 있어도 둘째 문장 첫머리가 첫 문장 끝을 받아야 흐름이 이어진다. CCC가 깨진 단락이라면 두 줄 뽑기에서 stress chain의 마지막 낱말이 요점에 닿지 않을 수 있다.

두 점검 가운데 CCC를 먼저 한다. 각 자리가 채워졌는지 확인한 다음 두 줄 뽑기로 흐름을 본다. 빈자리가 있는데 흐름부터 다듬으면 빈자리는 그대로 남는다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing) — topic position의 old information이 앞 문장과의 연결과 단락 전체의 전개를 독자에게 알려 준다는 설명. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 3(단락 규모의 C-C-C). [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) — "this" 뒤에 명사를 붙이라는 권고. 두 층위를 함께 보는 관점과 두 줄 뽑기는 이 장에서 정리했다.

다음: [Part 3 — 섹션별 작성법](./chapter_22_title_abstract.md)
