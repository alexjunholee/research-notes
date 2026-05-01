# 좋은 서론은 질문 하나를 독자에게 남긴다

**출처**: He, Zhang, Ren, Sun, 2015 — *Deep Residual Learning for Image Recognition*, arXiv:1512.03385 → CVPR 2016

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

깊은 신경망은 학습이 더 어렵다. 이 논문은 *지금까지보다 훨씬 깊은* 망의 학습을 *수월하게 만드는* residual learning 골격을 내놓는다. 깊이의 중요성 위에서 한 질문이 자연스럽게 따라온다 — *더 좋은 망을 만드는 일이 단순히 층위를 더 쌓는 일만큼 쉬운가.* 이 질문에 답하기 어려웠던 한 자리는 vanishing/exploding gradient라는 잘 알려진 문제였다. 그런데 그 문제를 normalization 기법들로 어느 정도 풀고 나서도, 깊이가 더 늘어나자 *예상과 다른* 자리에서 정확도가 *포화하다 떨어지는* 현상이 관찰됐다 — 학습 자체에 문제가 없는데도 깊은 망이 얕은 망보다 *학습 오류*까지 높아졌다. 이 현상이 overfitting과 *분리되는* 한 지점이 본 논문의 출발점이다.

---

## 분석 — 왜 이 표현이 좋은가

KISS-ICP가 *we move in the opposite direction*으로 자세 전환을 평서문에 박았다면, ResNet은 같은 자리를 *수사적 질문*에 박았다. *Is learning better networks as easy as stacking more layers?* — 이 한 문장이 분야의 기본 가정을 *질문의 형태*로 드러내고, 다음 문장이 그 기본이 작동하지 않는 자리를 짚는다. mensh-kording rule 6의 *분야 통증 → 기존 한계 → 우리 접근* 골격이 평서문 3-beat 대신 *질문 + 장애물 + 반전*의 3-beat로 변형된 사례다. 후배가 자기 분야의 기본 가정을 *직접 부정*하기 어려울 때, 그 가정을 *질문으로 던지는* 우회로가 한 도구로 쓰일 수 있다.

이 발췌의 두 번째 강점은 *degradation problem*이라는 coined term이다. 깊은 망의 정확도 저하는 직관적으로 *overfitting*으로 진단되기 쉬운데, 저자들은 그 라벨을 *명시적으로 거부*한다 — *Unexpectedly, such degradation is not caused by overfitting*. 기존의 진단 라벨에 들어가지 않는 현상을 발견했을 때 그 현상에 *별도 이름*을 붙이는 일이 contribution의 절반을 만든다. 이름이 붙고 나면 기존 도구(regularization, dropout)로 풀리지 않는다는 진술이 가능해지고, 자신들의 새 도구(residual mapping)가 들어설 자리가 비어 있게 된다. 후배가 새로운 현상을 발견했을 때 첫 단계에서 *이름을 붙이고 기존 라벨에서 분리*하는 두 작업이 분야 통증을 본인 자리로 끌어오는 운영이다.

Stress position의 활용도 짚어 둘 만하다. *Unexpectedly*가 문장의 *맨 앞*에 놓인 점이 한 도구다. 영어 문장에서 부사가 맨 앞에 오면 그 부사가 강조 위치가 되어 다음 절의 명제 전체에 *비대칭 무게*를 실어 준다. 거기서 *예상과 다르다*는 신호가 먼저 들어오고, 그 다음에 *degradation이 overfitting이 아니라는* 진술이 따라온다. 같은 정보를 *Such degradation, surprisingly, is not caused by overfitting*으로 풀어쓰면 *surprisingly*가 콤마 사이에 묻혀 신호가 약해진다. Gopen과 Swan이 강조한 reader expectation의 단어 단위 적용이다.

수치의 자리는 ORB-SLAM과 같은 비대칭 양식이다. 통증 진술은 *학습이 어렵다*, *degradation*이라는 짧은 라벨로 압축되고, contribution 진술 쪽에 구체 수치가 누적된다 — *substantially deeper*, *152 layers*, *8x deeper than VGG*, *ImageNet 3.57% error*. 통증의 무게를 단어 두세 개로 끝내고, contribution의 무게를 수치로 받친다. 통증을 길게 적으면 독자는 *그래서 이 통증이 진짜 통증인가*를 의심하고, contribution을 *형용사로만* 받치면 reviewer는 *그래서 얼마만큼 좋은가*를 묻는다. ResNet은 두 자리의 분배가 단단하다.

마지막으로 자세. *We present a residual learning framework to ease the training* — 새 발명을 *제안*하는 자세가 아니라 *학습을 수월하게 만드는 골격을 내놓는다*는 자세다. *propose*가 아닌 *present*, *novel*이 아닌 *to ease*. 한 발 물러난 자리에서 시작해 본문 contribution에서 단정성을 회복하는 비대칭이 ORB-SLAM의 *Building on excellent algorithms*와 같은 형태다. 후배가 자기 contribution을 *외부 톤은 점잖게 / 내부 진술은 단정적으로* 분배하는 안전한 기본값을 이 발췌가 한 번 더 보여 준다.

---

## 따라 쓰기 — 자기 분야에 적용

이 패턴은 *질문 + 장애물 + 반전 coined term*의 3-beat 골격이다. "Driven by [분야의 기본 가정], a question arises: [그 가정이 정말 작동하는가]? An obstacle to this question is [기존 라벨]. Unexpectedly, [기존 라벨로 설명되지 않는 현상이 있다] — and we name it [coined term]." — 분야의 기본 가정을 *직접 부정*하기 어려울 때, 그 가정을 *질문*으로 던지고, 그 질문에 답할 때 *기존 라벨이 작동하지 않는 자리*를 짚어 본인의 coined term으로 자리를 만든다. 분야 통증을 본인 contribution으로 *연결하는 다리*가 coined term이다.

*Unexpectedly*류 부사를 stress position에 두는 것이 한 운영 도구다. 새 현상을 짚을 때 그 부사를 문장 *맨 앞*에 두면 독자의 주의 자리가 정렬된다. 한 단락에 이 자리가 한 번만 나오게 하는 것이 안전한 기본 — 두 번 이상 나오면 *모든 것이 예상 밖*이 되어 신호가 사라진다.

수치 분배는 ResNet과 ORB-SLAM이 공통으로 쓰는 양식이다. 통증을 짧은 라벨 한두 단어로 끝내고, contribution 쪽에 *구체 수치 3-5개*를 누적한다. 형용사가 아닌 수치다 — *substantially deeper*는 통증·자세 진술이고, *152 layers*는 contribution 진술이다. 두 영역의 분배가 어그러지면 *과대주장으로 읽히는* 부분이 생긴다.

---

## 출처
- `he-2016-resnet` — He, K., Zhang, X., Ren, S., Sun, J., 2016. *Deep Residual Learning for Image Recognition.* IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 770-778. arXiv:1512.03385.

---
