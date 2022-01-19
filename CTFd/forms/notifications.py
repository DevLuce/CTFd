from wtforms import BooleanField, RadioField, StringField, TextAreaField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField


class NotificationForm(BaseForm):
    # title = StringField("Title", description="Notification title")
    title = StringField("제목", description="알림 제목")
    content = TextAreaField(
        # "Content",
        "내용",
        # description="Notification contents. Can consist of HTML and/or Markdown.",
        description="알림을 발송할 내용을 입력합니다. HTML 혹은 Markdown 형식으로 구성할 수 있습니다.",
    )
    type = RadioField(
        # "Notification Type",
        "알림 형식",
        choices=[("toast", "Toast"), ("alert", "Alert"), ("background", "Background")],
        default="toast",
        # description="What type of notification users receive",
        description="유저가 받을 알림 형식을 선택하세요.",
        validators=[InputRequired()],
    )
    sound = BooleanField(
        # "Play Sound",
        "소리 재생",
        default=True,
        # description="Play sound for users when they receive the notification",
        description="유저가 알림을 받으면 소리를 재생합니다.",
    )
    # submit = SubmitField("Submit")
    submit = SubmitField("적용")
