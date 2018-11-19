from django.shortcuts import render , get_object_or_404

# Create your views here.
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{"blogs":blogs})

def blogdetail(request,blog_id):
    blog_item = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/blogdetail.html', {"blog_item":blog_item})