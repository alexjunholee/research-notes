# Ch.21 — 문단 흐름

문장 단위는 다듬었는데 한 단락을 읽으면 흐름이 끊긴다고 느끼는 학생이 있다. 같은 단락의 다섯 문장을 따로따로 보면 멀쩡하지만, 이어 붙이면 어딘가가 어긋난다. 그 어긋남은 [Ch.29](./chapter_29_reader_expectations.md)의 stress·topic 5원칙이 단락 층위에서 깨질 때 생긴다.

[Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) §III의 원칙은 old before new다. 한 문장 안에서 작동하는 이 원칙은 한 단락 안에서도 같은 형태로 작동한다. Ch.19의 CCC가 어디에 무엇이 들어가는지 보여 주는 자리표라면, 여기서는 문장이 어떻게 흐르는지 본다.

---

## 21.1 두 층위가 동시에 작동한다

한 단락을 읽는 독자의 작업 기억은 두 층위를 동시에 처리한다. 문장 층위에서는 topic position(첫 자리)이 backward link를 걸고 stress position(끝 자리)이 새 정보를 받는다. 단락 층위에서는 첫 문장이 진입점이 되고 마지막 문장이 takeaway를 받는다.

두 층위가 같은 패턴(old → new)을 공유한다. 흐름이 자연스러운 문단은 두 층위에서 같은 방식의 인지 부담만 요구한다. 한 층위가 깨지면 독자는 매 문장에서 왜 이 정보가 지금 들어오는지를 다시 추측해야 한다. 그 추측이 쌓이면 문단 끝에서 takeaway가 무엇인지 흐려진다.

학생들이 가장 자주 어기는 곳이 단락 층위다. 문장 단위는 [Ch.29](./chapter_29_reader_expectations.md)의 5원칙으로 어느 정도 다듬어지지만, 문장 사이를 어떻게 묶는가는 별도의 작업으로 인식되지 않은 채 남는 경우가 많다.

---

## 21.2 Topic chain — 문장 간 backward link

**각 문장의 첫 명사구가 앞 문장의 어딘가와 연결되어야 한다.** 직전 문장의 stress position에 등장한 명사구가 다음 문장의 topic position을 받는 패턴이 가장 자연스럽다.

> 원문: The proposed method achieves 14% improvement on KITTI. Many KITTI sequences are challenging due to dynamic objects. Loop closure is critical.
>
> 연결을 일부 고친 문장: The proposed method achieves 14% improvement on KITTI. This benchmark contains many sequences that are challenging due to dynamic objects. Loop closure is critical.

예문의 14% 향상 수치는 문장 연결을 설명하기 위해 설정한 예시값이다. 두 문안은 같은 정보를 담고 있다. 수정문에서는 둘째 문장의 this benchmark가 앞 문장의 KITTI를 받아, 어느 자료의 sequence인지 바로 알 수 있다.

셋째 문장은 여전히 연결이 부족하다. Loop closure가 왜 중요한지, 앞의 성능이나 동적 물체와 어떤 관계인지는 주어진 문장만으로 알 수 없다. 이 빈틈을 메우려면 방법과 실험의 근거를 더 확인해야 한다. 동적 물체가 있는 sequence에서도 14% 향상이 유지된다고 덧붙이거나 critical을 most critical로 바꾸면, 연결을 고치는 동안 새 결과와 최상급 주장을 만든 셈이 된다.

**첫 명사구는 직전에 등장한 명사·대명사·요약 명사구를 받는다.** "this", "the result", "such configurations" 같은 요약 명사구가 backward link를 만드는 도구다.

---

## 21.3 Stress chain — 새 정보의 누적

**문장 끝(stress position)의 새 정보가 다음 문장 첫 자리(topic position)로 흘러간다.** 이 받기는 단락 안에서 정보를 누적하는 한 방법이다.

> ✓ Textureless walls provide weak image gradients. Weak image gradients make photometric motion estimation less informative. This loss of photometric information motivates adding geometric constraints in a hybrid method.

첫 문장의 weak image gradients를 둘째 문장이 그대로 받는다. 셋째 문장의 this loss of photometric information은 둘째 문장이 설명한 정보 부족을 받아, 기하 제약을 함께 쓰려는 이유로 연결한다. 질감 부족은 영상 밝기 변화에 기대는 추정을 어렵게 할 수 있지만, 그 자체로 geometric ICP의 실패 원인이 되지는 않는다. 기하 제약도 장면의 형상에 따라 부족할 수 있으므로, 이 예는 hybrid method의 성공을 보장하는 설명이 아니다. 마지막 문장이 담은 방법 선택의 이유가 이 문단의 takeaway에 해당한다.

**매 문장 끝에 보일러플레이트가 들어서면 stress chain이 비어 있다.** "in this paper", "of our approach" 같은 표현이 매 문장의 stress를 차지하면 어느 자리에 새 정보가 들어갔는지가 흐려진다. [Ch.29](./chapter_29_reader_expectations.md)의 stress position 진단과 같은 축에 있다.

---

## 21.4 흔한 결함 4종

**Topic 끊김.** 문장 첫 자리에 새 명사가 연속으로 등장. backward link 0. 진단법 — 한 단락의 첫 명사구만 추출해 한 줄로 나열, 그 줄이 흐르는지 본다.

**Stress 흩뿌리기.** 보일러플레이트가 매 문장 끝을 점유. 새 정보가 어디에 있는지 흐릿. 진단법 — 한 단락의 마지막 명사구만 추출해 한 줄로, 새 정보가 누적되는지 본다.

**메시지 둘.** 한 단락에 takeaway 후보가 둘. [Ch.11 §11.2의 두 번째 진단](./chapter_11_ccc_lens.md)과 같은 결함. 쪼갠다.

**접속사 남발.** "However", "Moreover", "Therefore"를 매 문장 첫 자리에 박는 패턴. backward link를 접속사가 대체하면 topic chain이 빈다. 정보의 관계를 표시할 때만 접속사를 남긴다.

---

## 21.5 자기 진단 — 두 줄 추출법

자기 단락 한 토막을 가지고 다음 두 작업을 돌려 본다.

1. 각 문장의 첫 명사구만 추출해 한 줄로 나열. 이 줄이 topic chain.
2. 각 문장의 마지막 명사구만 추출해 한 줄. 이 줄이 stress chain.

두 줄을 나란히 놓는다. topic chain이 끊기지 않고 흐르는가. stress chain이 새 정보를 누적하는가. 둘 중 하나라도 끊기면 그곳이 흐름 결함이 있는 자리다.

[Ch.29](./chapter_29_reader_expectations.md)의 reverse-read 진단을 단락 층위로 넓힌 도구다. 같은 도구를 읽기에 적용한 사례가 [Ch.12 reader expectations 진단](./chapter_12_reader_expectations_diagnosis.md)에 있다. 쓰기와 읽기 양쪽에서 같은 두 줄 추출이 작동한다.

---

## 21.6 CCC와의 관계

Ch.19의 CCC가 자리표라면 이 장의 두 줄 추출법은 흐름표다. 두 관점은 서로 보완한다.

CCC 골격이 잡힌 단락도 topic chain·stress chain이 무너질 수 있다. 첫 문장에 context가 잘 박혀 있어도, 그다음 문장의 topic이 첫 문장 stress를 받지 않으면 흐름이 깨진다. CCC가 깨진 단락은 두 줄 추출에서 stress chain의 마지막이 takeaway가 아닌 단어에 도달한다.

두 진단은 순서로 적용한다. CCC 자리표를 먼저 확인하고, 칸이 채워졌으면 두 줄 추출로 흐름을 검증한다. 칸이 비어 있는데 흐름부터 다듬으면 빈 칸이 그대로 남는다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) §III — old before new가 paragraph 층위에도 작동. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 3 연결. 두 층위의 통합적 관점과 두 줄 추출 진단법은 단락 퇴고를 실질적으로 돕기 위해 본문에서 새롭게 체계화했다.

다음: [Part 3 — 섹션별 작성법](./chapter_22_title_abstract.md)
