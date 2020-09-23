# Custom User

Django는 기본 유저를 제공하지만 원하는 요소가 없거나 필요없는 요소가 있을수 있다.

이를 해결하기 위해 기본 유저 모델, AUTH_USER_MODEL을 재정의하여 **커스텀 유저 모델**을 만든다.

**프로젝트의 첫 migrate를 실행하기 전에 완료해야한다!!**



## AUTH_USER_MODEL

> User를 나타내는 모델

- 기본 값 = `auth.user`
- 프로젝트 중간에 변경할 수 없다



## AbstarctBaseUser & AbstractUser

> models.Model - AbstractBaseUser - AbstractUser - User

### AbstractBaseUser

- password와 last_login 만 기본으로 제공한다.
- 자유도가 높지만 나머지 사항은 직접 작성해야한다.

### AbstractUser

- 관리자 권한과 함께 완전한 기능을 갖춘 유저모델을 구현하는 기본 클래스

https://docs.djangoproject.com/en/3.1/topics/auth/customizing/

#### models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser를 그대로 가져온것
class User(AbstractUser):
    pass
```

#### settings.py

```python
...
AUTH_USER_MODEL = '앱이름.유저클래스명'
AUTH_USER_MODEL = '앱이름.User'
```

#### admin.py

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



### 프로젝트 중간에 수정한다면 Migration과 DB를 초기화해야한다.

1. 숫자로 시작하는 모든 migration 파일을 삭제
   1. migrations 폴더는 삭제하면 안된다.
2. .sqlite3 파일도 삭제
3. 다시 migrate



### Custom Users / Built-in Auth forms

- AbstractBaseUser의 모든 subclass와 호환되는 forms는 그대로 사용할 수 있다.
- ModelForm은 기존의 User와 연결되어 있어서 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야한다.
  - UserCreationForm
  - UserChangeForm

#### forms.py

```python
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields +('custom_field', )
```

이후 **views.py**에 적용해준다.



## 유저모델 참조하기

- settings.AUTH_USER_MODEL
  - 유저 모델에 대한 1:N 혹은 M:N 관계를 정의할 때 사용
  - **models.py**에서 사용
- get_user_model()
  - 유저모델을 직접 참조하는 대신 **get_user_model()**을 사용한다
  - **models.py** 외에 모든 곳에서 참조할 때 사용



#### models.py

```python
from django.cong import settings
class 참조하는클래스(models.Model):
    # 참조되는 User
    변수명 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

이후 **views.py**에 적용해준다.





## Abstract Base Classes

> 몇가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

데이터베이스 테이블을 만드는데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는경우 해당 필드가 하위 클래스의 필드에 추가된다.

```python
class ABC(models.Model):
    something = models....
    class Meta:
        abstract = True
```



# M:N 관계

## 모델링

- 현실세계를 최대한 유사하게 반영하기 위함
- 일상에 가까운 예시를 통해 DB를 모델링하고, 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있는지에 대해 고민

모델링을 위해서 M:N 관계 구현은 필요하다

#### 1:N 관계에선 하나의 레코드가 여러개의 참조값을 가질수 없다.

## 중계모델

각각 다른 모델들과 1:N의 관계를 가져서 모델을 M:N의 관계로 연결을 해준다.

중계모델을 두고 **역참조**를 통해 서로의 관계를 확인할 수 있다.

## ManyToManyField

M:N의 관계에서 참조를 해주는 역할을 수행한다. 

참조를 하는 모델이나 되는 모델이나 어느 위치에 있어도 상관이 없다.

```python
모델내변수(주로 복수형) = models.ManyToManyField(참조할클래스, through='중계모델')
```

A : 참조 필드가 없는 모델, B: 참조 필드가 있는 모델

B는 A를 참조하지만 A가 B를 직접 참조는 못하고 역참조만 가능하다.

### related_name

```python
모델내변수(주로 복수형) = models.ManyToManyField(참조할클래스, through='중계모델', related_name='역참조시 변수처럼 사용할 문자열')
```

## 최종 형태

Django는 친절하게도 중계모델을 직접 만들지 않아도 자동으로 생성해준다.

```python
모델내변수(주로 복수형) = models.ManyToManyField(참조할클래스, related_name='역참조시 변수처럼 사용할 문자열')
```

중계 모델의 DB내 이름은 `appname_참조필드가있는모델_참조필드가없는모델`