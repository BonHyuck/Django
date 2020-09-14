# Django

## 가상 환경

- 파이썬 인터프리터, 라이브러리, 스크립트가 "시스템 파이썬"에 설치된 모든 라이브러리와 격리된 파이썬 환경
- 각 가상환경은 고유한 파이썬 환경을 가지며 독립적으로 설치된 패키지를 가짐
- 가상환경 지원 시스템
  - **venv**, virtualenv, conda, pyenv

### 왜 사용하는가?

- pip로 설치된 패키지는 모든 파이썬 스크립트에서 사용할 수 있다.
- 만일 다른 버전의 라이브러리가 필요하다면 제한이 있다.
- 라이브러리나 모듈의 의존성 때문에 충돌이 발생하거나 문제가 생길수 있다.



### 가상 환경 만들기

**`python -m venv 가상환경이름`**

#### 활성화

`source 가상환경이름\Scripts\activate`

- 가상 환경의 이름이 출력돼야 활성화 성공

#### 비활성화

`deactivate`

- 가상 환경의 이름이 사라짐



## 앞으로 모든 개발은 가상환경에서 실행

- 가상환경 생성
- VS code - interpreter 선택
- Terminal



### 패키지 관리

- pip freeze
  - 현재 환경에 설치된 패키지를 요구사항 포맷으로 출력

1. 패키지 요구사항 파일 생성
   - pip freeze > requirements.txt
2. 패키지 요구사항 설치
   - pip install -r requirements.txt



---

## Fixtures

> Django가 데이터베이스로 import 할 수 있는 데이터 모음

- dumpdata
  - 특정 앱의 관련된 데이터베이스의 모든 데이터를 출력
  - `python manage.py dumpdata 앱 이름.모델클래스 --옵션 > 파일명`
- loaddata
  - dumpdata를 통해 만들어진 fixtures 파일을 데이터베이스에 import
  - **fixtures 파일은 반드시 app 디렉토리 안에 fixtures 디렉토리에 있어야한다**
  - `python manage.py loaddata 경로`





