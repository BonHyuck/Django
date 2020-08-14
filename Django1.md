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
        path('index/', views.index)
        path('url명', url 경로)
    ]
    ```

#### Variable Routing

```django
urlpatterns = [
 	...
    path('url명/<받을 값의 타입:변수명>', url 경로)
    path('hello/<str:name>', views.hello)
]    
```



## View

- 앱 내 `view.py` 로 이동한다.

- 함수를 생성하는 방식으로 **무조건 함수의 첫 인자는 `request` 이다**

  - ```python
  def 함수이름(request, 다른 인자):
        return render(request, 'html 파일 이름', template에 전달할 Dictionary)
    ```
  
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
  
  - ```python
    def hello(request, name):
        ...
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



### Django Conventions

- **`trailing comma`** :
  - 목록을 작성할 때 맨 마지막 요소의 뒤에도 쉼표를 붙여, 다음 번에 요소를 추가하기 쉽도록 하는 컨벤션이 있다!
- **app 목록 작성 `[settings.py](http://settings.py)` > `INSTALLED APPS`**
  1. local apps
  2. 3rd party apps
  3. django default apps
- **view 목록 작성 `[views.py](http://views.py)`**
  - 각 view 간에는 두 줄 띄어쓰기
- **django imports style guide**
  1. standard library
  2. 3rd party library
  3. Django : 장고 내장 모듈
  4. local django : 직접 생성, 혹은 다른 뷰에서 가져오는 모듈



## DTL : Django Template Language

> Django Template System 에서 사용하는 built-in template system이다.

- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공
- 프로그래밍적 로직(view에서 작성)이 아니라 프레젠테이션을 **표현**하기 위한 것
- 파이썬처럼 if, for를 사용할 수 있지만 **python code로 실행되는 것은 아니다**

### Syntax : 공식문서 확인하기

- **Variable** : `{{variable}}`

- **Filter** : `{{variable|filter}}`

- **Tags** : `{% tag %}`

  - ```html
    <!-- for -->
    {% for some in something %}
    	{{ some }}
    {% endfor%}
    <!-- 1부터 번호 붙이기 -->
    {% for some in something %}
    	{{ forloop.counter }} : {{ menu }}
    {% endfor%}
    <!-- 비어 있을 경우 -->
    {% for empty in empty_list %}
    	{{ empty }}
    {% empty %}
    	<p>아무것도 없습니다.</p>
    {% endfor %}
    ```

  - ```html
    <!-- if -->
    {% if 'some' in something %}
    	<p>True</p>
    {% endif %}
    <!-- 필터 적용 -->
    {% if some_list|length > 10 %}
    	<p>크다</p>
    {% else %}
    	<p>작다</p>
    {% endif %}
    ```



### 템플릿 시스템 설계 철학

장고에게 템플릿 시스템이란 **표현을 제어하는 도구이자 표현에 관련된 로직일 뿐**이라고 생각한다. 이를 넘어서는 기능을 지원해서는 안된다.

