from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
#게시물
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField('Tag',blank=True)
    #좋아요 카운트 필드 (하나의 유저가 여러글에 좋아요 누를 수 있고 하나의 글이 여러 유저의 좋아요를 받을 수 있음)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_blog')

    class Meta:
        db_table = 'blog'
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
    
#댓글
class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # Blog 디비의 pk인 Blog id를 외래키로 가짐
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    #User 디비의 pk인 User id를 외래키로 가짐
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #1대 다 관계


    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.content + ' | ' + str(self.author)
    
#태그
class Tag(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name