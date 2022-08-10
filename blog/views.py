"""
Docstrings R us!!
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Docstrings R us!!!
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    Docstrings R us!!!
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Docstrings R us!!!
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        context = {
            'post': post,
            'comments': comments,
            'liked': liked,
            'comment_form': CommentForm()
        }
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(request, 'post_detail.html', context)
