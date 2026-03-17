# src/core/pdf

ReportLab 기반 뉴스레터 PDF 생성 모듈.

---

## 파일 구조

```
src/core/pdf/
├── frame.py              # A4 페이지 레이아웃 설정
├── document.py           # PDF 문서 생성 및 빌드
├── styles.py             # 텍스트 스타일 정의
├── header_footer.py      # 페이지 고정 헤더/푸터
├── components.py         # 콘텐츠 블록 (Flowable)
└── components-guide.md   # components.py 상세 가이드
```

---

## 각 파일 역할

### frame.py — `BSSMNewsLatterFrame`

A4 페이지 크기와 여백을 설정하고 `Frame`, `PageTemplate`을 생성한다.
다른 객체에 레이아웃 정보를 제공하는 단일 책임을 가진다.

```python
layout = BSSMNewsLatterFrame()
# layout.frame         → ReportLab Frame 객체
# layout.page_template → ReportLab PageTemplate 객체
```

- 페이지 크기: A4 (595 x 842 pt)
- 여백: 72pt (사방 1인치)

---

### document.py — `NewsletterDocument`

PDF 문서 전체를 관리한다. `BSSMNewsLatterFrame`을 받아 `PageTemplate`을 등록하고,
헤더/푸터를 `onPage` 콜백으로 연결한 뒤 `build(story)`로 PDF를 생성한다.

```python
doc = NewsletterDocument(
    filename="output.pdf",
    layout=layout,           # BSSMNewsLatterFrame 객체
    title="BSSM 뉴스레터",
    issue="2026년 3월호",
    date="2026.03.17",
)
doc.build(story)
```

---

### styles.py — `NewsletterStyleSheet`

뉴스레터 전체에서 사용하는 텍스트 스타일을 한곳에서 관리한다.
`ArticleBlock` 등 콘텐츠 객체에 전달해 사용한다.

| 속성 | 용도 | 크기 |
|---|---|---|
| `styles.title` | 문서 제목 | 24pt |
| `styles.article_title` | 기사 제목 | 14pt |
| `styles.body` | 기사 본문 | 10pt |
| `styles.caption` | 이미지 캡션 | 8pt |
| `styles.notice` | 공지 박스 텍스트 | 10pt |

```python
styles = NewsletterStyleSheet()
```

---

### header_footer.py — `NewsletterHeader`, `NewsletterFooter`

매 페이지 상단/하단에 고정 출력되는 요소. `NewsletterDocument` 내부에서
`onPage` 콜백으로 자동 호출되므로 직접 사용할 필요 없다.

- `NewsletterHeader` — 좌측: 뉴스레터 제목 / 우측: 호수 + 날짜 + 구분선
- `NewsletterFooter` — 가운데: 페이지 번호 + 구분선

---

### components.py — Flowable 콘텐츠 블록

`doc.build(story)`에 넘기는 리스트의 구성 요소들.
자세한 파라미터와 예시는 [components-guide.md](./components-guide.md) 참고.

| 클래스 | 설명 |
|---|---|
| `Divider` | 기사 간 수평 구분선 |
| `ArticleBlock` | 제목 + 본문 기사 블록 |
| `ImageBlock` | 이미지 + 캡션 블록 |
| `NoticeBlock` | 배경색 공지 박스 |

---

## 전체 흐름

```
BSSMNewsLatterFrame       # 1. 레이아웃(A4) 정의
       ↓
NewsletterDocument        # 2. 문서 생성, 헤더/푸터 등록
       ↓
story = [                 # 3. 콘텐츠 구성
    NoticeBlock(...),
    Divider(),
    ArticleBlock(...),
    ImageBlock(...),
]
       ↓
doc.build(story)          # 4. PDF 출력
```

---

## 최소 사용 예시

```python
from src.core.pdf.frame import BSSMNewsLatterFrame
from src.core.pdf.document import NewsletterDocument
from src.core.pdf.styles import NewsletterStyleSheet
from src.core.pdf.components import ArticleBlock, Divider, NoticeBlock

layout = BSSMNewsLatterFrame()
styles = NewsletterStyleSheet()

doc = NewsletterDocument(
    filename="newsletter.pdf",
    layout=layout,
    title="BSSM 뉴스레터",
    issue="2026년 3월호",
    date="2026.03.17",
)

story = [
    NoticeBlock("환영합니다."),
    Divider(),
    ArticleBlock(title="기사 제목", body="기사 본문...", styles=styles),
]

doc.build(story)
```
