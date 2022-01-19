from wtforms import BooleanField, FileField, SelectField, StringField, TextAreaField
from wtforms.fields.html5 import IntegerField, URLField
from wtforms.widgets.html5 import NumberInput

from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.csv import get_dumpable_tables


class ResetInstanceForm(BaseForm):
    accounts = BooleanField(
        # "Accounts",
        "계정",
        # description="Deletes all user and team accounts and their associated information",
        description="유저와 팀 계정 관련 모든 정보를 삭제합니다.",
    )
    submissions = BooleanField(
        # "Submissions",
        "제출",
        # description="Deletes all records that accounts gained points or took an action",
        description="계정이 획득한 포인트와 행동한 모든 기록을 삭제합니다.",
    )
    challenges = BooleanField(
        # "Challenges", description="Deletes all challenges and associated data"
        "문제",
        description="문제와 관련 모든 정보를 삭제합니다.",
    )
    pages = BooleanField(
        # "Pages", description="Deletes all pages and their associated files"
        "페이지",
        description="페이지와 관련 모든 정보를 삭제합니다.",
    )
    notifications = BooleanField(
        # "Notifications", description="Deletes all notifications"
        "알림",
        description="모든 알림을 삭제합니다.",
    )
    # submit = SubmitField("Reset CTF")
    submit = SubmitField("CTF 초기화")


class AccountSettingsForm(BaseForm):
    domain_whitelist = StringField(
        # "Account Email Whitelist",
        "메일 주소 화이트리스트",
        # description="Comma-seperated email domains which users can register under (e.g. ctfd.io, gmail.com, yahoo.com)",
        description="회원가입이 가능한 이메일 도메인을 설정합니다. 콤마 구분하여 여러 도메인을 입력할 수 있습니다. (e.g. ctfd.io, gmail.com, yahoo.com)",
    )
    team_creation = SelectField(
        # "Team Creation",
        "팀 생성",
        # description="Control whether users can create their own teams (Teams mode only)",
        description="팀을 유저가 직접 생성할 수 있는지 여부를 설정합니다. (Team Mode에서만 가능)",
        # choices=[("true", "Enabled"), ("false", "Disabled")],
        choices=[("true", "설정"), ("false", "해제")],
        default="true",
    )
    team_size = IntegerField(
        "팀 사이즈",
        widget=NumberInput(min=0),
        # description="Amount of users per team (Teams mode only)",
        description="팀당 팀원 수를 지정합니다. (Team Mode에서만 가능)",
    )
    num_teams = IntegerField(
        # "Total Number of Teams",
        "팀 총 개수",
        widget=NumberInput(min=0),
        # description="Max number of teams (Teams mode only)",
        description="최대 팀의 개수를 지정합니다. (Team Mode에서만 가능)",
    )
    verify_emails = SelectField(
        # "Verify Emails",
        "이메일 확인",
        # description="Control whether users must confirm their email addresses before playing",
        description="유저가 참가 전에 이메일을 통한 확인을 해야만 하는지 여부를 설정합니다.",
        # choices=[("true", "Enabled"), ("false", "Disabled")],
        choices=[("true", "설정"), ("false", "해제")],
        default="false",
    )
    team_disbanding = SelectField(
        # "Team Disbanding",
        "팀 해체",
        # description="Control whether team captains are allowed to disband their own teams",
        description="팀 대표가 자신의 팀을 해체할 수 있는지 여부를 설정합니다.",
        choices=[
            # ("inactive_only", "Enabled for Inactive Teams"),
            ("inactive_only", "팀비활성 가능 설정"),
            # ("disabled", "Disabled"),
            ("disabled", "해제"),
        ],
        default="inactive_only",
    )
    name_changes = SelectField(
        # "Name Changes",
        "이름 변경",
        # description="Control whether users and teams can change their names",
        description="유저명 또는 팀명을 변경할 수 있는지 여부를 설정합니다.",
        # choices=[("true", "Enabled"), ("false", "Disabled")],
        choices=[("true", "설정"), ("false", "해제")],
        default="true",
    )
    incorrect_submissions_per_min = IntegerField(
        # "Incorrect Submissions per Minute",
        "분당 오답 제출 허용 범위",
        widget=NumberInput(min=1),
        # description="Amount of submissions allowed per minute for flag bruteforce protection (default: 10)",
        description="브루트포스 제출을 방지하기 위한 분당 오답 제출 허용 범위를 지정합니다. (기본값 : 10)",
    )
    # submit = SubmitField("Update")
    submit = SubmitField("적용")


class ExportCSVForm(BaseForm):
    table = SelectField("Database Table", choices=get_dumpable_tables())
    submit = SubmitField("Download CSV")


class ImportCSVForm(BaseForm):
    csv_type = SelectField(
        # "CSV Type",
        "CSV 유형",
        choices=[("users", "Users"), ("teams", "Teams"), ("challenges", "Challenges")],
        # description="Type of CSV data",
        description="CSV 데이터의 유형",
    )
    # csv_file = FileField("CSV File", description="CSV file contents")
    csv_file = FileField("CSV 파일", description="CSV 파일 내용")


class LegalSettingsForm(BaseForm):
    tos_url = URLField(
        # "Terms of Service URL",
        "서비스 약관 URL",
        # description="External URL to a Terms of Service document hosted elsewhere",
        description="외부에서 호스트된 서비스 약관 URL을 링크할 수 있습니다.",
    )
    tos_text = TextAreaField(
        # "Terms of Service",
        "서비스 약관",
        # description="Text shown on the Terms of Service page",
        description="서비스 약관 페이지에 표시되는 텍스트입니다.",
    )
    privacy_url = URLField(
        # "Privacy Policy URL",
        "개인정보 보호정책 URL",
        # description="External URL to a Privacy Policy document hosted elsewhere",
        description="외부에서 호스트된 개인정보 보호정책 URL을 링크할 수 있습니다.",
    )
    privacy_text = TextAreaField(
        # "Privacy Policy",
        "개인정보 보호정책",
        # description="Text shown on the Privacy Policy page",
        description="개인정보 보호정책 페이지에 표시되는 텍스트입니다.",
    )
    # submit = SubmitField("Update")
    submit = SubmitField("적용")
