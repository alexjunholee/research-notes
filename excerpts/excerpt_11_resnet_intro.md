# 좋은 서론은 질문 하나를 독자 앞에 놓는다

**출처**: He, Zhang, Ren, Sun, 2015 — Deep Residual Learning for Image Recognition, arXiv:1512.03385 → CVPR 2016

---

## 발췌

Abstract 도입부:

> Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.

Introduction 두 번째 단락의 핵심 두 문장(참고문헌 번호 생략):

> Driven by the significance of depth, a question arises: Is learning better networks as easy as stacking more layers? An obstacle to answering this question was the notorious problem of vanishing/exploding gradients, which hamper convergence from the beginning.

Introduction 세 번째 단락의 degradation 진술 일부:

> Unexpectedly, such degradation is not caused by overfitting, and adding more layers to a suitably deep model leads to higher training error, …


---

## 한국어 의역

깊은 신경망은 학습시키기가 더 어렵다. 저자들은 이전보다 훨씬 깊은 망을 쉽게 학습시키는 residual learning framework를 내놓는다. 깊이가 중요하다는 데서 질문이 하나 생긴다. 층을 더 쌓기만 하면 더 좋은 망을 학습시킬 수 있는가? 이 질문에 답하는 데 걸림돌이던 것이 잘 알려진 vanishing/exploding gradient 문제였다. 이 문제 때문에 학습이 처음부터 수렴하지 않았다. 그런데 normalized initialization과 중간 normalization layer로 이 문제가 대체로 풀려 수십 층짜리 망도 수렴하기 시작하자, 이번에는 degradation 문제가 드러났다. 깊이가 늘면 정확도가 포화되고 그다음에는 빠르게 떨어진다. 뜻밖에도 이 저하는 overfitting 때문이 아니었다. 적당히 깊은 모델에 층을 더하면 학습 오류가 오히려 높아졌다.

---

## 분석 — 왜 이 표현이 좋은가

ResNet의 서론은 분야가 당연하게 여기던 가정을 질문으로 꺼낸다. "Is learning better networks as easy as stacking more layers?" 바로 다음 문장은 그 질문에 답하기 어려웠던 이유로 vanishing/exploding gradient를 들고, 그 장애가 normalization으로 대체로 풀렸다고 말한다. 장애가 풀린 뒤에 드러난 것이 degradation이다. 질문, 장애, 장애가 풀린 뒤 드러난 문제가 차례로 놓여 있어서 독자가 논문이 어떤 문제를 푸는지 서론 둘째·셋째 단락에서 알 수 있다. 분야의 기본 가정을 정면으로 부정하기 어려울 때는 이렇게 질문으로 던져 볼 수 있다.

degradation을 overfitting과 갈라놓은 것도 중요하다. 깊은 망의 정확도가 떨어지면 overfitting을 먼저 의심하기 쉽다. 저자들은 "Unexpectedly, such degradation is not caused by overfitting"이라고 쓰고, 층을 더하면 학습 오류까지 높아진다는 근거를 댄다. 이 현상은 앞선 연구 [11, 42]도 보고했고 저자들의 실험으로도 확인했다고 밝힌다. 학습 오류가 높아진다는 사실이 있어야 overfitting과 다른 문제라고 말할 수 있다. 저자들은 다음 단락에서 이것을 "not all systems are similarly easy to optimize"라는 최적화 문제로 풀고 residual mapping을 제안한다. 기존 진단으로 설명되지 않는 현상을 기존 이름과 떼어 놓으면, 그 현상을 자기 연구 문제로 다룰 수 있다.

"Unexpectedly"는 문장 맨 앞에 와서 뒤에 오는 진술이 예상과 다르다고 먼저 알린다. 같은 내용을 "Such degradation, surprisingly, is not caused by overfitting"으로 쓰면 부사가 쉼표 사이에 끼어 덜 눈에 띈다. 바로 앞 문장의 괄호 "(which might be unsurprising)"이 정확도 포화는 놀랍지 않을 수 있다고 미리 말해 두었기 때문에, "Unexpectedly"가 가리키는 대상이 분명해진다.

초록은 문제를 짧게 말하고 기여를 수치로 받친다. 문제는 "Deeper neural networks are more difficult to train" 한 문장이다. 기여 쪽에는 152 layers, "8× deeper than VGG nets", ImageNet test set에서 앙상블 오류 3.57%, ILSVRC 2015 분류 1위, CIFAR-10의 100층과 1000층 분석이 나온다. "substantially deeper"라는 형용사 뒤에 이 수치들이 따라온다.

초록 둘째 문장 "We present a residual learning framework to ease the training"은 학습을 쉽게 하는 framework를 내놓는다고 말한다. 바로 다음 문장에서는 "We explicitly reformulate the layers as learning residual functions"라고 무엇을 했는지 분명히 말하고, "We provide comprehensive empirical evidence"로 근거를 예고한다.

---

## 따라 쓰기 — 자기 분야에 적용

서론의 문제 제기는 이렇게 짜 볼 수 있다. "Driven by [분야의 기본 가정], a question arises: [그 가정이 정말 성립하는가]? An obstacle to answering this question was [기존에 알려진 장애]. [그 장애가 풀린 뒤], [기존 진단으로 설명되지 않는 현상] has been exposed. Unexpectedly, [그 현상은 기존 원인 때문이 아니다], [근거]." 이 현상에 이름이 없다면 이름을 붙이고, 기존 원인과 다르다는 근거를 함께 댄다.

"Unexpectedly" 같은 부사를 문장 첫머리에 두면 새 현상에 독자의 눈길을 모을 수 있다. 한 단락에 한 번만 쓴다. 여러 번 쓰면 무엇이 정말 예상 밖인지 흐려진다.

초록에서는 문제를 짧게 말하고 기여는 수치로 받친다. ResNet은 깊이, 기준 모델과의 비교, 오류율, 대회 결과를 댔고, ORB-SLAM은 시스템의 기능과 27개 평가 sequence를 댔다. 수치가 몇 개여야 한다는 규칙은 없다. "substantially deeper" 같은 형용사를 썼다면 "152 layers" 같은 수치가 뒤따르는지 확인한다. 수치 없이 형용사만 남으면 과장으로 읽힐 수 있다.

---

## 출처
- `he-2016-resnet` — He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep Residual Learning for Image Recognition. IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 770-778. arXiv:1512.03385.

---
