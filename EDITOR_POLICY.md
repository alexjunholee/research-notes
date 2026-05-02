# research-notes — 산문 교정 정책 (EDITOR_POLICY.md)

이 파일은 `prose-editor` 페르소나가 *Type B 후보 제시 자리*를 만났을 때 *어떤 결정을 자동 적용할지* 명시한다. grad-notes/EDITOR_POLICY.md와 같은 구조이지만, 어휘는 *논문 읽기·쓰기·발표* 도메인에 맞춘다.

페르소나 동작 (재확인):
1. `glossary`에 있음 → *자동 적용*
2. `preserve` 목록에 있음 → *자동으로 (c) 원문 유지*
3. `verb_substitutions`에 정의됨 → *자동 적용*
4. 정책 외 + `default: preserve_original` → *자동으로 (c) 원문 유지*

---

## 1. Glossary — 영문 용어 한국어 표기 (자동 적용)

논문·학술 도메인 전용. grad-notes glossary와 일부 겹친다 (PhD·tenure track 등).

| 원문 | 자동 치환 |
|------|-----------|
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
| method | 방법 |
| methods | 방법 |
| results | 결과 |
| discussion | 토의 |
| conclusion | 결론 |
| reference | 참고문헌 |
| references | 참고문헌 |
| citation | 인용 |
| bibliography | 참고문헌 |
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
| arxiv | arXiv (보존) |
| h-index | h-지수 |
| outline | 아웃라인 (보존) |
| section | 섹션 (보존) |
| subsection | 서브섹션 (보존) |
| paragraph | 단락 |
| figure | 그림 |
| table | 표 |
| caption | 캡션 |
| equation | 식 |
| proof | 증명 |
| lemma | 보조정리 |
| theorem | 정리 |
| corollary | 따름정리 |
| dataset | 데이터셋 (보존) |
| baseline | 베이스라인 (보존) |
| pipeline | 파이프라인 (보존) |
| benchmark | 벤치마크 (보존) |
| code | 코드 |
| repo | 저장소 |
| GitHub | GitHub (보존) |
| reproducibility | 재현성 |
| methodology | 방법론 |
| framework | 프레임워크 (보존) |
| implementation | 구현 |
| experiment | 실험 |
| evaluation | 평가 |
| ablation | 어블레이션 (보존) |

(*세션 대화·grad-notes 정책에서 도출된 초안 — 사용자 검토 권장. "보존" 표시는 한국어 표기로 옮기지 말고 영문/외래어를 그대로 두라는 뜻.*)

---

## 2. Preserve — 원문 추상어 보존 목록 (구체화 후보 제시 자체 금지)

논문 메타 가이드라는 도메인 특성상 *구조·과정·추상* 어휘가 핵심 어휘다. 좁히면 의미가 좁아지므로 보존.

- 논문
- 글쓰기
- 읽기
- 발표
- 구조
- 흐름
- 호흡
- 단계
- 과정
- 방법
- 관점
- 시각
- 시간
- 평가
- 기여
- 명제
- 주장
- 근거
- 증거
- 사례
- 패턴
- 양상
- 층위
- 경로
- 분야
- 기본
- 핵심
- 동기
- 의도
- 맥락
- 배경
- 함의
- 결론
- 의미
- 해석
- 분석
- 종합
- 비교
- 대조
- 관계
- 차이
- 균형
- 우선순위

이유: research-notes는 *어떻게 읽고 쓰는가*를 다루는 메타 가이드라, 추상어가 *층위 자체*를 가리킨다. "관점"을 "시야"로, "구조"를 "골격"으로 좁히면 의도된 폭이 무너진다.

---

## 3. Verb substitutions — Type A 동사 변경 자동 적용

| 원문 동사 | 능동/주어 이동 후 |
|-----------|------------------|
| 누적되다 | (행위자)가 누적하다 또는 (보존) |
| 임용되다 | (직책)이/가 되다 |
| 결정되다 | (행위자)가 결정하다 |
| 도출되다 | (행위자)가 도출하다 |
| 적용되다 | (행위자)가 적용하다 |
| 흡수되다 | (행위자)가 흡수하다 |
| 제시되다 | (행위자)가 제시하다 또는 (보존, 학술 관용) |
| 분석되다 | (행위자)가 분석하다 |
| 평가되다 | (행위자)가 평가하다 |
| 구성되다 | (행위자)가 구성하다 |

`제시되다`는 학술 관용으로 자주 등장 — 행위자 모호 시 보존 우선.

---

## 4. Subject preference — 주어 후보 우선순위

1. 인명·역할명 (Whitesides, Keshav, 저자, 독자, 심사위원, 본인)
2. 시간·과정 단계 (논문 첫 한 시간, 초고 작성 단계, 심사 직후)
3. 장소 (학회 자리, 첫 단락)
4. 동명사 (논문을 읽는 일, 인용을 다는 일)
5. 인물 대명사 (그/그녀/본인) — 앞 문장에 인물 도입된 경우만

---

## 5. Default — 정책 외 Type B 자리의 기본값

```
default: preserve_original
```

research-notes는 *추상어 보존 욕구*가 grad-notes보다 더 강하다 (메타 가이드 도메인). 기본값은 (c) 원문 유지로 둔다.

---

## 6. 정책 적용 결과 보고 형식

페르소나는 한 단락 처리 후 다음을 보고:
- *Auto-resolved by policy* — 정책으로 처리된 자리 N개
- *Surfaced as B-user* — 정책이 처리하지 못한 자리 M개
- *Policy gap proposal* — 향후 정책 추가 검토 가치 있는 자리

---

## 7. 정책의 한계

- *내용*: 사실 검증, 인용 출처, 수치 — 정책 영역 밖
- *구조*: 챕터 구조, 단락 순서, 아웃라인 — 정책 영역 밖
- *voice anchor*: STYLE_PROSE.md §7
- *Type A 변환 규칙*: EDITOR_PERSONA.md §5
