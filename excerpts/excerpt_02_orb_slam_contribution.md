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

이 논문은 feature 기반 단안(monocular) SLAM 시스템인 ORB-SLAM을 소개한다. ORB-SLAM은 작은 환경과 큰 환경, 실내와 실외에서 실시간으로 동작한다. 움직임이 심해 영상이 어지러워도(severe motion clutter) 잘 견디고, 시점 차이가 큰 상태에서도 루프 폐합(loop closing)과 재위치 추정(relocalization)을 할 수 있으며, 초기화도 완전히 자동으로 한다. 저자들은 최근 몇 년 동안 나온 뛰어난 알고리즘을 바탕으로, 트래킹, 매핑, 재위치 추정, 루프 폐합에 모두 같은 feature를 쓰는 새 시스템을 처음부터 설계했다.

서론 끝에는 주요 기여가 항목으로 정리되어 있다.

- 모든 작업에 같은 feature를 쓴다. 그래서 시스템이 더 효율적이고 단순하며 믿을 만해진다. 저자들이 쓴 ORB feature는 GPU 없이 실시간으로 계산되고, 시점과 조명 변화에 잘 견딘다.
- 큰 환경에서도 실시간으로 동작한다. covisibility graph(같은 지도 점을 함께 보는 키프레임끼리 잇는 그래프)를 써서 트래킹과 매핑을 전체 지도 크기와 상관없이 국소 영역에서만 한다.
- 저자들이 Essential Graph라고 부르는 pose graph를 최적화해 실시간으로 루프를 닫는다.
- 시점과 조명이 크게 바뀌어도 카메라 위치를 실시간으로 다시 찾는다.
- 모델 선택(model selection)에 기반한 자동 초기화 절차로 초기 지도를 만든다.
- 지도 점과 키프레임은 넉넉하게 만들고 아주 엄격하게 솎아 낸다(survival of the fittest). 이 방식은 트래킹을 더 강건하게 하고, 중복 키프레임을 버려서 오래 운용할 수 있게 한다.

---

## 분석 — 왜 이 표현이 좋은가

ORB-SLAM의 기여 진술은 시스템 논문이 자기 기여를 어떻게 묶어 보여 주는지 잘 보여 준다. 초록 첫 문장 "This paper presents ORB-SLAM, a feature-based monocular SLAM system that operates in real time, in small and large, indoor and outdoor environments"는 시스템의 이름과 종류, 핵심 능력을 한 문장에 담았다. 초록 뒤쪽 "we designed from scratch a novel system"의 `we`는 저자들을 가리킨다. Knuth의 §1 point 6은 `we`를 "you and me together"라는 뜻으로, 독자와 저자가 함께 따라가는 자리에 쓰라고 했는데, 여기서는 그런 용법이 아니다.

첫 문장의 feature-based, real time, small and large, indoor and outdoor는 실험에서 보여야 할 평가 기준이기도 하다. 논문은 ORB feature를 쓰고, CPU에서 실시간으로 돌고, 실내외 27개 sequence에서 동작함을 실험으로 보고한다. 초록이 약속한 것을 본문이 지켰는지는 이렇게 하나씩 대 볼 수 있다. Whitesides처럼 outline을 먼저 짜는 방식으로 쓰면, 초록의 약속이 본문의 그림, 표, 기여 목록에 들어 있는지 쓰는 도중에 확인할 수 있다.

서론 끝의 기여 목록은 항목마다 짜임이 같다. 어떤 모듈인지, 무엇이 새로운지, 그래서 무엇이 좋아지는지를 차례로 말한다. 첫 항목을 보면 tracking, mapping, relocalization, loop closing에 같은 feature를 쓴다는 것이 모듈이고, ORB feature가 GPU 없이 실시간으로 돌고 시점과 조명 변화에 강하다는 것이 새로운 점이며, 시스템이 "more efficient, simple and reliable"해진다는 것이 결과다. 여섯 항목이 같은 짜임을 따르니 독자가 항목끼리 비교하기 쉽다. 어느 항목에서 결과가 빠졌다면 그 기여는 약하다. 자기 논문의 기여 목록을 표로 옮겨 칸이 다 찼는지 보면 이것을 빨리 확인할 수 있다.

초록과 기여 목록도 서로 맞물린다. 초록의 "uses the same features for all SLAM tasks: tracking, mapping, relocalization, and loop closing"은 기여 목록의 첫 항목에서 자세히 풀린다. 이 발췌에서 뺀 초록의 다음 문장에 나오는 survival of the fittest는 마지막 항목과 짝을 이룬다. 자기 원고에서도 초록과 서론 마지막 단락을 나란히 놓고, 기여가 같은 핵심어와 근거로 이어지는지 확인한다. 빠진 약속이나 근거를 찾는 데 쓸모가 있다.

기여를 글머리표로 나눈 데도 이유가 있다. 같은 내용을 "We present a system that uses common ORB features for tracking, mapping, relocalization, and loop closing, while introducing a novel covisibility graph for real-time local mapping, and an Essential Graph for efficient large-scale optimization, and …"처럼 한 문장으로 쓰면 절이 접속사로 길게 이어져 기여끼리의 경계가 흐려진다. 항목이 셋에서 여섯 개 사이이고, 항목마다 두세 줄로 줄일 수 있고, 항목들의 짜임이 같을 때는 글머리표가 더 분명하다. ORB-SLAM의 기여 목록은 이 조건을 모두 갖췄다.

어조도 볼 만하다. "Building on excellent algorithms of recent years"는 선행 연구를 훌륭하다고 부르며 그 위에서 작업했음을 인정한다. 바로 뒤의 "we designed from scratch"는 시스템을 처음부터 새로 설계했다고 밝힌다. 기여 목록과 그 앞뒤 문장에서는 "use", "present", "make public" 같은 능동 동사로 단정한다. 선행 연구에는 예의를 갖추고 자기 기여는 분명하게 말하는 방식이 시스템 논문의 기여 단락에 잘 맞는다. "We propose a revolutionary …"처럼 과장하면 심사위원이 반감을 갖기 쉽고, "We try to …"처럼 약하게 쓰면 기여가 흐려진다.

---

## 따라 쓰기 — 자기 분야에 적용

시스템 논문의 기여 단락은 이렇게 짤 수 있다. "This paper presents [system name], a [형용사 2~3개] [task] system that [핵심 능력]. … The main contributions of this work are: 1) [모듈 + 새로운 점 + 결과], 2) …, 3) …" 항목마다 이 세 칸이 채워졌는지 보면 기여가 탄탄한지 알 수 있다. 첫 문장의 형용사는 곧 평가 기준이 되니, 원고를 다 쓴 뒤 Results 절이 그 기준대로 보고했는지 확인한다. ORB-SLAM의 versatile과 accurate는 제목, 초록, 실험에 모두 나온다.

초록의 문장과 기여 항목이 어떻게 이어지는지 직접 표로 그려 보면 좋다. 초록의 형용사와 명사구가 각각 어느 항목에서 풀리는지 짚는다. 어느 항목에서도 풀리지 않는 형용사는 약속만 하고 보여 주지 않은 것이다. 그런 형용사는 초록에서 빼거나, 기여 항목을 하나 더한다. ORB-SLAM의 "Essential Graph"와 "survival of the fittest"는 저자들이 붙인 이름이다. 이런 이름을 초록에 쓴다면 기여 항목에서도 같은 표현을 써야 독자가 찾아 읽고 인용하기 쉽다.

---

## 출처
- `murartal-2015-orbslam` — Mur-Artal, R., Montiel, J. M. M., Tardós, J. D., 2015. ORB-SLAM: A Versatile and Accurate Monocular SLAM System. IEEE Transactions on Robotics 31(5): 1147-1163. DOI: 10.1109/TRO.2015.2463671. arXiv:1502.00956.

---
