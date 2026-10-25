# university_is_dead 🎓

[English](README.md) | **한국어**

**Claude + Obsidian으로 강의를 공부하는 지침서와 노트 양식.**
강의 PDF를 넣고 `운체 3`, `다음`, `시험 정리본` 같은 짧은 명령어로 슬라이드 순서대로 깊게 설명 듣고, 필기 골격·시험 정리본·ELI5 그림책까지 만듭니다.

---

## 무엇을 할 수 있나

| 말하면 | 이렇게 됩니다 |
|---|---|
| `운체 3` | 3장을 핵심 질문 단위 그룹으로 나눈 지도를 보여 주고 그룹 1을 설명 |
| `운체 3-2` / `다음` | 그룹 하나만 슬라이드 순서대로, 수식·숫자 예시·셀프 체크 질문까지 |
| "골격 만들어줘" + PDF | `## 대제목 / ### Slide Title (한글) / - ` 형식의 빈 필기 노트 |
| "정리해줘" | 내 필기는 보존하고 빈 곳만 PDF 기준으로 채운 완성 노트 |
| "시험 정리본" | ★ 중요도, 비교 표, 연습문제 + 채점 기준, 시험 포인트 Q&A |
| `/eli5 {노트}` | 비유와 강의 정의를 구분한 HTML 그림책 |
| "저장해줘" / `운체 3 전부` | 그룹 설명을 `클코 설명/` 노트로 저장. 처음부터 끝까지 `다음 →` 링크로 이어짐 |
| "기출 분석" + 기출·시험 후기 | 연도별 문제 표, 빈출 주제, 우선순위를 `클코 정리/기출 분석.md`로 |
| (과목 예외에 `증명 과목`) | 정리마다 답안용 증명 템플릿, 역과 조건 표, 기출 형식 모의고사 |

## 5분 시작 가이드

1. 이 레포를 받습니다. GitHub에서 **Use this template** 또는 Code → Download ZIP.
2. `example-vault/`를 참고해 내 Obsidian vault에 과목 폴더를 만듭니다. 학기별 폴더 안에 두어도 되고, 그때는 과목 표에 그 경로까지 적습니다.
   ```
   (vault 루트)/
   ├── CLAUDE.md          ← Claude Code를 쓸 때 (4단계)
   ├── templates/         ← 이 레포의 templates/ 복사
   ├── tools/             ← 이 레포의 tools/ 복사
   └── {과목}/
       ├── 강의자료/        ← 교수님 PDF (읽기 전용)
       ├── {강의자료 제목}.md  ← 주차별 필기
       ├── 개념.md          ← 개념 허브 + 주차별 필기 표
       ├── 클코 정리/       ← 시험 정리본, 기출 분석
       ├── 클코 설명/       ← 그룹 설명 저장본
       └── 학습자료/        ← ELI5 HTML
   ```
   강의자료 PDF 이름은 필기 노트 이름과 같게 둡니다(`1주차 정렬 기초.md` ↔ `강의자료/1주차 정렬 기초.pdf`). 그래야 PDF 페이지 링크가 이어집니다.
3. `INSTRUCTIONS.md`를 열어 **"📝 여기만 고치세요"** 블록에 학교·과목·줄임말을 적습니다. 과목 폴더는 vault 루트 기준 경로로 적습니다(예: `딥러닝/`).
4. 지침을 Claude에 넣습니다.
   - **Claude Projects**: 내용을 프로젝트 지침(Project instructions) 칸에 붙여 넣고, 과목 폴더와 `templates/` 파일을 자료로 올립니다.
   - **Claude Code**: 같은 수정을 `CLAUDE.md`에 하고, `CLAUDE.md`·`templates/`·`tools/`를 vault 루트에 복사한 뒤 그 폴더에서 실행합니다. 링크 검사기에는 Python 3.8 이상이 필요합니다.
5. `{줄임말} 1`이라고 말해 봅니다.

## 레포 구성

| 경로 | 내용 |
|---|---|
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | 프로젝트 지침 원본 (Claude Projects용) |
| [`CLAUDE.md`](CLAUDE.md) | 같은 지침 (Claude Code용) |
| [`templates/`](templates) | 필기 골격, 개념.md, 시험 정리본, 클코 설명, 기출 분석, ELI5 HTML 빈 양식 |
| [`tools/check_links.py`](tools/check_links.py) | Obsidian 링크 검사기 (없는 노트·헤딩·첨부를 찾음) |
| [`example-vault/알고리즘/`](example-vault/알고리즘) | 가상 과목으로 채운 예시. Obsidian으로 열어 보세요 |
| [`docs/usage-examples.ko.md`](docs/usage-examples.ko.md) | 명령어별 대화 흐름 |
| [`docs/FAQ.ko.md`](docs/FAQ.ko.md) | 자주 묻는 질문 |

## 핵심 원칙

- **강의자료가 기준.** 슬라이드에 없는 내용은 "교재 보충"으로 표시합니다.
- **내 필기는 덮어쓰지 않음.** 보강만 최소한으로.
- **슬라이드 순서 그대로.** 그룹을 섞지 않고, 부록은 따로.
- **빈약하게 쓰지 않음.** 동기 → 직관 → 정의/수식 → 숫자 예시 → 한계 순서로.

## ⚠️ 강의자료는 올리지 마세요

교수님 강의자료와 강의 내용을 옮긴 노트는 저작물입니다. 내 vault를 GitHub에 백업한다면 이 레포의 [`.gitignore`](.gitignore)를 함께 쓰고, 공개 레포에는 올리지 마세요. 이 레포의 예시는 모두 새로 만든 가상 강의입니다.

## 기여하기

새 명령어, 과목 유형별 규칙, 템플릿 개선 모두 환영해요. [`CONTRIBUTING.md`](CONTRIBUTING.md)를 읽고 이슈 템플릿(Bug Report / Enhancement Request / Common Issue)으로 이슈를 연 뒤 PR을 보내 주세요. PR마다 지침 파일 동기화, 예시 vault 링크, 강의자료 업로드 여부를 자동으로 검사합니다.

## License

[MIT](LICENSE)
