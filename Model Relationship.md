# Model Relationship

- Many to One (1:N) : **ForeignKey()**
- Many to Many (M:N) : **ManyToManyField()**
- One to One (1:1) : **OneToOneField()**



## Many to One

### Foreign Key(외래 키)

- 참조하는 테이블에서 1개의 키에 해당하며 참조하는 측의 관계 변수는 참조되는 측의 테이블 키를 가리킨다.
- 참조하는 테이블과 참조되는 테이블이 동일할 수도 있다.(재귀적 외래 키)
  - ex) 대댓글



#### 참조하는 테이블 구성

##### models.py

```python
class 클래스명(models.Model):
    # 보통 변수명은 참조되는 테이블 클래스의 소문자 단수형태
    변수명 = models.ForeignKey(참조되는클래스명, on_delete=models.???)
    ...
```

##### on_delete 옵션

- **CASCADE : 부모가 삭제됐을 때 같이 삭제**
- PROTECT : 참조 되어 있는 경우 오류
- SET_NULL : 부모 객체가 삭제됐을 때 값을 NULL로
- SET_DEFAULT : 기본값으로 치환
- SET() : 특정함수 호출
- DO_NOTHING : 아무것도 안함
  - SQL ON DELETE 제한 조건 설정 필요
- RESTRICT : RestrictedError를 발생시켜 참조된 객체 삭제 방지

**migrate 로 DB에 들어갈때는 변수명_id 로 저장된다.**

```python
# 아래처럼 사용이 가능하다.
참조하는instance.참조된객체.참조된객체내변수
# 예시
comment = Comment.objects.get(pk=id)
# 댓글이 달려있는.게시글의.제목
title = comment.article.title
```



### 역참조

참조되는 객체가 참조하는 객체를 필요로 할 때 역참조를 한다.

- 1:N 관계에서 1을 통해 N을 가져온다.

```python
# QuerySet을 리턴한다. 배열처럼 활용할 수 있다.
참조되는instance.참조하는클래스명_set.all()
# 예시 
article.comment_set.all()
```



#### Related_name

##### models.py

```python
class 클래스명(models.Model):
    # 보통 변수명은 참조되는 테이블 클래스의 소문자 단수형태
    변수명 = models.ForeignKey(참조되는클래스명, on_delete=models.???, related_name='something')
    # 이 경우 article.comment_set.all() 이 아닌 article.something.all()로만 해야한다.
    ...
```

