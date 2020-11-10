from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    # author = models.CharField(max_length=100) #짦은 글자형태를 표현함 / 글자수 제한가능
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) # on_delete = "삭제가 되면" / CASCADE = 폭포가 떨어지듯이, 정보가 삭제되면 관련포스트클래스가 전부 지워짐
    body = models.TextField() # 본문 : 일반적인 장문을 요할 때, 사용
    image = models.ImageField(upload_to='post', null=True)
    created_at = models.DateTimeField() # 시간에 대한 표현 , 날짜시간 모두 표시
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        # return f'{self.author}: {self.body}'
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        
        return f'{self.body}'