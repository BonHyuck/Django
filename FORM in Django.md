# FORM in Django

**가상환경 잊지 말기**

- 가상환경 생성

```bash
python -m venv venv
```

- 가상환경 켜기

```bash
source venv/Scripts/activate
```

- 가상환경 끄기

```bash
deactivate
```



django에서는 많은 것을 자동화해준다. 그 중 하나는 Form을 Model에 맞게 생성해준다.

1. Model 생성

```python
from django.db import models

# Create your models here.
class 클래스명(models.Model):
    변수 = models.타입함수
```

2. forms.py 생성(Form은 다른 곳에 정의해도 되지만 파일 생성이 편하다)

```python
from django import forms
from .models import 모델내클래스

class 폼클래스이름(forms.ModelForm):
    class Meta:
        model = 가져올 모델
        # 어떤 필드를 가져올 것인가?
        # 전부 다 가져오기
        fields = '__all__'
        
```



## HTML 시작

위의 과정을 통해 form을 생성하면 django를 이용해 html까지 만든다.

### CRUD의 각 과정을 하나의 페이지에서 해준다

> 각 과정에서 보여주기와 실행을 하나의 함수에서 실행한다.

#### Create

```python
from django.shortcuts import render, redirect
from .forms import 폼클래스

def create(request):
    # DB에 접근해서 작성하기
    if request.method == "POST":
        form = 폼클래스(request.POST)
        # 들어온 정보의 유효성 검사
        if forms.is_valid():
            # 저장하기
            forms.save()
            return redirect('index')
    # 사용자가 작성해야할 Form 보여주기
    else:
         form = ArticleForm()
   	context = {
        'form' : form
    }
    return render(request, 'create.html', context)
```

정보를 받는 것과 처리하여 저장하는 것을 같은 함수(같은 페이지)에서 진행한다

#### Update

```python
def update(request, 받을 PK(or 값)):
    # Model.objects.get == 단 하나만 찾아온다.
    # 그래서 반드시 고유값을 참조한다.
    변수명 = Model클래스.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = 위 변수명)
        if form.is_valid():
            form.save()
            return redirect('이동할 페이지')
    # GET, PUT, ...
    else:
        form = Form클래스(instance=위 변수명)
    context = {
        'form' : form
    }
    return render(request, 'update.html', context)
```

#### Delete

해당 함수를 POST에서만 처리하게 `decorator`를 붙여준다.

```python
# django가 가진, views에서 쓸 decorators중 http 관련
from django.views.decorators.http import require_POST
# @decorator
@require_POST
def delete(request, pk):
    pass
```

