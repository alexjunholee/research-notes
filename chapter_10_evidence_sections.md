# Ch.10 — 방법·결과·그림·표는 주장 하나를 나눠 증명한다

논문은 여러 section으로 나뉘지만, 좋은 논문은 한 주장으로 묶인다. Method는 그 주장을 가능하게 한 선택을 설명하고, Results는 그 선택이 실제로 효과가 있었는지 보이고, Figures와 Tables는 독자가 한눈에 판단할 수 있게 만든다. 이 네 부분이 따로 놀면 논문은 길어지기만 하고 설득력은 늘지 않는다.

Method는 recipe가 아니다. 재현 가능해야 하지만, 모든 구현 디테일을 늘어놓는다고 좋은 method가 되지는 않는다. 독자가 알아야 하는 것은 어떤 선택이 contribution을 만들었는가다. 핵심 알고리즘은 pseudocode로, notation은 table로, hyperparameter는 비교 가능한 표로 정리한다. 중요한 것은 Results와의 짝이다. Method의 subsection 하나가 Results의 evidence 하나와 대응해야 한다.

Results는 숫자 전시장이 아니다. 실험 하나마다 “그래서 무엇이 증명되는가”가 있어야 한다. main result는 claim을 직접 받쳐야 하고, ablation은 어떤 component가 그 효과를 만들었는지 보여 줘야 한다. baseline 비교는 같은 dataset, 같은 split, 가능한 같은 hardware 조건에서 이루어져야 한다. 다른 논문의 숫자를 그대로 가져오면 조건이 다를 때 바로 공격 지점이 된다.

Discussion은 Results의 반복이 아니다. Results가 “무엇이 일어났는가”라면 Discussion은 “왜 그렇게 읽어야 하는가”다. 실패 사례도 이때 필요하다. 좋은 실패 사례는 논문을 약하게 만드는 것이 아니라 claim의 경계를 정확하게 만든다. 경계를 모르는 주장은 과장으로 읽히고, 경계를 아는 주장은 신뢰로 읽힌다.

Figure와 Table은 장식이 아니다. Figure는 구조와 qualitative difference를 보여 주는 데 강하고, Table은 비교와 숫자의 질서를 보여 주는 데 강하다. 같은 결과를 둘 다로 반복하면 하나는 잉여가 된다. table에서는 bold와 underline 같은 강조 규약이 논문 전체에서 같아야 한다. figure에서는 caption 첫 문장이 message를 말해야 한다. 독자가 본문을 읽기 전에도 무엇을 봐야 하는지 알 수 있어야 한다.

결국 방법, 결과, 그림, 표는 모두 같은 질문에 답한다. “내가 한 주장 하나가 실제로 버틸 수 있는가.” 10년 후의 스타일은 여기에서도 절제다. 보여 주고 싶은 것을 다 넣는 것이 아니라, 주장 하나를 정확히 받치는 것만 남기는 능력. 연구의 깊이는 자료의 양이 아니라 증거 배치의 정확성에서 보인다.

읽은 자료: Whitesides의 method/results 관점, Mensh와 Kording의 results-driven structure, figure/table anti-pattern 논의를 통합했다.
