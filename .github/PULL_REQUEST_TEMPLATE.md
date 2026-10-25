<!--  PR 보내 주셔서 고마워요! -->

**이 PR이 하는 일 / 필요한 이유**:

**관련 이슈**:

<!--
PR이 머지되면 연결된 이슈가 자동으로 닫힙니다.
사용법: `Fixes #<이슈 번호>` 또는 `Fixes (이슈 링크)`
-->

Fixes #

**변경 종류**:
- [ ] 지침 (`INSTRUCTIONS.md` / `CLAUDE.md`)
- [ ] 템플릿 (`templates/`)
- [ ] 예시 vault (`example-vault/`)
- [ ] 도구 (`tools/`)
- [ ] 문서 (`README.md`, `docs/`)

**리뷰어에게 따로 전할 점**:

**사용자가 체감하는 변화가 있나요?**:

<!--
없으면 아래 블록에 "NONE"이라고 쓰세요.
있으면 새 명령어, 바뀐 파일 이름 규칙처럼 사용자가 알아야 할 점을 적어 주세요.
기존 vault를 손봐야 한다면 "action required"를 포함해 주세요.
-->

```release-note

```

**체크리스트**:

- [ ] `CLAUDE.md`와 `INSTRUCTIONS.md`의 규칙 부분을 똑같이 맞췄다 (지침을 바꾼 경우)
- [ ] 실제 강의자료, 교수님 슬라이드, 실제 강의를 옮긴 노트, 기출 원본을 넣지 않았다 (예시는 가상 강의로 만든다)
- [ ] `python3 tools/check_links.py example-vault` 오류 0개
- [ ] 새 명령어나 규칙이면 `README.md`·`README.ko.md` 표와 `docs/usage-examples*.md`도 갱신했다
