# 기여 문장은 무엇을 만들었는지부터 말한다

**출처**: Mur-Artal, Montiel, Tardós, 2015 — *ORB-SLAM: A Versatile and Accurate Monocular SLAM System*, IEEE Transactions on Robotics 31(5): 1147-1163

---

## 발췌

Abstract 도입부:

> This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments. The system is robust to severe motion clutter, allows wide baseline loop closing and relocalization, and includes full automatic initialization. Building on excellent algorithms of recent years, we designed from scratch a novel system that uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing.

Introduction 끝의 contribution bullets (압축 인용):

> … to design from scratch ORB-SLAM, a novel monocular SLAM system whose main contributions are:
> - Use of the same features for all tasks: tracking, mapping, relocalization and loop closing. …
> - Real time operation in large environments. Thanks to the use of a covisibility graph, tracking and mapping is focused in a local covisible area, independent of global map size.
> - Real time loop closing based on the optimization of a pose graph that we call the Essential Graph. …
> - Real time camera relocalization with significant invariance to viewpoint and illumination. …
> - A new automatic and robust initialization procedure based on model selection …
> - A survival of the fittest approach to map point and keyframe selection that is generous in the spawning but very restrictive in the culling. …


---

## 한국어 의역

이 논문은 *ORB-SLAM*을 소개한다. feature 기반의 monocular SLAM 시스템으로, 실내·실외, 작은 공간·큰 공간 모두에서 실시간으로 동작한다. 격렬한 움직임에 강건하며, 넓은 기준선의 loop closing과 relocalization, 완전 자동 초기화를 포함한다. 최근의 우수한 알고리즘들 위에서, tracking·mapping·relocalization·loop closing 네 task 모두에 *동일한 feature*를 쓰는 시스템을 처음부터 설계했다. introduction은 이 시스템의 주요 기여를 여섯 항목으로 나열한다 — ① 모든 task에 같은 ORB feature를 사용해 단순성과 실시간성을 동시에 확보, ② covisibility graph로 큰 환경에서도 지역 영역에 집중하는 mapping, ③ Essential Graph 위의 pose graph 최적화로 실시간 loop closing, ④ viewpoint·조명 변화에 강건한 relocalization, ⑤ model selection 기반의 자동 초기화, ⑥ keyframe·map point의 *survival of the fittest* 정책으로 lifelong 운영.

---

## 분석 — 왜 이 표현이 좋은가

ORB-SLAM의 contribution 진술은 시스템 논문이 자기 기여를 어떻게 묶어 보여 주는가의 표준 형식이다. abstract는 한 문장으로 시스템을 선언한다 — "This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments." 능동·1인칭 + 시스템 명사 + 형용사 셋이라는 슬롯이 모두 채워져 있다. "We" 1인칭은 abstract 후반 "we designed from scratch a novel system"에서 등장하는데, Knuth rule 7의 권고("I" 대신 "we"를 써서 독자를 대화에 초대하라)를 그대로 구현한다. 이어지는 형용사 *feature-based*, *real time*, *small and large, indoor and outdoor*는 단순한 수식어가 아니라 *평가 축의 선언*이다. Results 섹션이 이 축들로 보고되는지 — feature-based(ORB feature 사용), real-time(GPU 없이 관점-rate), versatility(27 sequences across indoor/outdoor) — 가 약속과 이행의 일치를 가르는 기준이 된다. Whitesides가 §III에서 강조한 "promise-deliver alignment"의 한 페이지 시연이다.

Introduction 끝의 contribution 나열은 각 항목이 동일한 슬롯 구조를 따른다. *어떤 모듈* + *어떤 새로움* + *어떤 결과*. 가령 첫 항목은 "tracking, mapping, relocalization and loop closing 모두에 같은 ORB feature를 사용해(*모듈*)" 시스템을 통일하고, "ORB feature는 GPU 없이 실시간 동작이 가능하며 viewpoint·조명에 강건한(*새로움*)" 특성을 가지므로, "more efficient, simple and reliable(*결과*)"한 시스템이 된다. 같은 문법이 여섯 번 반복되어 독자가 항목 사이를 비교하기 쉽다. 한 항목이라도 슬롯이 비어 있다면 — 가령 "어떤 결과"가 누락되면 — 그 contribution은 약하다는 신호다. 자기 논문 contribution을 점검하는 가장 빠른 방법은 항목들을 표로 옮겨 슬롯이 모두 채워졌는지 보는 것이다.

Abstract 한 문장과 Introduction bullet의 1:1 대응도 이 발췌가 모범인 이유 중 하나다. abstract의 압축된 한 줄("uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing")이 introduction의 첫 bullet으로 그대로 풀려 나온다. *survival of the fittest* 같은 *coined term*도 abstract와 마지막 bullet 양쪽에 걸려 있어, 독자가 abstract만 읽고도 introduction의 어느 bullet과 대응하는지 즉시 짚을 수 있다. 두 진술이 어긋나면 글쓴이가 자기 기여를 못 잡았다는 신호인데, ORB-SLAM은 이 일치가 단단하다. 이 일치 검사는 reviewer가 가장 먼저 하는 작업이기도 하다. abstract와 §I 마지막 단락만 펼쳐 contribution이 같은 단어로 묶이는지 확인하면 5분 안에 글쓴이의 자기 인식 수준을 가늠할 수 있다.

번호·bullet 매김의 정당성도 짚어 둘 만하다. 같은 내용을 산문으로 풀면 — "We present a system that uses common ORB features for tracking, mapping, relocalization, and loop closing, while introducing a novel covisibility graph for real-time local mapping, and an Essential Graph for efficient large-scale optimization, and …" — 절들이 등위접속사로 길게 이어져 *어디까지가 한 contribution인지* 경계가 흐려진다. Bulleted 목록은 정보를 *구획화* 하는 도구다. 항목 수가 셋에서 여섯 사이이고, 각 항목이 두세 줄로 압축 가능하며, 항목들이 비교 가능한 동일 슬롯 구조를 가질 때 목록이 정당하다. ORB-SLAM은 세 조건을 모두 만족한다.

마지막으로 톤. "This paper presents"와 "we designed from scratch"는 *우리가 발명했다*가 아니라 *우리가 정리해 내놓았다*는 단정성을 가진다. *Building on excellent algorithms of recent years*가 그 자세를 명시한다 — 선행 연구를 *훌륭하다*고 부르며 그 위에서 작업했음을 인정하고 시작한다. 도전적이지 않다. 반면 contribution 항목 안에 들어가는 동사 — "introduce", "use", "present", "make public" — 는 단정적이다. 외부 톤은 점잖고 내부 진술은 단정적이라는 비대칭이 시스템 논문 contribution 단락이 지켜야 할 자세다. 후배가 자기 contribution을 적을 때 외부 톤을 단정적으로 쓰면("We propose a revolutionary …") reviewer의 거부 반응을 부르고, 내부 진술을 약하게 쓰면("We try to …") contribution이 무너진다. ORB-SLAM의 비대칭이 안전한 기본이다.

---

## 따라 쓰기 — 자기 분야에 적용

이 패턴은 시스템 논문 contribution 단락의 3-슬롯 골격이다. "This paper presents [system name], a [형용사2-3] [task] system that [핵심 능력]. … The main contributions of this work are: 1) [모듈+새로움+결과], 2) …, 3) …" — 각 항목이 동일한 세 슬롯을 채우는지가 contribution이 단단한지의 척도다. 형용사를 먼저 정하고, 그것이 곧 평가 축이 된다는 약속을 Results 섹션이 지키는지 사후 점검한다. ORB-SLAM의 *versatile and accurate*는 제목·abstract·평가 모두에 일관되게 박혀 있다.

Abstract 한 줄과 Introduction bullet의 1:1 대응을 직접 표로 그려 보는 것이 자기 점검 도구다. abstract의 형용사·명사구 하나하나가 어느 bullet에 풀려 나오는지 짚는다. 어디에서도 풀리지 않는 형용사가 있다면 그 형용사는 *약속만 있고 이행이 없는 상태*다. 그 형용사를 abstract에서 빼거나, contribution 한 항목을 추가하거나, 둘 중 하나를 한다. *coined term*(ORB-SLAM의 "Essential Graph", "survival of the fittest")이 abstract와 bullet 양쪽에 등장하면 독자의 검색·인용 동선이 매끈해진다. 이름을 붙일 만한 모듈이 있다면 그 이름이 두 위치 모두에 박혀 있어야 한다.

---

## 출처
- `murartal-2015-orbslam` — Mur-Artal, R., Montiel, J. M. M., Tardós, J. D., 2015. *ORB-SLAM: A Versatile and Accurate Monocular SLAM System.* IEEE Transactions on Robotics 31(5): 1147-1163. DOI: 10.1109/TRO.2015.2463671. arXiv:1502.00956.

---
