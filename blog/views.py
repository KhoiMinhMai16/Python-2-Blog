from django.shortcuts import render, get_object_or_404
from blog.models import Post
from blog.forms import CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', Data)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post':post})

def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,author=request.user,post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post":post, "form":form})