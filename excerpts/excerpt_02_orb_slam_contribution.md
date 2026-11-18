# 기여 문장은 무엇을 만들었는지부터 말한다

**출처**: Mur-Artal, Montiel, Tardós, 2015 — ORB-SLAM: A Versatile and Accurate Monocular SLAM System, IEEE Transactions on Robotics 31(5): 1147-1163

---

시스템 논문에서 가장 흔한 실수는 자신이 만든 구성 요소를 끝없이 나열하다가 정작 무엇이 좋아졌는지를 흐리는 것이다. ORB-SLAM은 초록 첫 문장에서 시스템의 정체와 성능을 먼저 못 박고, 서론 끝에서는 모든 기여를 동일한 세 박자 구조로 정렬해 이 함정을 피한다.

## 발췌

초록 도입부는 시스템의 이름과 성격, 동작 범위를 지체 없이 선언한다.

> This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments. The system is robust to severe motion clutter, allows wide baseline loop closing and relocalization, and includes full automatic initialization. Building on excellent algorithms of recent years, we designed from scratch a novel system that uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing.

서론의 마지막에서는 주요 기여 여섯 가지를 글머리표로 정리해 독자 앞에 펼쳐 놓는다(압축 인용).

> … to design from scratch ORB-SLAM, a novel monocular SLAM system whose main contributions are:
> - Use of the same features for all tasks: tracking, mapping, relocalization and loop closing. …
> - Real time operation in large environments. Thanks to the use of a covisibility graph, tracking and mapping is focused in a local covisible area, independent of global map size.
> - Real time loop closing based on the optimization of a pose graph that we call the Essential Graph. …
> - Real time camera relocalization with significant invariance to viewpoint and illumination. …
> - A new automatic and robust initialization procedure based on model selection …
> - A survival of the fittest approach to map point and keyframe selection that is generous in the spawning but very restrictive in the culling. …

---

## 한국어 의역

이 논문은 feature 기반 단안(monocular) SLAM 시스템인 ORB-SLAM을 제안한다. ORB-SLAM은 크고 작은 실내·실외 환경 모두에서 실시간으로 작동한다. 격렬한 움직임으로 영상이 크게 어지러워도(severe motion clutter) 안정적으로 버티며, 시점 차이가 큰 상황에서도 루프 폐합(loop closing)과 재위치 추정(relocalization)을 해내고, 초기화 역시 전 과정을 자동으로 처리한다. 저자들은 최근 몇 년간 나온 뛰어난 알고리즘들을 토대로 삼아, 트래킹·매핑·재위치 추정·루프 폐합이라는 SLAM의 모든 과업에 동일한 feature를 공유하는 새 시스템을 백지에서부터 설계했다.

서론 말미에서 저자들이 꼽은 여섯 가지 주요 기여는 다음과 같다.

- 모든 과업에 동일한 feature를 사용해 시스템을 더 효율적이고 간결하며 신뢰할 수 있게 만들었다. 채택한 ORB feature는 GPU 없이도 실시간으로 계산되며 시점과 조명 변화에 강하다.
- 대규모 환경에서도 실시간으로 동작한다. 같은 지도 점을 함께 관측하는 키프레임들을 잇는 covisibility graph 덕분에, 전체 지도 규모와 무관하게 국소 영역에 집중해 트래킹과 매핑을 수행할 수 있다.
- 저자들이 Essential Graph라 이름 붙인 pose graph를 최적화해 실시간으로 루프를 닫는다.
- 시점과 조명이 크게 달라져도 카메라 위치를 실시간으로 다시 찾아낸다.
- 모델 선택(model selection)에 기반한 새로운 자동 초기화 절차로 견고하게 초기 지도를 구축한다.
- 지도 점과 키프레임 관리에 적자생존(survival of the fittest) 전략을 도입해, 생성은 너그럽게 하되 솎아 내기(culling)는 엄격하게 적용한다. 그 결과 트래킹은 더 강건해지고 중복 키프레임이 제거되어 장기 운용이 가능해진다.

---

## 분석 — 왜 이 표현이 좋은가

ORB-SLAM의 도입부는 시스템 논문이 자기 기여를 어떻게 구조화해 보여 주어야 하는지 모범을 보여 준다. 초록 첫 문장("This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments")은 시스템의 이름과 분류, 핵심 역량을 단 한 문장에 압축한다. 뒤이어 나오는 "we designed from scratch a novel system"의 `we`는 독자와 저자가 함께 추론을 따라가는 자리에 `we`("you and me together")를 쓰라고 권했던 Knuth의 §1 point 6과 달리, 연구를 수행한 저자 집단을 당당히 가리키는 주어로 기능한다.

여기서 첫 문장에 얹힌 `feature-based`, `real time`, `small and large`, `indoor and outdoor` 같은 수식어는 단순한 미사여구가 아니라 본문 실험이 반드시 입증해야 할 평가 기준이기도 하다. 실제로 논문은 ORB feature를 채택해 CPU만으로 실시간 동작을 달성하고 실내외 27개 sequence에서 이를 검증함으로써 초록의 약속을 하나도 빠짐없이 회수한다. Whitesides처럼 outline을 먼저 세워 글을 쓰는 방식을 취하면, 초록에 내건 약속들이 본문의 그림, 표, 기여 목록에 빈틈없이 반영되었는지 집필 도중에 점검하기가 한결 수월하다.

서론 끝의 기여 목록이 특히 돋보이는 이유는 여섯 항목이 모두 똑같은 세 박자 짜임—**어떤 모듈인가 → 무엇이 새로운가 → 그래서 무엇이 좋아지는가**—을 따르기 때문이다. 첫 번째 항목을 예로 들면, 트래킹·매핑·재위치 추정·루프 폐합에 같은 feature를 쓴다는 점이 모듈이고, ORB feature가 GPU 없이 실시간으로 돌며 시점·조명 변화에 강하다는 점이 새로움이며, 그 덕분에 시스템이 "more efficient, simple and reliable"해진다는 점이 결과다. 모든 항목이 이 뼈대를 공유하니 독자는 각 기여의 무게를 나란히 비교할 수 있고, 저자 스스로도 어느 항목에 '결과'가 빠졌는지 표로 그려 보듯 금방 가려낼 수 있다.

또한 초록과 기여 목록은 서로 느슨하게 흩어지지 않고 톱니바퀴처럼 맞물린다. 초록에서 예고한 "uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing"은 기여 목록 첫머리에서 곧바로 상세히 풀리고, 이 발췌에서는 생략된 초록 후속 문장의 "survival of the fittest" 역시 마지막 기여 항목과 정확히 짝을 이룬다. 내 원고에서도 초록과 서론 마지막 단락을 나란히 펼쳐 두고, 같은 핵심어와 근거가 양쪽을 관통하고 있는지 확인해 볼 필요가 있다.

기여를 줄글 대신 글머리표로 분리한 선택도 영리하다. 만약 이 내용을 "We present a system that uses common ORB features for …, while introducing a novel covisibility graph …, and an Essential Graph …, and …"처럼 한 문장에 몰아넣었다면, 접속사로 길게 엮인 절들 사이에서 각 기여의 경계가 흐려졌을 것이다. 대개 기여 항목이 3~6개 정도이고 각 항목을 두세 줄로 압축할 수 있으며 구조가 평행을 이룰 때는 글머리표가 줄글보다 훨씬 명쾌하다.

어조의 균형 감각도 배울 만하다. "Building on excellent algorithms of recent years"라는 구절로 선행 연구의 성취를 정중히 인정한 직후, "we designed from scratch"로 자신들의 독자적 설계를 또렷이 밝힌다. 기여 목록 안팎에서는 `use`, `present`, `make public` 같은 능동 동사를 써서 망설임 없이 서술한다. "We propose a revolutionary …"처럼 과장하면 심사위원의 반감을 사기 쉽고, "We try to …"처럼 주저하면 기여가 흐려진다는 점에서, 선행 연구에는 예의를 갖추고 자기 기여는 담백하게 단정하는 이 어조가 시스템 논문에 가장 잘 어울린다.

---

## 따라 쓰기 — 자기 분야에 적용

시스템 논문의 기여를 정리할 때는 다음과 같은 틀을 세워 점검해 보자.

> "This paper presents [system name], a [형용사 2~3개] [task] system that [핵심 능력]. … The main contributions of this work are: 1) [모듈 + 새로운 점 + 결과], 2) …, 3) …"

각 항목에서 모듈·새로움·결과라는 세 칸이 모두 채워졌는지 살피면 약한 기여를 초기에 걸러 낼 수 있다. 특히 첫 문장에 넣은 형용사는 그대로 실험의 평가 지표가 되므로, 탈고 단계에서 Results 절이 그 기준을 빠짐없이 수치로 보고했는지 대조해야 한다. ORB-SLAM에서도 제목에 내세운 `versatile`과 `accurate`가 초록과 실험 전반을 관통한다.

작업을 마무리할 때는 초록의 문장과 서론의 기여 항목을 표로 짝지어 보는 습관이 유용하다. 초록의 형용사나 명사구가 어느 기여 항목에서도 풀리지 않는다면, 공수표만 날린 셈이니 초록에서 덜어 내거나 기여 항목을 보강해야 한다. 반대로 ORB-SLAM의 "Essential Graph"나 "survival of the fittest"처럼 저자가 새로 명명한 개념이 있다면, 초록과 기여 목록에 동일한 이름을 일관되게 써야 독자와 심사위원이 핵심을 한눈에 짚고 인용할 수 있다. 결국 좋은 기여 문장은 겸손한 인정 위에 세운 명료한 약속이며, 본문 전체를 묶는 설계도다.

---

## 출처
- `murartal-2015-orbslam` — Mur-Artal, R., Montiel, J. M. M., Tardós, J. D., 2015. ORB-SLAM: A Versatile and Accurate Monocular SLAM System. IEEE Transactions on Robotics 31(5): 1147-1163. DOI: 10.1109/TRO.2015.2463671. arXiv:1502.00956.

---
