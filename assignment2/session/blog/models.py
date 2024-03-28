
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    age = models.IntegerField(default=1 ,help_text="만나이를 입력해주세요")
    createdAt = models.DateTimeField(auto_now_add=True) 
    modification_date = models.DateTimeField(blank=True,null=True) ## 빈값 허용,데이터베이스에 null값 저장 허용

    def __str__(self):
        return self.title