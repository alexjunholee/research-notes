# 그림 1은 초록의 핵심 표현을 한눈에 보여 준다

**출처**: Chen, Vizzo, Läbe, Behley, Stachniss, 2021 — Range Image-based LiDAR Localization for Autonomous Vehicles, IEEE International Conference on Robotics and Automation (ICRA) 2021

---

## 발췌

초록 마지막 문장:

> The experimental results show that our method can reliably and accurately localize a mobile system in different environments and operate online at the LiDAR sensor frame rate to track the vehicle pose.

원문 Fig. 1 캡션의 첫 문장:

> Visualization of range images and triangular mesh map.

```
[ 그림 1의 네 패널을 글로 정리한 배치 ]

  왼쪽 위: Mesh map              오른쪽 위: Current scan
  왼쪽 아래: Synthetic range image  오른쪽 아래: Current range image
```

캡션에 따르면 왼쪽은 지도로 쓰는 삼각형 mesh와 그 mesh에서 렌더링한 synthetic range image이고, 오른쪽은 같은 위치에서 얻은 LiDAR point cloud와 그 scan에서 만든 range image다. mesh 지도에서 빨간 부분은 지면, 파란 부분은 지면이 아닌 구조다. 이 그림은 처리 흐름도가 아니다. 지도와 현재 관측을 같은 표현으로 나란히 보여 준다. 처리 흐름은 Fig. 2(Overview of our approach)에 따로 나온다. 서론의 기여 설명에 따르면 두 range image의 차이로 관측 모델을 만들고, 이를 Monte Carlo localization에 넣어 입자의 importance weight를 갱신한다. 추정하는 차량 자세는 $(x,y,\theta)$다. 원문은 LiDAR 프레임 속도의 온라인 동작이 수렴한 뒤(after convergence)의 이야기라고 밝힌다.

---

## 분석 — 왜 이 그림 1이 좋은가

그림 1은 초록에 나오는 지도와 현재 관측의 range image를 나란히 보여 준다. mesh 지도와 LiDAR scan이라는 서로 다른 두 데이터를 같은 range image로 바꾼다는 핵심이 네 패널의 짝으로 보인다. 독자는 초록을 읽고 그림 1을 보면서 방금 읽은 표현이 실제로 어떻게 생겼는지 확인할 수 있다. 위치 추정의 정확도와 처리 속도는 이 그림으로는 알 수 없고 실험 결과를 봐야 한다. 초록과 그림이 이렇게 짝을 이루는지 확인하자는 것은 이 노트의 제안이다.

Stachniss 연구진의 다른 논문들도 그림 1의 형식이 저마다 다르다. 이 발췌에서 가져올 것은 이 논문에서 초록의 핵심 명사와 그림의 두 입력, 공통 표현이 서로 맞물린다는 점이다.

Whitesides는 §2.3의 outline 항목 4(Introduction)에서 첫 문장이 연구의 목적과 그 목적이 왜 중요한지를 간결하게 말하는 것이 이상적이라고 했다. 이 노트는 같은 생각을 그림에도 적용한다. 제목(Range Image-based), 초록(range image로 만든 관측 모델), 그림 1(나란히 놓인 두 range image), 기여 설명(두 range image의 차이로 만든 관측 모델)이 같은 표현으로 이어진다. range image라는 명사구가 네 곳에 되풀이되므로 심사위원은 초록과 그림 1만 보고도 논문의 핵심을 짚을 수 있다. 그림 1을 점검할 때는 제목·초록·그림 1·기여의 네 곳에서 같은 핵심 명사구를 썼는지 먼저 확인한다.

그림 1은 지도와 현재 관측을 같은 표현으로 보여 주는 데 집중하고, 그림 2는 입자별 렌더링·관측 모델·자세 사후분포를 잇는 처리 흐름을 보여 준다. 핵심 표현과 시스템 다이어그램을 나누면 두 그림이 서로 다른 질문에 답한다. 박스 수에 정해진 한도는 없다. 핵심 흐름을 한눈에 따라갈 수 있는지, 세부 모듈 때문에 주요 입출력이 묻히지 않는지를 기준으로 나눈다.

캡션은 각 패널의 대상과 지도 색상의 뜻, 같은 위치에서 얻은 두 range image의 관계를 설명한다. 이 캡션은 네 문장이다. 약어, 색, 화살표, 패널을 설명하려면 캡션이 길어질 수 있다. 그림만 보고 해석하는 데 필요한 정보가 빠지지 않았는지 확인한다.

---

## 따라 쓰기 — 자기 분야에 적용

초록의 핵심 개념과 그림 1의 대응을 작업 순서에 넣는다. 초록에서 핵심 표현이나 처리 흐름을 설명하는 문장을 고르고, 동사·명사를 그림의 패널·박스·화살표·라벨에 대응시킨다. 그림 1에 대응하지 않는 초록의 단어는 그림 2에서 설명할 세부 내용인지, 실험 근거가 필요한 성능 주장인지, 지나친 형용사인지 구분한다. 초록에 대응하지 않는 그림 요소가 있다면 초록에 필요한 핵심 정보인지, 그림의 이해를 돕는 세부인지 판단한다. 초록과 그림을 함께 고친다.

먼저 초록의 중심 claim을 설명하는 최소 흐름만 박스로 둔다. 세부 모듈이 핵심 입출력을 가리면 overview와 상세 시스템 그림을 나눈다. 박스 수를 맞추기 위해 필요한 조건을 빼거나, 반대로 그림 2를 채우려고 세부를 억지로 늘리지 않는다.

캡션의 첫 문장에는 그림이 보여 주는 핵심 대상을 적는다. 흐름도라면 입력 → 핵심 표현 → 출력의 골격을 쓸 수 있다. 이어 그림을 해석하는 데 필요한 기호·색·panel을 설명한다. 알고리즘의 세부 내용·hyperparameter·실험 결과는 그림에 직접 필요할 때만 넣는다.

마지막으로 핵심 명사구가 제목·초록·그림 1·기여 항목의 네 곳에 모두 등장하는지 확인한다. 이 논문의 range image가 그 사례다. 새로 붙인 용어나 시스템 이름도 네 곳에서 같은 표현으로 쓴다.

---

## 출처
- `chen-2021-rangeimage` — Chen, X., Vizzo, I., Läbe, T., Behley, J., Stachniss, C., 2021. Range Image-based LiDAR Localization for Autonomous Vehicles. IEEE International Conference on Robotics and Automation (ICRA), 5802-5808. arXiv:2105.12121.

---
