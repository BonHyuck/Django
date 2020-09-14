# Django

## 관리자 계정 만들기

```bash
$ python manage.py createsuperuser
```



## 앱 내 admin.py

```python
from django.contrib import admin
from .models import 모델 내 클래스명

# Register your models here.
# 관리자에 등록하기
admin.site.register(모델 내 클래스명)
```



## views.py

위와 동일하게 View 내에서 사용할 수 있게끔 import를 해줘야한다.

```python
from django.shortcuts import render
from .models import 클래스명

def something(request):
    pass
```



## csrf_token

POST 방식으로 데이터를 전송할 때 `{% csrf_token %}` 를 form 태그 안에 넣어야 한다.

내부적 처리가 아닌 외부의 접근을 차단한다.



## POST 데이터 전송 이후 처리

POST 방식의 데이터 처리 이후 해당 함수는 html을 출력할 필요가 없다.

django.shortcuts 내에 redirect 가 있다.

```python
from django.shortcuts import render, redirect
def something(request):
    ...
    do something
	...
    return redirect('앱 이름:url 별명')
	# 이렇게 해당 url의 함수를 실행시켜 그쪽으로 이동한다.
```



## 값을 전달하면서 다른 페이지로 이동

```html
<!-- HTML -->
<a href="{% url '앱 이름:url 별명' 전달할 값 %}">Something</a>
```

```python
# Python
return redirect('앱 이름:url 별명', 전달할 값)
```



## DB(?) 명령어

- 클래스.objects.all() : 전체 조회
- 인스턴스.save() : 자료 저장
- 클래스.objects.create(key=value) : 자료 저장
- 클래스.objects.get(key=something) : 해당 key의 value가 something인 객체 조회
- 클래스.objects.get(key=something).delete() : 자료 삭제
- 