# STATIC

> image, css, js 파일 같이 내용이 고정되어 별도 처리없이 사용자에게 보여주는 파일

- 기본 static 경로 : **app_name/static/**

```django
<!-- Static 로드해오기 -->
{% load static %}
<img src="{% static 'static 폴더 내 경로'%}" alt="sample">
```

## STATIC_ROOT

- collectstatic이 배포를 위해 정적 파일을 **수집하는** 절대 경로
  - collectstatic : 배포 시 흩어져 있는 정적 파일을 모다 특정 디렉토리로 옮기는 작업

## STATIC_URL

- STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL

## STATICFILES_DRS

- app 내의 static 디렉토리 경로를 사용하는 것 외 추가적인 정적파일 경로 정의

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'crud' / 'static']
```



# MEDIA

> 사용자가 업로드하는 정적 파일

## MEDIA_ROOT

- 사용자가 업로드한 파일을 보관할 디렉토리의 절대 경로
- 업로드가 끝나면 어디에 파일이 저장되게 할 지 경로

## MEDIA_URL

- MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
- 업로드 된 파일의 주소 URL을 만들어주는 역할
- STATIC_URL과 다른 값을 가져야한다.

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'crud' / 'static']
# Media 루트 지정
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

개발단계에서 django.views.static.serve() view를 사용하여 MEDIA_ROOT에서 사용자가 업로드한 미디어 파일을 제공한다.

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 파일 업로드

#### 이미지 라이브러리 추가

```bash
pip install pillow
```



#### models.py 변경

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.FileField()
    # blank = 유효성 검사, 사용자가 데이터를 입력하지 않아도 무방
    # null = DB의 해당 컬럼이 null 값을 가져도 된다.
    image = models.ImageField(blank=True, null=True)
```

#### form 준비

```html
<form action="" method="POST" enctype="multipart/form-data">
    ...
</form>
```

#### views.py 변경

```python
#변수명 = 폼클래스(request.POST) 에서
# request.FILES 추가
변수명 = 폼클래스(request.POST, request.FILES)
변수명 = 폼클래스(request.POST, request.FILES, instance=인스턴스)
```



### 업로드 시 폴더 구분 방법

FileField 혹은 ImageField에 `*upload_to*='%Y/%m/%d/'` 를 추가해준다

```python
  image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
```



### 무작정 업로드가 아닌 서버를 위한 업로드

#### 썸네일 형태로 이미지 조작해서 업로드

#### 라이브러리 다운로드

```bash
pip install pilkit
pip install django-imagekit
```

#### settings.py 에 추가

```python
INSTALLED_APPS = [
    'imagekit',
    ...
]
```

#### models.py 변경

```python
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.db import models
class 모델클래스(models.Model):
    ...
    image = ProcessedImageField(
        blank = True,
        # 어떻게 처리할 것인가>
        # Thumbnatil(x축px, y축px)
        processors = [Thumbnail(200, 300)],
        # 형식
        format='JPEG',
        options={'quality' : 90}
    )

```



