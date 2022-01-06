from wtforms import (
    FileField,
    HiddenField,
    PasswordField,
    RadioField,
    SelectField,
    StringField,
    TextAreaField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.constants.themes import DEFAULT_THEME
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.config import get_themes


class SetupForm(BaseForm):
    ctf_name = StringField(
        # "Event Name", description="The name of your CTF event/workshop"
        "이벤트명",
        description="CTF 이벤트/워크샵의 이름을 지정합니다.",
    )
    ctf_description = TextAreaField(
        # "Event Description", description="Description for the CTF"
        "이벤트 설명",
        description="본 CTF에 대해 설명해주세요.(옵션)",
    )
    user_mode = RadioField(
        # "User Mode",
        "참가 모드",
        choices=[("teams", "Team Mode"), ("users", "User Mode")],
        default="teams",
        # description="Controls whether users join together in teams to play (Team Mode) or play as themselves (User Mode)",
        description="참가자가 팀에 참가하여 진행하는지(Team Mode), 개인으로 참가하여 진행하는지(User Mode) 여부를 선택합니다.",
        validators=[InputRequired()],
    )

    name = StringField(
        # "Admin Username",
        "관리자 아이디",
        # description="Your username for the administration account",
        description="관리자 계정의 아이디를 입력해주세요.",
        validators=[InputRequired()],
    )
    email = EmailField(
        # "Admin Email",
        "관리자 이메일",
        # description="Your email address for the administration account",
        description="관리자 계정의 이메일을 입력해주세요.",
        validators=[InputRequired()],
    )
    password = PasswordField(
        # "Admin Password",
        "관리자 비밀번호",
        # description="Your password for the administration account",
        description="관리자 계정의 비밀번호를 입력해주세요.",
        validators=[InputRequired()],
    )

    ctf_logo = FileField(
        # "Logo",
        "로고",
        # description="Logo to use for the website instead of a CTF name. Used as the home page button.",
        description="이벤트명 대신 사용할 로고입니다. 홈페이지 이동 버튼으로 사용됩니다.",
    )
    # ctf_banner = FileField("Banner", description="Banner to use for the homepage.")
    ctf_banner = FileField("배너", description="홈페이지 상단 배너 이미지입니다.")
    ctf_small_icon = FileField(
        # "Small Icon",
        "아이콘",
        # description="favicon used in user's browsers. Only PNGs accepted. Must be 32x32px.",
        description="브라우저에 표시되는 favicon 입니다. 오직 PNG 파일만 허용됩니다. 32x32px 파일을 업로드해주세요.",
    )
    ctf_theme = SelectField(
        # "Theme",
        "테마",
        # description="CTFd Theme to use",
        description="커스텀 테마를 선택할 수 있습니다.",
        choices=list(zip(get_themes(), get_themes())),
        default=DEFAULT_THEME,
        validators=[InputRequired()],
    )
    theme_color = HiddenField(
        # "Theme Color",
        "테마 색상",
        # description="Color used by theme to control aesthetics. Requires theme support. Optional.",
        description="테마별로 적용되는 색상입니다. 해당 테마의 지원이 요구됩니다.(옵션)",
    )

    start = StringField(
        # "Start Time", description="Time when your CTF is scheduled to start. Optional."
        "시작 시간",
        description="CTF의 시작 시간입니다. (옵션)",
    )
    end = StringField(
        # "End Time", description="Time when your CTF is scheduled to end. Optional."
        "종료 시간",
        description="CTF의 종료 시간입니다. (옵션)",
    )
    # submit = SubmitField("Finish")
    submit = SubmitField("완료")
