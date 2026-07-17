# 그림 1은 초록을 한 컷으로 압축한다

**출처**: Chen, Vizzo, Läbe, Behley, Stachniss, 2021 — Range Image-based LiDAR Localization for Autonomous Vehicles, IEEE International Conference on Robotics and Automation (ICRA) 2021

---

## 발췌

초록 마지막 문장(원문 인용):

> The experiments suggest that our approach can reliably localize a vehicle in challenging environments and at high frame rates with respect to a previously generated map of the area.


```
[ 그림 1 묘사 — 인용·재현 대신 구조만 적는다 ]

  ┌──────────────┐    ┌────────────────┐    ┌───────────────┐    ┌─────────────┐
  │ 3D LiDAR scan│ →  │ range image    │ →  │ map reference │ →  │ 6-DoF pose  │
  │ (online)     │    │ (2D projection)│    │ scan match    │    │ estimate    │
  └──────────────┘    └────────────────┘    └───────────────┘    └─────────────┘
```

캡션(요지): 본 연구의 입력은 online 3D LiDAR scan, 중간 표현은 range image(2D projection), 매칭 대상은 사전 구축된 map의 reference scan, 출력은 6-DoF pose estimate.


---

## 분석 — 왜 이 그림 1이 좋은가

그림 1은 초록과 1:1로 대응한다. 초록 마지막 문장에는 vehicle을 reliably localize한다, 사전 map과 매칭한다, 높은 frame rate라는 세 명제가 들어 있다. 그림 1은 이 세 명제를 다시 보여 준다. vehicle은 LiDAR scan 입력, 사전 map은 reference scan 박스, localize는 pose estimate 결과에 대응한다. 독자가 초록을 읽고 그림 1로 눈을 옮기면 방금 읽은 단어가 그림의 박스와 정렬된다. cxli233의 Friends Don't Let Friends 시리즈가 비판하는, 그림 1과 초록이 따로 노는 안티패턴의 정반대다. 그림 1을 만들 때 가장 먼저 이 대응을 점검해야 한다.

Stachniss 연구진의 여러 논문에서는 입력 sensor → 핵심 표현 → 출력 결정으로 이어지는 system overview를 볼 수 있다. 다만 KISS-ICP, surfel SLAM, OverlapNet, MOS의 모든 그림 1이 같은 3~4개 박스 구조라고 단정하지 않는다. 이 발췌에서 가져올 원칙은 연구진 전체의 고정 template가 아니라, 이 논문에서 초록의 핵심 명사와 그림의 입력·표현·출력이 대응한다는 점이다.

Whitesides §III의 promise-deliver alignment는 그림 1까지 이어진다. 제목(Range Image-based), 초록(range image projection으로 localize), 그림 1(중간에 놓인 range image 박스), 기여 항목(range image 표현의 효율성)에서 같은 명제가 반복된다. range image라는 명사구가 네 곳에 되풀이되므로 심사위원은 초록만 읽고도 논문의 핵심을 짚을 수 있다. 그림 1을 점검할 때는 제목·초록·그림 1·기여의 네 곳에서 같은 핵심 명사구를 썼는지 먼저 확인한다.

그림 1은 입력·표현·매칭·출력의 큰 흐름에 집중한다. 자세한 시스템 다이어그램을 별도 그림으로 나누면 overview와 구현 세부가 서로 다른 질문에 답할 수 있다. 박스 수에 보편적인 4~5개 제한은 없다. 핵심 흐름을 한눈에 따라갈 수 있는지, 세부 모듈 때문에 주요 입출력이 묻히지 않는지를 기준으로 나눈다.

캡션은 그림을 본문 없이 이해하는 데 필요한 입력·핵심 표현·출력을 설명한다. 모든 그림 1 캡션을 한 문장으로 제한할 필요는 없다. 약어·색·화살표·panel을 설명하려면 더 길어질 수 있다. 길이보다 그림만으로 해석하는 데 필요한 정보가 빠지지 않았는지 본다.

---

## 따라 쓰기 — 자기 분야에 적용

초록과 그림 1의 1:1 대응을 작업 순서에 넣는다. 초록의 마지막 문장을 먼저 쓰고, 그 문장의 동사·명사·형용사를 그림 1의 박스·화살표·라벨에 직접 대응시킨다. 초록에 대응하지 않는 단어가 있다면 그림 2에 들어갈 세부 내용이거나 지나친 형용사다. 그림 1에 대응하지 않는 박스가 있다면 초록에서 빠진 정보다. 두 곳을 함께 다듬는다.

먼저 초록의 중심 claim을 설명하는 최소 흐름만 박스로 둔다. 세부 모듈이 핵심 입출력을 가리면 overview와 상세 시스템 그림을 나눈다. 박스 수를 맞추기 위해 필요한 조건을 빼거나, 반대로 그림 2를 채우려고 세부를 억지로 늘리지 않는다.

캡션의 첫 문장에는 입력 → 핵심 표현 → 출력의 골격을 적는다. 이어 그림을 해석하는 데 필요한 기호·색·panel을 설명한다. 알고리즘의 세부 내용·hyperparameter·실험 결과는 그림에 직접 필요할 때만 넣는다.

마지막으로 핵심 명사구가 제목·초록·그림 1·기여 항목의 네 곳에 모두 등장하는지 확인한다. 이 논문의 range image가 그 사례다. coined term이나 시스템 이름을 네 곳에서 일관되게 써야 심사위원의 첫인상도 단단해진다.

---

## 출처
- `chen-2021-rangeimage` — Chen, X., Vizzo, I., Läbe, T., Behley, J., Stachniss, C., 2021. Range Image-based LiDAR Localization for Autonomous Vehicles. IEEE International Conference on Robotics and Automation (ICRA), 5802-5808. arXiv:2105.12121.

---
