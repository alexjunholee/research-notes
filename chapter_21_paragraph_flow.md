# Ch.21 — 문단 흐름

문장 단위는 다듬었는데 한 문단을 읽으면 흐름이 끊긴다고 느끼는 학생이 있다. 같은 단락의 문장 다섯을 따로따로 보면 다 멀쩡한데, 이어 붙이면 어딘가가 어긋난다. 그 어긋남의 정체가 ch14가 다룬 stress·topic 5원칙의 *paragraph layer*다.

[Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) §III가 한 줄로 박아 둔다. *old before new*. 한 문장 안에서 작동하는 이 원칙이 한 문단 안에서도 같은 형태로 작동한다는 진단이다. ch04의 CCC가 *어디에* 무엇이 들어가는가의 자리표라면, 이 챕터는 *어떻게 흐르는가*의 흐름표다.

---

## 21.1 두 layer가 동시에 작동한다

한 문단을 읽는 독자의 working memory는 두 layer를 동시에 받는다. 문장 layer에서는 topic position(첫 자리)이 backward link를 걸고 stress position(끝 자리)이 새 정보를 받는다. 문단 layer에서는 첫 문장이 단락의 진입점이 되고 마지막 문장이 takeaway를 받는다.

두 layer가 같은 패턴(old → new)을 공유한다. 잘 굴러가는 문단은 두 곳에서 *같은* 인지 부담만을 요구한다. 한 layer가 깨지면 독자는 매 문장에서 *왜 이 정보가 지금 들어오는지*를 다시 추측해야 한다. 그 추측이 누적되면 문단 끝에 도달했을 때 *takeaway가 무엇이었는지*가 흐려진다.

학생들이 가장 자주 어기는 곳이 paragraph layer다. 문장 단위는 ch14의 5원칙으로 어느 정도 다듬어지지만, 문장 사이를 *어떻게 묶는가*는 별도의 작업으로 인식되지 않은 채 남는 경우가 많다.

---

## 21.2 Topic chain — 문장 간 backward link

🔴 **각 문장의 *첫 명사구*가 앞 문장의 어딘가와 연결되어야 한다.** 직전 문장의 stress position에 등장한 명사구가 다음 문장의 topic position을 받는 패턴이 가장 자연스럽다.

> ❌ The proposed method achieves 14% improvement on KITTI. Many sequences are challenging due to dynamic objects. Loop closure is critical.
>
> ✓ The proposed method achieves 14% improvement on KITTI. The improvement holds across sequences with dynamic objects, where loop closure is most critical.

❌ 쪽은 세 문장의 첫 명사구가 *the proposed method · many sequences · loop closure*로 끊긴다. 연결이 0이다. ✓ 쪽은 *the proposed method → the improvement → where loop closure*로 backward link가 한 줄로 이어진다.

🟡 **첫 명사구는 새 명사가 아니라 직전에 등장한 명사·대명사·요약 명사구로.** "this", "the result", "such configurations" 같은 요약 명사구가 backward link를 만드는 도구다.

---

## 21.3 Stress chain — 새 정보의 누적

🔴 **문장 끝(stress position)의 새 정보가 다음 문장 첫 자리(topic position)로 흘러간다.** 이 *받기*가 깨지면 단락 안에서 정보가 누적되지 않는다.

> ✓ Geometric ICP failed on textureless walls. These walls dominate indoor scans, where photometric gradients are weak. Weak gradients motivate hybrid methods.

세 문장의 stress가 각각 *textureless walls · weak gradients · hybrid methods*. 다음 문장의 topic이 직전 stress를 받아 단락이 한 방향으로 흐른다. 단락의 마지막 stress에 *hybrid methods*가 도달했을 때, 그 끝점이 단락 전체의 takeaway 후보로 잡힌다 — ch04 §1의 conclusion 위치와 정확히 일치한다.

🟡 **매 문장 끝에 보일러플레이트가 들어서면 stress chain이 비어 있다.** "in this paper", "of our approach" 같은 표현이 매 문장 stress를 차지하면 *어느 자리에 새 정보가 박혔는지*가 흐려진다. ch14의 stress position 진단과 같은 축.

---

## 21.4 흔한 결함 4종

🔴 **Topic 끊김.** 문장 첫 자리에 새 명사가 연속으로 등장. backward link 0. 진단법 — 한 단락의 첫 명사구만 추출해 한 줄로 나열, 그 줄이 흐르는지 본다.

🔴 **Stress 흩뿌리기.** 매 문장 끝에 보일러플레이트가 점유. 새 정보가 어디에 있는지 흐릿. 진단법 — 한 단락의 마지막 명사구만 추출해 한 줄로, 새 정보가 누적되는지 본다.

🔴 **메시지 둘.** 한 단락에 takeaway 후보가 둘. ch04 §5의 흔한 실수 첫 항과 같은 결함. 쪼갠다.

🟡 **접속사 남발.** "However", "Moreover", "Therefore"를 매 문장 첫 자리에 박는 패턴. backward link를 *접속사*가 대체하면 topic chain이 비어 있다는 증거. 접속사는 한 단락에 한두 번이 상한.

---

## 21.5 자기 진단 — 두 줄 추출법

자기 단락 한 토막을 가지고 다음 두 작업을 돌려 본다.

1. 각 문장의 *첫 명사구*만 추출해 한 줄로 나열. 이 줄이 topic chain.
2. 각 문장의 *마지막 명사구*만 추출해 한 줄. 이 줄이 stress chain.

두 줄을 나란히 놓는다. topic chain이 끊기지 않고 흐르는가. stress chain이 새 정보를 누적하는가. 둘 중 하나라도 깨지면 그곳이 흐름 결함이 박힌 곳이다.

ch14의 reverse-read 진단(자기 문장 단위)이 paragraph layer로 격상된 도구. 같은 도구를 *읽기* 측면에서 적용한 글이 [Part 1 ch07 reader expectations 진단](./chapter_12_reader_expectations_diagnosis.md)이다. 쓰기와 읽기 양쪽에서 같은 두 줄 추출이 작동한다.

---

## 21.6 CCC와의 관계

ch04의 CCC가 *자리표*라면 ch06은 *흐름표*다. 두 frame이 충돌하지 않고 보완한다.

CCC 골격이 잡힌 단락도 topic chain·stress chain이 무너질 수 있다. 첫 문장에 context가 잘 박혀 있어도, 그다음 문장의 topic이 첫 문장 stress를 *받지 않으면* 흐름이 깨진다. CCC가 깨진 단락은 두 줄 추출에서 stress chain의 마지막이 *takeaway가 아닌 단어*에 도달한다.

두 진단은 순서로 적용한다. CCC 자리표를 먼저 확인하고, 칸이 채워졌으면 두 줄 추출로 흐름을 검증한다. 칸이 비어 있는데 흐름부터 다듬으면 빈 칸이 그대로 남는다.

---

**출처.** [Gopen & Swan 1990](https://www.americanscientist.org/article/the-science-of-scientific-writing) §III — *old before new*가 paragraph layer에도 작동. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 3 cross-link. 두 layer 통합 frame과 두 줄 추출 진단법은 자체.

다음: [Part 2 그룹 C — 섹션별 작성법](./chapter_22_title_abstract.md)
