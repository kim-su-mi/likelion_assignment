from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog

# Create your views here.
def create(request):
    if request.method == 'POST':
        new_blog = Blog()
    
        new_blog.title = request.POST['title']
        new_blog.content = request.POST['content']

        new_blog.save()

        return redirect('detail',new_blog.id)
    return render(request,'new.html')

def detail(request,blog_id):
    blogs = Blog.objects.all() #모든 게시글 가져오기
    return render(request, 'detail.html',{'blogs':blogs})