# 좋은 서론은 질문 하나를 독자에게 남긴다

**출처**: He, Zhang, Ren, Sun, 2015 — Deep Residual Learning for Image Recognition, arXiv:1512.03385 → CVPR 2016

---

## 발췌

Abstract 도입부:

> Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously.

Introduction 첫 단락의 핵심 두 문장:

> Driven by the significance of depth, a question arises: Is learning better networks as easy as stacking more layers? An obstacle to answering this question was the notorious problem of vanishing/exploding gradients, which hamper convergence from the beginning.

Introduction 후반의 degradation 진술 한 줄:

> Unexpectedly, such degradation is not caused by overfitting, and adding more layers to a suitably deep model leads to higher training error.


---

## 한국어 의역

깊은 신경망은 학습하기가 더 어렵다. 이 논문은 지금까지보다 훨씬 깊은 망을 쉽게 학습하기 위한 residual learning 골격을 내놓는다. 여기서 한 질문이 자연스럽게 따라온다. 더 좋은 망을 만드는 일이 단순히 층을 더 쌓는 일만큼 쉬운가? 이 질문에 답하기 어려웠던 까닭은 잘 알려진 vanishing/exploding gradient 문제였다. 그런데 normalization 기법으로 그 문제를 어느 정도 푼 뒤에도 깊이가 늘어나자 정확도가 포화한 뒤 떨어지는 현상이 관찰됐다. 학습 자체에는 문제가 없는데도 깊은 망의 학습 오류가 얕은 망보다 높아졌다. 이 현상이 overfitting과 다르다는 지점에서 논문이 출발한다.

---

## 분석 — 왜 이 표현이 좋은가

KISS-ICP가 we move in the opposite direction이라는 평서문으로 자세를 바꿨다면, ResNet은 수사적 질문을 썼다. Is learning better networks as easy as stacking more layers? 이 한 문장이 분야의 기본 가정을 질문으로 드러내고, 다음 문장이 그 가정이 깨지는 지점을 짚는다. Mensh-Kording 규칙 6의 분야 통증 → 기존 한계 → 우리 접근 골격이 평서문 세 박자 대신 질문 + 장애물 + 반전의 세 박자로 바뀐 사례다. 자기 분야의 기본 가정을 직접 부정하기 어렵다면 그 가정을 질문으로 던지는 우회로를 쓸 수 있다.

두 번째 강점은 degradation problem이라는 이름이다. 깊은 망의 정확도 저하는 직관적으로 overfitting으로 진단하기 쉽지만, 저자들은 그 라벨을 명시적으로 거부한다. Unexpectedly, such degradation is not caused by overfitting. 기존 진단으로 설명할 수 없는 현상에 별도 이름을 붙이면 기여가 분명해진다. 이름이 붙으면 기존 도구(regularization, dropout)로는 풀리지 않는 문제라고 말할 수 있고, 자신들의 새 도구(residual mapping)가 들어설 자리도 생긴다. 새로운 현상을 발견했다면 이름을 붙이고 기존 라벨에서 분리해야 그 현상을 자신의 연구 문제로 다룰 수 있다.

Stress position의 활용도 눈여겨볼 만하다. Unexpectedly가 문장 맨 앞에 놓여 다음 절의 명제 전체에 무게를 싣는다. 예상과 다르다는 신호가 먼저 들어오고, degradation은 overfitting이 아니라는 진술이 뒤따른다. 같은 정보를 Such degradation, surprisingly, is not caused by overfitting으로 풀어쓰면 surprisingly가 쉼표 사이에 묻혀 신호가 약해진다. Gopen과 Swan이 강조한 reader expectation을 단어 수준에서 적용한 사례다.

수치의 배치는 ORB-SLAM과 마찬가지로 비대칭이다. 통증은 학습이 어렵다는 진술과 degradation이라는 짧은 라벨로 압축하고, 기여 쪽에는 substantially deeper, 152 layers, 8x deeper than VGG, ImageNet 3.57% error 같은 구체적인 수치를 쌓는다. 통증은 단어 두세 개로 끝내고 기여는 수치로 받친다. 통증을 길게 적으면 독자는 그 문제가 정말 심각한지 의심하고, 기여를 형용사로만 받치면 심사위원은 얼마나 좋은지 묻는다. ResNet은 두 부분의 무게를 단단하게 나눴다.

마지막은 자세다. We present a residual learning framework to ease the training은 새 발명을 제안하기보다 학습을 수월하게 만드는 골격을 내놓는다고 말한다. propose가 아니라 present이고, novel이 아니라 to ease다. 한발 물러나 시작한 뒤 본문의 기여에서는 단정성을 회복하는 비대칭이 ORB-SLAM의 Building on excellent algorithms와 같은 형태다. 겉의 어조는 점잖게 두되 기여는 단정적으로 진술하는 안전한 기본값을 보여 준다.

---

## 따라 쓰기 — 자기 분야에 적용

질문 + 장애물 + 반전된 이름이 세 박자의 골격을 이룬다. "Driven by [분야의 기본 가정], a question arises: [그 가정이 정말 작동하는가]? An obstacle to this question is [기존 라벨]. Unexpectedly, [기존 라벨로 설명되지 않는 현상이 있다] — and we name it [coined term]." 분야의 기본 가정을 직접 부정하기 어려울 때는 그 가정을 질문으로 던진다. 이어 기존 라벨이 설명하지 못하는 지점을 짚고 본인의 coined term으로 이름 붙인다. 그 이름이 분야의 통증을 본인의 기여로 연결한다.

Unexpectedly 같은 부사를 stress position에 두면 새 현상에 독자의 주의를 모을 수 있다. 다만 한 단락에서는 한 번만 쓰는 편이 안전하다. 두 번 이상 나오면 모든 것이 예상 밖이 되어 신호가 사라진다.

ResNet과 ORB-SLAM은 통증을 짧은 라벨 한두 단어로 끝내고, 기여 쪽에는 구체적인 수치 3~5개를 쌓는다. 형용사가 아니라 수치로 받치는 방식이다. substantially deeper는 통증과 자세에 관한 진술이고, 152 layers는 기여에 관한 진술이다. 두 영역의 무게를 잘못 나누면 일부 문장이 과대주장으로 읽힌다.

---

## 출처
- `he-2016-resnet` — He, K., Zhang, X., Ren, S., Sun, J., 2016. Deep Residual Learning for Image Recognition. IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 770-778. arXiv:1512.03385.

---
