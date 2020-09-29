# DB ManyToMany (M:N)

> 중게 모델을 사용해서 서로 다른 두 테이블을 묶어준다.

## ManyToManyField(to, **options)

- M:N 관계를 나타내기 위해 사용하는 필드
- 하나의 필수 위치 인자**(연결할 모델)**가 필요하다.
- 모델 내 새로운 컬럼이 생기는게 아닌 중개 테이블이 생긴다.

### Arguments

- **related_name** : 역참조시 사용할 이름
  - 선택사항이지만 필수적으로 사용해야 할 상황이 있음
- **through** : 중개 테이블을 직접 작성할 때 사용하거나 중개 테이블에 추가 정보가 필요할 때
- **symmetrical** : ManyToManyField가 자기 자신의 모델을 가리킬 때 양방향인지 단방향인지 결정
  - 양방향 = True
  - 단방향 = False



#### 좋아요 예시

```python
@require_POST
def like(request):
    # 인증된 사용자만 가능
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # 좋아요 취소
        # 포함 여부로 확인
        #if request.user in article.like_users.all():        
        # 존재 여부로 확인
        if article.like_users.filter(pk=request.user.pk).exists():
        # 해당 user가 article에 좋아요를 눌렀는지 안눌렀는지        
            article.like_users.remove(request.user)
        else:
            # 좋아요
            article.like_users.add(request.user)
        return redirect('index')
    return redirect('login')
```

