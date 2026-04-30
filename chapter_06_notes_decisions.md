# Ch.6 — 노트는 기억 창고가 아니라 다음 결정을 남기는 장치다

논문을 언제든 다시 열어 요약할 수 있는 시대에는 긴 노트의 가치가 줄어든다. 6개월 후 필요한 것은 밑줄의 색이나 요약 문단의 길이가 아니라, 내가 왜 이 논문을 남겼는가다. 노트는 기억 창고가 아니라 다음 결정을 위한 장치다. 다시 돌아왔을 때 이 논문이 baseline인지, related work인지, 반박 대상인지, 아니면 버려도 되는지 바로 알 수 있어야 한다.

한 편의 노트에는 5 Cs 위에 세 칸만 더 붙이면 충분하다. 첫째, claim과 근거 위치. 직접 인용할 문장이 있을 때만 짧은 원문을 남기고, 대부분은 내 말로 쓴 claim과 page, section, figure, table, equation 번호를 남긴다. 둘째, 내 작업과의 거리. 이 논문이 내 thesis의 어디에 붙는지 적는다. 셋째, 다음 액션. 중단, 보류, 진행 중 무엇인지와 다시 볼 시점을 남긴다.

reference manager는 본체가 아니다. DOI, arXiv, OpenReview, venue page, publisher page가 source of truth이고, manager는 그 정보를 논문 양식에 맞게 내보내는 호환 계층이다. 손으로 BibTeX를 typing할 필요는 없지만, 자동 생성된 metadata도 한 번은 본인이 통과해야 한다. DOI가 맞는가. 저자 철자가 맞는가. peer-reviewed version인지 preprint인지 구분되는가. 같은 paper가 두 key로 중복되지 않았는가.

한 편을 저장할 때의 단위는 PDF가 아니라 paper packet이다. packet에는 논문 URL, DOI/arXiv ID, PDF, code repository, project page, supplementary, OpenReview thread, dataset link가 들어간다. PDF는 그중 하나일 뿐이다. PDF 위 표시를 남기는 일은 임시 읽기 흔적일 수 있지만, 재호출의 단위로는 약하다.

모델은 paper packet 위에서 작동한다. “5 Cs를 채우되 각 항목마다 근거 위치를 붙이고, 근거가 없으면 없음이라고 적어라.” “내 thesis keyword와 가까운 reference 후보 5편을 고르되 왜 가까운지 한 줄씩 적어라.” “paper A와 B의 방법, 가정, dataset, metric, 한계를 표로 비교하라.” 이렇게 물어야 한다. 그리고 최종 노트에는 도구의 문장이 아니라 내가 확인한 claim과 위치만 남긴다.

검색은 tag만으로 굴러가지 않는다. plain text, citation key, DOI/arXiv ID, embedding search, grep이 함께 작동한다. tag를 많이 다는 것보다 검색 가능한 문장으로 쓰는 편이 낫다. 한 달에 한 번 정리할 것도 highlight가 아니라 claim ledger다. 서로 충돌하는 claim, 같은 baseline을 공유하는 paper, 내 hypothesis를 바꾼 paper를 한 줄씩 뽑는다.

노트가 좋은지 판단하는 기준은 간단하다. 6개월 후의 내가 paper를 다시 열기 전에 다음 행동을 알 수 있는가. 알 수 있다면 좋은 노트다. 알 수 없다면 아무리 길어도 보관된 텍스트일 뿐이다.
