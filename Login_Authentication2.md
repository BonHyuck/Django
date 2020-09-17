# 회원 관리

## 회원정보 삭제

#### 사용자의 접근을 위한 url 설정

#### urls.py

```python
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
	...
    path('delete/', views.delete, name="delete"),
]
```

#### views.py 에 기능 추가

```python
from django.views.decorators.http import require_POST

# POST일때만 수행
@require_POST
def delete(request):
    # 현재 로그인돼있는 사람의 요청인지 확인
    if request.user.is_authenticated:
        # request.user에 유저 정보가 들어있음
        request.user.delete()
    return redirect('경로')
```

#### 요청을 보내기 위한 Form 만들기

```django
<form action="{% url 'delete' %}" method="POST">
    {% csrf_token%}
    <input type="submit" value="DELETE"/>
</form>
```



## 비밀번호 변경

비밀번호를 저장할 때 암호화가 되기 때문에 직접적인 수정이 아닌 **덮어쓰기** 방식으로 비밀번호를 변경한다.

#### 사용자의 접근을 위한 url 설정

#### urls.py

```python
from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
	...
    path('password_change/', views.password_change, name="password_change"),
]
```

#### views.py 에 기능 추가

```python
from django.contrib.auth.forms import PasswordChangeForm

def password_change(request):
    if request.method == "POST":
        # request.POST로 입력값들을 받아온다.
        # PasswordChangeForm은 user 정보를 먼저 받게끔 되어있다.
        form =  PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('이동할 경로')
    else:
        # user자체를 인자로 받는다.
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'html 파일', context)
```

##### 비밀번호를 변경하고 나면 세션id가 사라져서 로그아웃이 된다

- 비밀번호를 변경하고 나서 redirect 전에 세션이 사라지는 것을 방지해준다
- `update_session_auth_hash(request, user)`

#### views.py

```python
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def password_change(request):
    if request.method == "POST":
        # request.POST로 입력값들을 받아온다.
        # PasswordChangeForm은 user 정보를 먼저 받게끔 되어있다.
        form =  PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('이동할 경로')
    else:
        # user자체를 인자로 받는다.
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'html 파일', context)
```

#### `form.save()` 의 리턴값은 해당하는 object 이다.



#### @request_POST

- POST 방식의 요청에만 반응하고 그 외에는 405 에러를 띄운다
  - 405 Method not Allowed : 메서드 호출 불가