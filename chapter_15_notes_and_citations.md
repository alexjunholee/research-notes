# Ch.15 — AI 시대의 노트와 인용 관리

본인이 어제 읽은 한 편의 본문은 3개월 후에 잊는다. 6개월 후에는 abstract도 흐릿하다. 이 사실은 여전히 맞다. 달라진 것은 저장 방식이다. 노트는 나중에 다시 돌아왔을 때 왜 이 논문을 남겼는가를 바로 알게 하는 결정 기록이다.

AI가 논문을 다시 열어 요약해 줄 수 있는 시대에는 긴 요약의 가치가 줄어든다. 대신 세 가지가 중요해진다. 어떤 claim이 있었는가. 그 claim의 근거가 논문 어디에 있었는가. 그 claim이 내 작업에서 어떤 결정을 바꾸는가. 이 세 가지는 AI가 대신 보관해 주지 않는다. 사람이 확인하고 적어 둬야 한다.

ch04가 입력 pipeline의 흘러 들어오는 곳이었다면, 이 장은 그 자료를 저장하고 재호출하는 단계에 들어간다. ch03의 5 Cs가 1st pass의 출력 양식이라면, 이 장은 그 위에 근거 위치와 결정 층위를 더 얹는다.

---

## 15.1 노트 양식 — 5 Cs + 3 추가 칸

ch03의 5 Cs (종류·맥락·타당성·기여·명료성)가 한 편의 1st pass 출력이라면, 노트로 박을 때는 그 위에 세 칸이 더 붙는다.

**5+1 — 근거 위치.** 자기 글에서 쓸 만한 claim 하나와 그 claim의 위치를 적는다. page·section·figure·table·equation 번호 중 하나가 붙어야 한다. 직접 인용할 문장이 있을 때만 짧은 원문을 남기고, 대부분은 내 말로 쓴 claim + 위치로 충분하다. 6개월 후 introduction을 쓸 때 필요한 것은 "이 주장을 어느 표가 받쳤는가"의 한 줄이다.

**5+2 — 본인 작업과의 거리.** 이 한 편이 자기 thesis와 어떤 관계인가? 네 분류가 있다. baseline 후보, related work, 반박 대상, 무관. 무관도 분류의 한 항목이다. 무관임을 적어두는 작업이 6개월 후 왜 이 한 편을 cite 안 했는가에 답하는 자료가 된다.

**5+3 — 다음 액션.** 중단·보류·진행 (ch01의 결정 게이트). 진행이면 언제 다시 돌아올지 한 줄. 보류 큐에는 다시 돌아올 시점이 함께 적혀야, 그제서야 그 시점이 되었을 때 weekly digest 블록에서 그 자료가 잡힌다.

노트는 한 편당 한 페이지 상한이다. 긴 요약을 만들수록 나중에 안 읽힌다. 정독 자료가 필요하면 별도 파일을 만들고, 한 페이지 노트에는 claim·근거 위치·내 작업과의 거리만 남긴다. 노트와 정독 자료가 같은 파일에 섞이면, 6개월 후 어느 한 편을 정독했는가가 안 잡히는 함정에 빠진다.

노트 파일명은 저자-연도-키워드 형식이 검색 가능성이 높다. ASCII 키워드를 박는 편이 grep·검색에서 마찰이 적다. 분야 쪽 논의라면 `mur-artal-2015-orbslam.md` 같은 식의 키가 흔히 쓰인다.

---

## 15.2 인용 관리 — reference manager는 본체가 아니다

인용 관리는 paper의 진실을 보관하는 일이 아니다. 진실의 본체는 DOI·arXiv·OpenReview·venue page·publisher page에 있고, reference manager는 그 정보를 논문 양식에 맞게 내보내는 호환 계층에 가깝다.

손으로 BibTeX를 typing하지 않는다. 자동 생성 출처는 DOI, arXiv, CrossRef, Semantic Scholar, OpenAlex, venue page다. Google Scholar의 export는 빠르지만 필드가 비거나 venue 정보가 거칠게 들어오는 일이 있으므로 최종본의 기준으로 두지 않는다.

자동 생성된 항목도 한 번은 본인이 통과한다. 확인할 것은 많지 않다.

| 항목 | 확인할 것 |
|---|---|
| ID | DOI 또는 arXiv ID가 맞는가 |
| 저자 | 첫 저자·마지막 저자·철자가 맞는가 |
| venue | conference/journal 이름과 연도가 맞는가 |
| 버전 | arXiv preprint인지, peer-reviewed version인지 구분되는가 |
| key | 같은 paper가 두 key로 중복되지 않았는가 |

reference manager는 lab 관행이나 공동저자 환경에 맞춰 쓰면 된다. 다만 그것이 노트 시스템의 본체가 되면 곤란하다. PDF 파일과 annotation을 많이 모았다는 사실은 지식이 쌓였다는 뜻이 아니다. 지식은 확인한 claim과 내 작업에서 바뀐 결정으로 남는다.

100편을 넘기는 라이브러리에서도 핵심은 도구 이름이 아니다. 같은 paper가 하나의 canonical key로만 존재하고, citation metadata가 source-of-truth URL과 연결되어 있고, build 단계에서 reference 오류를 잡을 수 있으면 충분하다. reference manager는 그 조건을 만족시키는 여러 방법 중 하나다.

---

## 15.3 paper packet + AI 질의

한 편을 저장할 때의 단위는 PDF가 아니라 paper packet이다. packet에는 논문 URL, DOI/arXiv ID, PDF, code repository, project page, supplementary, OpenReview thread, dataset link가 들어간다. PDF는 그중 하나일 뿐이다. PDF 위에 표시를 남기는 일은 임시 읽기 흔적일 수는 있지만, 6개월 뒤의 재호출 단위로는 약하다.

AI 보조 도구는 세 갈래로 붙는다.

**갈래 1 — 0차 5 Cs 후보.** paper packet을 AI에 넣고 "5 Cs를 채우되 각 항목마다 근거 위치를 붙이고, 근거가 없으면 없음이라고 적어라"를 묻는다. 본인은 그 결과를 통과시키는 작업으로 1st pass를 시작한다.

**갈래 2 — reference 후보.** reference 목록과 forward citation graph를 AI에 주고 "내 thesis 키워드와 가까운 5편을 고르되, 왜 가까운지 한 줄씩 적어라"를 묻는다. 다음 입력 pipeline의 후보가 거기서 만들어진다. 후보를 고르는 일은 AI에 맡길 수 있지만, 후보를 읽을지 말지의 결정은 본인이 한다.

**갈래 3 — related work 비교표.** paper A와 paper B의 차이점을 한 표로 정리해 달라고 AI에 요청한다. 표의 칸은 방법·가정·데이터셋·metric·한계·내 작업과의 거리 정도면 충분하다. 본인이 source 위치를 확인한 후에만 그 표가 자기 글의 related work 단락의 골격이 된다.

AI가 만든 5 Cs 노트는 초안이다. 그대로 보관하지 않는다. 최종 노트에는 AI 문장을 남기는 대신, 본인이 확인한 claim과 위치를 남긴다. hallucination의 가장 위험한 형태는 그럴듯한 citation 위치다. section·table·equation 번호가 맞지 않으면 그 항목은 버린다.

---

## 15.4 검색과 재호출 — 태그보다 질문

노트는 시간이 지날수록 가치가 오르는 자료다. 그러자면 검색 가능성이 1순위에 놓인다. 2026년의 검색은 태그만으로 굴러가지 않는다. plain text, citation key, DOI/arXiv ID, embedding search, grep이 같이 작동한다. 그래서 태그 수보다 검색 가능한 문장이 더 중요하다.

태그는 최소한으로 둔다.

| 축 | 값 |
|---|---|
| 분야 | slam · cv · dl · vfm · vla |
| 모드 | skim · read · implement · cite |
| 거리 | baseline · related · rebuttal · out |

세 축의 조합으로 한 편을 분류하면, 내 thesis의 baseline 후보 SLAM 논문 5편이 한 검색으로 잡힌다. 더 세밀한 분류는 related work 비교표에서 처리한다.

정기 청소의 목적도 바뀐다. 한 달에 한 번, 30분 블록을 두고 claim ledger를 정리한다. 이번 달 노트에서 서로 충돌하는 claim, 같은 baseline을 공유하는 paper, 내 hypothesis를 바꾼 paper를 각각 한 줄씩 뽑는다. paper A·paper B 모두 가정 X에서 시작하지만 metric Y에서 갈라진다 같은 한 줄이, 본인의 thesis가 놓일 곳을 만들어 간다.

흥미로운 한 편이 노트에 박힌 채 사용되지 않으면 그 한 편이 없는 것과 같다. Whitesides가 글쓰기 관점에서 적은 한 줄 — "어떤 프로젝트도 결코 '완료'되지 않는다. 흥미롭지만 미발표인 것은 존재하지 않는 것과 같다" — 이 노트 시스템에서도 같은 명제가 된다. 읽은 것을 글로 옮기지 않으면, 읽기는 금방 사라진다.

노트 → 글쓰기로의 흐름은 단순하다. 자기 paper의 related work 한 단락은 노트에서 6편을 골라 한 표로 묶는 작업이다. 그 표가 글의 한 단락의 골격이 되고, 표의 각 칸 — 방법·가정·한계·본인 작업과의 거리 — 이 단락의 한 문장씩으로 풀려 나간다. 이 흐름은 [Part 3 ch02 (Introduction)](./chapter_23_introduction.md)·[ch03 (Related Work)](./chapter_24_related_work.md)에서 다시 쓰인다.

노트가 자료의 외장 working memory에서 자기 thesis의 글의 골격으로 옮겨간다. 6개월 동안 누적된 100편의 노트가 본인의 첫 paper의 related work 단락 한 줄 한 줄로 풀려 나가는 풍경이, 이 장이 가리킨 끝점이다.

---

**출처.** [Whitesides 2004](https://onlinelibrary.wiley.com/doi/10.1002/adma.200400767) §V (in-progress vs published — "흥미롭지만 미발표인 것은 존재하지 않는 것과 같다") — 노트 시스템의 관점 거울. Part 3 [ch02 (Introduction)](./chapter_23_introduction.md) — 노트 → 글쓰기 흐름의 출구. 5 Cs + 3 추가 칸 양식, paper packet, AI 보조 도구의 검증 원칙, claim ledger 운영은 이 장에서 정리했다.

다음: Part 1 끝. → [Part 2 — 쓰기](./chapter_16_mindset.md)
