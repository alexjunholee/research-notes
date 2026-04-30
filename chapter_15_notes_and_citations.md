# Ch.15 — 노트와 인용 관리

본인이 어제 읽은 한 편의 본문은 3개월 후에 잊는다. 6개월 후에는 abstract도 흐릿하다. 이 사실이 노트의 frame을 정한다. 노트는 *읽은 직후의 자기*가 *6개월 후의 자기*에게 보내는 메모이고, 미래의 자기를 *모르는 사람*으로 두고 적는다.

여기서 본인이 자주 어기는 한 가지가 있다. *그 순간에만 통하는* 약어·줄임을 노트에 박는 결정이다. 한 달 후에는 그 약어가 본인에게도 외부어가 된다. 노트는 본인의 *외장 working memory*이지, 검색되는 데이터베이스가 아니라는 frame부터 깔려 있다.

ch04가 input pipeline의 *흘러 들어오는 곳*이었다면, 본 챕터는 그 자료를 *저장하고 재호출하는* 단계에 들어간다. ch03의 5 Cs가 1st pass의 출력 양식이라면, 본 챕터는 그 위에 *저장* layer를 더 얹는다.

---

## 15.1 노트 양식 — 5 Cs + 3 추가 칸

ch03의 5 Cs (Category·Context·Correctness·Contribution·Clarity)가 한 편의 1st pass 출력이라면, 노트로 박을 때는 그 위에 세 칸이 더 붙는다.

**5+1 — 인용 가능 한 줄.** 자기 글에서 한 번 cite할 만한 *그 한 줄*을 원문 인용으로 박아 둔다. 위치(page·line·equation 번호)도 함께. 6개월 후 본인이 introduction을 쓸 때 *"X가 Y라고 보고했다"*가 필요해진 시점에, 그 한 줄이 노트에 박혀 있으면 paper를 다시 열지 않아도 된다.

**5+2 — 본인 작업과의 거리.** 이 한 편이 자기 thesis와 어떤 관계인가? 네 분류가 있다. *baseline 후보*, *related work*, *반박 대상*, *무관*. 무관도 분류의 한 항목이다. 무관임을 적어두는 작업이 6개월 후 *왜 이 한 편을 cite 안 했는가*에 답하는 자료가 된다.

**5+3 — 다음 액션.** stop·defer·proceed (ch01의 결정 게이트). proceed면 *언제* 다시 돌아올지 한 줄. defer 큐에는 다시 돌아올 시점이 함께 적혀야, 그제서야 그 시점이 되었을 때 weekly digest 블록에서 그 자료가 잡힌다.

🟡 노트는 한 편당 한 페이지 상한이다. 한 편에 두 페이지를 쓰면 그건 정독한 글이지 노트가 아니고, 정독 자료에는 별도 파일을 만든다. 노트와 정독 자료가 같은 파일에 섞이면, 6개월 후 *어느 한 편을 정독했는가*가 안 잡히는 함정에 빠진다.

노트 파일명은 *저자-연도-키워드* 형식이 검색 가능성이 높다. ASCII 키워드를 박는 편이 grep·검색에서 마찰이 적다. 분야 layer라면 `mur-artal-2015-orbslam.md` 같은 식의 키가 흔히 쓰인다.

---

## 15.2 인용 관리 — BibTeX·Zotero·Better BibTeX

🔴 BibTeX 항목을 손으로 typing하지 않는다. typo가 reference 깨짐의 1차 원인이다. 자동 생성 출처는 셋이다.

| 출처 | 도구 |
|---|---|
| Google Scholar | Cite 버튼 → BibTeX |
| Semantic Scholar | API 또는 BibTeX export |
| DOI | CrossRef API 한 줄 |

자동 생성된 항목도 한 번은 본인이 통과한다. journal 이름이 약어로 되어 있거나, 저자 이름의 first name이 initial로만 박혀 있거나, year가 비어 있는 항목이 자동 생성에서 자주 어긋난다.

100편을 넘기는 라이브러리에서는 [Zotero](https://www.zotero.org/) + [Better BibTeX](https://retorque.re/zotero-better-bibtex/) 조합이 거의 필수다. citation key를 *저자-연도-키워드* 형식으로 자동 생성하고, 같은 key가 둘 이상이면 자동으로 suffix가 붙는다. 100편 라이브러리에서 본인이 손으로 key를 관리하면, 같은 paper가 두 다른 key로 박혀 있는 사고가 흔히 생긴다.

PDF + 메타데이터 + tag를 한 set로 보관하는 작업이 Zotero의 본체다. PDF에 친 형광펜이 노트와 함께 박히면, 6개월 후 *어느 한 줄을 강조했는가*가 그대로 호출된다. 분야 instantiation은 robotics-practice ch20 § 20.8.5에 정리되어 있다. Overleaf, Mathpix, Tables Generator 같은 도구가 BibTeX 도구와 한 set로 묶인다.

---

## 15.3 PDF 리더 + AI 워크플로우

PDF 리더 ([Acrobat](https://www.adobe.com/acrobat.html)·[Foxit](https://www.foxit.com/)·[Highlights](https://highlightsapp.net/)·[Skim](https://skim-app.sourceforge.io/))에 친 형광펜·코멘트가 노트로 자동 흘러가는 통로가 있다. Zotero·Highlights 같은 도구가 그 통로를 받고, PDF 한 편의 형광펜이 노트 파일의 한 칸으로 옮겨진다. 그러자면 한 편 정독 후 본인이 *PDF에서 노트로 옮기는* 작업이 자동화된다.

AI 보조 layer는 세 갈래로 붙는다.

**갈래 1 — 0차 5 Cs 자동 채움.** PDF를 AI에 던지고 *"5 Cs를 한 번에 채워 줘"*를 묻는다. ch04 §3에서 다룬 0차 triage의 frame과 같은 결이다. 본인은 그 결과를 통과시키는 작업이 1st pass의 시작점이 된다.

**갈래 2 — reference 큐레이션.** PDF의 reference 목록을 AI에 던지고 *"내 thesis 키워드와 가장 가까운 5편을 골라 줘"*를 묻는다. 다음 input pipeline의 한 항목이 거기서 만들어진다. 한 편의 reference 30편 중 본인이 1st pass 후보로 옮길 5편이 그 시점에서 추려진다.

**갈래 3 — related work 비교.** paper A와 paper B의 차이점을 한 표로 정리해 달라고 AI에 요청한다. 본인이 검증한 후 그 표가 자기 글의 related work 단락의 골격이 된다.

🔴 AI가 만든 5 Cs 노트는 *초안*이다. 본인이 한 번 통과한 후에 저장한다. AI hallucinate가 노트 시스템의 가장 큰 함정이고, 검증 없이 박힌 5 Cs는 6개월 후 본인이 *그 한 편을 안 읽은 채* 인용하게 만들 수 있다.

robotics-practice ch20 § 20.8.5의 권고가 같은 결을 분야 instantiation으로 짚는다.

> *"PDF 리더 + AI 조합이 효율적이다 — Acrobat 형광펜 + Claude/GPT로 요약·BibTeX 생성·related work 비교, Google Scholar Cite 버튼, Zotero + Better BibTeX는 100편 이상에서 유용."*
>
> — robotics-practice ch20 § 20.8.5

AI를 켜는 단계와 본인이 들어가는 단계가 한 set로 묶여 있고, AI가 만든 결과를 *그대로 박지 않는* 입장이 두 단계 모두에 깔려 있다.

---

## 15.4 노트 시스템 운영 — 검색 가능성과 정기 청소

노트는 *시간이 지날수록 가치가 오르는* 자료다. 그러자면 검색 가능성이 1순위에 놓인다. 키워드 tagging 규약을 한 set로 통일해 두면, 1년 후 본인이 *3개월 전 어느 한 편을 어디에 두었는가*를 한 번에 잡는다.

권장 tagging 축은 셋이다.

| 축 | 값 |
|---|---|
| 분야 | slam · cv · dl · vfm · vla |
| 모드 | read · implement · cite · skim |
| 거리 | baseline · related · rebuttal · 무관 |

세 축의 조합으로 한 편을 분류하면, *내 thesis의 baseline 후보 SLAM 논문 5편*이 한 검색으로 잡힌다. 그 5편이 글쓰기 단계의 related work 단락의 골격이 된다.

정기 청소가 본 시스템에 한 단계를 더 얹는다. 한 달에 한 번, 30분 블록을 둔다. 한 달 동안 박힌 노트를 다시 훑고 *연결되는 두 편*을 찾아 *한 줄 메타 노트*를 만든다. *paper A·paper B 모두 가정 X에서 시작* 같은 한 줄이, 본인의 thesis가 놓일 곳을 거기서 만들어 간다.

🟡 흥미로운 한 편이 노트에 박힌 채 사용 안 됨은 *그 한 편이 없는 것*과 같다. Whitesides가 글쓰기 frame에서 적은 한 줄 — *"어떤 프로젝트도 결코 '완료'되지 않는다. 흥미롭지만 미발표인 것은 존재하지 않는 것과 같다"* — 이 노트 시스템에서도 같은 명제가 된다. 5분 핵심에 박힌 한 줄이 본 가이드의 글쓰기 frame과 본 챕터의 노트 frame을 한 결로 묶어 둔다.

노트 → 글쓰기로의 흐름은 단순하다. 자기 paper의 related work 한 단락은 노트에서 *6편을 골라 한 표로 묶는* 작업이다. 그 표가 글의 한 단락의 골격이 되고, 표의 각 칸 — *방법·가정·한계·본인 작업과의 거리* — 이 단락의 한 문장씩으로 풀려 나간다. 이 흐름이 곧 본 가이드의 [Part 2 ch08 (Introduction)](./chapter_23_introduction.md)·[ch09 (Related Work)](./chapter_24_related_work.md)과 같은 결이다.

노트가 자료의 *외장 working memory*에서 자기 thesis의 *글의 골격*으로 옮겨간다. 6개월 동안 누적된 100편의 노트가 본인의 첫 paper의 related work 단락 한 줄 한 줄로 풀려 나가는 풍경이, 본 챕터가 가리킨 끝점이다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V (in-progress vs published — *"흥미롭지만 미발표인 것은 존재하지 않는 것과 같다"*) — 노트 시스템의 frame 거울. robotics-practice ch20 § 20.8.5 *PDF 리더 + AI 조합* — 분야 instantiation 인용. Part 2 [ch08 (Introduction)](./chapter_23_introduction.md) — 노트 → 글쓰기 흐름의 출구. 5 Cs + 3 추가 칸 양식, 정기 청소 운영, AI 보조 layer 정책, tagging 3축은 자체.

다음: Part 1 끝. → [Part 2 — 쓰기](./chapter_16_mindset.md)
