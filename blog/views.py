from django.shortcuts import render, redirect
from .forms import BlogPostForm
from .models import BlogPost


def create_blog_post(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    
    if request.method == 'POST':
        if request.user.user_type == 'doctor':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                blog_posts = blog_posts = BlogPost.objects.order_by('-created_at').all()
                return render(request, 'blog_post_list.html',{'blog_posts': blog_posts})
        else:
            return redirect('customer_dashboard')
    else:
        form = BlogPostForm
    return render(request, 'create_blog_post.html', {'form': form})


def blog_post_list(request):
    if request.user.user_type == 'patient':
        blog_posts = BlogPost.objects.filter(is_draft=False).order_by('-created_at')
    else:
        blog_posts = blog_posts = BlogPost.objects.order_by('-created_at').all()   
    return render(request, 'blog_post_list.html', {'blog_posts': blog_posts})
