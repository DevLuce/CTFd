from wtforms import (
    BooleanField,
    HiddenField,
    MultipleFileField,
    SelectField,
    StringField,
    TextAreaField,
)
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm


class PageEditForm(BaseForm):
    title = StringField(
        # "Title", description="This is the title shown on the navigation bar"
        "제목",
        description="네비게이션바에 표시되는 제목입니다.",
    )
    route = StringField(
        # "Route",
        "경로",
        description="(예: /page)와 같이 페이지가 라우팅 될 경로입니다. 링크를 입력하여 해당 페이지에 연결할 수도 있습니다.",
    )
    # draft = BooleanField("Draft")
    draft = BooleanField("초안 작성")
    # hidden = BooleanField("Hidden")
    hidden = BooleanField("숨김")
    # auth_required = BooleanField("Authentication Required")
    auth_required = BooleanField("로그인(인증) 필요")
    # content = TextAreaField("Content")
    content = TextAreaField("내용")
    format = SelectField(
        # "Format",
        "형식",
        # choices=[("markdown", "Markdown"), ("html", "HTML")],
        choices=[("markdown", "마크다운"), ("html", "HTML")],
        default="markdown",
        validators=[InputRequired()],
        # description="The markup format used to render the page",
        description="페이지 렌더링에 사용되는 마크업 방식",
    )


class PageFilesUploadForm(BaseForm):
    file = MultipleFileField(
        # "Upload Files",
        "파일 업로드",
        # description="Attach multiple files using Control+Click or Cmd+Click.",
        description="Control+Click 또는 Cmd+Click 을 사용하여 여러 파일을 첨부할 수 있습니다.",
        validators=[InputRequired()],
    )
    # type = HiddenField("Page Type", default="page", validators=[InputRequired()])
    type = HiddenField("페이지 형식", default="page", validators=[InputRequired()])
