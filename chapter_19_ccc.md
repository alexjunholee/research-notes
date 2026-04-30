# Ch.19 — CCC: 단락·섹션·논문의 fractal

한 단락도 잘 닫지 못하는 학생이 논문 전체를 닫아야 한다는 요구를 받는다. 닫는 문제가 같은 형태로 세 번 반복된다는 점만 보이면 처방은 한 가지로 줄어든다. [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 3이 그 한 가지를 맥락-Content-Conclusion(CCC)으로 정식화했다.

---

## 19.1 독자의 두 질문

독자가 한 단락 또는 한 섹션을 읽기 시작할 때 두 가지 질문을 동시에 던진다. "왜 이걸 읽고 있지?"와 "그래서 어쩌라고?"다. 앞 질문은 context의 부재가 만들고, 뒤 질문은 conclusion의 부재가 만든다. CCC가 두 질문에 동시에 답하는 최소 골격이다.

신입생들이 자연스럽게 따라가는 구조는 시간순(chronological)이다. "처음에 A를 시도했는데 실패했고, 그래서 B로 갔는데 이건 또 다른 문제가 있어서, 결국 C에 도달했다." 이 구조는 lab notebook에는 적합하지만 논문에는 main failure mode다. Mensh-Kording이 §"chronological structure is the main failure mode"에 적은 표현 그대로다. 독자는 글쓴이가 결과에 도달한 시간 순서를 신경 쓰지 않는다.

CCC가 시간순의 대안으로 들어선다. 첫 문장에서 context를 박고, 본문에서 novel content를 풀고, 마지막 문장에서 takeaway를 닫는다. 시간순이 *과정*을 그대로 노출한다면, CCC는 *과정의 결과*만 전달한다.

---

## 19.2 3-scale fractal

같은 패턴이 단락·섹션·논문 세 스케일에 그대로 반복된다.

- **단락.** 첫 문장 = topic/context. 가운데 문장들 = novel content. 마지막 문장 = takeaway.
- **섹션.** 도입 1단락 = 섹션의 목적과 위치. 본문 단락들 = develop. 마무리 단락 = land.
- **논문 전체.** Introduction = context. Results = content. Discussion = conclusion.

세 스케일 어느 한 곳이라도 깨지면 fractal이 무너진다. 단락이 잘 닫혀 있어도 섹션이 시간순이면 독자는 길을 잃는다. 섹션이 CCC를 따라가도 단락마다 첫 문장이 결과로 시작하면 독자는 매번 "왜 이걸 읽지?"를 다시 묻는다.

3-scale은 단순한 비유가 아니다. 같은 골격을 세 번 반복하면 독자의 working memory가 같은 패턴 인식만으로 논문 전체를 따라간다. 패턴이 매 스케일에서 일치할 때 인식 비용이 가장 낮다.

---

## 19.3 Abstract — full CCC self-contained

Abstract는 세 요소 모두를 한 단위 안에 담는 유일한 섹션이다. 한 문단 안에 context와 content와 conclusion이 모두 있어야 한다. Mensh-Kording rule 5는 이를 "key fits its lock" 비유로 적었다. 결과(key)가 갭(lock)에 정확히 들어맞아야 abstract가 완성된다는 뜻이다.

이 비유의 함의는 작업 순서에 있다. abstract를 처음에 쓰면 lock(갭)이 흔들리는 동안 key를 깎는 일이 된다. 본문이 안정된 뒤에 abstract를 쓰는 [Whitesides의 권고](./chapter_17_outline_first.md)와 같은 결론에서 만난다.

Abstract의 self-contained 성격은 다른 섹션과의 차이도 만든다. 섹션 단위에서는 다음 섹션의 도입이 이전 섹션의 결론을 이어받지만, abstract는 자기 안에서만 닫혀야 한다. 외부 참조가 abstract에 들어가면 self-contained 조건이 깨진다.

---

## 19.4 Tension — 문장 stress vs 단락 CCC

[Gopen & Swan 1990](https://www.americanscientist.org/sites/americanscientist.org/files/20053191534_306.pdf)이 §stress position에 적은 규칙은 *새 정보는 문장 끝*이다. Mensh-Kording rule 3은 *takeaway는 단락 끝*이다. 같은 "끝"을 다른 두 스케일에서 노린다. 학생들이 충돌처럼 받아들이는 지점이지만 충돌은 아니다.

같은 원리가 두 스케일에 적용된 결과로 보는 쪽이 정확하다. 독자의 기대가 *끝에서 충족된다*는 한 원리가 sentence와 paragraph 양쪽에 작동한다. 단락의 마지막 문장 안에서도 stress position 규칙은 그대로 살아 있고, 그 마지막 문장의 끝에 단락 전체의 takeaway가 놓인다.

이 책의 입장은 둘 다 끝을 노린다는 한 줄로 정리된다. 스케일이 다르고 끝이 가리키는 단위도 다르지만, 독자의 기대 방향은 같다 — 충돌하지 않는 두 규칙이 같은 문장 끝에서 만난다.

---

## 19.5 흔한 실수 5종

CCC가 깨지는 패턴은 비교적 정형화되어 있다.

- 단락 첫 문장에 결과부터 박는 경우 — context 슬롯이 비어 있고, 독자는 "왜 이걸 읽지?"를 묻는다.
- 단락 마지막 문장이 다음 단락의 도입으로 새는 경우 — conclusion 칸에 transition을 두면 takeaway가 사라진다. 가장 빈번한 결함이다.
- 섹션 도입 단락 없이 §2.1로 바로 진입하는 경우 — 섹션 스케일의 context가 비어 있다.
- Discussion에 새 결과가 등장하는 경우 — content 스케일과 conclusion 스케일이 섞인다. Discussion은 새 결과를 두는 곳이 아니다.
- Conclusion이 Results의 요약인 경우 — [Ch.5](./chapter_20_subheadings_and_conclusions.md)에서 따로 다룬다.

이 다섯은 체크리스트로 반복 점검할 수 있다. 단락 단위 결함은 비교적 빨리 보이지만, 섹션·논문 스케일의 결함은 결국 사람의 진단이 필요하다.

---

**출처.** [Mensh & Kording 2017](https://doi.org/10.1371/journal.pcbi.1005619) rule 3·4·5. [Gopen & Swan 1990](https://www.americanscientist.org/sites/americanscientist.org/files/20053191534_306.pdf) (stress position). tension 화해 입장은 이 장에서 정리했다.

다음: [Ch.5 — 정보가 담긴 소제목과 결론 ≠ 요약](./chapter_20_subheadings_and_conclusions.md)
