from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django import forms
from django.urls import reverse

from posts.models import Posts, Comment


class PostList(ListView):
    model = Posts
    template_name = 'posts/post_list'

class PostCreate(CreateView):
    model = Posts
    fields = ['image', 'description', 'author']
    success_url = '/'

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=255)

class PostDetail(DetailView):
    model = Posts
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
            post = self.get.object(),
            author = request.user,
            text = comment_form.cleaned_data['comment']
            )
        else:
            raise Exception
        return redirect(reverse('detail', args=[self.get.object().id]))