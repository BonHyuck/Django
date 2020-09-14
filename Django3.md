# Django

## DB (Database)

- 체계화된 데이터의 모임

#### 쿼리(Query)

- 데이터 조회, 추출, 조작을 위한 명령어

#### 스키마(Schema)

- 데이터베이스의 구조와 제약 조건에 대한 명세

#### 테이블(Table)

- 열과 행의 모델을 사용해 조직된 데이터 요소의 집합

- 필드(Field) / 열(Column) / 속성
- 레코드(Record) / 행(Row) / 튜플



## Model

- 데이터에 대한 하나의 정보 소스
- 저장된 데이터베이스의 구조
- 사용자가 저장하는 데이터의 필드와 동작을 포함
- django는 model을 통해 데이터에 접속 및 관리
- 일반적으로 model은 하나의 데이터베이스 테이블에 매핑

### ORM (Object-Relational-Mapping)

> 객체 지향 언어를 사용하여 호환되지 않는 유형의 시스템간에 데이터를 변환하는 기술

#### 장점

- SQL을 잘 알지 못해도 DB 조작 가능
- 절차적 접근이 아닌 객체 지향적 접근으로 인한 높은 생산성

#### 단점

- ORM만으로 완전한 서비스 구현이 어려운 경우가 있다.

**현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것. (생산성)**



### Model 구축

1. Project 생성 이후 App 생성
2. App 폴더 내 **model.py** 로 이동

3. DB 조작을 위한 Class를 생성한다.

   ```python
   from django.db import models
   
   # Create your models here.
   # model의 기본 Model을 상속받는다.
   class 클래스명(models.Model):
       변수 = models.필드()
       # 필드로 타입을 잡아주고 설정값을 넣어서 조작한다.
       변수 = models.필드(설정 값)
   ```

4. **`python manage.py makemigrations`** 명령어로 migration 생성

5. Model 이 수정될 때마다 **4번**을 수행한다.

6. 수정이 끝나면 **`python manage.py migrate`** 명령어로 적용한다.



## Migrations

> Django가 Model에 생긴 변화를 반영하는 방법

- 명령어
  - **makemigrations**
    - model을 변경한 것에 기반한 새로운 migration(설계도)을 만들 때 사용
  - **migrate**
    - DB에 반영
  - sqlmigrate 앱이름 migration번호
    - migration에 대한 SQL 구문을 보기 위해 사용
  - showmigrations
    - 프로젝트 전체의 migration과 각각의 상태 확인



## DB API

- django에서는 DB를 편하게 조작할 수 있도록 database-abstract API(=database-access API)를 자동으로 만듦

#### `클래스명.매니저(오브젝트).쿼리 = ClassName.Manager.QuerySet API`

- **Manager** 
  - django 모델에 데이터베이스query 작업이 제공되는 인터페이스
  - 모든 django 모델 클래스에 objects 라는 Manager를 추가
- **QuerySet**
  - 데이터베이스로부터 전달받은 객체 목록
  - QuerySet 안의 객체는 0개, 1개 혹은 여러개일 수 있음
  - 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음



## CRUD

> 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리기능

**Create(생성), Read(읽기), Update(갱신), Delete(삭제)**



### 데이터 작성

데이터를 작성하는 3가지 방법

1. 첫번째 방법
   1. 변수명 = 클래스() : 모델 클래스로부터 인스턴스 생성
   2. 인스턴스로 클래스 변수에 접근해 해당 인스턴스 변수를 변경
      - 인스턴스.변수 = 값
   3. 인스턴스.save() -> 실제 저장
2. 두번째 방법
   1. 클래스로 인스턴스 생성시 keyword 인자를 함께 작성
      1. 변수 = 클래스(keyword = value)
   2. 인스턴스.save() -> 실제 저장
3. 세번째 방법
   1. 클래스.objects.create(keyword=value, keyword2=value2) -> 바로 저장





