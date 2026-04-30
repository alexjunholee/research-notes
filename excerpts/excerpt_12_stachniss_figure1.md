# Stachniss group Figure 1 — *abstract 한 컷 시각화*의 양식

**출처**: Chen, Vizzo, Läbe, Behley, Stachniss, 2021 — *Range Image-based LiDAR Localization for Autonomous Vehicles*, IEEE International Conference on Robotics and Automation (ICRA) 2021
**위치**: Figure 1 + caption + abstract 마지막 한 문장 (arXiv:2105.12121)
**분야**: 로보틱스 / LiDAR localization

---

## 발췌

Abstract 마지막 문장 (원문 인용):

> The experiments suggest that our approach can reliably localize a vehicle in challenging environments and at high frame rates with respect to a previously generated map of the area.


```
[ figure 1 묘사 — 인용·재현 대신 구조만 적는다 ]

  ┌──────────────┐    ┌────────────────┐    ┌───────────────┐    ┌─────────────┐
  │ 3D LiDAR scan│ →  │ range image    │ →  │ map reference │ →  │ 6-DoF pose  │
  │ (online)     │    │ (2D projection)│    │ scan match    │    │ estimate    │
  └──────────────┘    └────────────────┘    └───────────────┘    └─────────────┘
```

Caption (요지): 본 연구의 입력은 online 3D LiDAR scan, 중간 표현은 range image (2D projection), 매칭 대상은 사전 구축된 map의 reference scan, 출력은 6-DoF pose estimate.


---

## 분석 — 왜 이 figure 1이 좋은가

이 figure 1이 모범인 첫째 이유는 *abstract와의 1:1 대응*이다. abstract 마지막 문장이 *vehicle을 reliably localize한다 / 사전 map과 매칭한다 / 높은 frame rate*라는 세 명제를 담는다. figure 1이 같은 세 명제를 *그림으로 다시 한 번* 던진다 — vehicle = LiDAR scan 입력, 사전 map = reference scan 박스, localize = pose estimate 결과. 독자가 abstract 한 문단을 읽고 figure 1로 눈을 옮기는 순간, *방금 읽은 단어*가 *방금 본 박스*와 정렬된다. cxli233의 *Friends Don't Let Friends* 시리즈가 비판하는 *figure 1과 abstract가 따로 노는* 안티패턴의 정반대다. 후배가 figure 1을 만들 때 가장 먼저 점검할 항목이 이 1:1 대응이다.

둘째 강점은 *그룹 문체의 일관성*이다. Stachniss group의 figure 1은 본 논문 외에도 KISS-ICP, surfel SLAM, OverlapNet, MOS 등에서 모두 *입력 sensor → 핵심 표현 → 출력 결정*의 4-박스 구조를 쓴다. 입력이 LiDAR scan / image / point cloud이고 출력이 pose / map / mask로 바뀌어도 *3-4 박스 + 화살표*의 형태가 유지된다. 그룹의 문체가 한 figure 1 양식에 박혀 있고, 후배가 그 그룹의 새 논문을 펼쳤을 때 *어디가 핵심인지*를 figure 1만 보고 짚을 수 있다. 양식의 일관성이 *읽기 비용*을 낮추는 도구다.

셋째는 *Whitesides §III의 promise-deliver alignment*가 figure 1까지 확장된 사례라는 점이다. title (Range Image-based), abstract (range image projection으로 localize), figure 1 (range image 박스가 중간 위치), contribution bullet (range image 표현의 효율성) — 같은 명제가 네 곳에서 반복된다. *range image*라는 한 명사구가 네 곳에 박혀 있어서 reviewer가 abstract만 읽고도 본 논문의 핵심 한 줄을 즉시 짚는다. 후배 글쓰기에서 *제목·abstract·figure 1·contribution*의 네 곳에 본인의 핵심 명사구가 *모두 같은 단어*로 박혀 있는지 확인하는 단계가 figure 1 점검의 출발점이다.

넷째는 *단순함의 운영*이다. figure 1에 박스 4개 + 화살표 3개. 그 이상 욕심내지 않았다. 본 논문의 시스템 다이어그램은 figure 2로 분리되어 있고 거기에는 module 7-8개가 들어간다. figure 1은 *abstract 1 컷*이고 figure 2는 *시스템 다이어그램*이라는 분리가 명확하다. 후배가 figure 1에 module 7개를 욱여넣으면 *abstract 1 컷*이 깨지고, figure 2가 비어 보이게 된다. *figure 1은 4-5 박스 한도, 그 이상은 figure 2로 분리*가 안전한 기본이다.

다섯째는 caption의 압축이다. Stachniss group의 figure 1 caption은 보통 한 문장 — *입력 → 핵심 표현 → 출력*. 알고리즘 디테일은 들어가지 않는다. 본 논문 figure 1 caption도 같은 양식이다. caption이 길어지면 독자가 *figure 1만으로 시스템을 이해해야 한다는* 신호로 읽히는데, 그 무게는 figure 1이 감당할 몫이 아니다. caption이 *한 문장*이라는 제약 그 자체가 figure 1을 abstract 한 컷에 묶어 두는 도구다.

---

## 따라 쓰기 — 자기 분야에 적용

이 패턴은 *abstract → figure 1*의 1:1 대응을 작업 순서에 박는 일이다. abstract 마지막 한 문장을 먼저 쓰고, 그 문장의 *동사·명사·형용사*를 figure 1의 *박스·화살표·라벨*에 직접 매핑한다. 매핑되지 않는 단어가 abstract에 있다면 그 단어가 *figure 2 자리*의 디테일이거나 *과잉 형용사*다. 매핑되지 않는 박스가 figure 1에 있다면 그 박스가 *abstract에 들어가야 할 정보*가 빠진 자리다. 두 자리를 동시에 다듬는다.

박스 수는 4-5개를 기본으로 둔다. 4-5개에 들어가지 않는 시스템은 figure 1의 자리가 아니라 figure 2의 자리다. figure 1은 *abstract 1 컷*, figure 2는 *시스템 다이어그램*. 두 자리를 분리하지 않으면 figure 1이 너무 무거워지고 figure 2가 비어 보인다. 이 분리가 박사 첫 논문에서 가장 자주 빠지는 자리.

caption은 한 문장으로 끝낸다. *입력 → 핵심 표현 → 출력*의 골격에 본인 분야 명사를 끼워 넣는다. 알고리즘 디테일·hyperparameter·실험 결과는 caption의 자리가 아니다. caption이 두 줄을 넘어가면 figure 2 caption일 가능성이 큰 셈이다.

핵심 명사구가 *제목·abstract·figure 1·contribution bullet* 네 자리 모두에 등장하는지가 마지막 점검이다. 본 논문의 *range image*가 그 사례다. 후배의 *coined term* 또는 *시스템 이름*이 네 자리에 일관되게 박혀 있어야 reviewer의 1차 인상이 단단해진다.

---

## 출처
- `chen-2021-rangeimage` — Chen, X., Vizzo, I., Läbe, T., Behley, J., Stachniss, C., 2021. *Range Image-based LiDAR Localization for Autonomous Vehicles.* IEEE International Conference on Robotics and Automation (ICRA), 5802-5808. arXiv:2105.12121.

---
