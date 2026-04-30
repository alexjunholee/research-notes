# Nilsson — 글쓰기 과정 6 points

**출처**: Nils J. Nilsson (lecture transcribed in Knuth, Larrabee, Roberts, 1989) — *Mathematical Writing*, Stanford CS Report STAN-CS-88-1193 / MAA Notes 14
**bibkey**: `nilsson-in-knuth-1989`
**위치**: §34 — Nilsson의 6 points: start early / rewrite / read / model the reader / master the medium / master the material

---

## 발췌

> [발췌 보류 — Knuth 1989 §34에서 Nilsson의 6 points 제목 어구와 각 항목의 짧은 부연 한 줄에서 fair use 1 paragraph 발췌 예정.]

---

## 분석

Nilsson의 6점은 글쓰기를 *결과물*이 아니라 *과정*으로 본 가장 압축된 체크리스트다. Halmos의 두 명령이 *원칙*을 압축한다면, Nilsson의 여섯 점은 *습관*을 압축한다. 두 발췌가 자매 쌍을 이룬다. 무엇을 지킬 것인가(원칙)와 매일 무엇을 할 것인가(과정). 분석은 여섯 항목의 한국어 풀이, 항목 순서가 가지는 의미, 본 가이드와의 1:1 매핑, 자기 점검 체크리스트로의 변환을 네 단락으로 진행한다.

여섯 점을 한국어로 옮기고 한두 줄씩 풀어 본다. **Start early — 일찍 시작하라.** 글쓰기는 마감 일주일 전에 끝나는 일이 아니다. 데이터 수집과 *동시에* 단락이 자라야 한다. 실험 결과가 나오기 전에 Method 섹션의 1차 초고가 있으면 그 초고의 빈자리가 어떤 실험이 더 필요한지 역으로 알려 준다. Mensh와 Kording이 rule 9에서 권한 "draft alongside experiments"가 이 한 점의 절차적 표현이다. **Rewrite — 다시 써라.** 초고는 *발견을 위한 도구*이지 *완성품*이 아니다. 한 번에 좋은 글이 나온다는 환상이 가장 큰 함정이다. 본 가이드의 4단계 파이프라인(Stage 2 초고 → Stage 3 수정 → Stage 3b 흐름 → Stage 4 교정)이 이 한 단어의 절차화다. **Read — 읽어라.** 좋은 글은 좋은 독자에게서 나온다. 자기 분야 SOTA 논문 다섯 편을 매주 정독하지 않으면 자기 글이 어디에서 부족한지 가늠할 자(尺)가 없다. Part 1 전체가 이 한 점의 부연이다. **Model the reader — 독자를 모델링하라.** 누가 어떤 순서로 무엇을 알고 읽는가를 머릿속에 시뮬레이션한다. Gopen과 Swan의 "reader expectations"와 같은 명령이지만 행동 지시가 더 명료하다 — *시뮬레이션 하라*. **Master the medium — 매체를 다스려라.** LaTeX, BibTeX, 표기 매크로, figure 도구. 매체에 끌려가면 사고가 끌려간다. shortcuts.tex을 정비하지 않으면 글을 쓰는 동안 표기 일관성에 정신이 빠져 substance에 집중할 수 없다. Part 2 ch16 표기법·매크로 위생 챕터의 정당화가 이 한 점이다. **Master the material — 내용을 다스려라.** 모르는 것은 잘 쓸 수 없다. Whitesides가 §I에서 "글쓰기로 사고가 정련된다"고 했지만, 정련될 *재료*가 있어야 한다. 모르는 채로 쓰면 글의 빈틈이 메워지지 않는다.

여섯 점의 *순서* 자체가 메시지를 전달한다. start early(외부 시간) → rewrite(자기 절차) → read(외부 입력) → model the reader(타자) → master the medium(도구) → master the material(내용). 외부, 자기, 입력, 타자, 도구, 내용의 동심원적 확장으로 읽힌다. 혹은 *시간 축*을 따라 *작업의 단단함*이 깊어지는 순서로도 읽힌다. 일찍 시작하는 것이 가장 쉽고, 내용을 마스터하는 것이 가장 오래 걸린다. 이 순서가 우연이 아니다. Nilsson은 후배가 *오늘부터 가능한 것*부터 *평생에 걸쳐 단단해지는 것*까지를 차례로 배치했다.

여섯 점은 본 가이드와 1:1로 매핑된다. start early는 Part 2 ch02(아웃라인부터)와 ch03(시간 배분)에 대응한다. rewrite는 4단계 파이프라인 전체에 대응한다. read는 Part 1 전체에 대응한다. model the reader는 ch07(독자 기대치로 진단하기)과 ch14(문장 구조와 독자 기대)에 대응한다. master the medium은 ch16(표기법·매크로 위생)에 대응한다. master the material은 가이드 외부의 작업이지만, 모든 글쓰기 챕터의 *전제*로 깔린다. 이 매핑은 *6점이 가이드를 어떻게 정당화하는가*의 표가 된다. 후배가 가이드를 펼쳐 들고 "오늘 어디부터 봐야 하는가" 물을 때 6점 중 자신의 약점을 짚으면 챕터 진입점이 정해진다.

여섯 점을 자기 점검 체크리스트로 바꾸면 더 강해진다. 매주 일요일 저녁에 묻는다. ① 이번 주에 글을 *일찍 시작*했는가 — 마감에 쫓겨 시작하지 않았는가. ② 적어도 한 단락을 *다시 썼는가* — 처음 쓴 그대로 두지 않았는가. ③ 자기 분야 *좋은 글을 읽었는가* — 정독한 논문이 한 편이라도 있는가. ④ *독자를 그렸는가* — 누구에게 무엇을 어떤 순서로 보일지 명시했는가. ⑤ *매체*를 다스렸는가 — LaTeX, 표기, 매크로의 정합성을 점검했는가. ⑥ *내용*을 충분히 아는가 — 글에서 흐릿한 자리가 있다면 그 자리는 사고가 흐릿한 자리다. 한 항목이라도 No가 나오면 다음 주 1순위 작업으로 옮긴다. 매주 6 문항이라는 가벼운 자기 점검이 6개월 누적되면 글쓰기 습관이 단단해진다.

---

## 따라 쓰기 패턴

이 패턴은 매주 자기 글쓰기 진단의 6문 체크다. 일찍 시작했나 / 다시 썼나 / 좋은 글을 읽었나 / 독자를 그렸나 / 매체(LaTeX·표기)를 다스렸나 / 내용을 충분히 아는가. 한 항목이라도 No면 다음 주 1순위 작업으로. 6개월 누적되면 6 점 모두에서 어느 정도 단단함이 생긴다.

여섯 점을 *동시에* 잘하려고 하면 어느 하나도 잘하기 어렵다. 약한 점 하나를 골라 한 주 또는 한 달의 1순위 작업으로 두는 방식이 누적에 유리하다. 가령 "이번 달은 model the reader에만 집중한다 — 모든 단락에 대해 누가 어떤 순서로 무엇을 알고 읽는지 명시하기"처럼.

---

## Tags

`mindset`, `process`, `six-points`, `checklist`, `habit`, `rewrite`, `model-the-reader`, `master-medium`, `master-material`, `nilsson`, `aphorism`

## Related chapters

- [Ch.6 — 왜 읽는가](../chapter_06_why_read.md) — "read"의 부연
- [Ch01 — 마음가짐](../chapter_16_mindset.md)
- [Ch02 — 아웃라인부터](../chapter_17_outline_first.md)
- [Ch03 — 시간 배분](../chapter_18_time_budget.md)
- [Ch14 — 문장 구조와 독자 기대](../chapter_29_reader_expectations.md)
- [Ch16 — 표기 위생](../chapter_31_notation_hygiene.md)
- [Halmos — Do organize. Do not distract.](./excerpt_05_halmos_organize_dont_distract.md)
- [Knuth proof rewrite](./excerpt_04_knuth_proof_rewrite.md)
