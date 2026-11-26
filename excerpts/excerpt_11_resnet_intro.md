# 좋은 서론은 질문 하나를 독자 앞에 놓는다

**출처**: He, Zhang, Ren, Sun, 2015 — Deep Residual Learning for Image Recognition, arXiv:1512.03385 → CVPR 2016

---

학계 전체가 당연하게 믿고 있던 전제를 정면으로 부정하면 독자의 저항을 부르기 쉽다. ResNet 논문은 기존의 통념을 공격하는 대신, 누구나 수긍할 만한 질문 하나를 독자 앞에 가만히 내려놓음으로써 딥러닝의 패러다임을 바꿀 문제를 자연스럽게 꺼내 보인다.

## 발췌

Abstract 도입부는 문제의 핵심과 저자들의 해법을 군더더기 없는 두 문장으로 제시한다.

> Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.

이어지는 Introduction 두 번째 단락의 핵심 두 문장(참고문헌 번호 생략)에서, 저자들은 분야의 암묵적 가정을 하나의 질문으로 끌어올린다.

> Driven by the significance of depth, a question arises: Is learning better networks as easy as stacking more layers? An obstacle to answering this question was the notorious problem of vanishing/exploding gradients, which hamper convergence from the beginning.

세 번째 단락에서는 그 장애물을 걷어 낸 자리에 드러난 뜻밖의 현상, 곧 degradation 문제를 짚는다.

> Unexpectedly, such degradation is not caused by overfitting, and adding more layers to a suitably deep model leads to higher training error, …

---

## 한국어 의역

신경망이 깊어질수록 학습시키기는 더 어려워진다. 우리는 기존에 쓰던 것보다 훨씬 깊은 신경망도 수월하게 학습시킬 수 있는 잔차 학습 프레임워크(residual learning framework)를 제안한다. 망의 깊이가 중요하다는 사실이 밝혀지면서 자연스레 질문 하나가 떠오른다. 더 좋은 신경망을 학습시키는 일이 그저 층을 더 많이 쌓는 것만큼 단순할까? 오랫동안 이 질문에 답하지 못하게 가로막아 온 것은 악명 높은 기울기 소실·폭발(vanishing/exploding gradient) 문제였다. 이 문제는 학습 초반부터 수렴을 방해한다. 그런데 정규화 초기화(normalized initialization)와 중간 정규화 층(intermediate normalization layer) 덕분에 이 장애가 대체로 해소되어 수십 층짜리 망도 수렴하기 시작하자, 이번에는 성능 저하(degradation)라는 전혀 다른 문제가 모습을 드러냈다. 망이 깊어질수록 정확도가 포화 상태에 이르더니 이내 급격히 떨어진다. 뜻밖에도 이러한 저하는 과적합(overfitting) 때문이 아니었다. 이미 적당히 깊은 모델에 층을 더 얹으면 오히려 학습 오차(training error) 자체가 높아졌다.

---

## 분석 — 왜 이 표현이 좋은가

ResNet 서론의 가장 뛰어난 성취는 분야가 의심 없이 받아들이던 전제를 공격적인 반박 대신 차분한 **질문**으로 꺼내 놓았다는 점이다. "Is learning better networks as easy as stacking more layers?"(층을 더 쌓기만 하면 더 나은 망을 얻을 수 있는가?)라는 질문이 던져지자마자, 저자들은 바로 다음 문장에서 그 질문에 오랫동안 답하지 못했던 이유로 vanishing/exploding gradient를 짚는다. 그리고 그 장애물이 normalization 기법으로 대체로 해결된 뒤에야 비로소 진짜 적, 곧 degradation 문제가 모습을 드러냈다고 서술한다. **질문 → 기존의 장애물 → 장애물 해소 뒤에 드러난 새로운 문제**로 이어지는 이 3단 계단은 논리적 비약이 전혀 없어, 독자는 서론 둘째·셋째 단락을 지나며 논문이 해결하려는 난제의 정체를 정확히 붙잡게 된다. 학계의 기본 가정을 정면으로 뒤집기 조심스러울 때일수록, 이처럼 질문의 형태로 독자를 서서히 설득하는 방식이 힘을 발휘한다.

degradation 현상을 기존의 익숙한 원인인 과적합(overfitting)과 단호히 분리해 낸 대목도 결정적이다. 깊은 신경망의 테스트 정확도가 떨어지면 독자나 심사위원은 본능적으로 과적합을 먼저 의심한다. 저자들은 "Unexpectedly, such degradation is not caused by overfitting"이라고 선을 그은 뒤, 층을 더 쌓을수록 **학습 오차(training error)** 까지 함께 올라간다는 결정적 증거를 제시한다(저자들은 이 현상이 앞선 연구 [11, 42]에서도 보고되었고 자신들의 실험으로도 이를 재확인했다고 밝힌다). 학습 오차 자체가 치솟는다는 근거가 있어야만 비로소 과적합과는 본질적으로 다른 문제임을 입증할 수 있기 때문이다. 이렇게 기존 진단명과 현상을 떼어 놓은 덕분에, 저자들은 다음 단락에서 이를 "not all systems are similarly easy to optimize"(모든 시스템이 똑같이 최적화하기 쉬운 것은 아니다)라는 최적화 문제로 재정의하고 residual mapping을 해법으로 내세울 발판을 마련한다. 기존의 틀로 설명되지 않는 현상에 고유한 이름과 증거를 붙여 분리해 내야만, 그것이 온전한 내 연구 문제로 성립한다.

단어의 자리 배치 역시 치밀하다. 문장 맨 앞을 여는 부사 `"Unexpectedly"`는 뒤에 이어질 진술이 독자의 통념을 깰 것임을 미리 알리는 신호등 구실을 한다. 만약 같은 내용을 `"Such degradation, surprisingly, is not caused by overfitting"`처럼 문장 중간 쉼표 사이에 끼워 넣었다면 놀라움의 힘이 반감되었을 것이다. 더욱이 바로 앞 문장 안에 둔 괄호 `"(which might be unsurprising)"`이 정확도 포화 현상 자체는 놀랍지 않을 수 있다고 미리 선을 그어 둔 덕분에, 문두의 `"Unexpectedly"`가 정확히 무엇을 겨냥하는지 한층 또렷하게 도드라진다.

초록의 설계 역시 교과서적이다. 문제는 `"Deeper neural networks are more difficult to train"` 단 한 문장으로 깔끔하게 짚고, 곧장 기여의 구체적 수치로 무게중심을 옮긴다. `152 layers`, `"8× deeper than VGG nets"`, ImageNet test set 앙상블 오류 `3.57%`, ILSVRC 2015 분류 1위, CIFAR-10에서의 100층·1000층 분석이 촘촘히 뒤따른다. `"substantially deeper"`라는 추상적 형용사를 던진 뒤 빈말로 남기지 않고 곧바로 숫자로 증명해 내는 구조다. 또한 둘째 문장에서 `"We present a residual learning framework to ease the training"`으로 큰 틀을 밝힌 뒤, 이어지는 문장들에서 `"We explicitly reformulate the layers as learning residual functions"`로 구체적 접근법을 못 박고 `"We provide comprehensive empirical evidence"`로 실험적 입증을 예고하며 호흡을 빈틈없이 이어 간다.

---

## 따라 쓰기 — 자기 분야에 적용

기존 연구가 놓친 새로운 병목을 문제로 제기하고 싶다면 ResNet 서론의 문장 골격을 빌려 보자.

> "Driven by [분야의 기본 가정], a question arises: [그 가정이 정말 성립하는가]? An obstacle to answering this question was [기존에 알려진 장애]. [그 장애가 풀린 뒤], [기존 진단으로 설명되지 않는 현상] has been exposed. Unexpectedly, [그 현상은 기존 원인 때문이 아니다], [결정적 근거]."

만약 포착한 현상에 아직 통용되는 이름이 없다면 간결한 이름을 붙이고, 왜 기존의 원인으로는 설명되지 않는지 대조 근거를 반드시 나란히 대야 한다.

문장의 강조 효과를 살리고 싶을 때는 `"Unexpectedly"` 같은 태도 부사를 문장 첫머리에 세워 독자의 시선을 새로운 현상에 집중시키는 기법이 효과적이다. 다만 한 단락에 두 번 이상 쓰면 정작 무엇이 진짜 뜻밖의 발견인지 흐려지므로, 가장 결정적인 문장 딱 한 곳에만 아껴 써야 한다.

마지막으로 초록에서는 문제를 짤막하게 던지고 기여는 반드시 구체적인 수치로 받쳐야 한다. ResNet이 층수, 기준 모델 대비 배수, 오류율, 대회 순위로 답했고 ORB-SLAM이 시스템 기능과 27개 평가 sequence로 답했듯, 정해진 숫자 개수에 얽매일 필요는 없다. 다만 `"substantially deeper"` 같은 수식어를 썼다면 `"152 layers"`처럼 그 말을 증명할 수치가 뒤따르는지 확인해야 한다. 수치가 빠진 형용사는 근거 없는 자화자찬으로 읽히기 쉽다. 좋은 서론은 독자에게 익숙한 질문에서 출발해, 누구나 납득할 수밖에 없는 증거로 새로운 문제의 문을 연다.

---

## 출처
- `he-2016-resnet` — He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep Residual Learning for Image Recognition. IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 770-778. arXiv:1512.03385.

---
