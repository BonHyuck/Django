# Django

## 여러개의 어플리케이션 관리

**url을 분리를 하여 다수의 어플리케이션으로 관리하는 것이 중요하다**



각 어플리케이션(App) 폴더 내 `urls.py` 생성

- Django에선 따로 파일을 만들어 주지 않는다.

기존의 양식과 똑같이 작성한다.

#### 어플리케이션/urls.py

```django
from django.urls import path
# . 은 현재 위치를 의미한다.
from . import views

urlpatterns = [
	path('어플리케이션 내 경로', views.이름, name='내가 지어주는 이름'),
    path('index/', views.index, name='index'),
]
```

- 다른 어플리케이션에 같은 이름이 있을 수 있다.
  - 그렇기 때문에 `app_name`을 추가해준다

```django
from django.urls import path
# . 은 현재 위치를 의미한다.
from . import views

app_name = '어플리케이션 이름'
urlpatterns = [
	path('어플리케이션 내 경로', views.이름, name='내가 지어주는 이름'),
    path('index/', views.index, name='index'),
]
```



프로젝트 폴더의 `urls.py`도 수정이 필요하다

#### urls.py

```django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('어플리케이션 명(경로)/', include('해당 어플리케이션의 urls')),
    path('articles/', include('articles.urls'))
    path('pages/', include('pages.urls'))
]
```



#### HTML

url을 지정해줄땐 `{% url '내가 정해준 이름' %}` 으로 설정한다.

```html
<a href='{% url 'index' %}'></a>
```

기존의 template 폴더 내 어플리케이션 이름의 폴더를 만들어서 해당 폴더 내에 모든 html 파일을 넣는다

만일 다른 어플리케이션에서 같은 이름을 쓰면 `app_name` 설정 이후 `{% url '어플리케이션 명:지정된 이름' %}` 으로 설정한다.

```html
<a href='{% url 'articles:index' %}'></a>
```



## 공용 Template 만들기

여러 HTML 파일이 공유하는 코드가 있을 것이다.(ex. 부트스트랩, 메뉴바). 매번 복사, 붙여넣기로 진행할 수는 없으니 여러 파일이 공유하는 코드를 하나의 파일로 만들어서 지정한다.

1. **프로젝트 폴더** 내 template 폴더를 생성한다.
2. html 파일 생성을 하고 파일 내 공유할 코드를 아래와 같이 작성한다.

```html
{% block 이름 %}
  공유할 코드
{% endblock %}
{% block content %}
<p>
    something
</p>
{% endblock %}
{% block title %}<title>Document</title>{% endblock %}
```

3. settings.py > TEMPLATES > APP_DIRS 확인

```json
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'프로젝트 이름'/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



설정을 원하는 HTML 파일로 이동하여

```django
{% extends 'base.html' %}
{% block 블록이름 %}
  대체할 내용
{% endblock %}
{% block content %}
  <h1>index 페이지입니다.</h1>
{% endblock %}
```





