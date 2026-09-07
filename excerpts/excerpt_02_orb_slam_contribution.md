# 기여 문장은 무엇을 만들었는지부터 말한다

**출처**: Mur-Artal, Montiel, Tardós, 2015 — ORB-SLAM: A Versatile and Accurate Monocular SLAM System, IEEE Transactions on Robotics 31(5): 1147-1163

---

## 발췌

초록 도입부:

> This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments. The system is robust to severe motion clutter, allows wide baseline loop closing and relocalization, and includes full automatic initialization. Building on excellent algorithms of recent years, we designed from scratch a novel system that uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing.

서론 끝의 기여 항목(압축 인용):

> … to design from scratch ORB-SLAM, a novel monocular SLAM system whose main contributions are:
> - Use of the same features for all tasks: tracking, mapping, relocalization and loop closing. …
> - Real time operation in large environments. Thanks to the use of a covisibility graph, tracking and mapping is focused in a local covisible area, independent of global map size.
> - Real time loop closing based on the optimization of a pose graph that we call the Essential Graph. …
> - Real time camera relocalization with significant invariance to viewpoint and illumination. …
> - A new automatic and robust initialization procedure based on model selection …
> - A survival of the fittest approach to map point and keyframe selection that is generous in the spawning but very restrictive in the culling. …


---

## 한국어 의역

이 논문은 feature 기반 단안 SLAM 시스템인 ORB-SLAM을 제안한다. 실내외와 크고 작은 다양한 환경에서 실시간으로 구동되며, 급격한 움직임에도 흔들리지 않는 강건성을 자랑한다. 또한 넓은 기준선의 루프 폐합(loop closing)과 재위치 추정(relocalization), 완전 자동 초기화 기능을 종합적으로 갖추었다. 최근 축적된 우수 알고리즘들의 성과를 계승하여, 트래킹·매핑·재위치 추정·루프 폐합이라는 네 가지 핵심 과제 전반에 같은 ORB 특징을 사용하는 구조를 백지 상태에서 설계했다. 서론 끝머리에서는 시스템의 학술적 기여를 다음과 같이 여섯 갈래로 요약한다. ① 모든 작업에 동일한 ORB 특징점을 적용하여 연산 단순성과 실시간 성능을 동시에 달성함. ② 가시성 그래프(covisibility graph)를 활용해 광범위한 환경에서도 국소 영역 중심의 효율적 매핑 수행. ③ Essential Graph 기반 포즈 그래프 최적화를 통한 실시간 루프 폐합. ④ 시점 및 조명 변화에 높은 불변성을 유지하는 카메라 재위치 추정. ⑤ 모델 선택 기반의 견고한 자동 초기화 절차 확립. ⑥ 키프레임과 지도 점에 적자생존 원칙을 도입하여 장기적 시스템 운영 안정성 확보.

---

## 분석 — 왜 이 표현이 좋은가

ORB-SLAM의 기여 진술은 시스템 논문이 자기 기여를 묶어 보여 주는 유용한 사례다. 초록은 "This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments"라는 한 문장으로 시스템을 선언한다. 능동형 동사 + 시스템 명사 + 핵심 능력이라는 슬롯이 채워져 있다. "We"라는 1인칭은 초록 후반의 "we designed from scratch a novel system"에서 등장하며, Knuth §1 point 6의 `we`와 `I`에 대한 권고와 맞닿는다. 이어지는 feature-based, real time, small and large, indoor and outdoor는 단순한 수식어를 넘어 향후 실험 섹션에서 증명해야 할 구체적 평가 축의 선언이다. 결과 섹션이 feature-based(ORB feature 사용), real-time(CPU에서 실시간 동작), versatility(27 sequences across indoor/outdoor)라는 축을 실제로 보고하는지가 약속과 이행의 일치를 가른다. Whitesides §III의 outline-first 구조와 함께 읽으면, 초록의 약속이 본문의 그림·표·기여 목록에서 실현되는지 점검할 수 있다.

Introduction 끝의 contribution 나열은 각 항목이 동일한 슬롯 구조를 따른다. 어떤 모듈 + 어떤 새로움 + 어떤 결과. 가령 첫 항목은 "tracking, mapping, relocalization and loop closing 모두에 같은 ORB feature를 사용해(모듈)" 시스템을 통일하고, "ORB feature는 GPU 없이 실시간 동작이 가능하며 viewpoint·조명에 강건한(새로움)" 특성을 가지므로, "more efficient, simple and reliable(결과)"한 시스템이 된다. 같은 문법이 여섯 번 반복되어 독자가 항목 사이를 비교하기 쉽다. 한 항목이라도 슬롯이 비어 있다면 — 가령 "어떤 결과"가 누락되면 — 그 contribution은 약하다는 신호다. 자기 논문 contribution을 점검하는 가장 빠른 방법은 항목들을 표로 옮겨 슬롯이 모두 채워졌는지 보는 것이다.

Abstract 한 문장과 Introduction bullet의 대응도 이 발췌가 모범인 이유 중 하나다. abstract의 압축된 한 줄("uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing")이 introduction의 첫 bullet으로 그대로 풀려 나온다. 다만 survival of the fittest는 마지막 bullet에만 등장하므로 abstract와 bullet의 일대일 대응 사례로 보기는 어렵다. ORB-SLAM에서 두 진술이 단단하게 맞물리는 대목은 모든 기여가 아니라, 네 task에 같은 feature를 쓴다는 핵심 주장이다. 자기 원고도 abstract와 Introduction 마지막 단락을 나란히 펼쳐, contribution이 같은 핵심 단어와 근거로 묶이는지 확인한다. 이 비교는 글쓴이의 '자기 인식 수준'을 판정하는 5분 검사가 아니라, 약속과 근거의 누락을 찾는 편집 도구다.

번호를 매긴 까닭도 분명하다. 같은 내용을 "We present a system that uses common ORB features for tracking, mapping, relocalization, and loop closing, while introducing a novel covisibility graph for real-time local mapping, and an Essential Graph for efficient large-scale optimization, and …"처럼 산문으로 풀면 절들이 등위접속사로 길게 이어져 기여의 경계가 흐려진다. 글머리표 목록은 정보를 구획화하는 도구다. 항목이 셋에서 여섯 사이이고, 각 항목을 두세 줄로 압축할 수 있으며, 항목들이 비교 가능한 같은 슬롯 구조를 가질 때 글머리표 목록으로 구조화하는 편이 훨씬 명확하다. ORB-SLAM은 세 조건을 모두 만족한다.

마지막은 어조다. "This paper presents"는 시스템을 제시한다는 말이고, "we designed from scratch"는 새 시스템을 처음부터 설계했다는 기여를 명시한다. 앞선 "Building on excellent algorithms"와 함께 읽으면 선행 알고리즘의 공로를 인정하면서 시스템 설계의 새로움을 주장하는 문장이다. Building on excellent algorithms of recent years는 선행 연구를 훌륭하다고 부르며 그 위에서 작업했음을 인정한다. 세부 기여 항목에서는 "introduce", "use", "present", "make public"처럼 능동적이고 단정적인 동사들을 채택한다. 바깥의 어조는 점잖게 두되 안쪽의 진술은 단정하는 비대칭이 시스템 논문의 기여 단락에 알맞다. 바깥의 어조를 지나치게 단정하면("We propose a revolutionary …") 심사위원의 거부 반응을 부르고, 안쪽 진술을 약하게 쓰면("We try to …") 기여가 무너진다. ORB-SLAM의 비대칭이 안전한 기본값이다.

---

## 따라 쓰기 — 자기 분야에 적용

이 패턴은 시스템 논문 contribution 단락의 3-슬롯 골격이다. "This paper presents [system name], a [형용사2-3] [task] system that [핵심 능력]. … The main contributions of this work are: 1) [모듈+새로움+결과], 2) …, 3) …" — 각 항목이 동일한 세 슬롯을 채우는지가 contribution이 단단한지의 척도다. 형용사를 먼저 정하고, 그것이 곧 평가 축이 된다는 약속을 Results 섹션이 지키는지 사후 점검한다. ORB-SLAM의 versatile and accurate는 제목·abstract·평가 모두에 일관되게 박혀 있다.

Abstract 한 줄과 Introduction bullet의 대응을 직접 표로 그려 보는 것이 자기 점검 도구다. abstract의 형용사·명사구 하나하나가 어느 bullet에 풀려 나오는지 짚는다. 어디에서도 풀리지 않는 형용사가 있다면 그 형용사는 약속만 있고 이행이 없는 상태다. 그 형용사를 abstract에서 빼거나, contribution 한 항목을 추가하거나, 둘 중 하나를 한다. ORB-SLAM의 "Essential Graph"와 "survival of the fittest"는 Introduction bullet에서 정의된 coined term이다. coined term을 abstract에도 쓴다면 연결된 bullet에서 같은 표현을 유지해야 독자의 검색·인용 동선이 매끈해진다.

---

## 출처
- `murartal-2015-orbslam` — Mur-Artal, R., Montiel, J. M. M., Tardós, J. D., 2015. ORB-SLAM: A Versatile and Accurate Monocular SLAM System. IEEE Transactions on Robotics 31(5): 1147-1163. DOI: 10.1109/TRO.2015.2463671. arXiv:1502.00956.

---
