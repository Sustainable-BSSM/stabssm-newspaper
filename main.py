from src.core.pdf.components import ArticleBlock, Divider, ImageBlock, NoticeBlock
from src.core.pdf.document import NewsletterDocument
from src.core.pdf.frame import BSSMNewsLatterFrame
from src.core.pdf.styles import NewsletterStyleSheet

if __name__ == "__main__":
    layout = BSSMNewsLatterFrame()
    styles = NewsletterStyleSheet()

    doc = NewsletterDocument(
        filename="newsletter_2026_03.pdf",
        layout=layout,
        title="BSSM 뉴스레터",
        issue="2026년 3월호",
        date="2026.03.17",
    )

    story = [
        NoticeBlock("2026년 3월호 BSSM 뉴스레터에 오신 것을 환영합니다."),
        Divider(),
        ArticleBlock(
            title="1학기 안내",
            body="2026년 3월 2일부터 1학기 수업이 시작됩니다. 수업 시간표는 학교 홈페이지를 확인해 주세요.",
            styles=styles,
        ),
        Divider(),
        ArticleBlock(
            title="동아리 모집",
            body="올해도 다양한 동아리가 신입 부원을 모집합니다. 관심 있는 학생은 각 동아리 부스를 방문해 주세요.",
            styles=styles,
        ),
    ]

    doc.build(story)
    print("PDF 생성 완료: newsletter_2026_03.pdf")
