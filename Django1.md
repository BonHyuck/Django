# Django

Static Web : HTML, CSS, 약간의 JS를 활용한 **정적인** 웹사이트

Django는 Spotify, Instagram, Dropbox, Delivery Hero 등에 쓰였다.

## 웹 프로토콜

클라이언트가 **요청(request)**를 보내면 서버에서 **응답(response)**를 보낸다



**Django는 파이썬으로 작성된 오픈소스 웹 어플리케이션 프레임워크로, 모델-뷰-컨트롤러 모델 패턴을 따른다.**

## MVC 패턴

| MVC        | django   |    |
| ---------- | -------- | -------- |
| Model      | Model    |데이터 관리 |
| View       | Template |인터페이스(화면) |
| Controller | View     |중간관리(상호동작) |

![Django - MTV 패턴](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F224E483557C7D2A52E)

1. Request를 보낸다.
2. URL를 통해 View로 보내진다.
3. View 가 Template에서 정보를 가져온다.
4. Response로 클라이언트에 보여진다.



## Setting

**VS Code**

- Django Extension 다운로드

- Preference: Open Setting(JSON) 으로 들어가기

- ```json
  "files.associations": {
          "**/*.html": "html",
          "**/templates/**/*.html": "django-html",
          "**/templates/**/*": "django-txt",
          "**/requirements{/**,*}.{txt,in}": "pip-requirements"
      },
      "emmet.includeLanguages": {"django-html": "html"}
  ```

- `pip install django` 로 django 설치

- `django-admin startproject 프로젝트명` 으로 django 프로젝트 시작

  - `-` (하이픈) 사용 금지
  - python 혹은 django에서 기본적으로 쓰는 이름 사용 금지

- 새로 생성된 폴더 내부로 들어가서 `python manage.py runserver` 

- `python manage.py startapp 앱 이름` 으로 앱 생성

  - **등록보다 먼저 수행해야 함**

- **`settings.py` 로 이동**

  - ```python
    INSTALLED_APPS = [
        # 여기에 추가 
        'articles',
    	...	   				
    ]
    ```

  - 1. local apps
    2. 3rd party apps
    3. django apps

- **`url.py`로 이동**

  - ```python
    from 앱이름 import views(동작할 View)
    urlpatterns = [
     	...
        path('url명', url 경로)
        path('index/', )
    ]
    ```



## View

- 앱 내 `view.py` 로 이동한다.

- 함수를 생성하는 방식으로 **무조건 함수의 첫 인자는 `request` 이다**

  - ```python
    def index(request):
        pass
    ```

  - ```python
    def dinner(request):
        menus = ['족발', '햄버거', '치킨', '초밥']
        pick = random.choice(menus)
        return render(request, 'dinner.html', {'pick': pick,})
    ```

  - View 에서 Template으로 내용을 전달할 땐 Dictionary 형태로 전달



## Templates

- 앱 폴더 내 **templates** 라는 폴더 생성

  - 해당 **templates** 폴더 안에 HTML 작성

- View에서 전달받은 변수는 **중괄호 2개**로 감싸줘서 사용한다.

  - ```python
    <h1>오늘 저녁은 {{pick}} 입니다.</h1>
    ```



## 코드 작성 순서

1. urls.py
2. view.py
3. templates



#### Django imports Style Guide

1. Standard library
2. 3rd Party
3. Django
4. Local django