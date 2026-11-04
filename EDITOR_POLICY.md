# research-notes — 산문 교정 정책

- 실행 계약: `../writing-tools/PROTOCOL.md`
- 상태: 2026-07-23 기준 provisional
- 독자: 첫 논문을 읽고 쓰고 발표하는 대학원생

이 파일은 `research-notes`의 용어와 의미 폭을 지키기 위한 프로젝트
정책이다. 자동 치환표나 자동 능동화 규칙이 아니다. R0~R3 판정과 수정
권한은 `writing-tools/PROTOCOL.md`가 정한다.

## 1. 용어 후보

아래 표는 원고에서 반복되는 표기의 후보 목록이다. 전 항목은 저자 확인
전까지 `provisional`이다. 문맥과 독자의 검색 필요를 보지 않고 일괄
치환하지 않는다. 저자가 표기를 확정하면 사용한 `dataset_id`, 그 데이터셋
`decisions.jsonl`의 판정 ID, 적용 범위, 예외를 적고
`author_confirmed`로 승격한다. 현재 정본은
`../writing-tools/evals/datasets/ko-prose-author-v1/decisions.jsonl`이다.

| 원문 | 후보 표기 |
|---|---|
| PhD | 박사 과정 |
| postdoc | 포닥 |
| lab | 연구실 |
| tenure track | 종신트랙 |
| collaboration | 협업 |
| advisor | 지도교수 |
| committee | 심사위원회 |
| qualifier | 자격시험 |
| dissertation | 학위논문 |
| defense | 학위 심사 |
| funding | 연구비 |
| paper | 논문 |
| abstract | 초록 |
| introduction | 서론 |
| method / methods | 방법 |
| results | 결과 |
| discussion | 토의 |
| conclusion | 결론 |
| reference / references / bibliography | 참고문헌 |
| citation | 인용 |
| peer review | 동료 심사 |
| review | 심사 |
| reviewer | 심사위원 |
| revision | 개정 |
| rebuttal | 답변서 |
| conference | 학회 |
| journal | 학술지 |
| workshop | 워크숍 |
| poster | 포스터 |
| oral | 구두 발표 |
| preprint | 사전 출판본 |
| arXiv | arXiv |
| h-index | h-지수 |
| outline | 아웃라인 |
| section | 섹션 |
| subsection | 서브섹션 |
| paragraph | 단락 |
| figure | 그림 |
| table | 표 |
| caption | 캡션 |
| equation | 식 |
| proof | 증명 |
| lemma | 보조정리 |
| theorem | 정리 |
| corollary | 따름정리 |
| dataset | 데이터셋 |
| baseline | 베이스라인 |
| pipeline | 파이프라인 |
| benchmark | 벤치마크 |
| code | 코드 |
| repo | 저장소 |
| GitHub | GitHub |
| reproducibility | 재현성 |
| methodology | 방법론 |
| framework | 프레임워크 |
| implementation | 구현 |
| experiment | 실험 |
| evaluation | 평가 |
| ablation | 어블레이션 |

논문 제목, 코드·UI의 문자열, 실제 검색어, 직접 인용은 표의 적용 대상이
아니다.

## 2. 의미 폭을 보호할 말

다음 말은 이 메타 가이드에서 실제 분석 층위를 가리킬 수 있다.

`논문`, `글쓰기`, `읽기`, `발표`, `구조`, `흐름`, `호흡`, `단계`, `과정`,
`방법`, `관점`, `시각`, `시간`, `평가`, `기여`, `명제`, `주장`, `근거`,
`증거`, `사례`, `패턴`, `양상`, `층위`, `경로`, `분야`, `기본`, `핵심`,
`동기`, `의도`, `맥락`, `배경`, `함의`, `결론`, `의미`, `해석`, `분석`,
`종합`, `비교`, `대조`, `관계`, `차이`, `균형`, `우선순위`

이를 더 구체적인 비유나 좁은 말로 바꾸면 뜻이 달라질 수 있다. 이런 수정은
R2로 보낸다. 반대로 목록에 있다는 이유만으로 문법 오류나 실제 모호함을
면제하지 않는다.

## 3. 동사 후보

| 원문 | 살펴볼 후보 | 확인할 위험 |
|---|---|---|
| 누적되다 | 쌓이다 / 누적하다 / 원문 유지 | 행위자와 의도 |
| 결정되다 | 결정하다 / 원문 유지 | 결정 주체 |
| 도출되다 | 도출하다 / 나오다 | 학술 강도 |
| 적용되다 | 적용하다 / 쓰이다 | 주체와 대상 |
| 흡수되다 | 흡수하다 / 받아들이다 | 주체와 범위 |
| 제시되다 | 제시하다 / 나오다 / 원문 유지 | 논문 관용과 귀속 |
| 분석되다 | 분석하다 / 원문 유지 | 분석 주체 |
| 평가되다 | 평가하다 / 원문 유지 | 평가 주체·기준 |
| 구성되다 | 구성하다 / 이루어지다 | 구성 주체 |

표는 후보 검색용이다. 새 동사를 금지하지 않으며 자동 적용도 하지 않는다.
주체·강도·범위·귀속이 움직일 수 있으면 R2다.

## 4. 주체를 찾을 때

인명·역할, 시간·과정 단계, 장소, 관찰 가능한 동작을 차례로 살펴볼 수
있다. 자동 순위가 아니며 원문에 없는 행위자를 만들지 않는다. `저자`,
`독자`, `심사위원`도 실제 문맥이 그 주체를 가리킬 때만 쓴다.

## 5. 기본 처리

```text
R0: 기계 검사 뒤 직접 적용 가능
R1: 최소 후보를 만들고 충실성 검수
R2: 원문을 유지한 채 저자 선택
R3: Stage 3 확인으로 이동
```

정책 밖 표현은 저자 선택 전까지 원문을 유지한다. `원문 유지`는 자동으로
문제가 없다고 확정하는 장치가 아니라 조용한 의미 변경을 막는 대기 상태다.

## 6. 보고

- 적용한 R0:
- 저자 승인 후보인 R1:
- 저자 선택이 필요한 R2:
- 사실·출처 확인이 필요한 R3:
- 새 정책 후보와 근거 판정 ID:

정책 항목은 모델 제안만으로 늘리지 않는다. 저자 판정과 validation을 거친다.

## 7. 경계

- 인용, 논문 주장, 저자 귀속, 최신 관례는 Stage 3에서 확인한다.
- 논증 순서와 새 예시 생성은 Stage 4의 권한 밖이다.
- 수학·코드·표 안 문자열은 산문 치환 대상이 아니다.
- 저자 판정이 없는 `VOICE_CARD` 예문은 참고 후보이지 승인 전범이 아니다.
