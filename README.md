# ![](https://github.com/CTFd/CTFd/blob/master/CTFd/themes/core/static/img/logo.png?raw=true)

![CTFd MySQL CI](https://github.com/CTFd/CTFd/workflows/CTFd%20MySQL%20CI/badge.svg?branch=master)
![Linting](https://github.com/CTFd/CTFd/workflows/Linting/badge.svg?branch=master)
[![MajorLeagueCyber Discourse](https://img.shields.io/discourse/status?server=https%3A%2F%2Fcommunity.majorleaguecyber.org%2F)](https://community.majorleaguecyber.org/)
[![Documentation Status](https://api.netlify.com/api/v1/badges/6d10883a-77bb-45c1-a003-22ce1284190e/deploy-status)](https://docs.ctfd.io)

## What is CTFd?

<!-- CTFd is a Capture The Flag framework focusing on ease of use and customizability. It comes with everything you need to run a CTF and it's easy to customize with plugins and themes. -->

CTFd 는 쉽게 사용할 수 있으며 커스터마이징이 가능한 해킹 방어 대회(Capture The Flag) 프레임워크입니다. CTF 를 주최하는데 필요한 모든 것이 제공되며 플러그인과 테마를 사용하여 쉽게 커스터마이징을 할 수 있습니다.  

![CTFd is a CTF in a can.](https://github.com/CTFd/CTFd/blob/master/CTFd/themes/core/static/img/scoreboard.png?raw=true)

## What is CTFd-Korean?

CTFd-Korean 은 Apache License 2.0에 의거하여 [CTFd](https://github.com/CTFd/CTFd) 오픈소스를 한국어 버전으로 수정하여 재배포한 것입니다. CTFd-Korean 을 통해 한국어 사용자 환경에서 CTFd 플랫폼을 이용할 수 있습니다.     
본 소스코드 또한 Apache License 2.0 을 따르며 누구나 수정 및 재배포를 할 수 있습니다. 

## Features

<!-- - Create your own challenges, categories, hints, and flags from the Admin Interface -->
- 관리자 인터페이스 내에서 문제, 카테고리, 힌트, 플래그를 생성할 수 있습니다.
  <!-- - Dynamic Scoring Challenges -->
  - 해결 횟수가 많아질 수록 획득 점수가 하락하는 문제 생성 가능
  <!-- - Unlockable challenge support -->
  - 문제 잠금 해제 기능 지원
  <!-- - Challenge plugin architecture to create your own custom challenges -->
  - 커스텀 문제를 출제할 수 있는 플러그인 아키텍쳐 지원
  <!-- - Static & Regex based flags -->
  - Static & Regex 기반 플래그
    <!-- - Custom flag plugins -->
    - 커스텀 플래그 플러그인
  <!-- - Unlockable hints -->
  - 잠금 해제 가능한 힌트 기능
  <!-- - File uploads to the server or an Amazon S3-compatible backend -->
  - 서버 혹은 AWS S3 호환 백엔드 파일 업로드
  <!-- - Limit challenge attempts & hide challenges -->
  - 문제 시도 제한 & 문제 숨김 기능
  <!-- - Automatic bruteforce protection -->
  - 브루트포스 제출 방지 기능
<!-- - Individual and Team based competitions -->
- 개인 및 팀 기반 경시
  <!-- - Have users play on their own or form teams to play together -->
  - 유저는 개인 혹은 팀으로 참여할 수 있음
<!-- - Scoreboard with automatic tie resolution -->
- 스코어보드에 자동 연동
  <!-- - Hide Scores from the public -->
  - 점수 비공개 기능
  <!-- - Freeze Scores at a specific time -->
  - 특정 시간대에 점수를 고정할 수 있는 프리징 기능
<!-- - Scoregraphs comparing the top 10 teams and team progress graphs -->
- 상위 10개 팀과 팀 진행 사항을 비교할 수 있는 그래프 제공
<!-- - Markdown content management system -->
- Markdown 컨텐츠 관리 시스템
<!-- - SMTP + Mailgun email support -->
- SMTP + Mailgun 이메일 지원
  <!-- - Email confirmation support -->
  - 이메일 확인 기능 지원
  <!-- - Forgot password support -->
  - 비밀번호 찾기 지원
<!-- - Automatic competition starting and ending -->
- 자동 경시 시작 및 종료
<!-- - Team management, hiding, and banning -->
- 팀 관리, 숨김, 벤 기능
<!-- - Customize everything using the [plugin](https://docs.ctfd.io/docs/plugins/overview) and [theme](https://docs.ctfd.io/docs/themes/overview) interfaces -->
- [플러그인](https://docs.ctfd.io/docs/plugins/overview) 과 [테마](https://docs.ctfd.io/docs/themes/overview) 인터페이스를 사용하여 커스터마이징할 수 있습니다.
<!-- - Importing and Exporting of CTF data for archival -->
- 데이터 보관 및 이전을 위한 CTF 데이터 불러오기 및 추출하기 기능
- And a lot more...

## Install

1. Install dependencies: `pip install -r requirements.txt`
   1. You can also use the `prepare.sh` script to install system dependencies using apt.
2. Modify [CTFd/config.ini](https://github.com/CTFd/CTFd/blob/master/CTFd/config.ini) to your liking.
3. Use `python serve.py` or `flask run` in a terminal to drop into debug mode.

You can use the auto-generated Docker images with the following command:

`docker run -p 8000:8000 -it ctfd/ctfd`

Or you can use Docker Compose with the following command from the source repository:

`docker-compose up`

Check out the [CTFd docs](https://docs.ctfd.io/) for [deployment options](https://docs.ctfd.io/docs/deployment/installation) and the [Getting Started](https://docs.ctfd.io/tutorials/getting-started/) guide

## Live Demo

https://demo.ctfd.io/

## Support

To get basic support, you can join the [MajorLeagueCyber Community](https://community.majorleaguecyber.org/): [![MajorLeagueCyber Discourse](https://img.shields.io/discourse/status?server=https%3A%2F%2Fcommunity.majorleaguecyber.org%2F)](https://community.majorleaguecyber.org/)

If you prefer commercial support or have a special project, feel free to [contact us](https://ctfd.io/contact/).

## Managed Hosting

Looking to use CTFd but don't want to deal with managing infrastructure? Check out [the CTFd website](https://ctfd.io/) for managed CTFd deployments.

## MajorLeagueCyber

CTFd is heavily integrated with [MajorLeagueCyber](https://majorleaguecyber.org/). MajorLeagueCyber (MLC) is a CTF stats tracker that provides event scheduling, team tracking, and single sign on for events.

By registering your CTF event with MajorLeagueCyber users can automatically login, track their individual and team scores, submit writeups, and get notifications of important events.

To integrate with MajorLeagueCyber, simply register an account, create an event, and install the client ID and client secret in the relevant portion in `CTFd/config.py` or in the admin panel:

```python
OAUTH_CLIENT_ID = None
OAUTH_CLIENT_SECRET = None
```

## Credits

- Logo by [Laura Barbera](http://www.laurabb.com/)
- Theme by [Christopher Thompson](https://github.com/breadchris)
- Notification Sound by [Terrence Martin](https://soundcloud.com/tj-martin-composer)
