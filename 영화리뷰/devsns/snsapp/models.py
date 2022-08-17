from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# 익명게시판 모델
class Post(models.Model):
    #id는 내부에서 만들어줌

    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')

    Type=(
        ('D', 'Dresses'),
        ('M', 'Blouses & Shirts'),
        ('C', 'Coats'),
        ('B', 'Bombers'),
        ('T', 'T-shirts & Sweaters'),
        ('S', 'Sweatshirts'),
        ('Car', 'Cardigans & Sweaters'),
        ('J','Jackets'),
        ('T', 'Trousers'),
        ('Je','Jeans'),
        ('S', 'Shorts')
    )
    cloth_type = models.CharField(max_length=20,choices=Type, default='')


    def __str__(self):
        return self.title #admin page에 어떻게 나타나
        
# 익명게시판 댓글 모델
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE) 
    # 코멘트는 포스트에 종속되어있기때문에 forignkey로 불러옴
    # on_delete=models.CASCADE 글이 삭제되면 같이 삭제될거다
    def __str__(self):
        return self.comment

# 자유게시판 모델
class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # 유저객체를 참조하는 컬럼
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 자유게시판 댓글 모델
class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField()
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.comment
